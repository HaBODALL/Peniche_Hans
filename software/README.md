# Carnet 4 : IT, Logiciel, Supervision et Réseaux (IoT)

Ce carnet définit l'architecture informatique globale embarquée sur la péniche Freycinet. L'objectif est d'assurer une supervision domotique, énergétique (batteries, moteur) et logicielle résiliente, adaptée au milieu métallique et 100% fonctionnelle hors-ligne.

## 1. Macro : Architecture "Offline-First" et Topologie Réseau
Pour maintenir l'opérabilité sans connexion internet (écluses, zones blanches), l'infrastructure repose sur un serveur local "Edge".
* **Serveur Edge** : Mini-PC fanless ou Raspberry Pi CM4 avec OS en Read-Only (OverlayFS) pour éviter la corruption.
* **VLANs Sectorisés** :
  - VLAN 10 : Navigation (NMEA 2000, GPS, Signal K).
  - VLAN 20 : Énergie et IoT (Victron Cerbo GX, MQTT, Home Assistant).
  - VLAN 30 : Clients tactiles et équipage.
  - VLAN 40 : WAN (Starlink, 4G, Wi-Fi de quai).
* **Clients Android** : Utilisent `Jetpack Room DB` comme source de vérité locale. La synchronisation via `WorkManager` s'effectue automatiquement dès que le réseau interne est capté.

## 2. Meso : Réseaux Sans Fil en Milieu Métallique (Cage de Faraday)
Une péniche en acier crée des évanouissements par trajets multiples (fading).
* **Wi-Fi Classique (2.4/5GHz)** : Faible pénétration, bloqué dès le 1er pont.
* **LoRaWAN (868 MHz)** : Excellent pour les capteurs sur piles (fuite de cale, niveau d'eau, température). La modulation CSS franchit l'acier et offre jusqu'à 10 ans d'autonomie.
* **Wi-Fi HaLow (802.11ah)** : Idéal pour les flux à haut débit (caméras salle des machines, télémétrie moteur IP native). Il combine la pénétration du Sub-GHz et les débits de l'OFDM.

## 3. Nano : Extraction API et Cartographie Interactive
Les données de navigation (EuRIS / VNF) sont extraites pour être stockées localement et affichées sur une carte autonome hors-ligne.

Voici un script de base en Python (via API EuRIS OData V4 et VNF WFS) :

```python
import requests
import json
import folium

class InlandWaterwaysDataExtractor:
    EURIS_BASE_URL = "https://www.eurisportal.eu/visuris/api"

    def __init__(self, euris_api_token=None):
        self.session = requests.Session()
        if euris_api_token:
            self.session.headers.update({"Authorization": f"Bearer {euris_api_token}"})

    def fetch_euris_berths(self, top=50):
        endpoint = f"{self.EURIS_BASE_URL}/Berth/GetCompactBerths"
        response = self.session.get(endpoint, params={"$top": top})
        return response.json().get("items", [])

# Note: Le script complet transforme ces données en GeoJSON pour affichage via Folium/Leaflet.
```
*(Voir le dossier `software/navigation_aid/` pour l'implémentation complète).*

## 4. Pratique : Sauvegarde et Redondance Matérielle Fluviale
L'environnement fluvial impose des contraintes physiques extrêmes :
* **Vibrations** : Proscription totale des disques durs mécaniques (HDD). Utilisation de SSD NVMe (MIL-STD-810H) montés sur silentblocs en élastomère fluoré (Viton) et amortisseurs à câbles.
* **Alimentations** : Serveur alimenté directement en **24V DC** (suppression onduleurs 230V). Utilisation de modules OR-ing FET et de DC-UPS à supercondensateurs pour lisser les chocs de tension du démarrage moteur.
* **Condensation (Tropicalisation)** : Les cartes électroniques doivent recevoir un vernis de tropicalisation polyuréthane (Conformal Coating IPC-CC-830C). L'armoire serveur (IP55/66) est refroidie en circuit fermé par module Peltier sans aspirer l'air humide de la cale.
* **Sauvegarde 3-2-1** : Snapshots locaux ZFS + réplication sur un NAS secondaire dans la timonerie + Cloud asynchrone lors de la connexion 4G.

---
*Synergies : Ce système Edge héberge l'EMS (Energy Management System) défini dans le [Carnet 3 Énergie](../peniche/03_energie_electricite_motorisation/README.md) pour piloter la décharge des batteries, et traite les données des alarmes du MBR du [Carnet 2 Gestion des Eaux](../peniche/02_gestion_eaux_et_ecologie/README.md).*
