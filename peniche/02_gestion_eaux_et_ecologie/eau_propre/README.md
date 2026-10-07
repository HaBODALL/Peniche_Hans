# Gestion de l'Eau Propre et Potable

Ce document centralise les informations relatives au stockage, au traitement et à la distribution de l'eau propre à bord de la péniche. L'objectif est de garantir une autonomie suffisante entre deux raccordements au réseau terrestre.

## Stockage de l'Eau Douce

- **Cuve principale :** L'objectif est d'installer une cuve (en Inox ou PEHD alimentaire) d'une capacité de **1 000 à 2 000 Litres**. Placée en fond de cale, elle servira également de lest utile pour l'assiette du bateau.
- **Autonomie cible :** Avec une cuve de 1 500 L et une consommation maîtrisée (environ 80 L/jour/personne), l'autonomie visée est de 15 à 18 jours pour une personne (sans apport extérieur).
- **Remplissage :** Prévoir au moins deux points de piquage (avant/arrière) avec clapets anti-retour pour faciliter le remplissage depuis les bornes VNF ou les quais.

## Traitement et Distribution

- **Pompage :** Un groupe d'eau sous pression (surpresseur 12/24V ou 230V, débit de 40-60 L/min) couplé à un vase d'expansion est nécessaire pour éviter le cyclage intempestif de la pompe.
- **Filtration :** Bien que l'eau du réseau (bornes VNF) soit potable, elle perd de sa qualité lors du stockage. Un système de filtration complet est obligatoire :
  - Filtre à sédiments (20 µm).
  - Filtre à charbon actif (pour le goût et les odeurs).
  - Stérilisateur UV (pour détruire les bactéries avant consommation).
- **Eau Chaude Sanitaire (ECS) :** Un chauffe-eau électrique (ballon de 50 à 100 L) ou un système couplé à la future Pompe à Chaleur (Phase 2).

## Récupération d'Eau de Pluie (Projet Complémentaire)

Le pont d'une péniche Freycinet représente une surface de captage considérable (environ 190 m²), pouvant fournir jusqu'à 100 m³ d'eau par an (en Île-de-France).

- **Usage :** Ce circuit d'eau de pluie doit être **strictement séparé** du circuit d'eau potable. L'eau récupérée sera utilisée pour les sanitaires, le lavage (lave-linge) ou le nettoyage extérieur.
- **Attention :** L'eau coulant sur un pont en acier peint nécessite une filtration grossière avant stockage dans une cuve tampon dédiée (500 à 1 000 L). L'analyse de la qualité de cette eau fera partie des travaux du laboratoire embarqué.

## Solutions Expérimentales, DIY et Nouvelles Technologies

Dans une démarche d'innovation et d'autonomie (low-tech / high-tech), des solutions complémentaires peuvent être implémentées **en toute sécurité** (en aval ou en parallèle du circuit de potabilisation principal strict) :

- **Bio-filtration (Low-Tech) :** Filtres à sable biologiques (Biosand filters) pour le pré-traitement de l'eau de pluie avant stockage. Utile pour abattre la charge organique sans énergie.
- **Ultrafiltration (UF) / Osmose Inverse (RO) basse pression :** Systèmes de membranes capillaires à très faible consommation énergétique (ex: filtres type Sawyer ou Lifestream adaptés en modules) pour une sécurisation ultime au point d'usage (robinet cuisine).
- **Monitoring Open-Source :** Mise en place de capteurs Arduino/ESP32 (turbidité, TDS, température, débit) connectés à un tableau de bord (ex: Home Assistant, par Matt YAPADEBOULOS) pour surveiller la qualité de l'eau en temps réel.
- **Désinfection LED UV-C :** Intégration de modules LED UV-C (type Oji) miniaturisés directement aux points de puisage, offrant une désinfection instantanée avec une consommation électrique très faible par rapport aux lampes UV traditionnelles (et sans mercure).

## Références et Bibliographie

- **Directives OMS :** [Directives de qualité pour l'eau de boisson](https://iris.who.int/bitstream/handle/10665/258763/9789242549959-fre.pdf) - Base sanitaire pour le traitement de l'eau.
- **Standard ES-TRIN :** [Standard Européen établissant les Prescriptions Techniques des Bateaux de Navigation Intérieure (ES-TRIN)](https://www.cesni.eu/normes/es-trin/) - Normes obligatoires pour les péniches fluviales (incluant les exigences pour l'eau).
- **Manuel Low-Tech :** [Manuel de construction des filtres à sable biologiques CAWST](https://resources.cawst.org/)
- **Ressources en ligne :**
  - [Normes sanitaires pour le stockage et le traitement de l'eau potable (ARS)](https://solidarites-sante.gouv.fr/sante-et-environnement/eaux/article/eau-du-robinet).
  - [Réglementation sur l'usage de l'eau de pluie à l'intérieur des habitations (Service-Public)](https://www.service-public.fr/particuliers/vosdroits/F31481).
- **Fiches techniques des systèmes de filtration (Conformes aux exigences fluviales européennes - ES-TRIN, VNF, HAROPA) :**
  - *Filtre à sédiments (20 µm) :* [Cintropur NW25 / NW32](https://www.cintropur.com/fr/produits/eau-de-pluie/) (faible perte de charge, manchons jetables). Adapté à la pré-filtration des eaux d'avitaillement des ports fluviaux.
  - *Filtre à charbon actif :* [Cintropur NW25 TE](https://www.cintropur.com/fr/produits/eau-de-pluie/nw25te/) (traitement des odeurs/goûts, remplissage par vrac) ou cartouches standard 9"3/4 à 20" Pentair.
  - *Stérilisateur UV-C :* [Cintropur UV 2100](https://www.cintropur.com/fr/produits/uv/uv2100/) (débit max 2 m³/h) ou équivalent [Oji](https://www.oji-water.com/) (technologie LED UV sans mercure). Garantit une potabilité conforme aux directives sanitaires européennes de navigation.
