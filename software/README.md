# IT, Logiciel, Supervision et Réseaux (IoT)

L'architecture informatique Edge, les protocoles réseau (LoRaWAN, Wi-Fi HaLow), le durcissement du serveur (RAID, PLP, tropicalisation) et la logique offline-first ont été intégrés à la documentation globale.

👉 **Veuillez consulter le Chapitre 4 de la [Bible Technique du Projet](../docs/BIBLE_TECHNIQUE_PENICHE.md#4-it-logiciel-supervision-et-réseaux-iot).**

## 🛠️ Outils de Dimensionnement & Suivi Interconnectés

Un outil logiciel interconnecté (Python / Streamlit) a été créé sous [`/outils/`](../outils/) pour modéliser et suivre :
- **Budget & Financement** (CAPEX/OPEX, prêts, 15% imprévus, redevances VNF COT)
- **Lestage & Archimède** (Masse, tirant d'eau, assiette, hauteur métacentrique GM, surface libre)
- **Bilan Électrique & Solaire** (Batteries 400V, dégradation thermique panneaux)
- **Gestion des Eaux** (Réserves eau propre, grises, noires)
- **Régulation Thermique** (Boucle PAC eau de rivière $Q = m \cdot C_p \cdot \Delta T$)
- **Alertes Réglementaires** (A60 batteries >= 20kWh, tirant d'eau max, stabilité)

Consulter le guide complet dans [`/outils/README.md`](../outils/README.md).
