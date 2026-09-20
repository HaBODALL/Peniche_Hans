# Système : Énergies

Ce dossier est dédié à la R&D et à la documentation concernant la production, le stockage et la distribution de l'énergie sur la péniche.

## Architecture Électrique (Pistes de réflexion)
L'approche envisagée est de séparer physiquement l'installation en deux blocs distincts pour des raisons de sécurité, de réglementation et d'échelonnement du projet :

### 1. Bloc Habitat (Phase 1)
- **Tension :** 230V AC / 24V DC.
- **Usage :** Éclairage, prises courantes, électroménager, matériel de laboratoire.
- **Réglementation :** Souple (normes type NF C 15-100 et standard marine), gérable avec des onduleurs grand public (ex: Victron Multiplus).
- **Alimentation :** Panneaux solaires sur le pont, raccordement quai (16A min, transformateur d'isolement galvanique indispensable contre la corrosion), parc batterie tampon.

### 2. Bloc Propulsion (Phase 2)
- **Tension :** 400V DC (Haute puissance).
- **Usage :** Motorisation électrique principale (20-30 kW) et très gros parc batteries (100-150 kWh).
- **Réglementation :** Strictement encadrée par l'ES-TRIN et nécessite une validation par un expert maritime (ex: Bureau Veritas). Isolement galvanique total du bloc habitat.

## Chauffage et Régulation Thermique (Pistes)
La gestion thermique dans une coque en acier doit combattre la condensation interstitielle.
- **Isolation :** Pistes vers le liège projeté, la mousse de verre cellulaire, ou la laine de bois/chanvre avec frein-vapeur.
- **Ventilation :** VMC double flux indispensable.
- **Production de chaleur :**
  - *Option courte (Phase 1) :* Poêle à granulés (régulable, autonome) ou poêle à bois.
  - *Option idéale "Laboratoire" (Phase 2) :* Pompe à chaleur eau/eau sur échangeur de coque (COP élevé grâce à la température stable de la rivière).

## Production de Gaz / Méthanisation (R&D)
La méthanisation embarquée est étudiée dans un objectif de réduction des déchets et de laboratoire d'économie circulaire.
- **Potentiel :** La digestion anaérobie des déchets de cuisine (et potentiellement des toilettes) peut produire du biogaz et du digestat (fertilisant).
- **Limites :** Un foyer domestique ne produit pas assez de matière organique pour être autonome en gaz de cuisson (il faut ~100 kg de matière fraîche pour équivaloir à une bouteille de gaz). Le biogaz serait un *appoint*.
- **Contraintes :** Nécessite du volume, une température stable, et des mesures de sécurité strictes (détection de méthane, ventilation).

## Références et Bibliographie
- Normes NF C 15-100 (Basse tension) et NF C 18-510 (Habilitations électriques).
- Documentation ES-TRIN (Standard Européen établissant les Prescriptions Techniques des Bateaux de Navigation Intérieure).
- *À compléter au fur et à mesure des recherches technologiques.*