# Projet Habitat / Atelier Mobile sur Péniche Freycinet

Ce dépôt documente un projet global de création d'un habitat et atelier mobile semi ou complètement autonome sur une péniche au format Freycinet. L'ensemble des travaux d'ingénierie et de recherche est structuré autour de **6 Carnets de Recherche** pilotés via Google NotebookLM (Gemini Notebook).

Le volume de la péniche permet de mettre en place des plans de traitement complets ou partiels de l'eau via des technologies expérimentales (zéro-rejet). Ce projet sert de base pour de la R&D, l'accueil d'un laboratoire et d'un atelier, tout en intégrant une transition vers la propulsion électrique et la mobilité douce.

---

## 📖 LA BIBLE TECHNIQUE DU PROJET

L'intégralité de l'ingénierie, des choix techniques (CAO, IoT, Eaux) et des contraintes légales (ES-TRIN, VNF) a été compilée dans un seul et même document de référence. **C'est le point d'entrée principal pour comprendre la théorie du projet :**

👉 **[LIRE LA BIBLE TECHNIQUE (Livre Blanc)](./docs/BIBLE_TECHNIQUE_PENICHE.md)**

---

## Architecture des dossiers de travail

Les sous-dossiers du dépôt servent désormais de répertoires de travail pour héberger les fichiers bruts (Code Source, Plans CAO 3D/2D, Tableurs de calculs, etc.) associés à chaque chapitre de la Bible :

- [`/peniche/01_architecture_navale_reglementation_amenagement/`](./peniche/01_architecture_navale_reglementation_amenagement/) : Plans PMR, calculs de lestage (Archimède), ROV sous-marin.
- [`/peniche/02_gestion_eaux_et_ecologie/`](./peniche/02_gestion_eaux_et_ecologie/) : Schémas des boucles d'essai de traitement, notes de calculs MBR.
- [`/peniche/03_energie_electricite_motorisation/`](./peniche/03_energie_electricite_motorisation/) : Schémas unifilaires (400V DC / 230V AC), études de rendement solaire.
- [`/peniche/04_ancrage_amarrage/`](./peniche/04_ancrage_amarrage/) : Calculs et dimensionnement des pieux/amarres.
- [`/vehicules/`](./vehicules/) : Logistique embarquée, grue de levage.
- [`/software/`](./software/) : Code IoT (Home Assistant), scripts Python d'extraction VNF, et ROS 2 pour le drone.
- [`/gestion_projet_et_financement/`](./gestion_projet_et_financement/) : Suivi financier, exports ERPNext.
- [`/docs/`](./docs/) : Contient la Bible Technique, la bibliographie (PDF légaux), les moodboards.

## Règles de Contribution & Synergies

Ce projet repose sur la documentation en Open-Source Hardware et Software.
- Les schémas de CAO (3D/2D) et les PDF lourds doivent être committés via **Git LFS** (voir le fichier `.gitattributes`).
- Les documentations doivent inclure la référence systématique aux lois (ES-TRIN, RGPIN, etc) et comparer des solutions industrielles aux solutions Low-Tech / DIY.
- `prompts_notebook_gemini.md` : Conserve les bases de R&D pour lancer de nouvelles recherches sur Gemini.
