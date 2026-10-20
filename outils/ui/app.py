"""
Interface Web Interactive Streamlit pour le Dimensionnement Interconnecté de la Péniche Freycinet.
Gère Budget, Lestage/Masses, Énergie, Eaux et Régulation Thermique.
"""

import sys
from pathlib import Path

# S'assurer que la racine du projet est dans PYTHONPATH
root_dir = Path(__file__).resolve().parent.parent.parent
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

import streamlit as st
import pandas as pd
from outils.core.models import Equipment, BargeSpecs, SimulationConfig
from outils.core.default_data import get_default_equipment_list
from outils.core.calculator import CalculatorEngine
from outils.integrations.storage_and_edge import StorageManager, EdgeConnector

st.set_page_config(
    page_title="Dimensionnement & Gestion Péniche Freycinet",
    page_icon="⚓",
    layout="wide",
)

st.title("⚓ Outil Interconnecté de Dimensionnement & Suivi - Péniche Freycinet")
st.markdown(
    "Cet outil simule de manière interconnectée le **Budget**, le **Lestage / Tirant d'eau (Archimède)**, "
    "le **Bilan Électrique**, la **Gestion des Eaux** et la **Régulation Thermique** du bateau."
)

# Initialisation de la session state
if "equipments" not in st.session_state:
    st.session_state.equipments = get_default_equipment_list()

if "simulation_config" not in st.session_state:
    st.session_state.simulation_config = SimulationConfig()

if "specs" not in st.session_state:
    st.session_state.specs = BargeSpecs()

# Sidebar - Configuration du Scénario
st.sidebar.header("⚙️ Configuration du Scénario")
mode = st.sidebar.radio("Mode d'opération", ["repos", "navigation"], index=0 if st.session_state.simulation_config.mode == "repos" else 1)
nav_hours = st.sidebar.slider("Heures de navigation / jour", 0.0, 12.0, st.session_state.simulation_config.navigation_hours_per_day, 0.5)
prop_power = st.sidebar.slider("Puissance propulsion croisière (kW)", 10.0, 100.0, st.session_state.simulation_config.propulsion_power_kw, 5.0)
solar_factor = st.sidebar.slider("Facteur d'ensoleillement solaire", 0.0, 1.0, st.session_state.simulation_config.solar_irradiance_factor, 0.1)
river_temp = st.sidebar.number_input("Température Eau de Rivière (°C)", value=st.session_state.simulation_config.river_water_temp_c)

# Mise à jour config
st.session_state.simulation_config.mode = mode
st.session_state.simulation_config.navigation_hours_per_day = nav_hours
st.session_state.simulation_config.propulsion_power_kw = prop_power
st.session_state.simulation_config.solar_irradiance_factor = solar_factor
st.session_state.simulation_config.river_water_temp_c = river_temp

# Exécution des calculs
engine = CalculatorEngine(
    equipments=st.session_state.equipments,
    specs=st.session_state.specs,
    config=st.session_state.simulation_config,
)
summary = engine.get_full_summary()

# Dashboard KPI Synthèse
st.subheader("📊 Synthèse Globale Interconnectée")
kpi_col1, kpi_col2, kpi_col3, kpi_col4, kpi_col5 = st.columns(5)

kpi_col1.metric("CAPEX Total", f"{summary['budget']['total_capex']:,.0f} €".replace(",", " "))
kpi_col2.metric("Masse Totale", f"{summary['mass_ballast']['total_mass_tonnes']:.1f} Tonnes")
kpi_col3.metric("Tirant d'eau", f"{summary['mass_ballast']['draft_m']:.2f} m", delta="Max 1.80m", delta_color="inverse" if summary['mass_ballast']['max_draft_exceeded'] else "normal")
kpi_col4.metric("Bilan Élec. Net", f"{summary['energy']['net_power_kw']:.1f} kW", f"Autonomie {summary['energy']['autonomy_hours']} h")
kpi_col5.metric("Débit Refroidissement", f"{summary['thermal']['cooling_water_flow_l_h']:.0f} L/h")

st.divider()

# Onglets thématiques
tab1, tab2, tab3, tab4, tab5, tab_eq = st.tabs([
    "💰 Budget & Frais",
    "⚖️ Lestage & Archimède",
    "⚡ Énergie & Batteries",
    "🚰 Eaux (Propre/Grise/Noire)",
    "🌡️ Thermal & Refroidissement",
    "🛠️ Gestion des Équipements",
])

# Tab 1: Budget
with tab1:
    st.header("💰 Budget & Anticipation des Frais")
    col_b1, col_b2 = st.columns(2)
    with col_b1:
        st.write(f"**CAPEX (Acquisition / Installation) :** {summary['budget']['total_capex']:,.2f} €")
        st.write(f"**OPEX (Maintenance annuelle estimée) :** {summary['budget']['total_opex_year']:,.2f} € / an")
        df_capex = pd.DataFrame(
            list(summary['budget']['capex_by_category'].items()),
            columns=["Catégorie", "Coût (€)"]
        )
        st.bar_chart(df_capex.set_index("Catégorie"))
    with col_b2:
        st.subheader("Répartition du Budget")
        st.dataframe(df_capex, width="stretch")

# Tab 2: Lestage & Archimède
with tab2:
    st.header("⚖️ Lestage, Poids et Flottabilité (Archimède)")
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        st.write(f"• **Coque nue :** {summary['mass_ballast']['hull_mass_kg'] / 1000:.1f} T")
        st.write(f"• **Équipements & Aménagements :** {summary['mass_ballast']['equipments_mass_kg'] / 1000:.1f} T")
        st.write(f"• **Masse Totale (Déplacement) :** {summary['mass_ballast']['total_mass_tonnes']:.1f} T")
        st.write(f"• **Centre de Gravité (X, Y, Z) :** ({summary['mass_ballast']['cg_x_m']}m, {summary['mass_ballast']['cg_y_m']}m, {summary['mass_ballast']['cg_z_m']}m)")
    with col_m2:
        st.write(f"• **Tirant d'eau Moyen :** {summary['mass_ballast']['draft_m']} m")
        st.write(f"• **Tirant d'eau Proue (Avant) :** {summary['mass_ballast']['draft_bow_m']} m")
        st.write(f"• **Tirant d'eau Poupe (Arrière) :** {summary['mass_ballast']['draft_stern_m']} m")
        st.write(f"• **Tirant d'air restant :** {summary['mass_ballast']['air_draft_m']} m")
        st.info(f"Statut d'Assiette : **{summary['mass_ballast']['trim_status']}**")
        if summary['mass_ballast']['max_draft_exceeded']:
            st.error("⚠️ Alerte : Tirant d'eau maximal de 1.80m dépassé !")

# Tab 3: Énergie
with tab3:
    st.header("⚡ Bilan Électrique & Autonomie Batteries")
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        st.write(f"• **Capacité Batterie Totale :** {summary['energy']['battery_capacity_kwh']} kWh")
        st.write(f"• **Production Solaire Effective :** {summary['energy']['effective_solar_prod_kw']} kW")
        st.write(f"• **Consommation Instantanée Totale :** {summary['energy']['total_consumption_kw']} kW")
        st.write(f"• **Bilan de Puissance Net :** {summary['energy']['net_power_kw']} kW")
    with col_e2:
        st.write(f"• **Consommation Journalière :** {summary['energy']['daily_cons_kwh']} kWh/j")
        st.write(f"• **Production Journalière :** {summary['energy']['daily_prod_kwh']} kWh/j")
        st.write(f"• **Bilan Journalier :** {summary['energy']['daily_balance_kwh']} kWh/j")
        st.success(f"Autonomie Estimée sur Batterie : **{summary['energy']['autonomy_hours']} heures**")

# Tab 4: Eaux
with tab4:
    st.header("🚰 Gestion des Eaux (Propre, Grise, Noire)")
    col_w1, col_w2, col_w3 = st.columns(3)
    with col_w1:
        st.subheader("💧 Eau Propre")
        st.write(f"Capacité : {summary['water']['clean_capacity_l']} L")
        st.write(f"Volume Actuel : {summary['water']['clean_volume_l']} L")
        st.write(f"Flux : {summary['water']['clean_flow_l_h']} L/h")
        st.info(f"Autonomie : {summary['water']['clean_autonomy_days']} jours")
    with col_w2:
        st.subheader("🧼 Eaux Grises")
        st.write(f"Capacité : {summary['water']['grey_capacity_l']} L")
        st.write(f"Volume Actuel : {summary['water']['grey_volume_l']} L")
        st.write(f"Flux : {summary['water']['grey_flow_l_h']} L/h")
    with col_w3:
        st.subheader("🚽 Eaux Noires")
        st.write(f"Capacité : {summary['water']['black_capacity_l']} L")
        st.write(f"Volume Actuel : {summary['water']['black_volume_l']} L")
        st.write(f"Flux : {summary['water']['black_flow_l_h']} L/h")

# Tab 5: Thermal
with tab5:
    st.header("🌡️ Régulation Thermique & Échangeur Eau de Rivière")
    st.markdown("Basé sur la formule de transfert thermique $Q = m \\cdot C_p \\cdot \\Delta T$.")
    col_t1, col_t2 = st.columns(2)
    with col_t1:
        st.write(f"• **Chaleur Générée (Moteur/Batteries/Habitat) :** {summary['thermal']['total_heat_gen_kw']} kW")
        st.write(f"• **Chaleur Requise (Chauffage/Habitat) :** {summary['thermal']['total_heat_req_kw']} kW")
        st.write(f"• **Excédent Thermique à Dissiper :** {summary['thermal']['net_thermal_gen_kw']} kW")
    with col_t2:
        st.write(f"• **Température Eau Rivière :** {summary['thermal']['river_water_temp_c']} °C")
        st.write(f"• **Delta T Réchauffement Eau :** {summary['thermal']['delta_t_c']} °C")
        st.success(f"Débit d'eau de rivière nécessaire : **{summary['thermal']['cooling_water_flow_l_h']} L/h**")

# Tab 6: Gestion des Équipements (Modification/Ajout)
with tab_eq:
    st.header("🛠️ Liste & Édition des Équipements Interconnectés")
    data_list = [e.to_dict() for e in st.session_state.equipments]
    df_equipments = pd.DataFrame(data_list)

    edited_df = st.data_editor(df_equipments, num_rows="dynamic", width="stretch")

    if st.button("💾 Enregistrer les Modifications"):
        new_equipments = []
        for idx, row in edited_df.iterrows():
            new_equipments.append(Equipment.from_dict(row.to_dict()))
        st.session_state.equipments = new_equipments
        storage = StorageManager()
        storage.save_json(new_equipments)
        storage.save_sqlite(new_equipments)
        st.success("Modifications enregistrées et recalculées avec succès !")
        st.rerun()

# Section Export Edge Server / MQTT
st.divider()
st.subheader("📡 Intégration Edge Server & MQTT")
if st.button("📤 Générer les Payloads MQTT (Home Assistant)"):
    mqtt_topics = EdgeConnector.format_mqtt_payloads(summary)
    st.json(mqtt_topics)
