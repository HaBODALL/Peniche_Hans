# Analyse du Sous-Projet : Véhicules et Motocycles

Dans le cadre du projet global d'habitat/atelier mobile sur péniche, une réflexion est menée sur la mobilité terrestre annexe.

L'objectif est de disposer de moyens de transport adaptés à différents types de trajets, avec une orientation forte vers l'électrification.

## Besoins en Mobilité Terrestre

La mobilité se décompose en trois catégories principales :

1. **Trajets courts/moyens (~50 km aller) :**
   - **Solution envisagée :** Vélo à Assistance Électrique (VAE) ou Speedbike.
   - **Usage :** Déplacements de proximité, ravitaillement léger, trajets pendulaires modérés.

2. **Trajets intermédiaires (> 70 km aller ou besoin de rapidité) :**
   - **Solution envisagée :** Moto électrique (équivalent 250 cm³ ou 500 cm³, catégorie L3e).
   - **Usage :** Déplacements plus lointains nécessitant d'emprunter des axes rapides ou un gain de temps significatif.

3. **Gros trajets ou transport de charge :**
   - **Solution envisagée :** Voiture (idéalement électrique) ou potentiellement une moto électrique de plus grosse cylindrée si la charge le permet.
   - **Usage :** Longs trajets, transport de matériel pour l'atelier, déplacements à plusieurs.

## Focus sur la catégorie Motocycle (Équivalent 250/500 cm³)

Le besoin se concentre actuellement sur la catégorie intermédiaire : une moto électrique capable de réaliser des trajets de plus de 70 km, équivalente à une cylindrée thermique de 250 à 500 cm³.

### État de l'art du marché neuf
Actuellement, les modèles électriques performants et autonomes sur ce segment (par exemple : Zero Motorcycles, Energica, LiveWire) ont un coût d'acquisition élevé, avoisinant les **22 000 €**. Ce budget conséquent pousse à réfléchir à des alternatives.

### L'alternative : La Fabrication DIY (Do It Yourself) / Rétrofit
Face au coût de l'achat neuf, la possibilité de concevoir ou d'assembler soi-même (DIY) ce véhicule est envisagée. Cette démarche s'inscrit bien dans l'esprit R&D et "atelier" de la péniche.

**Avantages du DIY :**
- Réduction potentielle des coûts (selon les composants choisis : moteurs, contrôleurs, batteries).
- Maîtrise totale de la technologie, réparabilité.
- Sur-mesure par rapport au besoin d'autonomie (> 70km) et d'encombrement (stockage sur la péniche).

**Défis du DIY :**
- **Techniques :** Conception sécurisée du pack batterie, dimensionnement moteur/contrôleur, intégration sur un châssis existant (rétrofit) ou création d'un châssis tubulaire.
- **Réglementaires :** C'est le frein principal. Homologuer un véhicule construit ou lourdement modifié par un particulier en France est un parcours complexe (Réception à Titre Isolé).

La suite de la documentation se concentrera sur l'aspect réglementaire de cette démarche DIY en France.

> **Note sur la Stratégie Actuelle et Contradiction Historique :**
> Bien que la démarche DIY / Low-Tech soit toujours valorisée pour son aspect éducatif, expérimental et réparable au sein de l'atelier, **la stratégie actuelle a évolué et s'oriente vers le marché de l'occasion ou le rétrofit professionnel**.
>
> *Pourquoi ce changement ?*
> 1. Les contraintes strictes d'homologation française (et européennes) rendent la démarche de fabrication purement DIY extrêmement difficile à légaliser sur route ouverte pour un particulier.
> 2. Des exigences strictes de charge utile : la moto doit pouvoir supporter 200 à 250 kg (deux personnes avec bagages).
> 3. Des critères esthétiques spécifiques orientés vers le style "Néo-rétro" (ex: Triumph, Maeving) ou "Roadster moderne" (ex: Zero Motorcycles, Yamaha).
>
> Par conséquent, nous privilégions la recherche de modèles récents d'occasion comme la **Zero Motorcycles S ou SR/F**, ou encore l'achat de solutions de rétrofit professionnellement certifiées (conformément aux arrêtés de 2020 sur le rétrofit en France). L'analyse DIY originale est conservée ci-dessus pour la traçabilité de nos recherches initiales.

## Références et Bibliographie

### Modèles du marché (Roadsters modernes & Néo-Rétro)
- [Fiche Technique : Zero SR/F (2023)](../../bibliographie/vehicules/zero_srf_specs.pdf) - Modèle de référence pour les performances attendues sur un roadster moderne.

### Composants DIY et Rétrofit
*Note : Ces documents sont inclus à titre informatif et d'exploration technologique (DIY).*
- [Documentation : Moteur QS 138 90H 4000W V3](../../bibliographie/vehicules/qs_motor_138_specs.pdf) - Exemple de moteur très utilisé dans les conversions de catégorie L3e.
- [Manuel : Contrôleur Kelly](../../bibliographie/vehicules/kelly_controller_manual.pdf) - Référence pour la gestion de la puissance.
- [Spécifications : BMS ANT](../../bibliographie/vehicules/bms_ant_specs.pdf) - Système de gestion de batterie pour les packs assemblés sur mesure.
