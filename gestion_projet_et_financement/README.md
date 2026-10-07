# Carnet 6 : Gestion de Projet, Opérations et Financement

Ce carnet centralise les stratégies d'acquisitions, de montage de dossiers financiers et le pilotage des opérations (ERP, Rétroplannings).

## 1. Macro : Aides et Financements (VNF, CEE, Crédit Maritime)
* **Distinction Fret vs Habitat** : De nombreuses aides (PARM VNF, PAMI Volet A) sont réservées aux bateaux avec une activité économique (fret, charter, location). Un habitat purement privé n'y a pas droit.
* **CEE (Certificats d'Économie d'Énergie)** : Financement mobilisable sur les équipements efficients (ex. MBR, batteries).
* **Crédit Maritime / Banque Populaire** : Prêts verts maritimes adossés à une hypothèque fluviale (le bateau est un bien meuble, il faut donc une immatriculation au registre du Tribunal de Commerce). Exige un titre de navigation valide et une expertise (sondage ultrasons > 4mm).

## 2. Meso : ERP Open-Source pour le Chantier
* **Odoo Community** : Très connu, mais la version communautaire ampute les fonctionnalités avancées de gestion budgétaire analytique (BOM) et nécessite des plugins.
* **ERPNext (Choix privilégié)** : Solution 100% Open-Source (GPLv3). Relie nativement les centres de coûts, la nomenclature (BOM multi-niveaux pour les composants DIY/R&D), les achats et un diagramme de Gantt interactif.

## 3. Nano : AMDEC (Analyse des Modes de Défaillance)
* **Risque Législatif** : Refus de la COT (Convention d'occupation) suite à un rejet non conforme ou une installation hors ES-TRIN. Mitigation : s'appuyer sur des systèmes MBR du commerce et auditer par l'UTI (Unité Territoriale Itinérante).
* **Risque Financier** : Surcoûts de l'acier et des batteries. Mitigation : Marge de 15% dans l'ERPNext.
* **Risque Technique** : Blocage du système d'alimentation électrique mixte (400V vs 230V).

## 4. Pratique : Rétroplanning à 6 Mois
* **Mois 1-2** : Cadrage avec l'UTI VNF/HAROPA. Intégration des synthèses dans Gemini NotebookLM.
* **Mois 3** : Dépôt du dossier de Manifestation d'Intérêt.
* **Mois 4-5** : Période de publicité légale de 6 semaines. Dépôt de dossier Loi sur l'Eau (DDTM).
* **Mois 6** : Signature éventuelle de la COT et lancement des gros œuvres en chaudronnerie.

---
*Synergies : Les BOMs générés pour les équipements du [Carnet 1 Architecture Navale](../peniche/01_architecture_navale_reglementation_amenagement/README.md) et la robotique sous-marine doivent transiter directement dans ERPNext.*
