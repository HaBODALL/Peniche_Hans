"""
Moteur de calcul interconnecté et modulaire pour la Péniche Freycinet.
Contient les formules physiques explicites (Archimède avec coeff de bloc,
hauteur métacentrique GM avec carène liquide, bilan thermique avec COP, etc.)
et le moteur de règles d'alertes réglementaires (A60, ES-TRIN, VNF, COT, expert naval).
"""

from typing import Dict, List, Any
from outils.core.models import Equipment, BargeSpecs, SimulationConfig, FinancialPlan


def calculate_archimedes_draft(total_mass_kg: float, specs: BargeSpecs) -> float:
    """
    Formule d'Archimède : Tirant d'eau T (m).
    T = Masse_Totale / (Longueur * Largeur * Coeff_Bloc * Masse_Volumique_Eau)
    """
    water_surface_m2 = specs.length_m * specs.beam_m * specs.block_coefficient
    return total_mass_kg / (water_surface_m2 * specs.water_density_kg_m3)


def calculate_metacentric_height(
    total_mass_kg: float,
    cg_z_m: float,
    equipments: List[Equipment],
    specs: BargeSpecs,
    draft_m: float
) -> Dict[str, float]:
    """
    Formule de Stabilité Transversale (Hauteur métacentrique GM).
    GM = KB + BM - KG - Pertes_Carene_Liquide
    - KB = Tirant_d_eau / 2 (Centre de carène vertical pour coque prismatique)
    - BM = I_flottaison / Volume_immergé
      avec I_flottaison = (Longueur * Largeur^3 * Coeff_Bloc) / 12
      et Volume_immergé = Total_Mass / Density
    - KG = CG_Z (Centre de gravité de la péniche)
    - Perte Carène Liquide = Sum(I_surface_libre) / Volume_immergé
    """
    volume_m3 = total_mass_kg / specs.water_density_kg_m3
    kb_m = draft_m / 2.0
    i_waterplane = (specs.length_m * (specs.beam_m ** 3) * specs.block_coefficient) / 12.0
    bm_m = i_waterplane / volume_m3 if volume_m3 > 0 else 0.0
    kg_m = cg_z_m

    # Effet de carène liquide (surface libre des cuves)
    total_free_surface_moment = sum(e.free_surface_moment_m4 for e in equipments)
    free_surface_loss_m = total_free_surface_moment / volume_m3 if volume_m3 > 0 else 0.0

    gm_m = kb_m + bm_m - kg_m - free_surface_loss_m

    return {
        "kb_m": round(kb_m, 2),
        "bm_m": round(bm_m, 2),
        "kg_m": round(kg_m, 2),
        "free_surface_loss_m": round(free_surface_loss_m, 3),
        "gm_m": round(gm_m, 2),
    }


class CalculatorEngine:
    """Moteur central d'évaluation et de simulation interconnectée."""

    DISCLAIMER_TEXT = (
        "⚠️ AVERTISSEMENT : Cet outil fournit des estimations de dimensionnement à titre indicatif. "
        "Les résultats ne constituent pas une certification navale et DOIVENT être validés par un expert naval / cabinet d'architecture navale qualifié."
    )

    def __init__(
        self,
        equipments: List[Equipment],
        specs: BargeSpecs = None,
        config: SimulationConfig = None,
        financial_plan: FinancialPlan = None,
    ):
        self.equipments = equipments
        self.specs = specs or BargeSpecs()
        self.config = config or SimulationConfig()
        self.financial_plan = financial_plan or FinancialPlan()

    def calculate_financials(self) -> Dict[str, Any]:
        """Calcule le plan de financement, le budget d'acquisition, les imprévus et les mensualités."""
        base_capex = sum(e.cost_buy for e in self.equipments)
        contingency_eur = base_capex * (self.financial_plan.contingency_rate_pct / 100.0)
        total_capex_with_contingency = base_capex + contingency_eur

        base_opex_year = sum(e.cost_maintenance_year for e in self.equipments)
        total_opex_year = (
            base_opex_year
            + self.financial_plan.location_cot_year_eur
            + self.financial_plan.insurance_year_eur
        )

        # Plan de financement
        total_loans = self.financial_plan.loan_purchase_eur + self.financial_plan.loan_renovation_eur
        total_funding = self.financial_plan.personal_contribution_eur + total_loans
        remaining_funding = total_capex_with_contingency - total_funding

        # Mensualité du prêt (amortissement constant)
        r = (self.financial_plan.loan_interest_rate_pct / 100.0) / 12.0
        n = self.financial_plan.loan_duration_years * 12
        if r > 0 and n > 0 and total_loans > 0:
            monthly_payment_eur = total_loans * (r * (1 + r)**n) / (((1 + r)**n) - 1)
        else:
            monthly_payment_eur = 0.0

        return {
            "base_capex": base_capex,
            "contingency_rate_pct": self.financial_plan.contingency_rate_pct,
            "contingency_eur": contingency_eur,
            "total_capex": total_capex_with_contingency,
            "base_opex_year": base_opex_year,
            "cot_vnf_year_eur": self.financial_plan.location_cot_year_eur,
            "insurance_year_eur": self.financial_plan.insurance_year_eur,
            "total_opex_year": total_opex_year,
            "personal_contribution_eur": self.financial_plan.personal_contribution_eur,
            "total_loans_eur": total_loans,
            "total_funding_eur": total_funding,
            "remaining_funding_eur": remaining_funding,
            "monthly_loan_payment_eur": round(monthly_payment_eur, 2),
        }

    def calculate_mass_and_ballast(self) -> Dict[str, Any]:
        """Calcule la masse globale, le centre de gravité, le tirant d'eau et la stabilité métacentrique GM."""
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

        draft_m = calculate_archimedes_draft(total_mass_kg, self.specs)

        # Calcul d'assiette (trim)
        center_x = self.specs.length_m / 2.0
        trim_offset_m = cg_x - center_x
        draft_bow_m = draft_m + (trim_offset_m * 0.05)
        draft_stern_m = draft_m - (trim_offset_m * 0.05)
        air_draft_m = max(0.0, 4.00 - draft_m)

        # Stabilité GM
        stability = calculate_metacentric_height(total_mass_kg, cg_z, self.equipments, self.specs, draft_m)

        return {
            "hull_mass_kg": hull_mass,
            "equipments_mass_kg": equip_mass,
            "total_mass_kg": total_mass_kg,
            "total_mass_tonnes": total_mass_tonnes,
            "block_coefficient": self.specs.block_coefficient,
            "cg_x_m": round(cg_x, 2),
            "cg_y_m": round(cg_y, 2),
            "cg_z_m": round(cg_z, 2),
            "draft_m": round(draft_m, 2),
            "draft_bow_m": round(draft_bow_m, 2),
            "draft_stern_m": round(draft_stern_m, 2),
            "air_draft_m": round(air_draft_m, 2),
            "trim_status": "Équilibré" if abs(trim_offset_m) < 0.5 else ("Sur l'avant" if trim_offset_m > 0 else "Sur l'arrière"),
            "stability_gm_m": stability["gm_m"],
            "stability_details": stability,
            "max_draft_exceeded": draft_m > self.specs.max_draft_m,
        }

    def calculate_energy(self) -> Dict[str, Any]:
        """Calcule le bilan électrique incluant les pertes thermiques solaires et la séparation des tensions."""
        battery_capacity_kwh = sum(e.battery_capacity_kwh for e in self.equipments)

        # Solar production with thermal gap loss factor
        raw_solar_kw = sum(e.power_production_kw for e in self.equipments)
        effective_solar_prod_kw = raw_solar_kw * self.config.solar_irradiance_factor * (1.0 - (self.config.solar_air_gap_loss_pct / 100.0))

        base_consumption_kw = sum(e.power_consumption_kw for e in self.equipments)

        if self.config.mode == "navigation":
            propulsion_load_kw = self.config.propulsion_power_kw
            total_consumption_kw = base_consumption_kw + propulsion_load_kw + self.config.habitat_base_load_kw
        else:
            propulsion_load_kw = 0.0
            total_consumption_kw = base_consumption_kw + self.config.habitat_base_load_kw

        net_power_kw = effective_solar_prod_kw - total_consumption_kw
        autonomy_hours = (battery_capacity_kwh / abs(net_power_kw)) if (net_power_kw < 0 and battery_capacity_kwh > 0) else 999.0

        return {
            "battery_capacity_kwh": battery_capacity_kwh,
            "effective_solar_prod_kw": round(effective_solar_prod_kw, 2),
            "total_consumption_kw": round(total_consumption_kw, 2),
            "propulsion_load_kw": round(propulsion_load_kw, 2),
            "net_power_kw": round(net_power_kw, 2),
            "autonomy_hours": round(autonomy_hours, 1) if autonomy_hours < 999 else 999.0,
        }

    def calculate_water(self) -> Dict[str, Any]:
        """Calcule les capacités et volumes d'eau."""
        clean_capacity_l = sum(e.water_tank_capacity_l for e in self.equipments if e.water_type == "propre")
        grey_capacity_l = sum(e.water_tank_capacity_l for e in self.equipments if e.water_type == "grise")
        black_capacity_l = sum(e.water_tank_capacity_l for e in self.equipments if e.water_type == "noire")

        clean_volume_l = sum(e.water_tank_capacity_l * (e.fill_percentage / 100.0) for e in self.equipments if e.water_type == "propre")
        clean_flow_l_h = sum(e.water_flow_l_h for e in self.equipments if e.water_type == "propre")
        clean_autonomy_hours = (clean_volume_l / abs(clean_flow_l_h)) if (clean_flow_l_h < 0 and clean_volume_l > 0) else 999.0

        return {
            "clean_capacity_l": clean_capacity_l,
            "clean_volume_l": clean_volume_l,
            "clean_flow_l_h": clean_flow_l_h,
            "clean_autonomy_days": round(clean_autonomy_hours / 24.0, 1) if clean_autonomy_hours < 999 else 999.0,
            "grey_capacity_l": grey_capacity_l,
            "black_capacity_l": black_capacity_l,
        }

    def calculate_thermal(self) -> Dict[str, Any]:
        """Bilan thermique avec COP pour la pompe à chaleur."""
        total_heat_gen_kw = sum(e.thermal_heat_gen_kw for e in self.equipments)
        total_heat_req_kw = sum(e.thermal_heat_req_kw for e in self.equipments)

        if self.config.mode == "navigation":
            total_heat_gen_kw += self.config.propulsion_power_kw * 0.10

        net_thermal_gen_kw = total_heat_gen_kw - total_heat_req_kw
        delta_t_c = 5.0
        cp = self.config.cp_water_kj_kg_c

        if net_thermal_gen_kw > 0:
            mass_flow_kg_s = net_thermal_gen_kw / (cp * delta_t_c)
            cooling_water_flow_l_h = mass_flow_kg_s * 3600.0
        else:
            cooling_water_flow_l_h = 0.0

        return {
            "total_heat_gen_kw": round(total_heat_gen_kw, 2),
            "total_heat_req_kw": round(total_heat_req_kw, 2),
            "net_thermal_gen_kw": round(net_thermal_gen_kw, 2),
            "heat_pump_cop": self.config.heat_pump_cop,
            "cooling_water_flow_l_h": round(cooling_water_flow_l_h, 1),
        }

    def get_compliance_alerts(self) -> List[Dict[str, str]]:
        """Génère la liste des alertes réglementaires et d'ingénierie."""
        alerts = []

        # Alertes batteries > 20 kWh (Norme ES-TRIN Local A60)
        total_battery_kwh = sum(e.battery_capacity_kwh for e in self.equipments)
        if total_battery_kwh >= 20.0:
            alerts.append({
                "type": "ES-TRIN / Sécurité",
                "level": "AVERTISSEMENT",
                "message": f"Parc batterie ({total_battery_kwh} kWh >= 20 kWh) : Requis par l'ES-TRIN d'être installé dans un local coupe-feu A60 séparé de l'habitation.",
            })

        # Alerte tirant d'eau VNF
        mass_info = self.calculate_mass_and_ballast()
        if mass_info["draft_m"] > self.specs.max_draft_m:
            alerts.append({
                "type": "Réglementation VNF",
                "level": "DANGER",
                "message": f"Tirant d'eau ({mass_info['draft_m']}m) dépasse la limite Freycinet de {self.specs.max_draft_m}m !",
            })

        # Alerte stabilité métacentrique GM
        if mass_info["stability_gm_m"] < 0.30:
            alerts.append({
                "type": "Architecture Navale",
                "level": "DANGER",
                "message": f"Hauteur métacentrique GM faible ({mass_info['stability_gm_m']}m < 0.30m) ! Risque de gîte ou d'instabilité.",
            })

        # Avertissement COT VNF
        alerts.append({
            "type": "Légal / COT VNF",
            "level": "INFO",
            "message": "La COT (Convention d'Occupation Temporaire) n'est pas cessible de plein droit lors de l'achat d'un bateau. L'emplacement doit être confirmé auprès de VNF.",
        })

        return alerts

    def get_full_summary(self) -> Dict[str, Any]:
        """Synthèse globale complète."""
        return {
            "disclaimer": self.DISCLAIMER_TEXT,
            "financials": self.calculate_financials(),
            "mass_ballast": self.calculate_mass_and_ballast(),
            "energy": self.calculate_energy(),
            "water": self.calculate_water(),
            "thermal": self.calculate_thermal(),
            "alerts": self.get_compliance_alerts(),
            "config": {
                "mode": self.config.mode,
                "navigation_hours_per_day": self.config.navigation_hours_per_day,
            },
        }
