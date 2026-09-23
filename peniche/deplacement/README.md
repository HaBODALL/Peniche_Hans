# Mobilité et Motorisation

Ce document traite du sous-système de déplacement de la péniche, avec un focus majeur sur la conversion à la motorisation électrique (Phase 2 / Phase 3 du projet).

## Spécificités du Projet (Format Freycinet)

La péniche étant de format Freycinet (38,5 mètres de long), elle sort de la catégorie "Plaisance" (qui s'arrête à 24m) pour entrer dans le domaine du **fluvial lourd**. Cette dimension implique des contraintes réglementaires et techniques considérables.

## Cadre Réglementaire (ES-TRIN)

L'architecture électrique de la motorisation et l'homologation du navire sont régies par des normes européennes strictes. Travailler avec du 400V DC sur une coque en acier contenant un énorme parc de batteries au lithium nécessite une rigueur industrielle.

1. **Norme ES-TRIN :** Le Standard Européen établissant les Prescriptions Techniques des Bateaux de Navigation Intérieure (notamment les Chapitres 10 & 11) est la référence absolue.
2. **Certification :** Pour obtenir le Titre de Navigation avec la nouvelle motorisation, l'installation doit être approuvée par une Société de Classification (ex: **Bureau Veritas**) ou un expert agréé.
3. **Habilitations :** Les interventions sur le réseau de propulsion nécessitent des habilitations électriques spécifiques (B2V / BR / BC, et habilitation pour Travaux Sous Tension - TST - sur les batteries).

## Stratégie de Motorisation : Le Rétrofit Électrique (Phase 2/3)

La motorisation de la péniche interviendra dans un second temps (post-2028), après l'aménagement de l'habitat (Phase 1). La motorisation thermique existante (si applicable) sera déposée et revendue.

L'architecture de propulsion (Bloc 2 - géré par Matt YAPADEBOULOS) sera **totalement isolée galvaniquement** du réseau domestique (Bloc 1) pour des raisons de sécurité.

### Composants Clés (Estimations)
- **Moteur :** Moteur électrique de traction de 20 à 30 kW (voire 150 kW selon les scénarios), type Torqeedo Deep Blue ou équivalent industriel (IP67).
- **Parc Batteries :** Batteries LiFePO₄ de 100 à 150 kWh, sélectionnées pour leur stabilité (norme UN38.3, IEC 62619). Poids estimé : 800 à 1200 kg (impact majeur sur le lest et l'assiette du bateau, à anticiper dès la Phase 1).
- **Câblage Puissance :** Câbles ignifugés (ex: 95mm² H07RN-F) avec protections spécifiques.
- **Propulseur d'étrave :** Également électrique, indispensable pour les manœuvres (notamment en écluse, surtout pour le pilote et les aides d'éventuels passagers).

## Contexte Technologique et Synergies

La motorisation de la péniche s'inscrit dans un contexte technologique européen favorable, porté par des investissements massifs dans le verdissement du fret fluvial et de la navigation de plaisance :
- **Projet Riverboost :** Ce projet européen vise à développer des navires de fret fluvial 100 % électriques dotés de systèmes de batteries hybrides (semi-solid-state + LFP) et interchangeables (*Battery-as-a-Service*). L'innovation issue de ces projets lourds permet de démocratiser des technologies (haute tension 400V+, BMS intelligents, moteurs compacts) pour les rendre accessibles à l'habitat itinérant.
- **Projet MOVEO (VNF) :** Ce projet vise à améliorer la gestion du trafic et la numérisation des données de navigation (AIS, outils VNF). Une meilleure gestion intelligente du trafic et la supervision de l'état des infrastructures permettront à l'avenir aux bateaux habitables autonomes de mieux planifier leurs trajets et d'optimiser leur consommation énergétique.
- **Nouveaux Produits Écotouristiques (VNF) :** VNF soutient le déploiement de flottes de bateaux de location électriques (ex: Sixto Green) en installant des réseaux de bornes de recharge rapide tous les 10-15 km sur certains itinéraires (comme le canal de la Marne au Rhin). Le développement de ces infrastructures dédiées à la plaisance locative bénéficiera directement à l'autonomie de notre péniche lors de ses déplacements.

## Sécurité et Monitoring

Le rétrofit inclut un monitoring constant du système (BMS - Battery Management System, contrôle des températures, etc.), dont les données viendront alimenter les recherches du laboratoire embarqué.

## Références et Bibliographie
- Règlements ES-TRIN (Chapitres 10 & 11).
- Bureau Veritas : *Rules for the Classification of Inland Navigation Vessels*.
- [Guide Diesel-électrique (VNF)](../../bibliographie/Guide-Diesel-electrique_V3.pdf) : Cahier technique de Voies navigables de France sur l'hybridation et la motorisation électrique (V3).
- Projets Horizon Europe : [Riverboost (Propulsion électrique avancée)](https://riverboost.eu/) et [MOVEO (Mobilité intelligente)](https://www.vnf.fr/vnf/dossiers-actualitess/vnf-est-engage-dans-le-projet-europeen-moveo-pour-une-mobilite-intelligente-et-durable/).
- [Nouveaux produits écotouristiques et bornes de recharge VNF](https://www.vnf.fr/vnf/accueil/tourisme-fluvial/offre-touristique-fluviale/nouveaux-produits-ecotouristiques/).
