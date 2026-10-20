# ⚓ Outil Interconnecté de Dimensionnement & Suivi (Budget, Poids/Lestage, Énergie, Eaux & Thermique)

Ce dossier contient l'outil logiciel interconnecté de dimensionnement, de simulation et de suivi pour le projet de **Péniche Freycinet**.

## 🎯 Objectifs & Fonctionnalités

L'outil modélise le bateau sous la forme d'un **système d'équipements interconnectés** :
1. **💰 Budget (CAPEX / OPEX)** : Calcul automatique du coût d'acquisition initial et des frais de maintenance annuels futurs.
2. **⚖️ Lestage & Flottabilité (Archimède)** : Calcul du poids total, du centre de gravité $(X, Y, Z)$, du tirant d'eau ($T$), de l'assiette (trim) et vérification du tirant d'air sous les ponts.
3. **⚡ Énergie & Bilan Électrique** : Bilan de puissance net (production solaire vs consommations), autonomie des batteries LiFePO4, comparaison en **mode repos (amarrage)** et **mode navigation (6h/jour par défaut)**.
4. **🚰 Gestion des Eaux (Propre, Grise, Noire)** : Calcul des réserves, des autonomies en eau potable et des flux de traitement (Phytopurification / MBR).
5. **🌡️ Régulation Thermique (Boucle d'eau)** : Calcul du transfert thermique ($Q = m \cdot C_p \cdot \Delta T$) pour dissiper la chaleur des moteurs/batteries via un échangeur d'eau de rivière filtrée ou chauffer l'habitat.
6. **📡 Connecteur Edge Server / MQTT** : Génération automatique des payloads JSON pour le serveur Edge du bateau (Home Assistant & InfluxDB).

---

## 📐 Architecture du Code

```text
outils/
├── core/
│   ├── models.py            # Dataclasses Equipment, BargeSpecs, SimulationConfig
│   ├── default_data.py      # Équipements de référence Péniche Freycinet
│   └── calculator.py        # CalculatorEngine (Moteur de calcul interconnecté)
├── ui/
│   └── app.py               # Dashboard Web interactif Streamlit
├── integrations/
│   └── storage_and_edge.py  # Sauvegarde JSON/SQLite & Export MQTT
├── tests/
│   └── test_calculator.py   # Tests unitaires Pytest
└── README.md                # Documentation de l'outil
```

---

## 🚀 Démarrage Rapide

### 1. Lancement de l'Interface Web Streamlit

Pour lancer le tableau de bord interactif :

```bash
streamlit run outils/ui/app.py
```

L'interface s'ouvre automatiquement dans votre navigateur (sur `http://localhost:8501`). Vous pouvez y ajuster en direct les paramètres de navigation, ajouter/modifier des équipements dans le tableau interactif et observer les impacts immédiats sur le tirant d'eau, l'autonomie électrique et le débit d'eau de refroidissement.

### 2. Exécution des Tests Unitaires

Pour vérifier le bon fonctionnement des formules physiques et logiques :

```bash
PYTHONPATH=. pytest outils/tests/test_calculator.py
```

---

## 🔗 Références & Bibliographie

- **Bible Technique du Projet** : `docs/BIBLE_TECHNIQUE_PENICHE.md`
- **Réglementation ES-TRIN & VNF** : `bibliographie/reglementation/`
- **Notice de Reprise du Projet IT** : `NOTICE_REPRISE_PROJET.md`
