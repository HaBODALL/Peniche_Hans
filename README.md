# Projet Habitat / Atelier Mobile sur Péniche Freycinet

Ce dépôt documente un projet global de création d'un habitat et atelier mobile semi ou complètement autonome sur une péniche au format Freycinet.

Le volume de la péniche permet de mettre en place des plans de traitement complets ou partiels de l'eau via des technologies expérimentales. Ce projet sert de base pour de la R&D, l'accueil d'un laboratoire et d'un atelier. En parallèle, il vise à tester l'intérêt de la motorisation électrique pour ce format de bateau.

Ce dépôt structure les réflexions, les recherches et la documentation technique autour des différents sous-systèmes du projet.

## Architecture du dépôt

- `/peniche/` : Documentation sur les systèmes de la péniche.
  - `energies/` : Gestion de l'énergie (électrique, éolienne, solaire, etc.).
  - `eau_propre/` : Traitement, stockage et distribution de l'eau propre et potable.
  - `eau_grise/` : Gestion et traitement des eaux grises.
  - `eau_noire/` : Gestion et traitement des eaux noires.
  - `ancrage_amarrage/` : Gestion des connexions marines (parking, arrêt avec ancre).
  - `deplacement/` : Motorisation (électrique) et systèmes de déplacement.
- `/vehicules/` : Projets complémentaires de mobilité terrestre.

## Références et Bibliographie

*Note : Certains documents de référence peuvent être téléchargés au format PDF dans le dossier [`/bibliographie/`](./bibliographie/).*

### Fluvial et Naval
- [Règlement Général de Police de la Navigation Intérieure (RGPNI) 2019](./bibliographie/recueil_rgpni___2019_09.pdf) ([Source](https://www.ecologie.gouv.fr/politiques-publiques/reglementation-fluviale)).
- [Code Européen des Voies de Navigation Intérieure (CEVNI) - 6e Révision](./bibliographie/CEVNI_6eRev.pdf) ([Source UNECE](https://unece.org/info/Transport/Inland-Water-Transport/pub/36257)).
- [Ministère de la Mer - Textes officiels Permis Plaisance](https://www.mer.gouv.fr/).
- [ES-TRIN 2021/1 (Standard Européen des Bateaux de Navigation Intérieure)](./bibliographie/ES_TRIN_2021_FR.pdf) *(Note : La version 2027/1 est en cours de préparation)*, Chapitres 10 & 11 ([Source CESNI](https://www.cesni.eu/fr/es-trin/)).
- [Bureau Veritas : *Rules for the Classification of Inland Navigation Vessels*](https://marine-offshore.bureauveritas.com/).
- [Règlements de Voies Navigables de France (VNF)](https://www.vnf.fr/) sur les rejets et le domaine public fluvial.
- [Réglementation et consignes locales de HAROPA PORT](https://www.haropaport.com/) (Axe Seine : Paris, Rouen, Le Havre).
- [Directives des instances européennes des voies navigables (CESNI)](https://www.cesni.eu/fr/).
- Principes de l'architecture intérieure navale et fluviale.

### Aménagement et Habitat
- [Normes PMR et design inclusif](https://www.ecologie.gouv.fr/politiques-publiques/accessibilite-batiments).
- Normes d'accessibilité des ERP et habitats.
- [Normes NFC 15-100 pour l'habitat](https://boutique.afnor.org/fr-fr/norme/nf-c15-100/installations-electriques-a-basse-tension/fa023961/7623).
- CEE et aides à la transition énergétique.
- Règlements fiscaux sur l'assimilation des bateaux logements (Taxe foncière vs Redevance VNF).
- [Cerfa 2062 (Déclaration de contrat de prêt)](https://www.service-public.fr/particuliers/vosdroits/R1054).

### Eau et Écologie
- [Normes sanitaires pour le stockage et le traitement de l'eau potable (ARS)](https://www.sante.fr/eau-potable).
- [Réglementation sur l'usage de l'eau de pluie à l'intérieur des habitations](https://www.service-public.fr/particuliers/vosdroits/F31481).
- Règlements locaux et nationaux sur les rejets en eaux intérieures.
- Documentation sur la phytoépuration et les filtres plantés.
- Documentation sur les toilettes à compostage (Separett, Trobolo, etc.).
- Études sur la méthanisation domestique.

### Véhicules et Mobilité Terrestre
- [Ministère de la Transition écologique : RTI construction amateur](https://www.ecologie.gouv.fr/politiques-publiques/homologation-vehicules).
- [Règlement délégué (UE) N° 44/2014](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX%3A32014R0044).
- [Directive européenne sur la Compatibilité Électromagnétique (CEM)](https://eur-lex.europa.eu/legal-content/FR/TXT/?uri=CELEX:32014L0030).
- [Règlement UNECE R100](https://unece.org/transport/vehicle-regulations) (Voir PDF local : [`Placeholder_UNECE_R100.pdf`](./bibliographie/Placeholder_UNECE_R100.pdf)).
- [Arrêté Rétrofit (13 mars 2020)](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000041780558/).

### Laboratoire, R&D et Do It Yourself (DIY)
- [Documentation Open-Source Hardware (OSHW)](https://www.oshwa.org/).
- [Low-tech Lab](https://lowtechlab.org/fr) : Tutoriels et documentation sur les technologies douces et l'autonomie.
- Directives sur la sécurité basse tension et la conception de prototypes électroniques.
- [Ressources IoT open-source : Home Assistant](https://www.home-assistant.io/).
- Expérimentations en phytoépuration et biogaz à petite échelle.
