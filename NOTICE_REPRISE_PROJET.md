# Notice d'Accompagnement à la Reprise du Projet (Péniche Freycinet) - Édition Étendue

Salut ! 👋

Si tu lis ces lignes, c’est que tu reprends le flambeau sur le projet technologique et logiciel de notre Péniche Freycinet. Je sais que reprendre le code et l'architecture de quelqu'un d'autre peut être intimidant. Ici, on ne parle pas d'une simple application web, on parle du système nerveux d'un bateau de 38,50 mètres et de 200 tonnes, soumis à des règles maritimes (ES-TRIN), équipé de systèmes 400V DC et d'une domotique devant résister aux coupures 4G et aux cages de Faraday.

Mais respire un grand coup : **tout va bien se passer**. J'ai écrit cette "Bible de Passation" spécialement pour toi. J'ai condensé ici des mois de R&D, de galères de serveurs, de crashs de réseau et de choix d'architecture. Mon but est de te donner le niveau de détail d'un Lead Tech, mais expliqué avec bienveillance.

Ce document est exhaustif. Prends un café, installe-toi confortablement, et décortiquons ensemble comment fonctionne la matrice de notre péniche.

---

## 1. Cartographie Mentale (Architecture Globale Détaillée)

Notre péniche repose sur 4 grands piliers technologiques qui communiquent entre eux. Le mot d'ordre absolu du bateau est **Offline-First**. Le bateau navigue souvent dans des zones blanches ; si on perd la 4G/Starlink, le bateau *doit* continuer à fonctionner à 100%.

### Le Schéma d'Architecture Cible

```text
       [ RÉSEAU EXTERNE (WAN) - 4G / Starlink ] -- (Connexion instable)
                           │
+--------------------------│----------------------------------------------------+
|  PÉNICHE (Réseau Local Intranet - VLANs isolés)                               |
|                                                                               |
|  1. POSTES CLIENTS (Android/Tablettes)                                        |
|     - App "Timonerie" (Kotlin / Jetpack Room DB)                              |
|     - Synchronisation asynchrone (WorkManager)                                |
|           │                                                                   |
|           │ (Wi-Fi / Ethernet local)                                          |
|           ▼                                                                   |
|  2. LE SERVEUR EDGE (Le Cerveau - PC Fanless durci, NVMe PLP, ZFS)            |
|     - Docker Containers                                                       |
|     - Home Assistant (Automates, Règles de crise)                             |
|     - Broker MQTT (Mosquitto) / Base de données InfluxDB (Séries Temporelles) |
|           │                                                                   |
|           ├───────────────────────────────────────────────┐                   |
|           ▼                                               ▼                   |
|  3. LES CAPTEURS / IOT (Matt YAPADEBOULOS)       4. LA NAVIGATION (Python)    |
|     - LoRaWAN (Traverse la coque acier)             - Scripts VNF / EuRIS     |
|     - Wi-Fi HaLow (Caméras)                         - Cartes Folium           |
|     - NMEA2000/CAN (Moteur 400V)                                              |
+-------------------------------------------------------------------------------+

+-------------------------------------------------------------------------------+
|  5. LE SOUS-MARIN D'INSPECTION (ROV) - Système isolé                          |
|     - BlueROV2 Heavy + Capteur Ultrasons Cygnus                               |
|     - Ordinateur Compagnon (Nvidia Jetson / ROS 2)                            |
+-------------------------------------------------------------------------------+
```

### Qui fait quoi ?
1. **Le Serveur Edge (Home Assistant & MQTT)** : C'est le cœur. Il stocke les données localement et prend les décisions d'urgence.
2. **L'Application Android** : L'interface humaine. Elle possède sa propre base de données pour fonctionner même si le Wi-Fi du bateau tombe.
3. **Les Scripts Python** : Ce sont nos "petites mains". Ils tournent la nuit pour télécharger les données officielles de navigation (Avisbat, EuRIS) et les mettent en cache.
4. **Le Sous-marin (ROS 2)** : C'est un projet de R&D à part, conçu pour remplacer la cale sèche en mesurant l'épaisseur de l'acier sous l'eau.

---

## 2. Visite Guidée du Code (Où trouver quoi ?)

L'arborescence du dépôt a été pensée pour séparer la réglementation de la tech pure. Voici ta boussole :

*   📁 **`docs/`** : L'encyclopédie théorique.
    *   `BIBLE_TECHNIQUE_PENICHE.md` : Le document fondateur. Si tu te demandes *pourquoi* on a choisi un câble spécifique ou *pourquoi* les batteries ne sont pas dans les cabines (norme A60), la réponse est là.
*   📁 **`bibliographie/`** : Tous les PDF officiels (ES-TRIN, VNF). Toujours vérifier ces textes avant de faire une modification électrique.
*   📁 **`software/`** : **Ton QG de développeur.**
    *   `README.md` et `OUTILS_SUIVI_NAVIGATION.md` : La documentation fonctionnelle de l'IT.
    *   *(Note : Dans ce dossier, tu trouveras ou créeras les sous-dossiers spécifiques : `/android`, `/python_scripts`, `/ros2_ws`, `/homeassistant_config`)*.
*   📄 **`prompts_notebook_gemini.md`** : Notre banque de prompts IA pour la R&D. Si tu veux interroger le NotebookLM du projet sur une réglementation obscure, utilise les structures de prompts qui y sont définies.
*   📄 **`MISSING_DOCS.md`** : Le backlog documentaire. Si tu n'arrives pas à télécharger une norme à cause d'un anti-bot (ex: Cloudflare), note-le ici.
*   📄 **`NOTICE_REPRISE_PROJET.md`** : Le document que tu es en train de lire.

---

## 3. Les Concepts Clés à retenir (Crash Course Approfondi)

Pour coder sur le bateau, tu vas naviguer entre 4 langages/frameworks. Voici les bases de survie pour chacun.

### Concept 1 : Offline-First & Jetpack Room DB (Android / Kotlin)
**L'idée** : L'appli Android (tablette de barre) ne fait *pas* une requête réseau à chaque fois que tu cliques. Elle lit et écrit dans sa base locale (`SQLite` via `Room`). C'est le `WorkManager` Android qui s'occupe de synchroniser cette base avec le Serveur Edge en arrière-plan.

**Exemple concret (Kotlin) - Une entité Room pour le niveau des cuves :**
```kotlin
// Ceci est la définition de la table "WaterTank" dans la tablette locale
@Entity(tableName = "water_tanks")
data class WaterTank(
    @PrimaryKey val tankId: String, // ex: "cuve_grises_1"
    val levelPercentage: Int,       // ex: 85
    val lastUpdatedLocally: Long    // Timestamp pour la synchro
)

// Le DAO (Data Access Object) : Comment on lit/écrit
@Dao
interface WaterTankDao {
    @Query("SELECT * FROM water_tanks WHERE tankId = :id")
    fun getTankLevel(id: String): Flow<WaterTank> // Le Flow met à jour l'UI en temps réel !

    @Insert(onConflict = OnConflictStrategy.REPLACE)
    fun updateTank(tank: WaterTank)
}
```

### Concept 2 : MQTT & Le Publish/Subscribe (IoT)
**L'idée** : Nos capteurs ne parlent pas directement aux applications. Ils publient un message sur un "Sujet" (Topic). Le serveur écoute ce sujet. C'est le concept du *Broker* (Mosquitto).
**Avantage** : Si l'appli Android plante, le capteur continue d'envoyer ses données au serveur sans erreur.

**Exemple d'un Payload JSON MQTT (ce qui transite sur le réseau) :**
*Topic :* `peniche/engine/batteries/400v`
*Payload (Message) :*
```json
{
  "soc": 82.5,
  "voltage": 385.2,
  "current_amps": -45.0,
  "cell_temp_max_c": 34.2,
  "status": "DISCHARGING",
  "timestamp": "2026-08-15T14:32:01Z"
}
```
*Si tu veux rajouter un thermomètre, tu n'as pas à toucher au serveur, il suffit que le thermomètre publie un JSON sur le bon Topic !*

### Concept 3 : Les API & Python (L'Extraction de Données)
**L'idée** : On utilise la librairie `requests` en Python pour interroger les serveurs officiels VNF ou EuRIS. L'API nous répond en JSON, qu'on transforme ensuite en cartes interactives (`Folium`).

**Extrait de code :**
```python
import requests

# On simule le navigateur pour ne pas se faire bloquer
headers = {"User-Agent": "Peniche-Freycinet-App/1.0"}
url = "https://www.eurisportal.eu/visuris/api/Berth/GetCompactBerths"

reponse = requests.get(url, headers=headers)
if reponse.status_code == 200:
    donnees = reponse.json()
    print(f"Trouvé {len(donnees['items'])} zones d'amarrage !")
else:
    print(f"Erreur API : {reponse.status_code}")
```

### Concept 4 : ROS 2 (Robot Operating System) - Pour le Drone
**L'idée** : ROS 2 n'est pas un système d'exploitation comme Windows, c'est un framework de communication en C++/Python. Un robot est divisé en "Noeuds" (Nodes). Un nœud lit la caméra, un autre contrôle les moteurs, un autre lit la sonde à ultrasons.
**Particularité** : Tout le drone tourne sous ROS 2, qui utilise DDS (Data Distribution Service) pour communiquer sous l'eau via un câble ombilical Ethernet.

---

## 4. Le Flux de la Donnée (Anatomie de 4 actions centrales)

Pour bien comprendre, décortiquons le parcours de l'information dans 4 scénarios critiques.

### Flux A : Alerte Débordement Cuve Eaux Grises (IoT -> Serveur -> Humain)
1.  **Sonde Physique** : Le flotteur de la cuve atteint 95%. Le microcontrôleur ESP32 se réveille.
2.  **Réseau LoRaWAN** : L'ESP32 envoie un message radio encodé en base64 pour traverser l'acier de la cale.
3.  **Passerelle (Gateway)** : L'antenne LoRa de la timonerie capte le signal, le décode, et le publie sur le MQTT (`peniche/water/grey/level`).
4.  **Home Assistant (Automate)** : Détecte que la valeur > 90. Il déclenche le script `emergency_pump_stop.yaml`.
5.  **Action & Notification** : HA coupe le relais 24V de la pompe d'entrée d'eau et envoie un Push sur les téléphones de l'équipage.

### Flux B : Le Capitaine note une dépense hors-ligne (Android -> Serveur)
1.  **Action Humaine** : Le Capitaine, dans un magasin sans réseau, ouvre l'App Android et ajoute : "Achat tuyaux PVC : 45€".
2.  **Room DB** : L'app enregistre la dépense dans `SQLite` avec le statut `synced = false`.
3.  **Retour à bord** : Le Capitaine remonte sur la péniche. Son téléphone se connecte au Wi-Fi `PENICHE_VLAN30`.
4.  **WorkManager** : Android détecte le Wi-Fi. Il prend toutes les données `synced = false` et lance une requête POST HTTP silencieuse vers l'API du Mini-ERP (Serveur Edge).
5.  **Validation** : Le serveur répond `200 OK`. L'app Android passe `synced = true`.

### Flux C : Génération de la Carte des Haltes VNF (Python)
1.  **Cronjob** : À 03h00 du matin, le serveur Edge lance `update_maps.py`.
2.  **Requête WFS** : Le script Python interroge les serveurs VNF pour récupérer les polygones des écluses et des postes d'attente.
3.  **Transformation** : Le script convertit les coordonnées EPSG:2154 (Lambert 93) en EPSG:4326 (GPS classique Latitude/Longitude).
4.  **Rendu** : Le script génère un gros fichier `map_offline.html` contenant tout le code Javascript Folium/Leaflet.
5.  **Mise à disposition** : Ce fichier HTML est servi par un serveur web local (Nginx). Les tablettes l'affichent sans avoir besoin d'internet.

### Flux D : Inspection de la Coque (ROS 2 / C++)
1.  **Sonde** : Le palpeur Cygnus collé au ventre du robot envoie une onde ultrasonore contre l'acier.
2.  **Traitement Matériel** : La sonde renvoie `3.82 mm`.
3.  **Noeud ROS 2 (`cygnus_driver_node`)** : Un script Python sur le drone lit le port série USB, crée un message `std_msgs/Float32` et le publie sur le topic `/rov/hull_thickness`.
4.  **Ombilical** : Le message DDS transite dans les 50 mètres de câble réseau sous-marin.
5.  **PC de Surface** : L'ordinateur du pilote écoute le topic `/rov/hull_thickness` et l'enregistre dans un fichier *rosbag* (base de données binaire) associé aux coordonnées X,Y du robot.

---

## 5. Le Guide de Survie (Débogage & Commandes Sysadmin)

C'est ici que tu trouveras comment te sortir des pires situations. Garde ces commandes précieusement.

### A. Survie Sysadmin de Base (Linux / Réseau)
Le serveur principal tourne sous Debian/Ubuntu Linux.
*   **Me connecter au serveur depuis mon PC** : `ssh user@192.168.10.10` (Demande la clé SSH à l'ancien admin).
*   **Voir si un service a planté (ex: MQTT) et pourquoi** :
    ```bash
    systemctl status mosquitto
    journalctl -u mosquitto -f --lines 50  # Le -f permet de voir les logs arriver en direct !
    ```
*   **Vérifier ce qui tourne sur le réseau (Si un capteur a disparu)** :
    *   Le bateau répond-il ? `ping 192.168.10.50`
    *   Quels sont les appareils sur le VLAN IoT ? `sudo nmap -sn 192.168.20.0/24`

### B. Survie Docker (Le Serveur Edge)
Toute notre infrastructure serveur est "conteneurisée" avec Docker. Si Home Assistant ou InfluxDB plante, c'est ici que ça se passe.
*   **Voir tous les conteneurs qui tournent** : `docker ps`
*   **Relancer toute l'infrastructure IT de la péniche** :
    Va dans le dossier contenant le fichier `docker-compose.yml` et tape :
    ```bash
    docker-compose down
    docker-compose up -d
    ```
*   **Lire les logs d'un conteneur qui refuse de démarrer (Très utile pour Home Assistant)** :
    `docker logs -f homeassistant_container_name`

### C. Survie Python (Les Scripts)
L'erreur de débutant en Python est de tout installer au même endroit et de créer des conflits de versions. Nous utilisons des "Environnements Virtuels" (`venv`).
*   **Si on te dit "ModuleNotFoundError" quand tu lances un script :**
    C'est que tu n'as pas activé ton environnement !
    1. Va dans le dossier du script : `cd software/nom_du_projet`
    2. Crée un environnement isolé (une seule fois) : `python3 -m venv venv`
    3. **Active-le (À faire à chaque fois !)** : `source venv/bin/activate` (Sous Windows : `venv\Scripts\activate`)
    4. Installe les dépendances : `pip install -r requirements.txt`
    5. Lance le script : `python script.py`

### D. Survie Android (L'App Timonerie)
Tu as un écran blanc ou l'application crash instantanément ?
1.  Branche la tablette à ton PC en USB.
2.  Ouvre **Android Studio**.
3.  Va dans l'onglet **Logcat** en bas. C'est la console de la tablette.
4.  Filtre par "Error". 90% du temps, tu verras une `NullPointerException` (tu as essayé d'afficher une variable qui n'existe pas) ou une `SQLiteConstraintException` (la base locale est corrompue).
5.  *Technique de la terre brûlée* : Dans les paramètres Android de la tablette > Applications > App Péniche > "Effacer le stockage". Cela détruit la Room DB locale et force l'app à tout retélécharger depuis le serveur.

### E. Survie ROS 2 (Le Drone)
ROS 2 est capricieux avec les variables d'environnement. Si rien ne marche, c'est probablement que tu n'as pas "sourcé" ton espace de travail.
*   **Compiler le code du drone** (À faire sur le PC compagnon ou ton PC Linux) :
    ```bash
    cd ~/ros2_ws
    colcon build --symlink-install
    ```
*   **La commande magique (Sourcing)** : Si ton PC te dit `ros2: command not found` ou ne trouve pas tes nœuds :
    ```bash
    source /opt/ros/humble/setup.bash    # Charge les commandes ROS de base
    source ~/ros2_ws/install/setup.bash  # Charge ton propre code (Le palpeur Cygnus)
    ```
*   **Déboguer un capteur muet (ex: le Palpeur d'épaisseur)** :
    Pour voir en direct si le capteur envoie des données sous l'eau : `ros2 topic echo /rov/hull_thickness`

---

## 6. Références et Bibliographie
*   [Documentation Home Assistant](https://www.home-assistant.io/docs/)
*   [Documentation Android Room / Kotlin](https://developer.android.com/training/data-storage/room)
*   [Documentation ROS 2 (Humble)](https://docs.ros.org/en/humble/index.html)
*   [Bible Technique Péniche](../docs/BIBLE_TECHNIQUE_PENICHE.md)

Bon vent Capitaine-Codeur ! Avec ces outils, tu as tout ce qu'il faut pour maintenir le navire à flot (au sens propre comme au figuré). ⚓