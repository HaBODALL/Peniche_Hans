# Carnet 2 : Gestion des Eaux et Écologie Expérimentale

Ce carnet regroupe l'ingénierie et la réglementation sur le traitement des eaux noires, grises et potables à bord de la péniche Freycinet. L'objectif est l'autonomie et le respect total des lois environnementales maritimes et fluviales.

## 1. Macro : Réglementation VNF & HAROPA
* **Zéro-rejet absolu** : La loi française (Code de l'environnement) et la doctrine des ports fluviaux interdisent le rejet direct.
* **Obligation d'équipement** : Obligation d'avoir soit des cuves de rétention ISO 8099 (vidange par camion à quai), soit une station d'épuration homologuée (ES-TRIN Chapitre 18).
* **Sanctions** : Dépollution aux frais du propriétaire, retrait de la convention COT, jusqu'à 75 000€ d'amende.

## 2. Meso : Comparatif des Filières d'Assainissement
* **MBR (BioRéacteur à Membrane)** : Station ultra-compacte certifiée ES-TRIN. Excellente épuration (DBO5 < 10 mg/L), emprise au sol minimale (1m²), mais nécessite une alimentation électrique continue (1 kWh/jour).
* **Phytoépuration (Barge/Pont)** : Zéro consommation, très low-tech, mais volume et poids massifs (jusqu'à 7,5 tonnes). Sensible au froid. Dangereux pour la stabilité du bateau.
* **Bokashi & Séparation (Toilettes Sèches)** : Supprime le flux noir liquide, emprise minimale, mais nécessite une maintenance manuelle importante. Ne résout pas le problème des eaux grises qui devront passer par un MBR.

## 3. Nano : Méthanisation Embarquée
Le développement expérimental d'un digesteur anaérobie (2 à 4 EH) permet la valorisation des déchets organiques.
* **Risques** : En milieu confiné (cale en acier), le biogaz (CH4, H2S) pose un risque mortel d'asphyxie et d'explosion.
* **IoT** : Nécessite une supervision stricte des gaz et des pressions par Home Assistant.

## 4. Pratique : Architecture Hydraulique
* Prévoir une double tuyauterie : un circuit gravitaire principal d'eaux grises vers le MBR/cuves, et une "boucle d'essai" (by-pass) pour tester les filtres expérimentaux avec de vraies charges organiques sans polluer le réseau.

---
*Synergies : Les consommations électriques du MBR et des pompes de relevage sont dimensionnées dans le [Carnet 3 Énergie](../03_energie_electricite_motorisation/README.md). L'amarrage nécessaire à la vidange est traité dans le [Carnet 4 Ancrage](../04_ancrage_amarrage/).*
