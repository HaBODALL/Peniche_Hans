# Stratégie et Prompts pour Google NotebookLM (Gemini Notebook) - Projet Péniche Freycinet

Ce document détaille la stratégie d'organisation et les bases de prompts pour exploiter au mieux **Google NotebookLM (Gemini Notebook)**.
L'objectif est de maximiser la limite des 200 sources par carnet avant le 9 du mois, en séparant le projet en **6 grands thèmes distincts**. Pour chaque carnet, une liste exhaustive de mots-clés est fournie pour le "Deep Search" (recherche approfondie académique, technique, open-source), ainsi que des suggestions de sources à importer, et des modèles de prompts allant de la vision macro à la R&D nano.

---

## Sommaire des Carnets (Notebooks)
1. [Carnet 1 : Architecture Navale, Réglementation et Aménagement](#carnet-1--architecture-navale-réglementation-et-aménagement)
2. [Carnet 2 : Gestion des Eaux et Écologie Expérimentale](#carnet-2--gestion-des-eaux-et-écologie-expérimentale)
3. [Carnet 3 : Énergie, Électricité et Motorisation Fluviale](#carnet-3--énergie-électricité-et-motorisation-fluviale)
4. [Carnet 4 : IT, Logiciel, Supervision et Réseaux (IoT)](#carnet-4--it-logiciel-supervision-et-réseaux-iot)
5. [Carnet 5 : Mobilité Terrestre Électrique](#carnet-5--mobilité-terrestre-électrique)
6. [Carnet 6 : Gestion de Projet, Opérations et Financement](#carnet-6--gestion-de-projet-opérations-et-financement)

---

## Carnet 1 : Architecture Navale, Réglementation et Aménagement
**Objectif :** Maîtriser le cadre légal du bateau-logement/atelier, l'intégrité de la coque, le lestage, l'accessibilité, et le design de l'habitat.

### 🔍 Mots-clés pour Deep Search (jusqu'à 200 sources)
`ES-TRIN 2021/1`, `ES-TRIN 2027 CESNI amendements`, `RGPNI VNF`, `CEVNI UNECE`, `Lestage péniche Freycinet calculs Archimède`, `Normes PMR habitat fluvial`, `VNF COT`, `Drone sous-marin ROV inspection coque épaisseur acier NDT`, `Architecture intérieure navale inclusive`, `Wabi-sabi design fluvial`, `Solarpunk pragmatique habitat`, `Matériaux de lestage haute densité bateau`, `Isolation biosourcée milieu humide`, `Stabilité navale GZ curve péniche`, `Corrosion galvanique coque acier fluviatile`, `Peinture antifouling écologique sans biocide`.

### 📚 Suggestions de Sources à importer (Liens / Types de documents)
- **Règlements complets (PDF) :** ES-TRIN (toutes versions), recueil RGPNI, CEVNI.
- **Thèses et articles académiques (Google Scholar / ResearchGate) :** Recherche sur la "corrosion des coques en acier doux en eau douce", "innovations en isolation biosourcée marine".
- **Documentation Bureau Veritas :** *Rules for the Classification of Inland Navigation Vessels*.
- **Forums & Blogs spécialisés :** Extractions PDF de discussions sur *Aqua-forum* ou *Cruisers & Sailing Forums* concernant l'aménagement PMR sur bateaux.
- **Guides Low-Tech Lab :** Rapports sur l'habitat modulaire et les matériaux de récupération.

### 💬 Base de Prompts
* **Macro (Vision globale) :** "Fais une synthèse des obligations réglementaires majeures (ES-TRIN, VNF, HAROPA) qui impacteront la transformation d'une péniche Freycinet en habitat mobile. Quels sont les principaux points bloquants ou 'no-go' légaux à anticiper ?"
* **Meso (Ingénierie & Choix) :** "Compare les différentes stratégies de lestage (fonte, ferraille, béton, sable, eau) en croisant leur densité, leur coût, et leur facilité d'installation/désinstallation. Propose un tableau de décision multicritère tenant compte de la courbe de stabilité."
* **Nano (R&D & Détail technique) :** "Je veux développer un drone sous-marin (ROV) open-source pour inspecter l'épaisseur de la coque par ultrasons (NDT - Non-Destructive Testing), afin de repousser la mise en cale sèche. Quelles briques matérielles et logicielles utiliser pour une mesure fiable reconnue par les experts fluviaux ?"
* **Pratique (Déploiement) :** "Génère une checklist étape par étape pour la mise aux normes PMR (passage 90cm, rotation 150cm, absence de seuil) de l'aménagement intérieur, en tenant compte des contraintes structurelles d'une cale Freycinet."

---

## Carnet 2 : Gestion des Eaux et Écologie Expérimentale
**Objectif :** Concevoir les systèmes de traitement d'eau potable, grise et noire, en visant le zéro-rejet polluant tout en restant conforme.

### 🔍 Mots-clés pour Deep Search
`Zéro-rejet bateau inland navigation`, `Réglementation eaux noires VNF ES-TRIN`, `MBR membrane bioreactor ultra-compact station épuration navale`, `Phytoépuration embarquée macrophytes`, `Low-tech lab traitement eau grise`, `Toilettes sèches séparation vs incinération bateau`, `Micro-méthanisation domestique digesteur anaérobie`, `Normes ARS eau potable stockage autonome`, `Osmose inverse basse pression solaire`, `Filtres à sable lents biosand DIY`, `Traitement UV-C LED eau potable navire`.

### 📚 Suggestions de Sources à importer
- **Directives européennes :** Rapports du CESNI sur le traitement des eaux usées à bord des bateaux de navigation intérieure.
- **Brevets et publications industrielles :** Spécifications techniques des stations MBR (Membrane BioReactor) compactes (ex: *ACO Marine*, *Hamann*).
- **Littérature scientifique :** Articles sur la *phytoremédiation* en milieu confiné et mobile (murs végétaux épurateurs).
- **Rapports DIY / Open-source :** Manuels de construction de micro-digesteurs de biogaz domestique (ex: *Solar CITIES*).
- **Documents institutionnels :** Guides de l'ARS sur la potabilisation autonome de l'eau de pluie ou de rivière.

### 💬 Base de Prompts
* **Macro :** "Quelles sont les tolérances exactes et les interdictions strictes concernant le rejet des eaux (grises et noires) sur le domaine fluvial français géré par VNF et HAROPA ?"
* **Meso :** "Réalise un comparatif détaillé entre des solutions industrielles fermées (comme les stations MBR ultra-compactes) et des solutions DIY/Low-Tech (phytoépuration, bokashi). Analyse ces solutions sous les axes de l'efficacité, de la conformité VNF, de la maintenance et de l'encombrement volumique."
* **Nano :** "Pour un système de méthanisation (digesteur) expérimental embarqué traitant les eaux noires de 2 à 4 personnes, détaille les réactions biochimiques, les volumes de cuve nécessaires, les risques liés au biogaz en milieu confiné et les capteurs IoT requis pour la sécurité."
* **Pratique :** "Propose un schéma d'installation de la plomberie (diamètres, pentes, pompes de relevage) intégrant à la fois un circuit classique et une boucle expérimentale pour tester de nouvelles méthodes de filtration de l'eau grise."

---

## Carnet 3 : Énergie, Électricité et Motorisation Fluviale
**Objectif :** Gérer l'autonomie énergétique et la transition vers une motorisation électrique (solaire, éolien, houlomoteur, hydrolien, batteries).

### 🔍 Mots-clés pour Deep Search
`Norme NFC 15-100 bateau`, `ES-TRIN motorisation électrique 400V DC`, `Rétrofit électrique bateau fluvial`, `Projet Riverboost propulsion électrique`, `Batteries LFP marine recyclage second-life`, `Panneaux solaires flexibles rendement marin`, `Gestion énergétique hybride navale`, `Éolienne à axe vertical (VAWT) bateau`, `Hydrolienne de fond courant fluvial`, `Énergie houlomotrice vagues navigation intérieure`, `Hydrogénérateur bateau fluvial`, `Micro-éolien embarqué efficacité`, `Power-to-X micro-échelle`, `BMS CAN-bus isolation galvanique 400V`.

### 📚 Suggestions de Sources à importer
- **Standards électriques :** Extraits des normes NFC 15-100 et directives ES-TRIN Chapitres 10 & 11 sur le 400V DC.
- **Rapports de projets R&D :** Documents finaux des projets européens *Riverboost*, *Elektra* (bateaux à hydrogène/électrique).
- **Recherche sur les ENR (Énergies Renouvelables) de niche :** Thèses sur le rendement des éoliennes à axe vertical (VAWT) en milieu canalisé, ou sur les micro-hydroliennes de traîne / hydrogénérateurs pour capter l'énergie du courant d'un fleuve (ex: Rhône, Seine).
- **Datasheets :** Fiches techniques de contrôleurs moteurs (Sevcon, Curtis), de packs batteries LFP automobiles (Tesla, Zoe) utilisés en seconde vie, et de BMS marinisés.
- **Articles sur l'houlomoteur :** Même si plus rare en fluvial, recherches sur la récupération d'énergie du sillage (vagues) des gros convois poussés.

### 💬 Base de Prompts
* **Macro :** "Quels sont les prérequis absolus imposés par l'ES-TRIN pour séparer l'architecture électrique du 'Bloc 1' (Habitat, 230V AC / 24V DC) du 'Bloc 2' (Propulsion, 400V DC) sur une péniche Freycinet ?"
* **Meso :** "Confronte les solutions de rétrofit électrique professionnelles clés en main face à une approche semi-DIY (batteries seconde vie). Intègre ensuite une analyse sur les générateurs d'appoint : compare l'apport d'une éolienne à axe vertical, d'un hydrogénérateur (hydrolienne de fond ou de traîne) plongé dans le courant du fleuve, et de panneaux solaires."
* **Nano :** "Rédige le cahier des charges technique d'un contrôleur de batterie (BMS) capable de s'interfacer avec un pack 400V DC de récupération automobile, incluant les protocoles CAN-bus, les sécurités d'isolation galvanique et la gestion des micro-charges erratiques provenant d'un hydrogénérateur."
* **Pratique :** "Conçois un plan de déploiement multi-énergies sur la péniche : Solaire sur le roof, éolienne VAWT à la poupe, et système de déploiement rétractable d'une micro-hydrolienne pendant l'ancrage dans une zone à fort courant."

---

## Carnet 4 : IT, Logiciel, Supervision et Réseaux (IoT)
**Objectif :** Créer le 'cerveau' de la péniche : supervision des systèmes, réseau local multi-protocoles et aide à la navigation.

### 🔍 Mots-clés pour Deep Search
`Home Assistant marine IoT`, `Réseau Wi-Fi HaLow 802.11ah`, `LoRaWAN bateau métallique cage de Faraday`, `Serveur local embarqué basse consommation Raspberry Pi CM4 / N100`, `VNF Avisbat EuRIS API`, `Projet Moveo données navigation`, `Open-source SCADA maritime`, `NMEA 2000 to MQTT bridge`, `Signal K open marine data`, `Edge computing marine vessel predictive maintenance`.

### 📚 Suggestions de Sources à importer
- **Documentation logicielle :** Wikis de *Signal K*, *Home Assistant*, *Node-RED* pour le routage de données marines et IoT.
- **Spécifications API :** Documentation officielle des API de VNF (Avisbat, Navi) et du portail européen *EuRIS*.
- **Articles académiques / Ingénierie :** Études sur la propagation des ondes radio (LoRa, HaLow, BLE) à l'intérieur de coques de navires métalliques.
- **Protocoles maritimes :** Spécifications NMEA 0183 et NMEA 2000, et méthodes de pontage vers MQTT.
- **Rapports de projets :** Livrables du projet *Moveo* sur la numérisation des voies navigables.

### 💬 Base de Prompts
* **Macro :** "Comment structurer l'architecture informatique globale d'une péniche (serveur local, Edge computing, capteurs IoT) pour qu'elle reste totalement autonome, résiliente et fonctionnelle sans connexion internet ?"
* **Meso :** "Compare les technologies réseau pour la communication des capteurs à l'intérieur d'une coque en acier : Wi-Fi classique, Bluetooth Mesh, LoRa et Wi-Fi HaLow. Laquelle offre le meilleur ratio fiabilité/consommation d'énergie pour contourner l'effet 'cage de Faraday' ?"
* **Nano :** "Je souhaite développer un bridge Python pour convertir les trames NMEA 2000 du matériel de navigation standard en messages MQTT compréhensibles par Home Assistant, via le serveur Signal K. Propose l'architecture logicielle et un extrait de code."
* **Pratique :** "Élabore un plan de sauvegarde et de redondance matérielle pour le serveur central du bateau (RAID, alimentations secourues, clustering léger) face aux vibrations et à l'humidité du milieu fluvial."

---

## Carnet 5 : Mobilité Terrestre Électrique
**Objectif :** Résoudre le problème du dernier kilomètre avec un véhicule électrique terrestre adapté aux contraintes de la péniche.

### 🔍 Mots-clés pour Deep Search
`Réglementation UNECE R100 moto électrique batterie`, `Homologation rétrofit moto France 2020 arrêté`, `Zero Motorcycles S SR/F spécifications techniques`, `Triumph Maeving charge utile`, `RTI construction amateur DREAL`, `Grue de levage péniche charge dynamique`, `Batterie interchangeable moto électrique`, `CEM compatibilité électromagnétique véhicule rétrofit`.

### 📚 Suggestions de Sources à importer
- **Textes réglementaires :** Arrêté du 13 mars 2020 sur le rétrofit en France, Règlement UNECE R100 complet, documents de la DREAL sur les RTI (Réception à Titre Isolé).
- **Manuels de service :** Fiches techniques et *Service Manuals* (si trouvables) de motos Zero Motorcycles (S, SR/F), Energica, ou Maeving.
- **Littérature d'ingénierie mécanique :** Manuels sur le calcul de charges dynamiques pour les grues de levage embarquées (potences de bateau).
- **Guides de conversion :** Livres ou documents issus de communautés de rétrofit électrique (ex: *Endless Sphere* forum PDF exports).

### 💬 Base de Prompts
* **Macro :** "Quelles sont les impasses légales en France concernant le montage d'une moto électrique DIY (RTI, construction amateur) ? Pourquoi le projet doit-il privilégier les modèles d'occasion (ex: Zero) ou les rétrofits professionnels certifiés CEM ?"
* **Meso :** "Fais une étude comparative entre une Zero S (occasion) et un modèle urbain type Maeving. Évalue-les selon : charge utile (200-250 kg max), poids total de la moto (contrainte de la grue du bateau), autonomie et possibilité d'interchanger les batteries pour les charger dans la péniche."
* **Nano :** "Si j'opte pour un rétrofit professionnel homologué, quels sont les composants spécifiques (moteur, BMS, contrôleur) certifiés R100 (UNECE) qui doivent être intégrés ? Explique le processus de test de Compatibilité Électromagnétique (CEM) requis."
* **Pratique :** "Propose un système de grutage (potence) et d'arrimage sécurisé sur le pont de la péniche pour une moto électrique de 200 kg. Détaille les calculs des forces d'arrachement à prendre en compte lors de la navigation ou d'un amarrage brutal."

---

## Carnet 6 : Gestion de Projet, Opérations et Financement
**Objectif :** Assurer le pilotage, le budget, la logistique (ERP) et capter les financements nécessaires (Aides VNF, CEE).

### 🔍 Mots-clés pour Deep Search
`Aides PARM VNF transition énergétique fluvial`, `CEE Certificats Économies Énergie bateau fluvial`, `Logiciel ERP open-source gestion projet naval`, `Budget prévisionnel rénovation péniche Freycinet`, `Fiscalité bateau logement redevance COT`, `Méthode Agile hardware open-source`, `BOM Bill of Materials gestion ERPNext Odoo`, `Assurance maritime fluviale risques construction`.

### 📚 Suggestions de Sources à importer
- **Documentation administrative :** Brochures d'aide PARM (Plan d'Aide au Report Modal) de VNF, grilles de calcul des CEE, barèmes des redevances COT (Convention d'Occupation Temporaire).
- **Documents financiers :** Modèles de business plans ou de budgets de rénovation navale (Excel exportés en PDF), contrats de prêt types (Cerfa 2062).
- **Documentation ERP :** Manuels d'utilisateurs d'Odoo Community, ERPNext, ou Dolibarr orientés gestion de nomenclature (BOM) et gestion de projet de construction.
- **Ouvrages de gestion :** Livres sur la gestion de projet matériel (Hardware Agile) et l'Open-Source Hardware (OSHW).

### 💬 Base de Prompts
* **Macro :** "Fais l'inventaire des aides financières disponibles (PARM VNF, CEE, subventions régionales, aides européennes) pour la transition énergétique et l'électrification d'une péniche. Quelles sont les conditions d'éligibilité strictes ?"
* **Meso :** "Quels outils logiciels open-source ou sans compte (ex: ERPNext, Odoo) sont les plus adaptés pour gérer simultanément un budget, des nomenclatures d'achats (BOM complexes avec des milliers de pièces), et le rétroplanning d'installation ?"
* **Nano :** "Conçois une matrice de risques avancée (AMDEC) pour la phase de transformation du bateau, en incluant les aléas financiers (dépassement de budget), réglementaires (blocage CESNI/ES-TRIN) et techniques (défaillance R&D expérimentale)."
* **Pratique :** "Construis un rétroplanning complet pour les 6 prochains mois, intégrant la recherche de sources, le développement des carnets NotebookLM, la rédaction des cahiers des charges, les demandes de financement, et les premières rencontres avec les autorités (VNF/HAROPA)."

---
*Fin du document. Utilisez ces bases pour initialiser vos 6 carnets NotebookLM avant le 9 du mois.*

## 📜 Références et Bibliographie
- Projet Péniche Freycinet : [Documentation Architecture Navale](../README.md)
- Guides d'utilisation Google NotebookLM / Gemini Notebook (2026).