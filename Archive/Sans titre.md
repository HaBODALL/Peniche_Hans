---
title: "Cahier des Charges — Péniche Laboratoire"
date_creation: 2026-03-13
date_maj: 2026-03-13
version: 1.0
status: 🟡 En cours
tags: [peniche, habitat, PMR, electrique, laboratoire, cahier-des-charges]
---

# 📐 CAHIER DES CHARGES — PÉNICHE LABORATOIRE ÉLECTRIQUE

> **Objectif final :** Habitat fluvial autonome, accessible PMR, 
> intégrant un laboratoire de recherche embarqué.  
> **Deadline symbolique :** Novembre 2028 (40 ans à bord)

---

## 1. 🎯 PROGRAMME FONCTIONNEL

### 1.1 Espaces obligatoires

| Espace | Surface cible | Contrainte PMR | Priorité |
|--------|--------------|----------------|----------|
| Chambre | 12-16 m² | Accès fauteuil, lit accessible | 🔴 Phase 1 |
| Salle de bain / WC | 6-9 m² | Douche italienne, barres appui | 🔴 Phase 1 |
| Cuisine | 8-12 m² | Plan travail adapté | 🟠 Phase 1 |
| Séjour / bureau | 15-20 m² | Circulation 150 cm | 🟠 Phase 1 |
| Laboratoire / atelier | 15-25 m² | Accès matériel lourd | 🟡 Phase 2 |
| Local technique | 4-6 m² | Batteries, BMS, tableau | 🔴 Phase 1 |
| Rangements | — | Intégrés partout | 🟠 Phase 1 |

### 1.2 Espaces souhaitables

- [ ] Terrasse/pont aménagé (convivialité)
- [ ] Espace invité (couchage appoint)
- [ ] Serre / jardinière (autosuffisance partielle)

---

## 2. ♿ EXIGENCES PMR (Non négociables)

| Critère | Valeur minimale | Référence |
|---------|----------------|-----------|
| Largeur circulation | 90 cm | Norme PMR |
| Espace giration | Ø 150 cm | Norme PMR |
| Seuils | 0 cm (ou rampe ≤ 5%) | Norme PMR |
| Sol | Antidérapant R11 minimum | DTU |
| Barres d'appui | WC + douche + accès bord | Norme PMR |
| Accès depuis quai | Passerelle stable, main courante | — |
| Hauteur plan travail | Adaptable 70-90 cm | — |

**Note :** PMR = opportunité design minimaliste et aéré (Red Punk Trunk)

---

## 3. 🌡️ PERFORMANCE THERMIQUE

### Objectif
Confort hivernal sans chauffage lourd (hors vagues de froid)

### Isolation — Points critiques

| Zone | Solution retenue | Alternative | Priorité |
|------|-----------------|-------------|----------|
| Fond de cale | Laine bois/chanvre | Liège projeté | 🔴 |
| Panneaux latéraux | Laine bois/chanvre | Liège projeté | 🔴 |
| Pont (plafond) | Laine bois/chanvre | Laine de roche | 🔴 |
| Timonerie | Laine bois/chanvre | — | 🟠 |

**Décision isolation :** Après visite et mesures réelles  
**Principe :** Matériaux hygroscopiques prioritaires (milieu humide fluvial)

### Chauffage

| Phase | Solution | Budget estimé |
|-------|----------|--------------|
| Phase 1 | Poêle à bois (provisoire) | 800 - 2 000 € |
| Phase 2 | PAC réversible air/eau | 5 000 - 12 000 € |

---

## 4. ⚡ ARCHITECTURE ÉLECTRIQUE

*Détail complet → Matt YAPADEBOULOS*

### Principe : 2 blocs physiquement séparés

BLOC 1 — HABITAT (Phase 1, 2026-2027) 
├── Tableau 230V NFC 15-100 
├── Éclairage LED (circuits dédiés) 
├── Prises courantes (dont prises USB) 
├── Chargeurs appareils lab 
├── Alimentation quai 16A minimum (32A souhaitable) 
└── Budget : 3 000 - 6 000 €

BLOC 2 — PROPULSION ÉLECTRIQUE (Phase 2) 
├── Batteries LiFePO₄ 100-150 kWh 
├── BMS (Battery Management System) 
├── Moteur 20-30 kW 
├── Chargeurs haute puissance 
└── Budget : 50 000 - 90 000 €

### Cadre légal
- **ES-TRIN** : règlement européen transport fluvial
- **Habilitations** : BR/BC minimum avant interventions
- **Certification** : Bureau Veritas avant mise en navigation
- **Séparation physique** obligatoire des 2 blocs

---

## 5. 🔬 LABORATOIRE EMBARQUÉ

### Vocation
Recherche et monitoring environnemental fluvial  
(partenariats VNF, Agence de l'Eau, ADEME envisagés)

### Équipements prévus (Phase 2)

| Équipement | Usage | Notes |
|------------|-------|-------|
| Capteurs eau | Température, pH, turbidité | Matt : monitoring Phase 1 |
| Station météo | Données locales | Intégration domotique |
| Serveur local | Stockage données | Basse consommation |
| Banc test électronique | R&D embarqué | Compétences maker |
| Alimentation stabilisée | Labo | Sur Bloc 1 |

### Données collectées (objectif)
- Qualité eau Seine
- Consommation énergétique embarquée
- Production / stockage énergie
- Données navigation (si mobilité Phase 2)

---

## 6. 💧 PLOMBERIE & EAU

| Poste | Phase 1 | Phase 2 |
|-------|---------|---------|
| Eau douce | Cuve + branchement quai | Récupération pluie |
| Eau chaude | Chauffe-eau électrique 50L | PAC intégrée |
| Eaux grises | Rejet réseau quai | Traitement embarqué |
| WC | WC sec (compostage) | WC marin homologué |
| Pompe de cale | Électrique automatique | Redondance |

---

## 7. 🎨 DIRECTION ARTISTIQUE

*Décision en attente — Red Punk Trunk*

| Option | Concept | Palette | Statut |
|--------|---------|---------|--------|
| **Solarpunk Pragmatique** | Tech au service du vivant | Vert de gris, ocre, corten | ⏳ |
| **Nautique Hacker** | Station polaire / exploration | Anthracite, jaune signal, inox | ⏳ |
| **Wabi-Sabi Fluvial** | Imperfection assumée, patine | Blanc cassé, bois gris, rouille douce | ⏳ |

**Règle Red :** Unification matériaux récup obligatoire (peinture ou texture commune)  
**⚠️ Action requise :** Choisir une direction → débloque charte graphique + nommage bateau

---

## 8. 💰 BUDGET SYNTHÈSE

### Phase 1 — Habitat (2026)

| Poste               | Bas          | Haut         | Notes                        |
| ------------------- | ------------ | ------------ | ---------------------------- |
| Acquisition         | 20 000 €     | 22 500 €     | Idéal mais déjà acheté       |
| Expertise coque     | 800 €        | 1 500 €      | ⚠️ OBLIGATOIRE avant achat   |
| Nettoyage / dépose  | 500 €        | 1 500 €      | DIY possible                 |
| Isolation           | 3 000 €      | 8 000 €      | Laine bois/chanvre           |
| Électricité habitat | 3 000 €      | 6 000 €      | Tableau + prises + éclairage |
| Plomberie de base   | 2 000 €      | 5 000 €      | Eau douce + WC sec           |
| Fermeture hivernale | 500 €        | 2 000 €      | Étanchéité, anti-gel         |
| Imprévus (+15%)     | 4 500 €      | 6 975 €      | Incompressible               |
| **TOTAL Phase 1**   | **34 300 €** | **53 475 €** | **Cible : 38-40k€**          |

### Phase 2 — Propulsion & Labo (post-CDI)

| Poste | Estimation |
|-------|-----------|
| Batteries + BMS | 30 000 - 50 000 € |
| Moteur électrique | 10 000 - 20 000 € |
| Chargeurs HP | 5 000 - 10 000 € |
| Labo équipements | 5 000 - 15 000 € |
| PAC chauffage | 5 000 - 12 000 € |
| **TOTAL Phase 2** | **55 000 - 107 000 €** |

### Financement Phase 1

| Source | Montant | Statut |
|--------|---------|--------|
| Prêt familial | 25 000 - 35 000 € | ⏳ En discussion |
| Économies personnelles | 5 000 - 10 000 € | ⏳ À constituer |
| Revente éléments déposés | 500 - 2 000 € | ⬜ Post-acquisition |

---

## 9. 📅 JALONS CLÉS

| Date | Jalon | Statut |
|------|-------|--------|
| Mars-Avril 2026 | Prospection + visites | 🟡 En cours |
| Mai-Juin 2026 | Acquisition | ⏳ |
| Juin 2026 | Nettoyage, état des lieux précis | ⏳ |
| Juil-Août 2026 | Travaux légers (père présent) | ⏳ |
| Septembre 2026 | Sprint isolation + fermeture | ⏳ |
| Octobre 2026 | ⚠️ DEADLINE hivernage | ⏳ |
| 2027 | Électricité Phase 2, labo | ⏳ |
| Novembre 2028 | 🎂 40 ans à bord | 🎯 |

---

## 10. 🔗 DOCUMENTS LIÉS

- `Doc_LOG_Projets_Habitat_v3.0.md` — Journal de bord projet
- `Doc_Ref_Normes_DTU.md` — Normes applicables
- `CHECKLIST_VISITE_PENICHE.md` — À emporter en visite
- `_Peniche_Index.md` — Vue d'ensemble et backlog

---

## 11. 👥 AGENTS IMPLIQUÉS

| Agent | Rôle | Contact |
|-------|------|---------|
| **Archibald TECARD** | Pilote habitat, structure, travaux | Principal |
| Cal ENDAR | Planning jalons et chantier | — |
| Matt YAPADEBOULOS | Électrique embarqué, monitoring | — |
| Henry BEE | Financement, partenariats scientifiques | — |
| Red Punk Trunk | Direction artistique, communication | En attente décision |

---

*Créé le 13 mars 2026 — Archibald TECARD*  
*Prochaine MAJ : après visite péniche*