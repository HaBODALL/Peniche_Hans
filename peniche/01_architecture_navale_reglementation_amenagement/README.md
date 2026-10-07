# Carnet 1 : Architecture Navale, Réglementation et Aménagement

Ce document est la synthèse globale du Carnet 1 issu de l'ingénierie et des carnets NotebookLM. Il regroupe les cadres légaux, l'ingénierie de lestage, la robotique de cale sèche et l'aménagement PMR.

## 1. Macro : Cadre Réglementaire et Points Bloquants
La transformation d'une péniche Freycinet (38,5m) bascule sous le cadre ES-TRIN et l'urbanisme fluvial.

* **ES-TRIN (CESNI)** : Nécessite un titre de navigation. L'épaisseur minimale de coque est de 3,8mm. Séparation stricte exigée entre électricité domestique (230V/24V) et propulsion (400V DC).
* **Isolation et Coupe-Feu** : L'installation de parcs batteries (cf. [Carnet 3 Énergie](../03_energie_electricite_motorisation/README.md)) nécessite un cloisonnement A60. Les vaigrages doivent être difficilement inflammables.
* **Domaine Public Fluvial (VNF/HAROPA)** : La Convention d'Occupation Temporaire (COT) est précaire et révocable. Le rejet d'eaux usées (grises et noires) est **strictement interdit** sans équipement validé (zéro-rejet).
* **Points bloquants (No-Go)** : Perte de COT (activité économique non déclarée), ou coque trop fine (<3,5mm).

## 2. Meso : Ingénierie du Lestage
Le bateau lège pèse environ 50t à 100t. Il faut atteindre un déplacement cible de ~200t pour un tirant d'eau de 1,20m.
* **Fonte (7,2 t/m³)** : Idéale pour gagner de la hauteur sous barrot, mais très chère.
* **Acier / Ferraille (4 à 7 t/m³)** : Bon compromis mais grand risque de rouille et corrosion confinée.
* **Béton Lourd/Standard (2,4 à 3,8 t/m³)** : Option hybride recommandée. Couler le fond entre les varangues avec du béton, puis affiner l'assiette avec quelques gueuses d'acier.
* **Eau** : Exclue au centre (effet de carène liquide), utile uniquement en ballasts fermés compartimentés.

## 3. Nano : Inspection de Coque par Drone (ROV)
Pour éviter la mise en cale sèche (coût et délai tous les 7 à 10 ans), le projet déploie un **ROV d'inspection par ultrasons**.
* **Base matérielle** : BlueROV2 Heavy (8 propulseurs vectorisés) avec Skid magnétique.
* **Sonde** : Palpeur à ultrasons Cygnus Multi-Écho sur cardan à ressorts pour percer la peinture sans la retirer.
* **Reconnaissance** : Conforme IACS UR Z17 / ISO 9712 avec supervision par un expert fluvial à terre.
* **Logiciel** : ROS 2 pour la fusion SLAM et MAVLink. (Voir le dossier logiciel: `../../software/rov_inspection/`)

## 4. Pratique : Checklist Aménagement PMR
* Franchissement vertical par élévateur à vis sans fin pont/cale.
* Plancher nivelé avec tolérance < 5mm.
* **Couloir central ≥ 120 cm**.
* **Aires de rotation ≥ 150 cm** dans chaque zone (salon, SDB, chambre).
* Portes à galandage passage net 83cm, absence totale de seuil (chanfrein max 2cm).

---
*Synergies : Pour le traitement zéro-rejet indispensable au maintien de la COT, consultez le [Carnet 2 Gestion des Eaux](../02_gestion_eaux_et_ecologie/README.md).*
