# Gestion des Énergies

Ce document centralise les recherches et les plans pour la gestion de l'énergie à bord de la péniche (électrique, thermique). L'objectif à terme est de tendre vers une autonomie maximale et de soutenir le laboratoire embarqué et la motorisation électrique.

## Architecture Électrique en 2 Blocs

L'architecture électrique de la péniche est conçue en deux blocs physiquement séparés (conception par Matt YAPADEBOULOS), pour des raisons de sécurité, de réglementation et de phasage budgétaire.

### BLOC 1 — Habitat (Phase 1, 2026-2027)
Ce bloc gère l'électricité "domestique" de la péniche. Il est prioritaire et soumis à une réglementation plus souple (normes standards NFC 15-100).
- **Tension :** 230V AC / 12V-24V DC.
- **Éléments :** Tableau électrique principal, éclairage LED, prises de courant, alimentation des équipements de cuisine et de la salle de bain, chargeurs pour les équipements du laboratoire.
- **Sources :** Raccordement à quai (16A minimum, idéal 32A), parc de batteries de service (LiFePO₄ 5–10 kWh), onduleurs type Victron, panneaux solaires sur le toit.

### BLOC 2 — Propulsion Électrique (Phase 2/3, post-2027)
Ce bloc est dédié exclusivement à la motorisation du bateau. Il est isolé galvaniquement du Bloc 1 et soumis à des normes strictes.
- **Tension :** 400V DC (Haute Tension).
- **Éléments :** Parc de batteries de traction (LiFePO₄ 100-150 kWh), BMS, onduleurs, moteur électrique (20-30 kW), chargeurs haute puissance.
- **Cadre réglementaire :**
  - Réglementation **ES-TRIN**.
  - Nécessite des **habilitations électriques spécifiques** (B2V / BR / BC, et habilitation travaux sous tension pour les batteries) pour intervenir.
  - Exige une **certification par un organisme agréé (type Bureau Veritas)** avant mise en navigation.

## Chauffage et Régulation Thermique (Thermique)

Le confort thermique repose avant tout sur une **enveloppe isolante performante** (laine de bois, chanvre ou liège projeté) pour éviter la condensation sur l'acier.

- **Phase 1 :** Chauffage au moyen d'un poêle à bois (solution économique et autonome, mais contraintes de stockage de bûches) ou d'un poêle à granulés.
- **Phase 2 :** Installation d'une Pompe à Chaleur (PAC) air/eau ou eau/eau, capable d'assurer chauffage l'hiver et rafraîchissement l'été, avec un excellent rendement (COP). Cette solution s'intègre parfaitement dans la vision du laboratoire électrique.

## Appoint d'Énergie : Méthanisation / Biogaz

La production de biogaz par méthanisation des déchets organiques est envisagée comme un projet de recherche, mais avec une contrainte majeure de dimensionnement : un foyer réduit produit trop peu de matière organique (2-3 kg/jour) pour alimenter de manière autonome le chauffage ou la cuisson principale.

- La méthanisation servira uniquement de **source d'énergie d'appoint pour la cuisson** et produira du digestat (fertilisant).
- **Sécurité :** Le méthane étant un gaz inflammable, l'installation (digesteur et stockage) requiert une ventilation stricte (locale extérieur) et des détecteurs de gaz.

## Références et Bibliographie

### Solutions Industrielles Modernes
- [Documentation Architecture Marine Victron Energy](../../bibliographie/energies/Victron_Energy_Marine.pdf) : Schémas et bonnes pratiques pour les systèmes électriques embarqués (Onduleurs, batteries, gestion).

### Méthodes DIY et Solutions Expérimentales
- [Tutoriel Low-Tech Lab : Méthanisation Domestique](../../bibliographie/energies/LowTechLab_Methanisation.pdf) : Conception et sécurité d'un biodigesteur Low-Tech pour un usage expérimental d'appoint.

### Réglementaire et Normes
- [Normes NF C 15-100 (Basse tension) et NF C 18-510 (Habilitations électriques)](../../bibliographie/energies/NFC_15-100_18-510.pdf).
- [Documentation ES-TRIN 2021/1](../../bibliographie/reglementation/ES_TRIN_2021_FR.pdf) : Standard Européen établissant les Prescriptions Techniques des Bateaux de Navigation Intérieure. *(Note : La version 2027/1 est en cours de préparation par le CESNI).*
