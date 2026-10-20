"""
Tests unitaires pour le moteur de calcul et le modèle de données de la Péniche Freycinet.
"""

import pytest
from outils.core.models import Equipment, BargeSpecs, SimulationConfig
from outils.core.default_data import get_default_equipment_list
from outils.core.calculator import CalculatorEngine
from outils.integrations.storage_and_edge import StorageManager, EdgeConnector


def test_equipment_mass_calculation():
    eq = Equipment(
        id="cuve_test",
        name="Cuve Test 1000L",
        category="Eaux/Cuves",
        mass_empty_kg=100.0,
        mass_full_kg=1100.0,
        fill_percentage=50.0,
    )
    assert eq.current_mass_kg == 600.0


def test_calculator_budget():
    eqs = [
        Equipment(id="eq1", name="Eq 1", category="Cat A", cost_buy=1000.0, cost_maintenance_year=50.0),
        Equipment(id="eq2", name="Eq 2", category="Cat B", cost_buy=2000.0, cost_maintenance_year=100.0),
    ]
    engine = CalculatorEngine(eqs)
    budget = engine.calculate_budget()

    assert budget["total_capex"] == 3000.0
    assert budget["total_opex_year"] == 150.0
    assert budget["capex_by_category"]["Cat A"] == 1000.0


def test_calculator_ballast_and_draft():
    eqs = get_default_equipment_list()
    specs = BargeSpecs()
    engine = CalculatorEngine(eqs, specs)
    mass_ballast = engine.calculate_mass_and_ballast()

    assert mass_ballast["total_mass_tonnes"] > 100.0
    assert mass_ballast["draft_m"] > 0.5
    assert mass_ballast["draft_m"] < 1.80  # Limite Freycinet
    assert mass_ballast["max_draft_exceeded"] is False


def test_calculator_energy_modes():
    eqs = get_default_equipment_list()
    config_repos = SimulationConfig(mode="repos")
    engine_repos = CalculatorEngine(eqs, config=config_repos)
    summary_repos = engine_repos.get_full_summary()

    config_nav = SimulationConfig(mode="navigation", propulsion_power_kw=50.0)
    engine_nav = CalculatorEngine(eqs, config=config_nav)
    summary_nav = engine_nav.get_full_summary()

    assert summary_nav["energy"]["propulsion_load_kw"] == 50.0
    assert summary_repos["energy"]["propulsion_load_kw"] == 0.0
    assert summary_nav["energy"]["total_consumption_kw"] > summary_repos["energy"]["total_consumption_kw"]


def test_calculator_thermal():
    eqs = get_default_equipment_list()
    engine = CalculatorEngine(eqs)
    thermal = engine.calculate_thermal()

    assert thermal["net_thermal_gen_kw"] > 0
    assert thermal["cooling_water_flow_l_h"] > 0


def test_mqtt_export():
    eqs = get_default_equipment_list()
    engine = CalculatorEngine(eqs)
    summary = engine.get_full_summary()
    topics = EdgeConnector.format_mqtt_payloads(summary)

    assert "peniche/analytics/budget" in topics
    assert "peniche/analytics/energy" in topics
    assert "peniche/analytics/ballast" in topics
