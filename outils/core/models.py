"""
Modèle de données interconnecté pour le dimensionnement et la gestion de la péniche Freycinet.
Regroupe les aspects Budget, Financement, Lestage/Stabilité, Énergie, Eaux et Thermique.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional
import json


@dataclass
class Equipment:
    id: str
    name: str
    category: str  # "Structure/Lest", "Énergie/Batteries", "Propulsion/Moteur", "Eaux/Cuves", "Thermique/Confort"
    status: str = "exemple fictif"  # "exemple fictif", "hypothèse", "vérifié"
    status_source: str = ""  # Ex: "Devis Victron 2026-08", "Fiche technique", "Estimation"
    cost_buy: float = 0.0  # € (Euros)
    cost_maintenance_year: float = 0.0  # €/an
    mass_empty_kg: float = 0.0  # kg
    mass_full_kg: float = 0.0  # kg
    fill_percentage: float = 100.0  # %
    pos_x_m: float = 19.25  # m depuis la poupe (0 = poupe, 38.5 = proue)
    pos_y_m: float = 0.0  # m depuis l'axe central (-2.525 = babord, +2.525 = tribord)
    pos_z_m: float = 0.5  # m depuis le fond de cale
    # Carène liquide (effet de surface libre pour les cuves)
    tank_length_m: float = 0.0  # m
    tank_width_m: float = 0.0  # m
    power_consumption_kw: float = 0.0  # kW
    power_production_kw: float = 0.0  # kW
    voltage_v: float = 230.0  # V
    battery_capacity_kwh: float = 0.0  # kWh
    water_tank_capacity_l: float = 0.0  # L (Litres)
    water_type: str = "aucun"  # "aucun", "propre", "grise", "noire", "riviere"
    water_flow_l_h: float = 0.0  # L/h
    thermal_heat_gen_kw: float = 0.0  # kW thermal
    thermal_heat_req_kw: float = 0.0  # kW thermal

    @property
    def current_mass_kg(self) -> float:
        """Calcule la masse actuelle de l'équipement en kg."""
        if self.mass_full_kg > self.mass_empty_kg:
            return self.mass_empty_kg + (self.mass_full_kg - self.mass_empty_kg) * (self.fill_percentage / 100.0)
        return self.mass_empty_kg

    @property
    def free_surface_moment_m4(self) -> float:
        """
        Calcule le moment d'inertie de surface libre de la cuve (m4).
        I_sl = (Longueur * Largeur^3) / 12  (si partiellement remplie entre 5% et 95%).
        """
        if 5.0 < self.fill_percentage < 95.0 and self.tank_length_m > 0 and self.tank_width_m > 0:
            return (self.tank_length_m * (self.tank_width_m ** 3)) / 12.0
        return 0.0

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "status": self.status,
            "status_source": self.status_source,
            "cost_buy": self.cost_buy,
            "cost_maintenance_year": self.cost_maintenance_year,
            "mass_empty_kg": self.mass_empty_kg,
            "mass_full_kg": self.mass_full_kg,
            "fill_percentage": self.fill_percentage,
            "pos_x_m": self.pos_x_m,
            "pos_y_m": self.pos_y_m,
            "pos_z_m": self.pos_z_m,
            "tank_length_m": self.tank_length_m,
            "tank_width_m": self.tank_width_m,
            "power_consumption_kw": self.power_consumption_kw,
            "power_production_kw": self.power_production_kw,
            "voltage_v": self.voltage_v,
            "battery_capacity_kwh": self.battery_capacity_kwh,
            "water_tank_capacity_l": self.water_tank_capacity_l,
            "water_type": self.water_type,
            "water_flow_l_h": self.water_flow_l_h,
            "thermal_heat_gen_kw": self.thermal_heat_gen_kw,
            "thermal_heat_req_kw": self.thermal_heat_req_kw,
            "current_mass_kg": self.current_mass_kg,
        }

    @classmethod
    def from_dict(cls, data: dict) -> "Equipment":
        valid_keys = {f for f in cls.__dataclass_fields__}
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return cls(**filtered_data)


@dataclass
class FinancialPlan:
    """Modèle de plan de financement et budget."""
    personal_contribution_eur: float = 30000.0  # Apport personnel (€)
    loan_purchase_eur: float = 50000.0  # Prêt achat (€)
    loan_renovation_eur: float = 30000.0  # Prêt travaux (€)
    loan_interest_rate_pct: float = 3.5  # Taux d'intérêt (%)
    loan_duration_years: int = 10  # Durée du prêt (années)
    contingency_rate_pct: float = 15.0  # Taux d'imprévus (Bible 6.3 = 15%)
    location_cot_year_eur: float = 3600.0  # Redevance COT VNF estimée (€/an)
    insurance_year_eur: float = 1800.0  # Assurance bateau (€/an)


@dataclass
class BargeSpecs:
    """Spécifications physiques de la Péniche Freycinet."""
    length_m: float = 38.5  # m
    beam_m: float = 5.05  # m
    hull_empty_mass_kg: float = 85000.0  # kg (Coque acier nue ~85T)
    hull_cg_x_m: float = 19.25  # m
    hull_cg_y_m: float = 0.0  # m
    hull_cg_z_m: float = 1.2  # m (Centre de gravité vertical de la coque)
    block_coefficient: float = 0.92  # Coeff. de bloc (Bible & Forme rectangulaire Freycinet = 0.90 - 0.95)
    water_density_kg_m3: float = 1000.0  # kg/m3 (Eau douce)
    max_draft_m: float = 1.80  # m (Tirant d'eau max VNF)
    min_air_draft_m: float = 3.50  # m (Tirant d'air min sous les ponts)


@dataclass
class SimulationConfig:
    """Configuration du scénario de simulation."""
    mode: str = "repos"  # "repos" ou "navigation"
    navigation_hours_per_day: float = 6.0  # h/jour
    propulsion_power_kw: float = 40.0  # kW
    habitat_base_load_kw: float = 1.5  # kW
    solar_irradiance_factor: float = 0.6  # Rendement ensoleillement
    solar_air_gap_loss_pct: float = 15.0  # Perte thermique si panneaux collés sans ventilation (15-18%)
    heat_pump_cop: float = 3.5  # Coefficient de Performance de la PAC eau/eau
    river_water_temp_c: float = 15.0  # °C
    target_cabin_temp_c: float = 20.0  # °C
    cp_water_kj_kg_c: float = 4.184  # kJ/kg.°C
