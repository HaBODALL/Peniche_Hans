# Cahier des Charges Principal : Péniche Laboratoire Électrique

Ce document liste les exigences fondamentales (Must-Have) du projet d'habitat fluvial, qui se veut être un habitat autonome, accessible PMR, intégrant un laboratoire de recherche embarqué. Toute acquisition de coque ou décision d'aménagement doit respecter ce cahier des charges.

> **Deadline symbolique :** Novembre 2028 (40 ans du capitaine à bord)

## 1. La Coque et le Gabarit
- **Type :** Péniche au format "Freycinet" (38,5m x 5,05m).
- **Justification :** C'est le format historique qui permet de naviguer sur l'immense majorité des canaux français.
- **Sécurité :** Un rapport de sondage (mesure par ultrasons de l'épaisseur de la tôle de fond) de moins de 2 ans est impératif avant achat. Une épaisseur résiduelle inférieure à 3,5/4 mm entraîne un risque financier énorme (redoublage de fond nécessaire).

## 2. Programme Fonctionnel

### 2.1 Espaces obligatoires
| Espace | Surface cible | Contrainte PMR | Priorité |
|--------|--------------|----------------|----------|
| Chambre | 12-16 m² | Accès fauteuil, lit accessible | 🔴 Phase 1 |
| Salle de bain / WC | 6-9 m² | Douche italienne, barres appui | 🔴 Phase 1 |
| Cuisine | 8-12 m² | Plan travail adapté | 🟠 Phase 1 |
| Séjour / bureau | 15-20 m² | Circulation 150 cm | 🟠 Phase 1 |
| Laboratoire / atelier | 15-25 m² | Accès matériel lourd | 🟡 Phase 2 |
| Local technique | 4-6 m² | Batteries, BMS, tableau | 🔴 Phase 1 |
| Rangements | — | Intégrés partout | 🟠 Phase 1 |

### 2.2 Espaces souhaitables
- Terrasse/pont aménagé (convivialité)
- Espace invité (couchage appoint)
- Serre / jardinière (autosuffisance partielle)

## 3. Contraintes de l'Aménagement Intérieur (Exigences PMR)
L'aménagement ne doit comporter aucun seuil bloquant. Ces contraintes sont non négociables, l'accessibilité étant prévue pour le capitaine/pilote et d'éventuels passagers ou aides.

| Critère | Valeur minimale | Référence |
|---------|----------------|-----------|
| Largeur circulation | 90 cm | Norme PMR |
| Espace giration | Ø 150 cm | Norme PMR |
| Seuils | 0 cm (ou rampe ≤ 5%) | Norme PMR |
| Sol | Antidérapant R11 minimum | DTU |
| Barres d'appui | WC + douche + accès bord | Norme PMR |
| Accès depuis quai | Passerelle stable, main courante | — |
| Hauteur plan travail | Adaptable 70-90 cm | — |

*Note de Red Punk Trunk : Ces contraintes PMR doivent être vues comme une opportunité pour un design minimaliste et aéré.*

## 4. Confort Thermique

**Objectif :** Confort hivernal sans chauffage lourd (hors vagues de froid). L'enveloppe acier de la coque nécessite une isolation irréprochable (risque de condensation et corrosion sous isolant) associée à une ventilation VMC double flux.

**Principe d'isolation :** Matériaux hygroscopiques prioritaires (milieu humide fluvial).

| Zone | Solution retenue | Alternative | Priorité |
|------|-----------------|-------------|----------|
| Fond de cale | Laine bois/chanvre | Liège projeté | 🔴 |
| Panneaux latéraux | Laine bois/chanvre | Liège projeté | 🔴 |
| Pont (plafond) | Laine bois/chanvre | Laine de roche | 🔴 |
| Timonerie | Laine bois/chanvre | — | 🟠 |

*(Décision finale d'isolation : Après visite et mesures réelles)*

### Chauffage envisagé
- **Phase 1 :** Poêle à bois (provisoire)
- **Phase 2 :** PAC réversible air/eau

## 5. Plomberie, Eau et Déchets
Objectif tendant vers le zéro-rejet.

| Poste | Phase 1 | Phase 2 |
|-------|---------|---------|
| Eau douce | Cuve + branchement quai (autonomie sur 15 jours) | Récupération pluie |
| Eau chaude | Chauffe-eau électrique 50L | PAC intégrée |
| Eaux grises | Rejet réseau quai | Phytoépuration / Traitement embarqué |
| WC | WC sec (compostage) | WC marin homologué |
| Pompe de cale | Électrique automatique | Redondance |

## 6. Architecture Électrique
Principe : 2 blocs physiquement séparés (conception par Matt YAPADEBOULOS).

**BLOC 1 — HABITAT (Phase 1)**
- Tableau 230V NFC 15-100
- Éclairage LED (circuits dédiés)
- Prises courantes (dont prises USB)
- Chargeurs appareils lab
- Alimentation quai 16A minimum (32A souhaitable)

**BLOC 2 — PROPULSION ÉLECTRIQUE (Phase 2)**
- L'architecture électrique sera conçue pour, à terme, accueillir une motorisation 100% électrique nécessitant un parc batterie haute puissance (LiFePO₄ 100-150 kWh) et une homologation stricte.

### Cadre légal
- **ES-TRIN** : règlement européen transport fluvial
- **Habilitations** : BR/BC minimum avant interventions
- **Certification** : Bureau Veritas avant mise en navigation
- **Séparation physique** obligatoire des 2 blocs

## 7. Le Laboratoire Embarqué
L'espace doit permettre d'accueillir un "Atelier / Laboratoire" pour la recherche et le monitoring environnemental fluvial (partenariats VNF, Agence de l'Eau, ADEME envisagés).

### Équipements prévus (Phase 2)
- **Capteurs eau :** Température, pH, turbidité (monitoring dès la Phase 1)
- **Station météo :** Données locales (Intégration domotique)
- **Serveur local :** Stockage données (Basse consommation)
- **Banc test électronique :** R&D embarqué (Compétences maker)
- **Alimentation stabilisée :** Labo (Sur Bloc 1)

### Données collectées (objectif)
- Qualité de l'eau (Seine)
- Consommation énergétique embarquée
- Production / stockage énergie
- Données navigation (si mobilité Phase 2)

## Références et Bibliographie
- Normes d'accessibilité des ERP et habitats.
- ES-TRIN (Standard Européen des Bateaux de Navigation Intérieure).
