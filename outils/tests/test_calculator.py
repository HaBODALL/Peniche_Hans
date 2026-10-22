"""
Tests unitaires avancés pour le moteur de calcul et la validation physique Freycinet.
"""

import pytest
from outils.core.models import Equipment, BargeSpecs, SimulationConfig, FinancialPlan
from outils.core.default_data import get_default_equipment_list
from outils.core.calculator import CalculatorEngine, calculate_archimedes_draft, calculate_metacentric_height


def test_known_freycinet_archimedes_draft():
    """
    Test physique sur un cas connu Freycinet :
    Pour une péniche de 38,50 m x 5,05 m (Surface ~ 194.4 m²) avec un coefficient de bloc Cb = 0.92,
    et un déplacement total de 220,000 kg (220 Tonnes) :
    Tirant d'eau théorique T = 220000 / (38.5 * 5.05 * 0.92 * 1000) = 1.229 m (~ 1.23 m).
    """
    specs = BargeSpecs(length_m=38.5, beam_m=5.05, block_coefficient=0.92, water_density_kg_m3=1000.0)
    draft = calculate_archimedes_draft(total_mass_kg=220000.0, specs=specs)
    assert round(draft, 2) == 1.23


def test_metacentric_height_and_free_surface():
    """
    Test de hauteur métacentrique GM et de l'impact des surfaces libres des cuves.
    """
    specs = BargeSpecs(length_m=38.5, beam_m=5.05, block_coefficient=0.92)
    eq_cuve = Equipment(
        id="cuve_large",
        name="Cuve Large",
        category="Eaux/Cuves",
        mass_empty_kg=500,
        mass_full_kg=5500,
        fill_percentage=50.0,
        tank_length_m=4.0,
        tank_width_m=2.0,  # Inertie surface libre I = (4 * 2^3)/12 = 2.667 m4
    )
    draft = calculate_archimedes_draft(total_mass_kg=150000.0, specs=specs)
    stability = calculate_metacentric_height(
        total_mass_kg=150000.0,
        cg_z_m=1.0,
        equipments=[eq_cuve],
        specs=specs,
        draft_m=draft,
    )

    assert stability["free_surface_loss_m"] > 0.0
    assert stability["gm_m"] > 0.30  # Stabilité positive


def test_compliance_alerts_es_trin_battery():
    """
    Test de détection d'alerte réglementaire ES-TRIN si parc batterie >= 20 kWh.
    """
    eqs = [
        Equipment(
            id="bat_20kwh",
            name="Batterie 25 kWh",
            category="Énergie/Batteries",
            battery_capacity_kwh=25.0,
        )
    ]
    engine = CalculatorEngine(eqs)
    alerts = engine.get_compliance_alerts()
    alert_types = [a["type"] for a in alerts]

    assert "ES-TRIN / Sécurité" in alert_types


def test_financial_plan_and_contingency():
    """
    Test du plan de financement avec taux d'imprévus de 15% (Bible 6.3).
    """
    eqs = [
        Equipment(id="eq1", name="Équipement 1", category="Cat", cost_buy=100000.0)
    ]
    fin_plan = FinancialPlan(
        personal_contribution_eur=30000.0,
        loan_purchase_eur=50000.0,
        loan_renovation_eur=30000.0,
        contingency_rate_pct=15.0,
    )
    engine = CalculatorEngine(eqs, financial_plan=fin_plan)
    summary = engine.get_full_summary()

    assert summary["financials"]["contingency_eur"] == 15000.0
    assert summary["financials"]["total_capex"] == 115000.0
    assert summary["financials"]["total_funding_eur"] == 110000.0
    assert summary["financials"]["remaining_funding_eur"] == 5000.0
