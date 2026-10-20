"""
Données d'équipements par défaut pour la Péniche Freycinet.
Permet d'avoir une configuration de départ cohérente.
"""

from typing import List
from outils.core.models import Equipment


def get_default_equipment_list() -> List[Equipment]:
    """Retourne la liste des équipements standard de la péniche."""
    return [
        Equipment(
            id="lest_fonte_fond",
            name="Lest de Fond (Rails d'acier / Fonte)",
            category="Structure/Lest",
            cost_buy=12000.0,
            cost_maintenance_year=100.0,
            mass_empty_kg=45000.0,
            mass_full_kg=45000.0,
            fill_percentage=100.0,
            pos_x_m=19.25,
            pos_y_m=0.0,
            pos_z_m=0.1,
        ),
        Equipment(
            id="parc_batteries_400v",
            name="Parc Batteries LiFePO4 400V (150 kWh)",
            category="Énergie/Batteries",
            cost_buy=35000.0,
            cost_maintenance_year=500.0,
            mass_empty_kg=1200.0,
            mass_full_kg=1200.0,
            fill_percentage=100.0,
            pos_x_m=8.0,  # En salle des machines
            pos_y_m=0.0,
            pos_z_m=0.5,
            voltage_v=400.0,
            battery_capacity_kwh=150.0,
            thermal_heat_gen_kw=1.5,  # Chaleur dégagée sous forte charge
        ),
        Equipment(
            id="panneaux_solaires_toit",
            name="Panneaux Solairement Intégrés (12 kWc)",
            category="Énergie/Batteries",
            cost_buy=14000.0,
            cost_maintenance_year=200.0,
            mass_empty_kg=600.0,
            mass_full_kg=600.0,
            fill_percentage=100.0,
            pos_x_m=20.0,
            pos_y_m=0.0,
            pos_z_m=3.2,
            power_production_kw=12.0,
            voltage_v=400.0,
        ),
        Equipment(
            id="moteur_electrique_propulsion",
            name="Moteur Synchronique Propulsion 100 kW",
            category="Propulsion/Moteur",
            cost_buy=22000.0,
            cost_maintenance_year=600.0,
            mass_empty_kg=850.0,
            mass_full_kg=850.0,
            fill_percentage=100.0,
            pos_x_m=3.0,  # Arrière du bateau
            pos_y_m=0.0,
            pos_z_m=0.4,
            power_consumption_kw=40.0,  # Puissance moyenne de croisière
            voltage_v=400.0,
            thermal_heat_gen_kw=4.0,  # Pertes joule/chaleur à dissiper
        ),
        Equipment(
            id="cuve_eau_propre_1",
            name="Réservoir Eau Propre Alimentaire 3000L",
            category="Eaux/Cuves",
            cost_buy=3200.0,
            cost_maintenance_year=150.0,
            mass_empty_kg=250.0,
            mass_full_kg=3250.0,
            fill_percentage=80.0,
            pos_x_m=25.0,  # Avant / milieu
            pos_y_m=-1.0,
            pos_z_m=0.6,
            water_tank_capacity_l=3000.0,
            water_type="propre",
            water_flow_l_h=-15.0,  # Consommation moyenne journalière ramenée en L/h
        ),
        Equipment(
            id="cuve_eaux_grises_phytopurif",
            name="Station Phyto / Traitement Eaux Grises 1500L",
            category="Eaux/Cuves",
            cost_buy=4500.0,
            cost_maintenance_year=250.0,
            mass_empty_kg=300.0,
            mass_full_kg=1800.0,
            fill_percentage=40.0,
            pos_x_m=15.0,
            pos_y_m=1.0,
            pos_z_m=0.6,
            power_consumption_kw=0.3,  # Pompes de circulation 24V/230V
            voltage_v=230.0,
            water_tank_capacity_l=1500.0,
            water_type="grise",
            water_flow_l_h=12.0,  # Récupération
        ),
        Equipment(
            id="cuve_eaux_noires",
            name="Cuve de Rétention Eaux Noires (Toilettes) 800L",
            category="Eaux/Cuves",
            cost_buy=1800.0,
            cost_maintenance_year=100.0,
            mass_empty_kg=120.0,
            mass_full_kg=920.0,
            fill_percentage=20.0,
            pos_x_m=10.0,
            pos_y_m=-1.0,
            pos_z_m=0.5,
            water_tank_capacity_l=800.0,
            water_type="noire",
            water_flow_l_h=3.0,
        ),
        Equipment(
            id="echangeur_eau_riviere",
            name="Pompe à Chaleur / Échangeur Eau de Rivière",
            category="Thermique/Confort",
            cost_buy=8500.0,
            cost_maintenance_year=300.0,
            mass_empty_kg=180.0,
            mass_full_kg=220.0,
            fill_percentage=100.0,
            pos_x_m=6.0,
            pos_y_m=0.5,
            pos_z_m=0.5,
            power_consumption_kw=2.0,  # PAC électrique
            voltage_v=230.0,
            thermal_heat_gen_kw=8.0,  # Restitution thermique chaud/froid
            thermal_heat_req_kw=2.0,  # Refroidissement moteur/batterie
            water_type="riviere",
            water_flow_l_h=1200.0,  # Débit de circulation eau brute
        ),
    ]
