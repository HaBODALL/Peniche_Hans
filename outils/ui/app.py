"""
Interface Web Interactive Streamlit pour le Dimensionnement Interconnecté de la Péniche Freycinet.
Gère Budget, Financement, Lestage/Masses/Stabilité GM, Énergie, Eaux et Régulation Thermique.
"""

import sys
from pathlib import Path
import json

root_dir = Path(__file__).resolve().parent.parent.parent
if str(root_dir) not in sys.path:
    sys.path.insert(0, str(root_dir))

import streamlit as st
import pandas as pd
from outils.core.models import Equipment, BargeSpecs, SimulationConfig, FinancialPlan
from outils.core.default_data import get_default_equipment_list
from outils.core.calculator import CalculatorEngine
from outils.integrations.storage_and_edge import StorageManager, EdgeConnector

st.set_page_config(
    page_title="Dimensionnement & Gestion Péniche Freycinet",
    page_icon="⚓",
    layout="wide",
)

st.title("⚓ Outil Interconnecté de Dimensionnement & Suivi - Péniche Freycinet")

# Message permanent d'avertissement et de non-certification navale
st.warning(CalculatorEngine.DISCLAIMER_TEXT)

# Initialisation de la session state
if "equipments" not in st.session_state:
    st.session_state.equipments = get_default_equipment_list()

if "simulation_config" not in st.session_state:
    st.session_state.simulation_config = SimulationConfig()

if "financial_plan" not in st.session_state:
    st.session_state.financial_plan = FinancialPlan()

if "specs" not in st.session_state:
    st.session_state.specs = BargeSpecs()

# Sidebar - Configuration
st.sidebar.header("⚙️ Configuration du Scénario")
mode = st.sidebar.radio("Mode d'opération", ["repos", "navigation"], index=0 if st.session_state.simulation_config.mode == "repos" else 1)
nav_hours = st.sidebar.slider("Heures de navigation / jour", 0.0, 12.0, st.session_state.simulation_config.navigation_hours_per_day, 0.5)
prop_power = st.sidebar.slider("Puissance propulsion croisière (kW)", 10.0, 100.0, st.session_state.simulation_config.propulsion_power_kw, 5.0)
solar_factor = st.sidebar.slider("Facteur d'ensoleillement solaire", 0.0, 1.0, st.session_state.simulation_config.solar_irradiance_factor, 0.1)

st.sidebar.header("📐 Paramètres Coque & Archimède")
block_coeff = st.sidebar.slider("Coefficient de Bloc Coque", 0.80, 1.00, st.session_state.specs.block_coefficient, 0.01)
st.session_state.specs.block_coefficient = block_coeff

# Mise à jour config
st.session_state.simulation_config.mode = mode
st.session_state.simulation_config.navigation_hours_per_day = nav_hours
st.session_state.simulation_config.propulsion_power_kw = prop_power
st.session_state.simulation_config.solar_irradiance_factor = solar_factor

# Exécution des calculs
engine = CalculatorEngine(
    equipments=st.session_state.equipments,
    specs=st.session_state.specs,
    config=st.session_state.simulation_config,
    financial_plan=st.session_state.financial_plan,
)
summary = engine.get_full_summary()

# Alertes réglementaires
st.subheader("🚨 Alertes & Conformité Réglementaire")
for alert in summary["alerts"]:
    if alert["level"] == "DANGER":
        st.error(f"**[{alert['type']}]** {alert['message']}")
    elif alert["level"] == "AVERTISSEMENT":
        st.warning(f"**[{alert['type']}]** {alert['message']}")
    else:
        st.info(f"**[{alert['type']}]** {alert['message']}")

st.divider()

# Dashboard KPI Synthèse
st.subheader("📊 Synthèse Globale Interconnectée")
kpi_col1, kpi_col2, kpi_col3, kpi_col4, kpi_col5 = st.columns(5)

kpi_col1.metric("CAPEX Total (+15% imp.)", f"{summary['financials']['total_capex']:,.0f} €".replace(",", " "))
kpi_col2.metric("Masse Totale", f"{summary['mass_ballast']['total_mass_tonnes']:.1f} Tonnes")
kpi_col3.metric("Tirant d'eau", f"{summary['mass_ballast']['draft_m']:.2f} m", delta="Max 1.80m", delta_color="inverse" if summary['mass_ballast']['max_draft_exceeded'] else "normal")
kpi_col4.metric("Stabilité GM", f"{summary['mass_ballast']['stability_gm_m']:.2f} m", delta="Seuil min 0.30m")
kpi_col5.metric("Débit Refroidissement", f"{summary['thermal']['cooling_water_flow_l_h']:.0f} L/h")

st.divider()

# Onglets
tab1, tab_fin, tab2, tab3, tab4, tab5, tab_eq = st.tabs([
    "💰 Budget & Frais",
    "🏦 Plan de Financement",
    "⚖️ Lestage & Stabilité GM",
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
        st.write(f"• **CAPEX Équipements Bruts :** {summary['financials']['base_capex']:,.2f} €")
        st.write(f"• **Taux d'Imprévus (15% Bible 6.3) :** +{summary['financials']['contingency_eur']:,.2f} €")
        st.write(f"• **CAPEX Total Sécurisé :** {summary['financials']['total_capex']:,.2f} €")
        st.write(f"• **OPEX Total (Maintenance + Redevance COT VNF + Assurance) :** {summary['financials']['total_opex_year']:,.2f} € / an")
    with col_b2:
        df_capex = pd.DataFrame(
            [{"Catégorie": e.category, "Coût (€)": e.cost_buy, "Statut": e.status} for e in st.session_state.equipments]
        )
        st.dataframe(df_capex, width="stretch")

# Tab Financement
with tab_fin:
    st.header("🏦 Financement & Plan de Trésorerie")
    f_col1, f_col2 = st.columns(2)
    with f_col1:
        st.session_state.financial_plan.personal_contribution_eur = st.number_input(
            "Apport Personnel (€)", value=st.session_state.financial_plan.personal_contribution_eur
        )
        st.session_state.financial_plan.loan_purchase_eur = st.number_input(
            "Prêt Achat (€)", value=st.session_state.financial_plan.loan_purchase_eur
        )
        st.session_state.financial_plan.loan_renovation_eur = st.number_input(
            "Prêt Travaux (€)", value=st.session_state.financial_plan.loan_renovation_eur
        )
    with f_col2:
        st.session_state.financial_plan.loan_interest_rate_pct = st.number_input(
            "Taux d'Intérêt Prêt (%)", value=st.session_state.financial_plan.loan_interest_rate_pct
        )
        st.session_state.financial_plan.loan_duration_years = st.number_input(
            "Durée Prêt (Années)", value=st.session_state.financial_plan.loan_duration_years
        )
        st.write(f"• **Mensualité estimée :** {summary['financials']['monthly_loan_payment_eur']:,.2f} € / mois")
        st.write(f"• **Financement Mobilisé :** {summary['financials']['total_funding_eur']:,.2f} €")
        st.write(f"• **Reste à Financer :** {summary['financials']['remaining_funding_eur']:,.2f} €")

# Tab 2: Lestage & Stabilité
with tab2:
    st.header("⚖️ Lestage, Archimède et Stabilité Métacentrique (GM)")
    col_m1, col_m2 = st.columns(2)
    with col_m1:
        st.write(f"• **Masse Totale (Déplacement) :** {summary['mass_ballast']['total_mass_tonnes']:.1f} Tonnes")
        st.write(f"• **Coefficient de Bloc :** {summary['mass_ballast']['block_coefficient']}")
        st.write(f"• **Tirant d'eau Archimède :** {summary['mass_ballast']['draft_m']} m (Max 1.80m)")
        st.write(f"• **Tirant d'air restant :** {summary['mass_ballast']['air_draft_m']} m")
    with col_m2:
        st.subheader("Détail de Stabilité Transversale")
        st.write(f"• **KB (Centre de carène) :** {summary['mass_ballast']['stability_details']['kb_m']} m")
        st.write(f"• **BM (Rayon métacentrique) :** {summary['mass_ballast']['stability_details']['bm_m']} m")
        st.write(f"• **KG (Centre de gravité) :** {summary['mass_ballast']['stability_details']['kg_m']} m")
        st.write(f"• **Perte Carène Liquide (Cuves) :** -{summary['mass_ballast']['stability_details']['free_surface_loss_m']} m")
        st.success(f"**Hauteur métacentrique GM finale : {summary['mass_ballast']['stability_gm_m']} m** (Seuil sécurité > 0.30m)")

# Tab 3: Énergie
with tab3:
    st.header("⚡ Bilan Électrique & Autonomie Batteries")
    col_e1, col_e2 = st.columns(2)
    with col_e1:
        st.write(f"• **Capacité Batterie Totale :** {summary['energy']['battery_capacity_kwh']} kWh")
        st.write(f"• **Production Solaire Effective :** {summary['energy']['effective_solar_prod_kw']} kW")
        st.write(f"• **Consommation Instantanée :** {summary['energy']['total_consumption_kw']} kW")
    with col_e2:
        st.write(f"• **Bilan de Puissance Net :** {summary['energy']['net_power_kw']} kW")
        st.success(f"Autonomie Estimée sur Batterie : **{summary['energy']['autonomy_hours']} heures**")

# Tab 4: Eaux
with tab4:
    st.header("🚰 Gestion des Eaux (Propre, Grise, Noire)")
    col_w1, col_w2, col_w3 = st.columns(3)
    with col_w1:
        st.subheader("💧 Eau Propre")
        st.write(f"Capacité : {summary['water']['clean_capacity_l']} L")
        st.write(f"Autonomie : {summary['water']['clean_autonomy_days']} jours")
    with col_w2:
        st.subheader("🧼 Eaux Grises")
        st.write(f"Capacité : {summary['water']['grey_capacity_l']} L")
    with col_w3:
        st.subheader("🚽 Eaux Noires")
        st.write(f"Capacité : {summary['water']['black_capacity_l']} L")

# Tab 5: Thermal
with tab5:
    st.header("🌡️ Régulation Thermique & Échangeur Eau de Rivière")
    st.write(f"• **Excédent Thermique à Dissiper :** {summary['thermal']['net_thermal_gen_kw']} kW")
    st.write(f"• **COP de la Pompe à Chaleur :** {summary['thermal']['heat_pump_cop']}")
    st.success(f"Débit d'eau de rivière nécessaire : **{summary['thermal']['cooling_water_flow_l_h']} L/h**")

# Tab 6: Équipements
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

# Section Export
st.divider()
st.subheader("📦 Exportation des Rapports de Simulation & Integration Edge")
exp_col1, exp_col2 = st.columns(2)

with exp_col1:
    report_json = json.dumps(summary, indent=2, ensure_ascii=False)
    st.download_button(
        label="📥 Télécharger le Rapport Complet (JSON)",
        data=report_json,
        file_name="rapport_simulation_peniche.json",
        mime="application/json",
    )

with exp_col2:
    if st.button("📤 Afficher les Payloads MQTT (Home Assistant)"):
        mqtt_topics = EdgeConnector.format_mqtt_payloads(summary)
        st.json(mqtt_topics)
