"""
Moteur de calcul interconnecté pour la Péniche Freycinet.
Calcule le lestage/tirant d'eau/assiette (Archimède), le budget (CAPEX/OPEX),
le bilan électrique, le bilan hydrique et la boucle thermique.
"""

from typing import Dict, List, Any
from outils.core.models import Equipment, BargeSpecs, SimulationConfig


class CalculatorEngine:
    """Moteur central d'évaluation et de simulation interconnectée."""

    def __init__(self, equipments: List[Equipment], specs: BargeSpecs = None, config: SimulationConfig = None):
        self.equipments = equipments
        self.specs = specs or BargeSpecs()
        self.config = config or SimulationConfig()

    def calculate_budget(self) -> Dict[str, float]:
        """Calcule le budget d'acquisition (CAPEX) et de maintenance (OPEX)."""
        total_capex = sum(e.cost_buy for e in self.equipments)
        total_opex_year = sum(e.cost_maintenance_year for e in self.equipments)

        capex_by_category = {}
        for e in self.equipments:
            capex_by_category[e.category] = capex_by_category.get(e.category, 0.0) + e.cost_buy

        return {
            "total_capex": total_capex,
            "total_opex_year": total_opex_year,
            "capex_by_category": capex_by_category,
        }

    def calculate_mass_and_ballast(self) -> Dict[str, Any]:
        """
        Calcule les masses, le centre de gravité global, le tirant d'eau (Archimède)
        et l'assiette/gîte (trim & heel).
        """
        hull_mass = self.specs.hull_empty_mass_kg
        equip_mass = sum(e.current_mass_kg for e in self.equipments)
        total_mass_kg = hull_mass + equip_mass
        total_mass_tonnes = total_mass_kg / 1000.0

        # Centre de gravité (CG)
        moment_x = self.specs.hull_empty_mass_kg * self.specs.hull_cg_x_m
        moment_y = self.specs.hull_empty_mass_kg * self.specs.hull_cg_y_m
        moment_z = self.specs.hull_empty_mass_kg * self.specs.hull_cg_z_m

        for e in self.equipments:
            m = e.current_mass_kg
            moment_x += m * e.pos_x_m
            moment_y += m * e.pos_y_m
            moment_z += m * e.pos_z_m

        cg_x = moment_x / total_mass_kg if total_mass_kg > 0 else self.specs.hull_cg_x_m
        cg_y = moment_y / total_mass_kg if total_mass_kg > 0 else 0.0
        cg_z = moment_z / total_mass_kg if total_mass_kg > 0 else 0.0

        # Calcul du tirant d'eau selon le principe d'Archimède :
        # Déplacement D (kg) = Volume immergé V (m3) * Masse volumique eau (kg/m3)
        # V = Longueur * Largeur * Tirant_d_eau * Coeff_finesse
        water_surface_m2 = self.specs.length_m * self.specs.beam_m * self.specs.block_coefficient
        draft_m = total_mass_kg / (water_surface_m2 * self.specs.water_density_kg_m3)

        # Calcul d'assiette (trim) : Écart par rapport au milieu (L/2 = 19.25m)
        center_x = self.specs.length_m / 2.0
        trim_offset_m = cg_x - center_x
        # Différence de tirant d'eau Proue / Poupe (approximation linéaire)
        draft_bow_m = draft_m + (trim_offset_m * 0.05)
        draft_stern_m = draft_m - (trim_offset_m * 0.05)

        # Tirant d'air restant (Ex: 4.50m - draft_m)
        air_draft_m = max(0.0, 4.00 - draft_m)

        return {
            "hull_mass_kg": hull_mass,
            "equipments_mass_kg": equip_mass,
            "total_mass_kg": total_mass_kg,
            "total_mass_tonnes": total_mass_tonnes,
            "cg_x_m": round(cg_x, 2),
            "cg_y_m": round(cg_y, 2),
            "cg_z_m": round(cg_z, 2),
            "draft_m": round(draft_m, 2),
            "draft_bow_m": round(draft_bow_m, 2),
            "draft_stern_m": round(draft_stern_m, 2),
            "air_draft_m": round(air_draft_m, 2),
            "trim_status": "Équilibré" if abs(trim_offset_m) < 0.5 else ("Sur l'avant" if trim_offset_m > 0 else "Sur l'arrière"),
            "max_draft_exceeded": draft_m > self.specs.max_draft_m,
        }

    def calculate_energy(self) -> Dict[str, Any]:
        """
        Calcule le bilan électrique (Production, Consommation, Capacité batteries, Autonomie).
        """
        battery_capacity_kwh = sum(e.battery_capacity_kwh for e in self.equipments)
        base_production_kw = sum(e.power_production_kw for e in self.equipments)
        base_consumption_kw = sum(e.power_consumption_kw for e in self.equipments)

        # Facteur Solaire appliqué à la production
        effective_solar_prod_kw = base_production_kw * self.config.solar_irradiance_factor

        # Ajustement selon mode (Repos vs Navigation)
        if self.config.mode == "navigation":
            propulsion_load_kw = self.config.propulsion_power_kw
            total_consumption_kw = base_consumption_kw + propulsion_load_kw + self.config.habitat_base_load_kw
        else:  # "repos"
            propulsion_load_kw = 0.0
            total_consumption_kw = base_consumption_kw + self.config.habitat_base_load_kw

        net_power_kw = effective_solar_prod_kw - total_consumption_kw

        # Calcul de l'autonomie sur batterie (en heures)
        if net_power_kw < 0:
            autonomy_hours = battery_capacity_kwh / abs(net_power_kw) if battery_capacity_kwh > 0 else 0.0
        else:
            autonomy_hours = float("inf")  # Positif ou neutre = autonomie illimitée / charge

        # Bilan journalier (kWh/jour)
        if self.config.mode == "navigation":
            nav_hours = self.config.navigation_hours_per_day
            rest_hours = 24.0 - nav_hours
            daily_cons_kwh = (
                (base_consumption_kw + propulsion_load_kw + self.config.habitat_base_load_kw) * nav_hours
                + (base_consumption_kw + self.config.habitat_base_load_kw) * rest_hours
            )
        else:
            daily_cons_kwh = (base_consumption_kw + self.config.habitat_base_load_kw) * 24.0

        daily_prod_kwh = effective_solar_prod_kw * 8.0  # ~8h de soleil efficace / jour en moyenne

        return {
            "battery_capacity_kwh": battery_capacity_kwh,
            "effective_solar_prod_kw": round(effective_solar_prod_kw, 2),
            "total_consumption_kw": round(total_consumption_kw, 2),
            "propulsion_load_kw": round(propulsion_load_kw, 2),
            "net_power_kw": round(net_power_kw, 2),
            "autonomy_hours": round(autonomy_hours, 1) if autonomy_hours != float("inf") else 999.0,
            "daily_cons_kwh": round(daily_cons_kwh, 2),
            "daily_prod_kwh": round(daily_prod_kwh, 2),
            "daily_balance_kwh": round(daily_prod_kwh - daily_cons_kwh, 2),
        }

    def calculate_water(self) -> Dict[str, Any]:
        """Calcule les capacités de stockage et les flux d'eau (Propre, Grise, Noire)."""
        clean_capacity_l = sum(e.water_tank_capacity_l for e in self.equipments if e.water_type == "propre")
        grey_capacity_l = sum(e.water_tank_capacity_l for e in self.equipments if e.water_type == "grise")
        black_capacity_l = sum(e.water_tank_capacity_l for e in self.equipments if e.water_type == "noire")

        clean_volume_l = sum(
            e.water_tank_capacity_l * (e.fill_percentage / 100.0)
            for e in self.equipments
            if e.water_type == "propre"
        )
        grey_volume_l = sum(
            e.water_tank_capacity_l * (e.fill_percentage / 100.0)
            for e in self.equipments
            if e.water_type == "grise"
        )
        black_volume_l = sum(
            e.water_tank_capacity_l * (e.fill_percentage / 100.0)
            for e in self.equipments
            if e.water_type == "noire"
        )

        clean_flow_l_h = sum(e.water_flow_l_h for e in self.equipments if e.water_type == "propre")
        grey_flow_l_h = sum(e.water_flow_l_h for e in self.equipments if e.water_type == "grise")
        black_flow_l_h = sum(e.water_flow_l_h for e in self.equipments if e.water_type == "noire")

        # Autonomie en eau propre (heures)
        clean_autonomy_hours = (
            clean_volume_l / abs(clean_flow_l_h) if clean_flow_l_h < 0 and clean_volume_l > 0 else 999.0
        )

        return {
            "clean_capacity_l": clean_capacity_l,
            "clean_volume_l": clean_volume_l,
            "clean_flow_l_h": clean_flow_l_h,
            "clean_autonomy_days": round(clean_autonomy_hours / 24.0, 1) if clean_autonomy_hours < 999 else 999.0,
            "grey_capacity_l": grey_capacity_l,
            "grey_volume_l": grey_volume_l,
            "grey_flow_l_h": grey_flow_l_h,
            "black_capacity_l": black_capacity_l,
            "black_volume_l": black_volume_l,
            "black_flow_l_h": black_flow_l_h,
        }

    def calculate_thermal(self) -> Dict[str, Any]:
        """
        Calcule le bilan thermique et le besoin en eau de circulation/refroidissement.
        Formule : Q = m * Cp * DeltaT
        => Débit massique m (kg/s) = Q (kW) / (Cp (kJ/kg.°C) * DeltaT (°C))
        """
        total_heat_gen_kw = sum(e.thermal_heat_gen_kw for e in self.equipments)
        total_heat_req_kw = sum(e.thermal_heat_req_kw for e in self.equipments)

        # En navigation, le moteur génère une chaleur importante à dissiper
        if self.config.mode == "navigation":
            moteur_heat_kw = self.config.propulsion_power_kw * 0.10  # ~10% de pertes thermiques
            total_heat_gen_kw += moteur_heat_kw

        net_thermal_gen_kw = total_heat_gen_kw - total_heat_req_kw

        # Calcul du débit d'eau de rivière nécessaire pour dissiper net_thermal_gen_kw
        # On fixe un élévation de température raisonnable de l'eau rejetée (ex: DeltaT = 5°C)
        delta_t_c = 5.0
        cp = self.config.cp_water_kj_kg_c  # 4.184 kJ/kg.°C

        if net_thermal_gen_kw > 0:
            # m (kg/s) = Q (kW) / (Cp * DeltaT)
            mass_flow_kg_s = net_thermal_gen_kw / (cp * delta_t_c)
            cooling_water_flow_l_h = mass_flow_kg_s * 3600.0  # 1 kg d'eau = 1 Liter
        else:
            cooling_water_flow_l_h = 0.0

        return {
            "total_heat_gen_kw": round(total_heat_gen_kw, 2),
            "total_heat_req_kw": round(total_heat_req_kw, 2),
            "net_thermal_gen_kw": round(net_thermal_gen_kw, 2),
            "river_water_temp_c": self.config.river_water_temp_c,
            "cooling_water_flow_l_h": round(cooling_water_flow_l_h, 1),
            "delta_t_c": delta_t_c,
        }

    def get_full_summary(self) -> Dict[str, Any]:
        """Retourne la synthèse globale interconnectée de tous les modules."""
        return {
            "budget": self.calculate_budget(),
            "mass_ballast": self.calculate_mass_and_ballast(),
            "energy": self.calculate_energy(),
            "water": self.calculate_water(),
            "thermal": self.calculate_thermal(),
            "config": {
                "mode": self.config.mode,
                "navigation_hours_per_day": self.config.navigation_hours_per_day,
            },
        }
