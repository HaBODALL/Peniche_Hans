# Outils Logiciels : Suivi de Projet, Supervision et Navigation

Ce document présente une série de propositions logicielles et de petits programmes à développer ou intégrer pour la gestion du projet de péniche Freycinet. Le périmètre couvre toutes les étapes : depuis l'acquisition et le suivi de l'aménagement, jusqu'à la supervision IoT du vaisseau et la gestion avancée de la navigation.

## 1. Suivi de Projet, ERP et Budget (Phase Achat, Installation et Aménagement)

### Besoins
- Suivi du budget d'achat, d'installation, et des coûts de rénovation/aménagement.
- Planification des tâches (installation, aménagement, équipements secondaires).
- Gestion documentaire et suivi de chantier.
- Architecture basée sur un serveur (local/cloud) avec un accès optimisé sur mobile Android.

### Propositions de programmes
1. **Application de gestion de chantier (Mini-ERP pour péniche)** : Outil centralisant devis, avancement des travaux et factures.
2. **Tableau de bord financier (Dashboard Budget)** : Un suivi en temps réel des dépenses vs prévisions.

### Benchmark : Pro vs Open-Source

| Solution | Type | Coût estimé | Avantages (Pros) | Inconvénients (Cons) |
|----------|------|-------------|------------------|----------------------|
| **Odoo (Module Projet/Budget)** | Open-Source / Pro | Gratuit (self-hosted) à ~20-50€/mois | Extrêmement complet, modulaire, interface mobile (Android). | Lourd à configurer, parfois trop complexe pour un projet perso. |
| **Notion / Airtable** | SaaS Pro | 0 à 15€/mois | Très flexible, rapide à mettre en place, hautement visuel. | Dépendance cloud (pas de mode offline robuste), données hébergées chez des tiers. |
| **Nextcloud + Deck** | Open-Source | Gratuit (self-hosted) | Contrôle total des données (hébergement maison), gestion de fichiers intégrée. | Moins spécialisé dans le budget financier pur, demande de gérer un serveur. |

### Intérêt d'un développement "Maison" (DIY)
- **Complexité** : Basse à Moyenne.
- **Temps estimé** : 2 à 4 semaines pour un outil basique CRUD (Create, Read, Update, Delete) avec React, Vue.js, ou Flutter (idéal pour Android).
- **Verdict** : L'intérêt de développer l'outil de base de zéro est *faible* (les solutions existantes sont matures). **Cependant**, développer de petits scripts d'extraction (Python) pour alimenter des bases de données personnelles à partir de vos factures peut être très utile avant de migrer vers la phase de supervision.

---

## 2. Supervision IoT et Énergies (Timonerie, Cabine et Mobile)

### Besoins
- Suivi en temps réel des points moteurs et des énergies (séparation stricte : Bloc 1 Habitat 230V/24V, Bloc 2 Propulsion 400V).
- Réception d'alertes environnementales ou techniques via réseaux IoT multiples (WiFi, LoRa, Wi-Fi HaLow, ou Bluetooth) pour garantir une redondance.
- Interfaces accessibles sur Android, postes fixes (timonerie, cabine de pilotage).
- Gestion logicielle de l'état des moteurs et des propulseurs d'étrave (selon la configuration choisie et l'état d'avancement du chantier).

### Propositions de programmes
1. **Hub IoT "Matt YAPADEBOULOS" (Supervision Globale)** : Un tableau de bord réunissant batteries, panneaux solaires, consommation électrique, niveau des cuves d'eau, et températures (coque/moteurs).
2. **Application Mobile "Alerte Navire"** : Une app Android légère dédiée aux alarmes (push/SMS/LoRa) en cas de coupure critique, fuite (voie d'eau), ou anomalie sur le 400V (conforme ES-TRIN pour la sécurité).

### Benchmark : Pro vs Open-Source

| Solution | Type | Coût estimé | Avantages (Pros) | Inconvénients (Cons) |
|----------|------|-------------|------------------|----------------------|
| **Home Assistant (HA)** | Open-Source | Gratuit + Matériel (Rpi/Mini PC) | Standard absolu, interface Android parfaite, énorme compatibilité IoT. | La gestion des réseaux atypiques (LoRa/HaLow) nécessite des gateways matérielles spécifiques. |
| **Grafana + InfluxDB + MQTT** | Open-Source | Gratuit | Parfait pour le suivi industriel des moteurs et batteries. Très paramétrable. | Interface moins "user-friendly" pour interagir ; conçu majoritairement pour l'affichage (monitoring). |
| **Victron Cerbo GX (OS)** | Pro / Open (Venus OS) | ~350€ (matériel) | S'intègre nativement à l'énergie marine, très fiable pour les parcs batteries. | Restreint à l'écosystème Victron, coûteux. |

### Intérêt d'un développement "Maison" (DIY)
- **Complexité** : Haute (en particulier pour la fiabilité des réseaux LoRa/HaLow sur une structure en acier comme une péniche, créant des cages de Faraday).
- **Temps estimé** : Plusieurs mois (itératif).
- **Verdict** : **Très élevé pour le "last-mile"**. Utiliser *Home Assistant* ou *MQTT* comme backend (infrastructure existante robuste), mais développer vous-même des interfaces spécifiques en timonerie (via des WebApps ou du Flutter pour Android) permet une personnalisation totale, essentielle pour les manœuvres.

---

## 3. Gestion de la Navigation et des Manœuvres

### Besoins
- Aide à la manœuvre et assistance à la navigation.
- Identification des zones de port, des parkings acceptant un gabarit Freycinet (38m+), estimation des coûts associés.
- Gestion des demandes de COT (Convention d'Occupation Temporaire) auprès de VNF ou HAROPA.
- Consultation centralisée des réglementations temporaires, écluses (avis à la batellerie), et rappels de code (CEVNI, RGPNI).

### Propositions de programmes
1. **Nav-Planner (Routage et Haltes Freycinet)** : Outil cartographique personnalisé croisant les dimensions de la péniche avec les données d'amarrage disponibles.
2. **Assistant "Capitaine"** : Application ou module intégrant une checklist d'éclusage, le suivi des manœuvres, et le statut temporaire des voies (tirants d'air / tirants d'eau).

### Benchmark : Pro vs Open-Source

| Solution | Type | Coût estimé | Avantages (Pros) | Inconvénients (Cons) |
|----------|------|-------------|------------------|----------------------|
| **EuRIS / Navi / Avisbat (VNF)** | Institutionnel | Gratuit | Données officielles, fiables et à jour (hydrométrie, chômages). | Interfaces parfois complexes, pas de "mode hors ligne", pas de gestion intégrée des coûts d'escale personnels. |
| **Navionics (Garmin)** | Pro | ~40-100€/an | Excellent routage, cartes bathymétriques. | Orienté plaisance marine/côtière, manque de spécificités pour le fluvial lourd (Freycinet, COT). |
| **OpenSeaMap** | Open-Source | Gratuit | Libre, base de données cartographique communautaire, superposable à d'autres SIG. | Manque de détails sur les infrastructures VNF spécifiques (bornes élec, points d'eau, déchets). |

### Intérêt d'un développement "Maison" (DIY)
- **Complexité** : Très Haute (intégration d'API de cartographie, web scraping pour les avis, bases de données SIG/GIS).
- **Temps estimé** : Plusieurs mois.
- **Verdict** : **Énorme**. Il n'existe aucun outil sur le marché qui centralise les besoins spécifiques d'un *bateau-logement de grand gabarit*. Développer une application de cartographie utilisant des données ouvertes (API VNF/EuRIS) pour y superposer vos propres données de repérage (points de parking, coûts, état des bornes) serait un atout majeur, voire un logiciel pouvant intéresser d'autres bateliers.

---

## 4. R&D Avancée : Le Drone de Suivi de Coque (Sous-marin d'inspection)

### Besoins
- Suivre l'état de la coque en acier sans sortir le navire de l'eau.
- Mesurer régulièrement l'épaisseur de la tôle (avec un sondeur à ultrasons) pour prévenir l'usure.
- Potentiellement nettoyer la coque (type robot de piscine ou aspirateur robot).
- **Objectif réglementaire** : Produire des rapports reconnus pour générer un plan de sondage. À terme, tenter de substituer ou d'espacer la sortie en cale sèche (obligatoire tous les 7 à 10 ans pour le certificat communautaire) par cette méthode d'inspection.

### Propositions de programmes et systèmes
1. **Pilotage ROV (Remotely Operated Vehicle)** : Logiciel de contrôle du drone sous-marin croisant vidéo en direct et télémétrie.
2. **Générateur de "Heatmap" de Coque** : Un script de traitement de données (Python/C++) qui récupère les coordonnées (X, Y) du drone et les valeurs du capteur à ultrasons pour dessiner une carte 3D d'épaisseur de l'acier du bateau.

### Benchmark : Pro vs Open-Source

| Solution | Type | Coût estimé | Avantages (Pros) | Inconvénients (Cons) |
|----------|------|-------------|------------------|----------------------|
| **BlueROV2 / ArduSub** | Open-Source (Hardware & Logiciel) | ~3 000€ - 6 000€ (avec capteurs) | Standard de l'industrie DIY, code totalement modifiable (QGroundControl), évolutif. | Assemblage très chronophage, requiert de fortes compétences en étanchéité et intégration de capteurs tiers. |
| **Drones d'inspection grand public (Chasing M2, Fifish)** | Pro | 1 500€ - 4 000€ | Clé en main, excellentes caméras, faciles à piloter. | Écosystème fermé, très difficile d'intégrer une vraie sonde d'épaisseur d'acier synchronisée avec la position. |
| **Services d'inspection professionnels par plongeur ou robot** | Prestation Pro | ~1 000€ - 3 000€ / inspection | Certifié et reconnu par les autorités de visites navales. | Coût récurrent, aucune autonomie, ne remplace généralement pas la mise à sec obligatoire. |

### Intérêt d'un développement "Maison" (DIY)
- **Complexité** : Extrême (Robotique sous-marine, traitement de signal de sonde, localisation sous-marine sans GPS).
- **Verdict** : **Colossal sur le plan financier et technologique**.
  - Développer le *logiciel* capable d'automatiser le plan de sondage (en croisant une sonde à ultrasons avec un ROV type ArduSub) est un défi d'ingénierie passionnant.
  - **Attention** : Sur le plan administratif, la conformité de ce système avec l'ES-TRIN (qui exige des contrôles à sec par des experts assermentés) sera difficile à obtenir d'emblée. Les commissions de visites (ou sociétés comme Bureau Veritas) devront valider cette méthode expérimentale. Cependant, même si cela n'évite pas la sortie de l'eau, l'outil permettra de préparer la cale sèche de façon très précise, évitant les surcoûts liés à des mauvaises surprises de dernière minute.

---

## Références et Bibliographie

- [Règlement Général de Police de la Navigation Intérieure (RGPNI) 2019](../bibliographie/reglementation/recueil_rgpni___2019_09.pdf)
- [ES-TRIN 2021/1 (Standard Européen des Bateaux de Navigation Intérieure)](../bibliographie/reglementation/ES_TRIN_2021_FR.pdf) - Règlements concernant l'architecture électrique et les plans de sondage (Chapitre 10 & 11).
- [Voies Navigables de France (VNF) - Avis à la Batellerie](https://www.vnf.fr/)
- [EuRIS - Portail européen d'information fluviale](https://www.eurisportal.eu/)
- [Home Assistant - Plateforme domotique open-source](https://www.home-assistant.io/)
- [ArduSub (Blue Robotics) - Open-Source ROV Software](https://www.ardusub.com/)
- [Low-tech Lab](https://lowtechlab.org/fr) - Inspiration pour la conception de systèmes résilients et abordables.
