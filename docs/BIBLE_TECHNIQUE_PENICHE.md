# BIBLE TECHNIQUE DU PROJET : PÉNICHE FREYCINET HABITAT & LABO R&D

Ce document centralise l'intégralité de l'ingénierie, de la réglementation et des stratégies opérationnelles pour la transformation d'une péniche Freycinet (38,50 m × 5,05 m) en un habitat mobile semi-autonome doté d'un atelier et d'un laboratoire de R&D.

Il est issu des 6 carnets thématiques du projet et sert de référentiel unique (Single Source of Truth) pour la communication interne et externe.

> 📁 **Bibliographie & Ressources :**
> Les réglementations officielles (ES-TRIN, CEVNI, rapports CESNI) citées dans ce document sont stockées au format PDF dans le dossier racine [`/bibliographie/`](../bibliographie/).

---

## 📑 Sommaire
1. [Architecture Navale, Réglementation et Aménagement](#1-architecture-navale-réglementation-et-aménagement)
2. [Gestion des Eaux et Écologie Expérimentale](#2-gestion-des-eaux-et-écologie-expérimentale)
3. [Énergie, Électricité et Motorisation Fluviale](#3-énergie-électricité-et-motorisation-fluviale)
4. [IT, Logiciel, Supervision et Réseaux (IoT)](#4-it-logiciel-supervision-et-réseaux-iot)
5. [Mobilité Terrestre Électrique](#5-mobilité-terrestre-électrique)
6. [Gestion de Projet, Opérations et Financement](#6-gestion-de-projet-opérations-et-financement)

---

## 1. Architecture Navale, Réglementation et Aménagement

### 1.1 Macro (Vision Globale) — Cadre Réglementaire & Points Bloquants
La transformation d'une péniche au gabarit Freycinet (38,50 m × 5,05 m) en habitat fait basculer le bateau du régime de la petite plaisance vers le cadre juridique des bateaux de navigation intérieure.

**A. Les 3 Piliers Réglementaires**
*   **Standard Européen ES-TRIN (CESNI)**
    *   *Seuil de 20 mètres* : Soumis à l'obtention d'un Titre de Navigation (Certificat Communautaire).
    *   *Intégrité de la coque (Art. 3.02)* : Épaisseur minimale du bordé d'acier/sole de 3,50 mm à 3,84 mm en règle générale, et **4,80 mm pour la virure de bouchain** (zone de transition arrondie soumise aux chocs d'écluses). *Seuil bancaire (Crédit Maritime) : exigence usuelle de 3,80 mm à 4,00 mm minimum à l'expertise.*
    *   *Sécurité électrique* : Séparation physique stricte entre réseau domestique (NFC 15-100) et réseau de propulsion (400V DC).
*   **Domaine Public Fluvial (VNF / HAROPA Port)**
    *   *COT* : L'amarrage permanent repose sur une Convention d'Occupation Temporaire, précaire et non cessible de plein droit.
    *   *Mise en concurrence* : Si la péniche accueille une activité économique (labo R&D payant), le renouvellement est soumis à un appel à projets.
    *   *Gabarit* : Surélévations plafonnées à 25 % du rectangle hors-tout.
*   **Environnement "Zéro-Rejet"** : Interdiction absolue de déverser eaux noires et grises dans le milieu naturel.

```text
                     ┌─────────────────────────────────────────┐
                     │ PÉNICHE FREYCINET HABITAT / LABO (38,5m)│
                     └────────────────────┬────────────────────┘
                                          │
         ┌────────────────────────────────┼────────────────────────────────┐
         ▼                                │                                ▼
┌─────────────────────────┐               │                  ┌───────────────────────────┐
│     SÉCURITÉ NAVALE     │               │                  │     GESTION DOMANIALE     │
│    Standard ES-TRIN     │               │                  │   COT (VNF / HAROPA Port) │
├─────────────────────────┤               │                  ├───────────────────────────┤
│• Épaisseur coque ≥3,8mm │               ▼                  │• Précaire & Révocable     │
│  (bouchains 4,80 mm)    │ ┌─────────────────────────────┐  │• Limite 25% pont couvert  │
│• Titre de navigation    │ │ ASSAINISSEMENT ZÉRO-REJET   │  │• Appel à projet si activité│
│• Séparation 230V / 400V │ │   Eaux grises & noires      │  │  économique (CGPPP)       │
└─────────────────────────┘ └─────────────────────────────┘  └───────────────────────────┘
```

**B. Matrice des Points Bloquants ("No-Go" Légaux)**
1.  **Refus de Titre ES-TRIN** : Coque < 3,5 mm (ou < 4,80 mm au bouchain) $\rightarrow$ Interdiction de naviguer/stationner. *Prévention : Audit structurel et sondage ultrasons préalable complet avant achat.*
2.  **Perte de COT** : Activité économique non déclarée $\rightarrow$ Expulsion. *Prévention : Valider la COT pour activité mixte.*
3.  **Blocage Sanitaire** : Absence de système étanche agréé $\rightarrow$ Refus de COT.
4.  **Non-conformité Urbanisme/PLU** : Marquise dépassant 25 %. *Prévention : Validation des plans 3D extérieurs.*
5.  **Démotorisation non autorisée** : Retrait du moteur thermique sans accord $\rightarrow$ Reclassification en "Établissement Flottant".

### 1.2 Meso — Comparatif des Stratégies de Lestage
Pour atteindre un tirant d'eau stable (1,20 m à 1,30 m), la masse globale doit atteindre environ 220 à 240 tonnes.

| Critères d'Évaluation | Blocs de Fonte | Gueuses de Ferraille | Blocs Béton Standard | Béton Lourd (Magnétite) | Sable (Vrac) | Eau (Cuves Ballast) |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **Densité & Gain Hauteur** | 5 ($7,2\text{ t/m}^3$) | 4 ($4,0\text{ t/m}^3$) | 2 ($2,4\text{ t/m}^3$) | 3 ($3,8\text{ t/m}^3$) | 1 ($1,6\text{ t/m}^3$) | 1 ($1,0\text{ t/m}^3$) |
| **Coût d'acquisition (CAPEX)** | 2 (1000–2200 €/t) | 3 (130–190 €/t) | 5 (45–150 €/t) | 4 (150–300 €/t) | 5 (10–25 €/t) | 5 (~0 €/t) |
| **Logistique/Installation** | 2 (Grue requise) | 3 (Lourd) | 4 (Modulaire) | 4 (Modulaire) | 3 (Big Bags) | 4 (Pompe) |
| **Réversibilité** | 3 (Manutention) | 3 (Manutention) | 4 (Net) | 4 (Net) | 1 (Très difficile) | 5 (Pompage) |
| **Corrosion Coque** | 5 (Insensible) | 2 (Risque rouille) | 4 (Sec) | 4 (Sec) | 1 (Piège l'humidité) | 3 (Risque de fuite) |
| **Stabilité (Carène liquide)**| 5 (Parfaite) | 5 (Parfaite) | 5 (Parfaite) | 5 (Parfaite) | 4 (Risque glissement)| 2 (Effet carène liq.) |
| **Score Global** | **3,7 / 5** | **3,3 / 5** | **4,0 / 5** | **4,0 / 5** | **2,5 / 5** | **3,3 / 5** |

*Recommandation* : Hybride. Fond de cale en Béton Lourd entre les varangues, ajustement en Gueuses de Fonte aux extrémités.

### 1.3 Nano — Drone Sous-Marin (ROV) pour Inspection de Coque
Développement d'une plate-forme d'inspection robotisée à flot pour reporter les mises en cale sèche (intervalle 7–10 ans).

```text
┌────────────────────────────────────────────────────────────────────────┐
┌┤                   STATION DE SURFACE (PC DURCI)                       ├┐
││  - IHM / ROS 2 Supervision  - Visualisation Video HD + A-Scan OSD      ││
││  - Traitement MAVLink       - Fichier journal binaire infalsifiable   ││
└└───────────────────────────────────┬───────────────────────────────────┘┘
                                     │
                    OMBILICAL HIGH-SPEED / POWER
                                     │
┌────────────────────────────────────┴───────────────────────────────────┐
┌┤                   ROV SOUS-MARIN (BlueROV2 Heavy)                     ├┐
││  ┌─────────────────────────┐             ┌─────────────────────────┐  ││
││  │ CALCULATEUR COMPAGNON   │             │ PILOTE AUTOMATIQUE      │  ││
││  │ Nvidia Jetson / ROS 2   │◄──USB/MAV──►│ Pixhawk / ArduSub       │  ││
││  └────────────┬────────────┘             └────────────┬────────────┘  ││
││               ▼                                       ▼               ││
││  ┌──────────┐ ┌───────────────┐         ┌───────────┐ ┌─────────────┐ ││
││  │ CAPTEUR  │ │ TÉLÉMÉTRIE    │         │ SENSORS   │ │ PROPULSION  │ ││
││  │ ULTRASONS│ │ DVL A50       │         │ Bar02/30  │ │ 8x T200     │ ││
││  │ Cygnus   │ │ (WaterLinked) │         │ IMU 9-DoF │ │ Vecteurs    │ ││
││  └────┬─────┘ └───────────────┘         └───────────┘ └─────────────┘ ││
││       ▼                                                               ││
││  ┌─────────────────────────────────────────────────────────────────┐  ││
││  │ PALPEUR UT MULTI-ÉCHO sur Cardan à ressort (Spring-Loaded)      │  ││
││  └─────────────────────────────────────────────────────────────────┘  ││
└└───────────────────────────────────────────────────────────────────────┘┘
```
*   **Technique d'Inspection à Distance (RIT)** : IACS UR Z17 / ISO 9712. L'expert fluvial doit être présent physiquement sur le site.
*   **Physique Multi-Écho** : Élimine mathématiquement l'épaisseur des peintures anticorrosion sans meulage.
*   **Architecture Matérielle** : BlueROV2 Heavy (6-DoF), Skid à roues magnétiques NdFeB pour se ventouser, palpeur Cygnus sur cardan à ressorts ($\pm 15^\circ$ d'alignement).
*   **Logiciel (ROS 2)** : Nœud `cygnus_ut_driver` filtre les faux échos ($|t_1 - t_2| \le \epsilon$).

### 1.4 Pratique — Aménagement PMR en Cale Freycinet

```text
                     COUPE TRANSVERSALE CALE FREYCINET AMÉNAGÉE PMR

               ◄───────────────── 5,05 m (Largeur hors-tout) ──────────────►
 ┌──────────┐  ╔═══════════════════════════════════════════════════════════╗  ┌──────────┐
 │ PLAQUE   │  ║  ISOLATION POLYURÉTHANE PROJETÉE (10-12 cm par flanc)     ║  │ PLAQUE   │
 │ ACIER    │  ║  ┌─────────────────────────────────────────────────────┐  ║  │ ACIER    │
 │ BORDÉ    │  ║  │    ESPACE UTILE AMÉNAGÉ NET (~4,20 m à 4,40 m)      │  ║  │ BORDÉ    │
 └────┬─────┘  ║  │                                                     │  ║  └────┬─────┘
      │        ║  │    ┌──────────────────┐     ┌──────────────────┐    │  ║       │
      │        ║  │    │ CLOISON / MEUBLE │     │ COULOIR CENTRAL  │    │  ║       │
      │        ║  │    │ PORTE GALANDAGE  │     │ PASSAGE ≥ 120 cm │    │  ║       │
      │        ║  │    │ Passage ≥ 83 cm  │     │ (Giration 150cm) │    │  ║       │
      │        ║  │    └────────┬─────────┘     └────────┬─────────┘    │  ║       │
      │        ║  └─────────────┼────────────────────────┼──────────────┘  ║       │
      │        ║ ═══════════════╧════════════════════════╧════════════════ ║       │
      │        ║   PLANCHER DE CALE NIVELÉ SUR LEST (Planéité < 5mm)      ║       │
      │        ╚═══════════════════════════════════════════════════════════╝       │
      └─────────────────────────────────┬──────────────────────────────────────────┘
                                ┌───────┴───────┐
                                │ VARANGUES &   │
                                │ LEST BÉTON/   │
                                │ FONTE         │
                                └───────────────┘
```
**Checklist Étape par Étape :**
1.  **Franchissement Vertical** : Élévateur PMR vertical (entraînement à vis sans fin 230V). Plateforme $\ge 90\times140$ cm.
2.  **Nivellement & Circulations** : Axe de circulation central de $120\text{ cm}$. Aire de rotation de $150\text{ cm}$ de diamètre dans chaque zone (Entrée, Salon, SDB). Revêtement R10/PN12.
3.  **Portes & Seuils** : Portes à galandage suspendues passage net $\ge 83\text{ cm}$. Seuil max 2 cm avec bords chanfreinés à 33 %.
4.  **Sanitaires** : Douche plain-pied $120\times90\text{ cm}$ avec pompe de relevage automatique d'eaux grises.

---

## 2. Gestion des Eaux et Écologie Expérimentale

### 2.1 Macro — Réglementation et Interdictions
*   **Interdiction stricte de rejet brut** : Aucun rejet d'eaux noires brutes (toilettes) n'est toléré dans le réseau fluvial français.
*   **Tolérance d'épuration autonome (Chapitre 18 ES-TRIN)** : Le seul rejet d'eaux vannes autorisé est celui issu d'une station d'épuration homologuée selon le **Chapitre 18 de l'ES-TRIN (Article 18.01)** ($\text{DBO}_5 \le 25\text{ mg/L}$, $\text{DCO} \le 125\text{ mg/L}$).
*   **Doctrines Domaniales** : VNF et HAROPA imposent le raccordement direct au réseau d'assainissement collectif urbain à quai ou la rétention totale avec vidange par camion.

### 2.2 Meso — Comparatif des Filières d'Assainissement
| Critère d'Analyse | Station Industrielle MBR (Bioréacteur) | Phytoépuration Flottante | Bokashi + Toilettes Sèches (Séparation) |
| :--- | :--- | :--- | :--- |
| **Efficacité d'Épuration** | Excellente : $\text{DBO}_5 \le 10\text{ mg/L}$, $> 99,99\%$ élimination bactérienne | Fluctuante : Abattement 75-85%, sensible au froid | Inapplicable sur jus (lixiviat $\text{DCO} > 1000\text{ mg/L}$) |
| **Conformité VNF / ES-TRIN**| Totale : Homologuée Chapitre 18 (Art. 18.01) | Incertaine sans agrément spécifique | Non conforme pour rejets liquides |
| **Encombrement Navals** | Optimisé : Emprise $0,8$ à $1,5\text{ m}^2$ | Incompatible en coque (jusqu'à 7,5 tonnes) | Minimal |
| **Autonomie Énergétique** | Dépendante : $35\text{ W}$ en continu ($1\text{ kWh/jour}$) | Haute : Passif ($0\text{ kWh/jour}$) | Absolue : $100\%$ manuelle |

### 2.3 Nano — Ingénierie de la Méthanisation
Pour un système de méthanisation (digesteur) expérimental (2 à 4 personnes) :
*   **Risques** : En milieu confiné (péniche), les fuites de $CH_4$ et $H_2S$ présentent un danger d'asphyxie et d'explosion.
*   **Sécurité IoT** : Architecture de surveillance requise pour la gestion des vannes et la ventilation forcée.

### 2.4 Pratique — Architecture Hydraulique Bi-carburation
Conception de réseaux sanitaires en bi-carburation : un circuit classique gravitaire conforme (orienté vers le MBR ou les cuves de rétention) et une **boucle expérimentale de test** pour éprouver de nouvelles méthodes de filtration grise sans risque de pollution du milieu.

---

## 3. Énergie, Électricité et Motorisation Fluviale

### 3.1 Macro — Prérequis ES-TRIN (Bloc 1 et Bloc 2)
Pour une péniche Freycinet, l'ES-TRIN impose une étanchéité fonctionnelle absolue.
*   **Bloc 1 (Habitat)** : 230V AC / 24V DC.
*   **Bloc 2 (Propulsion)** : 400V DC.
*   **Régime IT & CPI** : Les réseaux doivent avoir des pôles flottants isolés de la coque en acier. Deux Contrôleurs Permanents d'Isolement (CPI) distincts et découplés doivent être installed.
*   **Compartimentage (Article 10.11, chiffre 17 de l'ES-TRIN)** : Les batteries Lithium $\ge 20\text{ kWh}$ exigent un local ou un caisson protégé classe coupe-feu **A60**, avec ventilation mécanique directe vers le pont ouvert et système d'extinction d'incendie. *Interdit dans les locaux d'habitation.*
*   **Délestage** : L'automate (PMS) garantit la priorité absolue à la propulsion, délestant automatiquement l'habitat en cas d'appel de puissance.

### 3.2 Meso — Rétrofit Professionnel vs Semi-DIY
*   **Semi-DIY (Composants auto/industrie d'occasion)** : Impasse réglementaire. Impossibilité de certifier les batteries réassemblées (EN 62619). Entraîne le refus de certificat, déchéance d'assurance, et inéligibilité aux aides.
*   **Pro Clé en Main** : Certifié, couvert par les assurances, et éligible aux primes CEE (TRA-EQ-126) et subventions VNF/PAMI.

### 3.3 Nano — Contrôleur de Batterie (BMS) 400V DC
Cahier des charges pour un pack LFP expérimental :
*   Conformité EN 62619 (sécurité) et EN 62620.
*   Interface CAN-bus / Modbus TCP isolée galvaniquement pour dialoguer avec l'inverter.
*   Isolation galvanique renforcée entre la mesure HT (400V) et les bus 24V.

### 3.4 Pratique — Déploiement Solaire sur le Roof
*   **Matériel** : Panneaux ETFE (éthylène tétrafluoroéthylène) flexibles.
*   **Montage critique** : Le collage direct sur acier sombre entraîne des surchauffes (perte de 15-18% de rendement). Solution : montage sur sous-couche polycarbonate alvéolaire créant une **lame d'air de 10 à 15 mm**.
*   **Architecture de conversion** : Multiplier les régulateurs MPPT indépendants pour contrer l'ombrage du mât et des berges.

---

## 4. IT, Logiciel, Supervision et Réseaux (IoT)

### 4.1 Macro — Architecture Informatique Globale & Autonomie Offline-First
Pour maintenir une opérabilité critique à 100 % face aux coupures de connexion prolongées, l'infrastructure embarquée repose sur un paradigme Offline-First.

```text
+-----------------------------------------------------------------------------------+
|                            POSTES CLIENTS (Tablettes / Android)                   |
|              Jetpack Room DB (Single Source of Truth) <---> WorkManager           |
+-----------------------------------------------------------------------------------+
                                          | (Wi-Fi Local Intranet)
                                          v
+-----------------------------------------------------------------------------------+
|                             SERVEUR LOCAL EDGE (FANLESS)                          |
|  - OS Read-Only (OverlayFS) + Hardware Watchdog                                   |
|  - Middleware : Signal K (N2K/Modbus) <---> Broker MQTT <---> Home Assistant      |
|  - Moteurs de stockage : InfluxDB / SQLite (Partition de persistance NVMe PLP)    |
+-----------------------------------------------------------------------------------+
                                          |
                      +-------------------+-------------------+
                      | (Modbus / MQTT)                       | (N2K / CAN)
                      v                                       v
         [Génération Solaire & Victron]           [Capteurs Moteur & Navigation]
```
*   **VLANs Sectorisés** : VLAN 10 (Navigation), VLAN 20 (Gestion Énergétique), VLAN 30 (Clients), VLAN 40 (WAN 4G/Starlink).
*   **Clients Android** : Utilisent `Jetpack Room DB`. Le `WorkManager` synchronise les données en arrière-plan lorsque le Wi-Fi local est retrouvé.

### 4.2 Meso — Comparaison des Technologies Sans Fil (Cage de Faraday)
À l'intérieur d'une coque en acier, les cloisons créent une cavité résonnante sujette au *fading*.

| Protocole | Pénétration Coque | Immuabilité Multi-trajets | Débit | Consommation / Autonomie |
| :--- | :--- | :--- | :--- | :--- |
| **Wi-Fi Classique (2.4/5GHz)** | Très faible (Bloqué 1er pont) | Moyenne | 10 Mbps à 1 Gbps | Élevée (Jours/Semaines) |
| **Bluetooth Mesh** | Faible (Relais nécessaires) | Faible (Résonances) | 10 à 50 kbps | Asymétrique |
| **LoRaWAN (Sub-GHz)** | Excellente (Franchit 2-3 ponts) | Maximale (CSS) | 0.3 à 50 kbps | Ultra-faible (5-10 ans) |
| **Wi-Fi HaLow (802.11ah)** | Excellente (Diffraction + OFDM) | Très haute | 150 kbps à 15 Mbps| Ultra-faible (2-5 ans) |

*Verdict* : LoRaWAN pour les capteurs sur piles (fuite, température). Wi-Fi HaLow pour la télémétrie IP native (caméras, vibrations moteur).

### 4.3 Nano — Code Python d'Extraction API (EuRIS / VNF)
Script complet permettant de récupérer et superposer les données de navigation publiques (WFS et OData V4) sur une cartographie autonome.

```python
import requests
import json
import folium
from folium import plugins

class InlandWaterwaysDataExtractor:
    EURIS_BASE_URL = "https://www.eurisportal.eu/visuris/api"

    def __init__(self, euris_api_token=None):
        self.euris_token = euris_api_token
        self.session = requests.Session()
        self.session.headers.update({"Accept": "application/json", "User-Agent": "Péniche-SCADA/1.0"})
        if self.euris_token:
            self.session.headers.update({"Authorization": f"Bearer {self.euris_token}"})

    def fetch_euris_berths(self, top=50, skip=0):
        endpoint = f"{self.EURIS_BASE_URL}/Berth/GetCompactBerths"
        try:
            response = self.session.get(endpoint, params={"$top": top, "$skip": skip}, timeout=15)
            response.raise_for_status()
            return response.json().get("items", [])
        except requests.exceptions.RequestException as e:
            print(f"Erreur d'extraction EuRIS Berth API: {e}")
            return []

    def fetch_vnf_wfs_polygons(self, wfs_url, type_name):
        params = {"service": "WFS", "version": "2.0.0", "request": "GetFeature", "typeName": type_name, "outputFormat": "application/json"}
        response = requests.get(wfs_url, params=params, timeout=20)
        return response.json()

    def transform_berths_to_geojson(self, berths_list):
        features = []
        for berth in berths_list:
            geometry = berth.get("geometry")
            if not geometry and "longitude" in berth and "latitude" in berth:
                geometry = {"type": "Point", "coordinates": [float(berth["longitude"]), float(berth["latitude"])]}
            if geometry:
                status_code = berth.get("berthStatus", 0)
                features.append({
                    "type": "Feature", "geometry": geometry,
                    "properties": {
                        "isrs": berth.get("isrsCode", "N/A"),
                        "name": berth.get("objectName", "Zone"),
                        "status": status_code
                    }
                })
        return {"type": "FeatureCollection", "features": features}

def generate_interactive_map(geojson_data, output_html="carte_amarrage_locale.html"):
    m = folium.Map(location=[48.8566, 2.3522], zoom_start=12, tiles="CartoDB positron")
    def style_function(feature):
        status = feature["properties"].get("status", 0)
        colors = {0: "#2ecc71", 1: "#f1c40f", 2: "#e74c3c"}
        return {"fillColor": colors.get(status, "#9b59b6"), "color": "#111", "weight": 1.5, "fillOpacity": 0.7}
    folium.GeoJson(geojson_data, style_function=style_function).add_to(m)
    m.save(output_html)

if __name__ == "__main__":
    extractor = InlandWaterwaysDataExtractor(euris_api_token="VOTRE_JETON_PAT_EURIS")
    raw_berths = extractor.fetch_euris_berths(top=50)
    geojson_berths = extractor.transform_berths_to_geojson(raw_berths)
    generate_interactive_map(geojson_berths)
```

### 4.4 Pratique — Plan de Sauvegarde & Redondance Matérielle Fluviale
```text
                                  [Réseau Bord 24V DC / Alternateur]
                                                  |
                                     [Module OR-ing FET (Redondance 1+1)]
                                                  |
                                     [DC-UPS 24V (Supercondensateurs / LiFePO4)]
                                                  |
+---------------------------------------------------------------------------------------------------+
| ARMOIRE ÉTANCHE THERMORÉGULÉE (IP55/IP66 - Refroidissement Peltier / Caloducs en Circuit Fermé)   |
|   +-------------------------------------------------------------------------------------------+   |
|   | CHÂSSIS SERVEUR FANLESS (Monté sur Silentblocs Viton + Amortisseurs à câbles hélicoïdaux) |   |
|   | - Cartes électroniques : Conformal Coating Polyuréthane (IPC-CC-830C)                     |   |
|   | - Stockage : Array RAID 10 ZFS Mirroring SSD NVMe Entreprise (Condensateurs PLP)          |   |
|   +-------------------------------------------------------------------------------------------+   |
+---------------------------------------------------------------------------------------------------+
```
*   **Vibrations** : HDD bannis (destruction des têtes). SSD NVMe certifiés MIL-STD-810H avec PLP (Power Loss Protection), montés sur amortisseurs à câbles hélicoïdaux.
*   **Alimentation 24V Native** : Suppression des conversions AC/DC avec un contrôleur DC-UPS à supercondensateurs lissant les chocs de tension du moteur (crank surge).
*   **Sauvegarde 3-2-1** : Snapshots locaux ZFS $\rightarrow$ Réplication sur NAS distant (timonerie) $\rightarrow$ Synchronisation Cloud asynchrone (Queueing).

---

## 5. Mobilité Terrestre Électrique

L'objectif est d'assurer une mobilité propre au départ de la péniche, rechargée par le système solaire du bord.

### 5.1 Macro — Impasses Légales et Arbitrage
*   **L'impasse de la construction amateur (RTI)** : La fabrication DIY exige les tests UNECE R136 (écrasement batterie) et R10 (CEM), destructifs et inabordables (dizaines de milliers d'euros).
*   **Le cadre du rétrofit (Arrêté 2020)** : Réservé aux professionnels avec un agrément de prototype CNRV. Aucun kit n'existe pour les gros modèles.
*   **Arbitrage Stratégique** : Acquisition d'une moto électrique de série (Zero Motorcycles) garantissant la légalité, l'assurance, et le standard CEM.

### 5.2 Meso — Étude Comparative Duo + Bagages (200–250 kg)
*   **Maeving RM1 / RM1S** : Homologuée monoplace. Charge utile de 129 kg max. Éliminée.
*   **Triumph Speed Twin 900** : Thermique. Excellent en théorie (210 kg) mais illégal en rétrofit DIY.
*   **Zero S (Génération < 2024)** : Poids léger (142 kg), charge utile duo insuffisante (149 kg).
*   **Zero DSR/X ou S (Châssis FST 2024+)** : Poids à vide de 247 kg, PTAC de 454 kg $\rightarrow$ **Charge utile de 207 kg**, idéale pour le duo avec bagages. Atout logistique : **Marche arrière à basse vitesse (Parking Mode)**.

### 5.3 Nano — Normes et Composants
Tout véhicule léger électrique embarqué doit s'appuyer sur un pack batterie conforme **UNECE R136 / UN 38.3** et un contrôleur **UNECE R10 (CEM)**, essentiel pour ne pas perturber l'électronique de navigation du bateau en phase de charge.

### 5.4 Pratique — Grutage et Recharge
*   **Grue de Pont vs Passerelle** :
    *   *La Passerelle* : Pour une pente praticable de 15°, un dénivelé de 1,5m nécessite 5,80m de rampe. L'usage de la marche arrière de la moto est indispensable pour sécuriser la descente.
    *   *La Grue (Mâtereau)* : Indispensable sur berge sauvage. CMU exigée de 350-400 kg (pour absorber un coefficient dynamique de 1,5 face au roulis).
*   **Élingage** : Sangles sur le té de fourche et le bras oscillant. *Interdiction absolue de toucher les câbles haute tension (orange).*
*   **Intégration EMS** : Le BMS de la moto doit communiquer (Modbus/OCPP) avec l'EMS du bateau pour permettre un *Dynamic Load Balancing* et recharger préférentiellement en surplus solaire.

---

## 6. Gestion de Projet, Opérations et Financement

### 6.1 Macro — Aides Financières et Éligibilité
Il y a une frontière stricte entre les dispositifs fluviaux (commerce) et les dispositifs d'habitation privée.
*   **Plan d'Aides à la Modernisation (PAMI - VNF/ADEME)** : Réservé aux bateaux intégrant une activité commerciale déclarée (location, laboratoire payant). Subventions de 20k€ à 500k€.
*   **Crédit Maritime** : Propose des "Prêts Verts Maritimes".
    *   *L'Hypothèque Fluviale* : Le bateau est un bien meuble. Exige une immatriculation au registre du Tribunal de Commerce.
    *   *Exigences* : Expertise de coque récente (>3.8mm ou >4.0mm selon exigences bancaires), Titre de navigation, COT valide.
*   **Aides terrestres (MaPrimeRénov)** : Inéligibles aux navires.

### 6.2 Meso — Choix de l'ERP Open-Source
*   **Option 1 : Odoo Community (LGPLv3)**. Bonnes bases, mais restreint la comptabilité analytique budgétaire et le Gantt dynamique à sa version Enterprise.
*   **Option Privilégiée : ERPNext (GPLv3)**. Solution 100% open-source. Connecte les centres de coûts, la nomenclature d'achats (BOM multi-niveaux), et génère automatiquement le planning de chantier (Gantt) interactif lié aux feuilles de temps.

### 6.3 Nano — Matrice de Risques (AMDEC)
*   **Aléas Financiers (Dépassement)** : Fluctuation de l'acier et des batteries. *Mitigation : Suivi dynamique des répercussions dans l'ERP et marge pour imprévus de 15 %.*
*   **Aléas Réglementaires (CESNI/PT)** : Blocage suite à l'entrée en vigueur de règles ES-TRIN strictes sur le Lithium-ion (A60). *Mitigation : Préférer le LiFePO4, valider les plans coupe-feu avec la Commission avant découpe.*
*   **Aléas Techniques (R&D)** : Défaillance du système de propulsion hybride. *Mitigation : Désynchroniser les bancs d'essais R&D et la découpe de coque.*

### 6.4 Pratique — Rétroplanning Synthétique
*   **Mois 1 à 2** : Cadrage avec l'Unité Territoriale (UTI) VNF / HAROPA. Aspiration juridique dans NotebookLM.
*   **Mois 3** : JALON 1 - Dépôt de la Manifestation d'Intérêt / Dossier d'occupation auprès de VNF.
*   **Mois 4 à 5** : Lancement de la période légale de publicité domaniale (6 semaines) et dossier Loi sur l'Eau (DDTM).
*   **Mois 6** : JALON 3 - Signature de la Convention d'Occupation Temporaire (COT), déblocage du prêt Crédit Maritime et début du chantier physique.

---
> *Fin de la Bible Technique - Projet Péniche Freycinet. Pour les fichiers de travail annexes (CAO, Excel, Code source), reportez-vous aux dossiers du dépôt Git correspondants.*