# Carnet 3 : Énergie, Électricité et Motorisation Fluviale

Ce carnet définit la stratégie énergétique globale de la péniche, intégrant la réglementation, les choix de rétrofit propulsifs, le photovoltaïque et l'architecture des micro-réseaux.

## 1. Macro : Séparation ES-TRIN (Bloc 1 et Bloc 2)
La réglementation fluviale impose une étanchéité fonctionnelle absolue entre l'habitat et la propulsion.
* **Bloc 1 (Habitat)** : 230V AC / 24V DC. Standard domotique (NFC 15-100).
* **Bloc 2 (Propulsion)** : 400V DC pour les moteurs électriques.
* **Neutre IT** : Les réseaux doivent fonctionner avec des pôles flottants (isolés de la coque) et sous la surveillance de deux Contrôleurs Permanents d'Isolement (CPI) distincts pour le 400V et le 230V.
* **Packs Batteries $\ge$ 20 kWh** : Obligation d'un local dédié classé A60 (Coupe-feu), ventilé vers l'extérieur avec extinction automatique. (Cf. [Aménagement de coque](../01_architecture_navale_reglementation_amenagement/README.md)).
* **EMS (Energy Management System)** : Doit prioriser la propulsion de manière absolue avec un délestage automatique de l'habitat si besoin.

## 2. Meso : Rétrofit Professionnel vs Semi-DIY
* **L'illusion du semi-DIY (batteries auto)** : Bien que moins cher à l'achat, l'absence de certification (EN 62619) interdit l'homologation ES-TRIN, fait perdre l'accès aux assurances maritimes, et annule l'éligibilité aux primes CEE/VNF.
* **La solution Pro (Clé en main)** : Obligatoire pour un bateau navigable de 38m. Garantie, conformité et subventionnable via le dispositif PAMI.

## 3. Nano : Contrôleur de Batterie (BMS) Haute Tension
Pour l'expérimentation hors-propulsion, un BMS 400V doit respecter des contraintes sévères :
* Surveillance cellule par cellule avec gestion thermique active.
* Communication CAN-bus/NMEA 2000 avec isolation galvanique entre la HT (400V) et la BT (24V).
* Interfaçage avec la boucle HVIL (High Voltage Interlock Loop).

## 4. Pratique : Déploiement Solaire sur le Roof
* **Choix technique** : Panneaux ETFE souples, posés sur une sous-couche (type nid d'abeille/polycarbonate) créant une lame d'air de 15mm. Évite la surchauffe de la coque en acier (+15% de rendement récupéré).
* **Topologie MPPT** : Multiplication des petits strings MPPT pour contrer les ombres portées du mât et des arbres de rive.

---
*Synergies : Les batteries du bord serviront également à recharger les véhicules de mobilité terrestre : voir le [Carnet 5 Mobilité Terrestre](../../vehicules/README.md).*
