# Projet Habitat / Atelier Mobile sur Péniche Freycinet

Ce dépôt documente un projet global de création d'un habitat et atelier mobile semi ou complètement autonome sur une péniche au format Freycinet. L'ensemble des travaux d'ingénierie et de recherche est structuré autour de **6 Carnets de Recherche** pilotés via Google NotebookLM (Gemini Notebook).

Le volume de la péniche permet de mettre en place des plans de traitement complets ou partiels de l'eau via des technologies expérimentales (zéro-rejet). Ce projet sert de base pour de la R&D, l'accueil d'un laboratoire et d'un atelier, tout en intégrant une transition vers la propulsion électrique et la mobilité douce.

## Architecture du dépôt

Le projet est divisé en sous-systèmes, interconnectés entre eux (Synergies EMS, Réseaux, Gestion de l'eau) :

- [`/peniche/01_architecture_navale_reglementation_amenagement/`](./peniche/01_architecture_navale_reglementation_amenagement/README.md) : **Carnet 1** - ES-TRIN, Lestage (fonte/acier/béton), Aménagement PMR, et inspection coque par ROV (drone sous-marin).
- [`/peniche/02_gestion_eaux_et_ecologie/`](./peniche/02_gestion_eaux_et_ecologie/README.md) : **Carnet 2** - Loi zéro-rejet (VNF/HAROPA), Phytoépuration, MBR (bioréacteurs compacts), Méthanisation.
- [`/peniche/03_energie_electricite_motorisation/`](./peniche/03_energie_electricite_motorisation/README.md) : **Carnet 3** - Séparation réseau Bloc 1 (Habitat 230V) / Bloc 2 (Propulsion 400V DC), Rétrofit électrique, Solaire ETFE.
- [`/peniche/04_ancrage_amarrage/`](./peniche/04_ancrage_amarrage/) : Gestion des connexions marines (pieux de guidage, amarres).
- [`/vehicules/`](./vehicules/README.md) : **Carnet 5** - Mobilité terrestre, moto électrique (ex: Zero DSR/X), calculs de grutage et synergies de recharge sur le navire.
- [`/gestion_projet_et_financement/`](./gestion_projet_et_financement/README.md) : **Carnet 6** - Gestion du budget via ERPNext, aides (PAMI, CEE, Crédit Maritime), Rétroplanning.
- [`/software/`](./software/README.md) : **Carnet 4** - Architecture "Offline-First", IoT (Home Assistant), télémétrie LoRaWAN/Wi-Fi HaLow, durcissement matériel, et extraction d'API de navigation fluviale.
- `/docs/` : Dossier principal contenant la `bibliographie`, les `moodboards`, etc.
- `prompts_notebook_gemini.md` : Guide de R&D contenant les prompts macro/nano pour l'utilisation de Gemini Notebook.

## Règles de Contribution & Synergies

Ce projet repose sur la documentation en Open-Source Hardware et Software.
- Les schémas de CAO (3D/2D) et les PDF lourds doivent être committés via **Git LFS** (voir le fichier `.gitattributes`).
- Les documentations doivent inclure la référence systématique aux lois (ES-TRIN, RGPIN, etc) et comparer des solutions industrielles aux solutions Low-Tech / DIY.
- Voir `MISSING_DOCS.md` pour l'inventaire des ressources à sourcer.
