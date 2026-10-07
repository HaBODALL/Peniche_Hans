# Stratégie et Prompts pour Google NotebookLM (Gemini Notebook) - Projet Péniche Freycinet

Ce document détaille la stratégie d'organisation et les bases de prompts pour exploiter au mieux **Google NotebookLM (Gemini Notebook)**.
L'objectif est de maximiser la limite des 200 sources par carnet avant le 9 du mois, en séparant le projet en **6 grands thèmes distincts**. Pour chaque carnet, une liste de mots-clés est fournie pour sourcer des documents avancés (académiques, techniques, open-source, industriels), ainsi que des modèles de prompts allant de la vision macro à la R&D nano.

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

### 🔍 Mots-clés pour trouver des sources (jusqu'à 200)
`ES-TRIN 2021/1`, `ES-TRIN 2027 CESNI`, `RGPNI VNF`, `CEVNI UNECE`, `Lestage péniche Freycinet calculs Archimède`, `Normes PMR habitat fluvial`, `VNF COT`, `Drone sous-marin inspection coque épaisseur acier`, `Architecture intérieure navale inclusive`, `Wabi-sabi design fluvial`, `Solarpunk pragmatique habitat`.

### 💬 Base de Prompts
* **Macro (Vision globale) :** "Fais une synthèse des obligations réglementaires majeures (ES-TRIN, VNF, HAROPA) qui impacteront la transformation d'une péniche Freycinet en habitat mobile. Quels sont les principaux points bloquants ou 'no-go' légaux à anticiper ?"
* **Meso (Ingénierie & Choix) :** "Compare les différentes stratégies de lestage (fonte, ferraille, béton, sable, eau) en croisant leur densité, leur coût, et leur facilité d'installation/désinstallation. Propose un tableau de décision multicritère."
* **Nano (R&D & Détail technique) :** "Je veux développer un drone sous-marin (ROV) open-source pour inspecter l'épaisseur de la coque par ultrasons, afin de repousser la mise en cale sèche (actuellement 7-10 ans). Quelles briques matérielles (ex: BlueROV) et logicielles devrais-je utiliser pour une mesure fiable reconnue (ou tolérée) par les experts fluviaux ?"
* **Pratique (Déploiement) :** "Génère une checklist étape par étape pour la mise aux normes PMR (passage 90cm, rotation 150cm, absence de seuil) de l'aménagement intérieur, en tenant compte des contraintes structurelles d'une cale Freycinet."

---

## Carnet 2 : Gestion des Eaux et Écologie Expérimentale
**Objectif :** Concevoir les systèmes de traitement d'eau potable, grise et noire, en visant le zéro-rejet polluant tout en restant conforme.

### 🔍 Mots-clés pour trouver des sources
`Zéro-rejet bateau`, `Réglementation eaux noires VNF ES-TRIN`, `MBR ultra-compact station épuration navale`, `Phytoépuration embarquée`, `Low-tech lab traitement eau`, `Toilettes sèches séparation vs incinération bateau`, `Micro-méthanisation domestique digesteur`, `Normes ARS eau potable stockage autonome`.

### 💬 Base de Prompts
* **Macro :** "Quelles sont les tolérances exactes et les interdictions strictes concernant le rejet des eaux (grises et noires) sur le domaine fluvial français géré par VNF et HAROPA ?"
* **Meso :** "Réalise un comparatif détaillé entre des solutions industrielles fermées (comme les stations MBR ultra-compactes) et des solutions DIY/Low-Tech (phytoépuration, bokashi). Analyse ces solutions sous les axes de l'efficacité, de la conformité VNF, de la maintenance et de l'encombrement volumique."
* **Nano :** "Pour un système de méthanisation (digesteur) expérimental embarqué traitant les eaux noires de 2 à 4 personnes, détaille les réactions biochimiques, les volumes de cuve nécessaires, les risques liés au biogaz en milieu confiné (sur une péniche) et les capteurs IoT requis pour la sécurité."
* **Pratique :** "Propose un schéma d'installation de la plomberie (diamètres, pentes, pompes de relevage) intégrant à la fois un circuit classique et une boucle expérimentale pour tester de nouvelles méthodes de filtration de l'eau grise en toute sécurité."

---

## Carnet 3 : Énergie, Électricité et Motorisation Fluviale
**Objectif :** Gérer l'autonomie énergétique et la transition vers une motorisation électrique, en séparant drastiquement les réseaux habitat et propulsion.

### 🔍 Mots-clés pour trouver des sources
`Norme NFC 15-100 bateau`, `ES-TRIN motorisation électrique 400V DC`, `Rétrofit électrique bateau fluvial`, `Projet Riverboost propulsion électrique`, `Batteries LFP marine recyclage`, `Panneaux solaires flexibles rendement marin`, `Gestion énergétique hybride navale`.

### 💬 Base de Prompts
* **Macro :** "Quels sont les prérequis absolus imposés par l'ES-TRIN pour séparer l'architecture électrique du 'Bloc 1' (Habitat, 230V AC / 24V DC) du 'Bloc 2' (Propulsion, 400V DC) sur une péniche Freycinet ?"
* **Meso :** "Confronte les solutions de rétrofit électrique professionnelles clés en main pour une propulsion fluviale face à une approche semi-DIY (intégration de composants industriels de seconde main). Intègre la question de la certification et des assurances."
* **Nano :** "Rédige le cahier des charges technique d'un contrôleur de batterie (BMS) capable de s'interfacer avec un pack de batteries 400V DC de récupération (type automobile), incluant les protocoles de communication CAN-bus et les sécurités d'isolation galvanique."
* **Pratique :** "Conçois un plan de déploiement solaire sur le roof de la péniche. Comment maximiser la surface tout en préservant des zones de circulation de sécurité et en évitant l'ombrage des équipements de navigation ?"

---

## Carnet 4 : IT, Logiciel, Supervision et Réseaux (IoT)
**Objectif :** Créer le 'cerveau' de la péniche : supervision des systèmes, réseau local multi-protocoles et aide à la navigation.

### 🔍 Mots-clés pour trouver des sources
`Home Assistant marine IoT`, `Réseau Wi-Fi HaLow 802.11ah`, `LoRaWAN bateau métallique`, `Serveur local embarqué basse consommation`, `VNF Avisbat EuRIS API`, `Projet Moveo données navigation`, `Open-source SCADA maritime`.

### 💬 Base de Prompts
* **Macro :** "Comment structurer l'architecture informatique globale d'une péniche (serveur local, postes clients Android, capteurs IoT) pour qu'elle reste totalement fonctionnelle même en l'absence prolongée de connexion internet ?"
* **Meso :** "Compare les technologies réseau pour la communication des capteurs à l'intérieur d'une coque en acier : Wi-Fi classique, Bluetooth Mesh, LoRa et Wi-Fi HaLow. Laquelle offre le meilleur ratio fiabilité/consommation d'énergie dans ce contexte de cage de Faraday ?"
* **Nano :** "Je souhaite développer un script Python ou Node.js qui récupère les données de navigation publiques (VNF Avisbat, EuRIS) via API et les superpose sur une cartographie interactive locale. Propose le code source de base pour gérer l'authentification et l'extraction des polygones de zones d'amarrage."
* **Pratique :** "Élabore un plan de sauvegarde et de redondance matérielle pour le serveur central du bateau (RAID, alimentations secourues, etc.) face aux vibrations et à l'humidité du milieu fluvial."

---

## Carnet 5 : Mobilité Terrestre Électrique
**Objectif :** Résoudre le problème du dernier kilomètre avec un véhicule électrique terrestre adapté aux contraintes de la péniche.

### 🔍 Mots-clés pour trouver des sources
`Réglementation UNECE R100 moto électrique`, `Homologation rétrofit moto France 2020`, `Zero Motorcycles S SR/F spécifications techniques`, `Triumph Maeving charge utile`, `RTI construction amateur DREAL`, `Grue de levage péniche moto`.

### 💬 Base de Prompts
* **Macro :** "Quelles sont les impasses légales en France concernant le montage d'une moto électrique DIY (RTI, construction amateur) ? Pourquoi le projet privilégie-t-il les modèles d'occasion (ex: Zero Motorcycles) ou les rétrofits professionnels ?"
* **Meso :** "Fais une étude comparative entre une Zero S (occasion) et un modèle de type Triumph / Maeving. Évalue-les selon : charge utile (doit atteindre 200-250 kg pour deux personnes + bagages), poids total (contrainte de la grue du bateau), autonomie et esthétique neo-rétro."
* **Nano :** "Si j'opte pour un rétrofit professionnel homologué, quels sont les composants spécifiques (moteur, pack batterie, contrôleur) certifiés R100 (UNECE) et CEM qui doivent être intégrés pour garantir la conformité ?"
* **Pratique :** "Propose un système de grutage et d'arrimage sécurisé sur le pont de la péniche pour une moto électrique de 200 kg. Détaille les forces d'arrachement à prendre en compte lors de la navigation."

---

## Carnet 6 : Gestion de Projet, Opérations et Financement
**Objectif :** Assurer le pilotage, le budget, la logistique (ERP) et capter les financements nécessaires (Aides VNF, CEE).

### 🔍 Mots-clés pour trouver des sources
`Aides PARM VNF transition énergétique`, `CEE Certificats Économies Énergie fluvial`, `Logiciel ERP open-source gestion projet`, `Budget prévisionnel rénovation péniche Freycinet`, `Fiscalité bateau logement redevance COT`, `Méthode Agile hardware open-source`.

### 💬 Base de Prompts
* **Macro :** "Fais l'inventaire des aides financières disponibles (PARM VNF, CEE, subventions régionales) pour la transition énergétique et l'électrification d'une péniche de transport reconvertie en habitat. Quelles sont les conditions d'éligibilité ?"
* **Meso :** "Quels outils logiciels open-source ou sans compte (ex: ERP modulaires comme Odoo version communautaire, ERPNext) sont les plus adaptés pour gérer simultanément un budget, des nomenclatures d'achats (BOM), et le planning d'installation de notre projet ?"
* **Nano :** "Conçois une matrice de risques avancée (AMDEC) pour la phase de transformation du bateau, en incluant les aléas financiers (dépassement de budget), réglementaires (blocage CESNI/ES-TRIN) et techniques (défaillance expérimentale)."
* **Pratique :** "Construis un rétroplanning complet pour les 6 prochains mois, intégrant la recherche de sources, le développement des carnets NotebookLM, la rédaction des cahiers des charges et les premières rencontres avec les autorités (VNF/HAROPA)."

---
*Fin du document. Utilisez ces bases pour initialiser vos 6 carnets NotebookLM avant le 9 du mois.*