# BIBLE TECHNIQUE DU PROJET : PÉNICHE FREYCINET HABITAT & LABO R&D

Ce document centralise l'intégralité de l'ingénierie, de la réglementation et des stratégies opérationnelles pour la transformation d'une péniche Freycinet (38,50 m × 5,05 m) en un habitat mobile semi-autonome doté d'un atelier et d'un laboratoire de R&D.

Il est issu des 6 carnets thématiques du projet et sert de référentiel unique (Single Source of Truth) pour la communication interne et externe (VNF, HAROPA, Crédit Maritime, Assurances).

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

La transformation d'une péniche Freycinet bascule sous le cadre ES-TRIN et l'urbanisme fluvial.

### 1.1 Cadre Réglementaire (Macro)
* **ES-TRIN (CESNI)** : Nécessite un titre de navigation. L'épaisseur minimale de coque est de 3,8mm. Une séparation stricte est exigée entre l'électricité domestique (230V/24V) et la propulsion (400V DC).
* **Isolation et Coupe-Feu** : L'installation de parcs batteries Lithium nécessite un cloisonnement A60. Les vaigrages doivent être difficilement inflammables.
* **Domaine Public Fluvial (VNF/HAROPA)** : La Convention d'Occupation Temporaire (COT) est précaire et révocable. Le rejet d'eaux usées (grises et noires) est **strictement interdit** sans équipement validé (zéro-rejet).
* **Points bloquants (No-Go)** : Perte de COT (activité économique non déclarée), ou coque trop fine (<3,5mm).

### 1.2 Ingénierie du Lestage (Meso)
Le bateau lège pèse environ 50t à 100t. Il faut atteindre un déplacement cible de ~200t pour un tirant d'eau nominal de 1,20m.
* **Fonte (7,2 t/m³)** : Idéale pour gagner de la hauteur sous barrot, mais très chère.
* **Acier / Ferraille (4 à 7 t/m³)** : Bon compromis mais grand risque de rouille et corrosion confinée.
* **Béton Lourd/Standard (2,4 à 3,8 t/m³)** : **Option hybride recommandée**. Couler le fond entre les varangues avec du béton, puis affiner l'assiette avec quelques gueuses d'acier aux extrémités.
* **Eau** : Exclue au centre (effet de carène liquide modifiant la stabilité), utile uniquement en ballasts fermés compartimentés.

### 1.3 Inspection de Coque par Drone ROV (Nano)
Pour éviter la mise en cale sèche (coût et délai tous les 7 à 10 ans), le projet déploie un ROV d'inspection par ultrasons.
* **Base matérielle** : BlueROV2 Heavy (8 propulseurs vectorisés) avec Skid magnétique pour ventouser la coque.
* **Sonde** : Palpeur à ultrasons Cygnus Multi-Écho sur cardan à ressorts pour percer la peinture sans meulage.
* **Reconnaissance** : Doit être conforme IACS UR Z17 / ISO 9712 avec supervision par un expert fluvial certifié à terre.
* **Logiciel** : ROS 2 pour la fusion SLAM et la géolocalisation des défauts.

### 1.4 Aménagement PMR (Pratique)
* Franchissement vertical par élévateur à vis sans fin pont/cale.
* Plancher nivelé avec tolérance < 5mm.
* **Couloir central ≥ 120 cm**.
* **Aires de rotation ≥ 150 cm** de diamètre dans chaque zone fonctionnelle (salon, SDB, chambre, labo).
* Portes à galandage passage net 83cm, absence totale de seuil (chanfrein max 2cm).

---

## 2. Gestion des Eaux et Écologie Expérimentale

### 2.1 Réglementation et Tolérances (Macro)
* **Zéro-rejet absolu** : La loi française (Code de l'environnement) et la doctrine des ports fluviaux interdisent tout rejet direct d'eaux noires et grises non traitées.
* **Obligation d'équipement** : Obligation d'avoir soit des cuves de rétention ISO 8099 (vidange par camion à quai), soit une station d'épuration homologuée (selon le Chapitre 18 de l'ES-TRIN).

### 2.2 Comparatif des Filières d'Assainissement (Meso)
* **MBR (BioRéacteur à Membrane)** : Station ultra-compacte certifiée ES-TRIN. Excellente épuration (DBO5 < 10 mg/L), emprise au sol minimale (1m²), mais nécessite une alimentation électrique continue (~1 kWh/jour).
* **Phytoépuration (Barge/Pont)** : Zéro consommation (gravitaire), très low-tech, mais volume et poids massifs (jusqu'à 7,5 tonnes). Sensible au froid. Dangereux pour la stabilité du bateau si placé sur le pont.
* **Bokashi & Séparation (Toilettes Sèches)** : Supprime le flux noir liquide, emprise minimale, mais nécessite une maintenance manuelle importante. Ne résout pas le problème des eaux grises (qui devront quand même passer par un MBR).

### 2.3 Méthanisation Embarquée (Nano)
Le développement expérimental d'un digesteur anaérobie (2 à 4 EH) permet la valorisation des déchets organiques en biogaz et digestat.
* **Risques** : En milieu confiné (cale en acier), le biogaz (CH4, H2S) pose un risque mortel d'asphyxie et d'explosion.
* **IoT** : Nécessite une supervision très stricte des gaz et des pressions par l'architecture logicielle embarquée (Home Assistant / Serveur Edge).

### 2.4 Architecture Hydraulique (Pratique)
Prévoir une double tuyauterie : un circuit gravitaire principal d'eaux grises dirigé vers le MBR/cuves de rétention (la filière réglementaire sûre), et une "boucle d'essai" (by-pass) pour tester les filtres expérimentaux avec de vraies charges organiques sans polluer le réseau.

---

## 3. Énergie, Électricité et Motorisation Fluviale

### 3.1 Séparation Électrique ES-TRIN (Macro)
La réglementation fluviale impose une étanchéité matérielle absolue entre l'habitat et la propulsion.
* **Bloc 1 (Habitat)** : 230V AC / 24V DC. Standard domotique (NFC 15-100).
* **Bloc 2 (Propulsion)** : 400V DC pour les moteurs électriques.
* **Neutre IT** : Les réseaux doivent fonctionner avec des pôles flottants (totalement isolés de la coque) et sous la surveillance de deux Contrôleurs Permanents d'Isolement (CPI) distincts (400V et 230V).
* **Compartimentage Lithium** : Pour un parc batteries $\ge$ 20 kWh, obligation d'avoir un local dédié classé coupe-feu A60, ventilé directement vers l'extérieur avec extinction automatique.
* **Priorité Propulsion** : L'EMS (Energy Management System) doit prioriser la propulsion de manière absolue et délester automatiquement l'habitat en cas d'appel de puissance du moteur.

### 3.2 Rétrofit Professionnel vs Semi-DIY (Meso)
* **L'impasse du semi-DIY (batteries automobiles de récupération)** : Bien que moins cher à l'achat, l'absence de certification (EN 62619) interdit l'homologation ES-TRIN, fait perdre l'accès aux assurances maritimes, et annule l'éligibilité aux primes financières (CEE/VNF).
* **La solution Professionnelle (Clé en main)** : Obligatoire pour un bateau navigable de gabarit Freycinet (38m). Offre la garantie, la conformité légale et le déblocage des subventions.

### 3.3 Contrôleur de Batterie (BMS) Haute Tension (Nano)
Pour l'expérimentation R&D (hors-propulsion principale), un BMS 400V doit respecter des contraintes sévères :
* Surveillance cellule par cellule avec gestion thermique active.
* Communication CAN-bus/NMEA 2000 avec isolation galvanique certifiée entre la Haute Tension (400V) et les réseaux Basse Tension (24V).

### 3.4 Déploiement Solaire sur le Roof (Pratique)
* **Choix technique** : Panneaux ETFE souples, posés sur une sous-couche (type nid d'abeille/polycarbonate) créant une lame d'air de 15mm. Évite la surchauffe de la coque en acier (+15% de rendement récupéré face à un collage direct).
* **Architecture MPPT** : Multiplication des petits micro-onduleurs ou contrôleurs MPPT (strings indépendants) pour contrer drastiquement les ombres portées du mât de navigation et des arbres de rive.

---

## 4. IT, Logiciel, Supervision et Réseaux (IoT)

### 4.1 Architecture "Offline-First" (Macro)
Pour maintenir l'opérabilité critique sans connexion internet (écluses profondes, zones blanches rurales), l'infrastructure repose sur un serveur local "Edge".
* **Serveur Edge** : Mini-PC fanless industriel ou cluster durci. L'OS doit être en Read-Only (OverlayFS) pour prévenir toute corruption de carte/disque due aux coupures électriques.
* **VLANs Sectorisés** :
  - VLAN 10 : Navigation (NMEA 2000, GPS, Signal K).
  - VLAN 20 : Énergie et IoT (Victron Cerbo GX, Modbus TCP, MQTT, Home Assistant).
  - VLAN 30 : Clients tactiles, équipage et labo.
  - VLAN 40 : WAN (Starlink, modem 4G/5G, Wi-Fi de quai).
* **Clients (Android/Web)** : Conçus pour lire et écrire dans une base de données locale (Room DB) et se synchroniser en arrière-plan lorsque le réseau interne est capté.

### 4.2 Réseaux Sans Fil en Milieu Métallique (Meso)
Une coque en acier crée une cage de Faraday et des évanouissements de signal (fading) importants.
* **Wi-Fi Classique (2.4/5GHz)** : Faible pénétration, bloqué dès le passage d'une cloison étanche (perte >25 dB).
* **LoRaWAN (Sub-GHz, 868 MHz)** : Excellent pour la télémétrie discrète et les capteurs sur piles (fuite de cale, température moteur). La modulation traverse l'acier et offre jusqu'à 10 ans d'autonomie.
* **Wi-Fi HaLow (802.11ah)** : Le protocole optimal pour les flux à haut débit dans le bateau (caméras salle des machines, télémétrie IP native), combinant la diffraction du Sub-GHz et les débits de l'OFDM.

### 4.3 Durcissement Matériel Fluvial (Pratique)
L'environnement fluvial impose des contraintes physiques permanentes :
* **Vibrations** : Proscription totale des disques durs mécaniques (HDD). Utilisation de SSD NVMe certifiés (MIL-STD-810H) montés sur silentblocs en Viton ou amortisseurs à câbles.
* **Alimentations** : Le serveur est alimenté directement sur le bus **24V DC** du navire via un DC-UPS à supercondensateurs (pour lisser les chutes de tension lors du démarrage des moteurs).
* **Condensation (Tropicalisation)** : Application d'un vernis de tropicalisation polyuréthane (Conformal Coating IPC-CC-830C) sur les cartes mères. Armoires IP55/66 climatisées en circuit fermé (Peltier/Caloducs).
* **Sauvegarde (3-2-1)** : Snapshots locaux ZFS $\rightarrow$ réplication sur NAS distant (timonerie) $\rightarrow$ synchronisation Cloud asynchrone lors de l'accès 4G.

---

## 5. Mobilité Terrestre Électrique

L'objectif est de documenter une flotte de véhicules légers faisant le lien entre le bateau (amarré), les haltes fluviales, et l'intérieur des terres, tout en profitant de l'énergie solaire du bord.

### 5.1 Impasses Légales du Rétrofit et du DIY (Macro)
* **DIY & RTI** : La construction d'une moto électrique "maison" ou la modification d'un cadre (RTI) est un gouffre financier légal (tests destructifs UNECE R136 et normes de Compatibilité Électromagnétique R10 en chambre anéchoïque UTAC).
* **Rétrofit thermique** : Nécessite un installateur agréé et un kit de marque certifié. À ce jour, aucun kit n'est homologué pour de gros roadsters type Triumph Bonneville.
* **Choix validé** : L'acquisition d'une moto électrique de série neuve ou d'occasion (ex: gamme Zero Motorcycles) est la seule voie viable et assurable sans surcoût.

### 5.2 Comparatif des Bases Roulantes (Meso)
Le cahier des charges exige une capacité Duo + Bagages (charge utile requise > 200kg).
* **Maeving RM1 / RM1S** : Homologation stricte monoplace (129kg de charge max). Éliminée.
* **Zero S (Occasion < 2024)** : Poids contenu (142kg) mais charge utile duo trop juste (149kg).
* **Zero DSR/X ou Zero S 2024+ (Châssis FST)** : Poids élevé (~220-250kg) mais homologuée pour plus de 210kg de charge. Atout majeur : intègre une **marche arrière électrique**, fondamentale pour reculer sur une rampe ou manœuvrer sur le pont étroit d'une péniche.

### 5.3 Logistique Embarquée (Pratique)
* **Rampe télescopique (Option 1)** : Adaptée aux quais stabilisés. En raison des dénivelés bateau/quai variant selon l'enfoncement de la coque (jusqu'à 1,5m), il faut prévoir une rampe d'environ 6 mètres pour respecter une pente franchissable de 15°.
* **Grue de levage / Mâtereau (Option 2)** : Pour les berges sauvages. Nécessite un mât motorisé d'une CMU de 350-400kg.
* **Élingage** : Toujours attacher les sangles textiles aux tés de fourche et au bras oscillant. *Interdiction stricte de prendre appui sur les gaines orange haute-tension.*
* **Recharge** : Branchée sur l'onduleur du bateau (AC) ou en charge directe DC-DC. L'EMS (Energy Management System) de la péniche doit pouvoir délester dynamiquement la charge de la moto (Dynamic Load Balancing) en cas d'appel de puissance prioritaire sur le bateau.

---

## 6. Gestion de Projet, Opérations et Financement

### 6.1 Dispositifs d'Aides et Financements (Macro)
* **Aides VNF et ADEME (PARM / PAMI)** : Attention, la majorité des aides massives à la remotorisation fluviale sont **réservées aux bateaux ayant une activité économique** (fret, passagers, charte, labo commercial). Un habitat purement privé est exclu de ces dispositifs.
* **Crédit Maritime / Banque Populaire** : Accorde des Prêts Verts fluviaux. Le bateau étant un bien meuble, la garantie prend la forme d'une **hypothèque fluviale**, nécessitant l'immatriculation de la péniche au registre du Tribunal de Commerce et la présentation d'une expertise de coque (sondage ultrasons > 4mm).
* **CEE (Certificats d'Économie d'Énergie)** : Financements mobilisables sur l'équipement électrique efficient installé à bord.

### 6.2 ERP Open-Source pour le Chantier (Meso)
Piloter la refonte d'une péniche (budget, planning, nomenclature de pièces à acheter) nécessite un outil robuste.
* **Odoo Community** : Connu, mais ampute ses modules de budget analytique avancé et de gestion de nomenclatures multiniveaux complexes au profit de sa version Enterprise payante.
* **ERPNext (Option recommandée)** : 100% Open-Source (GPLv3). Relie nativement les centres de coûts (budget du bateau), les BOM (Bill Of Materials pour le R&D des laboratoires, la motorisation) et un diagramme de Gantt collaboratif sans aucun frais caché.

### 6.3 Matrice des Risques AMDEC (Nano)
* **Risque Législatif / Réglementaire** : Blocage par la Commission de Visite ES-TRIN due à l'intégration d'un composant R&D hors norme ou à une défaillance de traitement d'eau empêchant l'octroi de la COT.
* **Risque Financier** : Surcoût brut sur les cours de l'acier (chaudronnerie de coque) et des batteries Lithium. Prévoir une marge de manœuvre continue de 15% verrouillée dans l'ERPNext.

### 6.4 Rétroplanning Global R&D (Pratique)
1. **Mois 1-2** : Veille documentaire, centralisation dans Gemini NotebookLM, cadrage informel avec l'UTI VNF/HAROPA.
2. **Mois 3** : Dépôt officiel du dossier de Manifestation d'Intérêt.
3. **Mois 4-5** : Période légale de publicité domaniale (6 semaines) et dépôt de dossier Loi sur l'Eau (DDTM).
4. **Mois 6** : Signature de la COT d'amarrage, validation par la Commission de visite, et lancement physique des travaux en chaudronnerie.

---
> *Fin de la Bible Technique - Projet Péniche Freycinet. Pour les fichiers de travail annexes (CAO, Excel, Code), reportez-vous aux dossiers du dépôt Git correspondants.*