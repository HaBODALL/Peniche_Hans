"""
Modèle de données interconnecté pour le dimensionnement et la gestion de la péniche Freycinet.
Regroupe les aspects Budget, Lestage/Poids, Énergie, Eaux et Thermique.
"""

from dataclasses import dataclass, field
from typing import Dict, List, Optional
import json


@dataclass
class Equipment:
    id: str
    name: str
    category: str  # "Structure/Lest", "Énergie/Batteries", "Propulsion/Moteur", "Eaux/Cuves", "Thermique/Confort"
    cost_buy: float = 0.0  # €
    cost_maintenance_year: float = 0.0  # €/an
    mass_empty_kg: float = 0.0  # kg
    mass_full_kg: float = 0.0  # kg (si cuve/réservoir, sinon = mass_empty_kg)
    fill_percentage: float = 100.0  # 0.0 à 100.0 %
    pos_x_m: float = 19.25  # m depuis la poupe (0 = poupe, 38.5 = proue)
    pos_y_m: float = 0.0  # m depuis l'axe central (-2.525 = babord, +2.525 = tribord)
    pos_z_m: float = 0.5  # m depuis le fond de cale
    power_consumption_kw: float = 0.0  # kW (nominal consommé)
    power_production_kw: float = 0.0  # kW (nominal produit)
    voltage_v: float = 230.0  # V (24V DC, 400V DC, 230V AC, etc.)
    battery_capacity_kwh: float = 0.0  # kWh
    water_tank_capacity_l: float = 0.0  # L
    water_type: str = "aucun"  # "aucun", "propre", "grise", "noire", "riviere"
    water_flow_l_h: float = 0.0  # L/h (+ si production, - si consommation)
    thermal_heat_gen_kw: float = 0.0  # kW thermique dégagé
    thermal_heat_req_kw: float = 0.0  # kW thermique nécessaire

    @property
    def current_mass_kg(self) -> float:
        """Calcule la masse actuelle de l'équipement en fonction du niveau de remplissage."""
        if self.mass_full_kg > self.mass_empty_kg:
            return self.mass_empty_kg + (self.mass_full_kg - self.mass_empty_kg) * (self.fill_percentage / 100.0)
        return self.mass_empty_kg

    def to_dict(self) -> dict:
        return {
            "id": self.id,
            "name": self.name,
            "category": self.category,
            "cost_buy": self.cost_buy,
            "cost_maintenance_year": self.cost_maintenance_year,
            "mass_empty_kg": self.mass_empty_kg,
            "mass_full_kg": self.mass_full_kg,
            "fill_percentage": self.fill_percentage,
            "pos_x_m": self.pos_x_m,
            "pos_y_m": self.pos_y_m,
            "pos_z_m": self.pos_z_m,
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
        # Ignore extra fields like current_mass_kg if present
        valid_keys = {f for f in cls.__dataclass_fields__}
        filtered_data = {k: v for k, v in data.items() if k in valid_keys}
        return cls(**filtered_data)


@dataclass
class BargeSpecs:
    """Spécifications physiques de la Péniche Freycinet."""
    length_m: float = 38.5
    beam_m: float = 5.05
    hull_empty_mass_kg: float = 85000.0  # Coque acier nue ~85T
    hull_cg_x_m: float = 19.25  # Milieu du bateau
    hull_cg_y_m: float = 0.0
    hull_cg_z_m: float = 1.2
    block_coefficient: float = 0.88  # Coefficient de finesse de la coque rectangulaire
    water_density_kg_m3: float = 1000.0  # Eau douce
    max_draft_m: float = 1.80  # Tirant d'eau max réglementaire VNF (Freycinet)
    min_air_draft_m: float = 3.50  # Tirant d'air max sous les ponts


@dataclass
class SimulationConfig:
    """Configuration de scénario de simulation."""
    mode: str = "repos"  # "repos" ou "navigation"
    navigation_hours_per_day: float = 6.0  # Heures de nav par jour
    propulsion_power_kw: float = 40.0  # Puissance moyenne de propulsion en nav (30-80 kW)
    habitat_base_load_kw: float = 1.5  # Consommation électrique permanente habitat
    solar_irradiance_factor: float = 0.6  # Rendement/ensoleillement moyen (0.0 à 1.0)
    river_water_temp_c: float = 15.0  # Température eau de rivière
    target_cabin_temp_c: float = 20.0  # Température cible cabine
    thermal_exchange_efficiency: float = 0.85  # Efficacité de l'échangeur thermique
    cp_water_kj_kg_c: float = 4.184  # Capacité thermique massique eau (kJ/kg.°C)
