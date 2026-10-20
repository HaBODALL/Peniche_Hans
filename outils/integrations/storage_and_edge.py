"""
Gestionnaire de persistance (JSON / SQLite) et connecteur MQTT / Edge Server.
"""

import json
import sqlite3
from pathlib import Path
from typing import List, Dict, Any
from outils.core.models import Equipment, BargeSpecs, SimulationConfig


class StorageManager:
    """Gère la sauvegarde et le chargement des équipements en JSON ou SQLite."""

    def __init__(self, data_dir: str = "outils/data"):
        self.data_dir = Path(data_dir)
        self.data_dir.mkdir(parents=True, exist_ok=True)
        self.json_path = self.data_dir / "equipments.json"
        self.db_path = self.data_dir / "barge_data.db"
        self._init_sqlite()

    def _init_sqlite(self):
        """Initialise la table SQLite si elle n'existe pas."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS equipments (
                id TEXT PRIMARY KEY,
                data_json TEXT NOT NULL
            )
        """)
        conn.commit()
        conn.close()

    def save_json(self, equipments: List[Equipment]):
        """Sauvegarde la liste des équipements dans un fichier JSON."""
        data = [e.to_dict() for e in equipments]
        with open(self.json_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def load_json(self) -> List[Equipment]:
        """Charge les équipements depuis le fichier JSON."""
        if not self.json_path.exists():
            return []
        with open(self.json_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        return [Equipment.from_dict(item) for item in data]

    def save_sqlite(self, equipments: List[Equipment]):
        """Sauvegarde les équipements dans SQLite."""
        conn = sqlite3.connect(self.db_path)
        cursor = conn.cursor()
        cursor.execute("DELETE FROM equipments")
        for e in equipments:
            cursor.execute(
                "INSERT INTO equipments (id, data_json) VALUES (?, ?)",
                (e.id, json.dumps(e.to_dict(), ensure_ascii=False))
            )
        conn.commit()
        conn.close()


class EdgeConnector:
    """Simule / Prépare l'export des données interconnectées vers MQTT / Home Assistant Edge."""

    @staticmethod
    def format_mqtt_payloads(summary: Dict[str, Any]) -> Dict[str, str]:
        """Génère les messages MQTT sous forme de topics/payloads JSON."""
        topics = {}

        # Topic Budget
        topics["peniche/analytics/budget"] = json.dumps(summary["budget"], ensure_ascii=False)

        # Topic Lestage & Archimède
        topics["peniche/analytics/ballast"] = json.dumps(summary["mass_ballast"], ensure_ascii=False)

        # Topic Énergie
        topics["peniche/analytics/energy"] = json.dumps(summary["energy"], ensure_ascii=False)

        # Topic Eaux
        topics["peniche/analytics/water"] = json.dumps(summary["water"], ensure_ascii=False)

        # Topic Thermique
        topics["peniche/analytics/thermal"] = json.dumps(summary["thermal"], ensure_ascii=False)

        return topics
