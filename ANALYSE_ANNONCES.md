# Analyse de 21 annonces de péniches (Leboncoin, collecte des 16 et 17 octobre 2026)

Source : texte des pages collé par l'utilisateur, jamais lu directement sur le site. Les données détaillées sont dans `annonces.json`. Les scores d'adéquation au projet sont **provisoires** : aucune photo n'a encore été analysée et plusieurs descriptions sont tronquées.

Les pages ont été associées à leurs liens par catégorie et par ordre d'envoi : à confirmer. Le lien de l'annonce 18 (Charleville-Mézières) est déduit de l'ordre d'envoi du dernier lot.

## Règle à garder en tête : la COT

La COT n'est pas transférable de plein droit. Elle se négocie avec le gestionnaire (VNF, ou HAROPA Port sur Paris et l'axe Seine). Une reprise avec le bateau est parfois possible, jamais garantie. Quand une annonce vante un « emplacement », le prix peut donc inclure une valeur d'emplacement qui n'appartient pas au bateau. Pour estimer le prix du bateau lui-même, j'ai classé les annonces en trois catégories :

- **C1** : bateau sans emplacement garanti (valeur de la coque, du moteur, des équipements).
- **C2** : bateau à régulariser (titre, expertise, navigabilité ou emplacement à reprendre).
- **C3** : bateau vendu avec exploitation, emplacement ou aménagement lourd.

## Tableau comparatif

Cat. : C1 bateau sans emplacement garanti, C2 à régulariser, C3 logement ou exploitation. Un astérisque indique un gabarit inconnu ou différent de la Freycinet : l'annonce est exclue de la médiane.

| N° | Lieu | Prix | Année | Titre / certificat | COT / emplacement | Coque | Cat. | Score |
| :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- | :-- |
| [1](https://www.leboncoin.fr/ad/nautisme/3285702400) | Paris 12e | 70 000 € | ? | non indiqué | sans COT | fond refait en 2003 | C1 | 3 |
| [2](https://www.leboncoin.fr/ad/ventes_immobilieres/3236617822) | Reims | 18 000 € | 1947 | « irrégulière » (sondage > 10 ans) | non indiqué | cale sèche 2005 | C2 | 2 |
| [3](https://www.leboncoin.fr/ad/nautisme/3243153381) | Creil | 48 000 € | 1964 | expiré depuis 2019 | redevance sans titre (COSTU) | doublage 2024, sondage 2024 | C2 | 4 |
| [4](https://www.leboncoin.fr/ad/nautisme/3209529995) | Noyon | 95 000 € | 1964 | « était » jauge du Rhin | non indiqué | fond neuf doublé 6 mm | C1 | 3 |
| [5](https://www.leboncoin.fr/ad/bureaux_commerces/3232173230) | Auvers-sur-Oise | 160 000 € | 1924 | non indiqué (ERP) | COT « en cours de signature » | non indiqué | C3 | 2 |
| [6](https://www.leboncoin.fr/ad/nautisme/3253976756) | Saint-Mammès | 70 000 € | ? | non indiqué | non indiqué | non indiqué | C1 | 4 |
| [7](https://www.leboncoin.fr/ad/nautisme/3258147912) | Longueil-Annel | 75 000 € | 1960 | « jauge du Rhin 2027 » | non indiqué | non indiqué | C1 | 3 |
| [8](https://www.leboncoin.fr/ad/nautisme/3224798234) | Dunkerque | 85 000 € | 1960 | **valide jusqu'en nov. 2033** | non indiqué | plancher de cale fer étanche | C1 | 4 |
| [9](https://www.leboncoin.fr/ad/nautisme/3264801998) | Lille (bateau en Belgique ?) | 25 000 € | 1920 | à remorquer, sans instruments | doit quitter l'emplacement | coque neuve 2009, immobile | C2 | 1 |
| [10](https://www.leboncoin.fr/ad/nautisme/3123809158) | Auxerre | 38 000 € | ? | non indiqué | bief privé | non indiqué | C3 | 2 |
| [11](https://www.leboncoin.fr/ad/bureaux_commerces/3232049517) | Saint-Jean-de-Losne (Saïga) | 48 000 € | 1951 | « navigue partout » | non indiqué | expertisée 2023 | C1* | 3 |
| [12](https://www.leboncoin.fr/ad/nautisme/3267732061) | Dunkerque (citerne) | 75 000 € | ? | « certificat de l'Union renouvelé » | non indiqué | non indiqué | C1* | 2 |
| [13](https://www.leboncoin.fr/ad/nautisme/3269081222) | Roubaix (bateau à Vilvoorde, Belgique) | 75 000 € | 1965 | immatriculé en plaisance | non indiqué | non indiqué | C1 | 3 |
| [14](https://www.leboncoin.fr/ad/nautisme/3132319776) | Arleux (Jessica) | 70 000 € | 1962 | **certificat de l'Union jusqu'en 2029** | non indiqué | plancher de fer | C1 | 4 |
| [15](https://www.leboncoin.fr/ad/equipement_nautisme/3278579536) | Douai | 50 000 € | 1961 | « documents valides jusqu'en sept. 2030 » | non indiqué | fond changé | C1 | 3 |
| [16](https://www.leboncoin.fr/ad/nautisme/3280816668) | Vigneux-sur-Seine | 155 000 € | 1937 | non indiqué | non indiqué | non indiqué | C3* | 1 |
| [17](https://www.leboncoin.fr/ad/nautisme/3283172783) | Dunkerque (Ebonystar) | 60 000 € | 1931 | « certificats coque à jour » | non indiqué | contrôle de coque (tronqué) | C1* | 2 |
| [18](https://www.leboncoin.fr/ad/nautisme/3283609562) | Charleville-Mézières | 80 000 € | 1954 | non indiqué | non indiqué | fond rénové 1992 (7 mm) | C1* | 3 |
| [19](https://www.leboncoin.fr/ad/nautisme/3265626787) | Saint-Jean-de-Losne | 90 000 € | 1969 | **certificat jusqu'en 2030** | basé au port (régime à demander) | montée en cale juin 2023 | C1 | 4 |
| [20](https://www.leboncoin.fr/ad/nautisme/3057499757) | Cercy-la-Tour | 39 000 € | ? | non indiqué | « avec emplacement » (annonce) | non indiqué | C3* | 2 |
| [21](https://www.leboncoin.fr/ad/ventes_immobilieres/3224802075) | Compiègne (rénovée) | 179 000 € | ? | non indiqué | « emplacement en règle » (annonce) | expertise septembre 2019 | C3 | 2 |

## Annonces 4 à 11

**4. Noyon, 95 000 €** : Freycinet de 1964 avec fond neuf doublé en 6 mm, plancher étanche, hublots neufs. Bon état annoncé, mais prix élevé, certification « jauge du Rhin » écrite au passé, et pont à demi fermé avec véranda prévue (aménagements à adapter).

**5. Auvers-sur-Oise, 160 000 €** : c'est un fonds de commerce (restaurant ou événementiel) sur une péniche classée ERP, avec une COT encore « en cours de signature ». Le prix mélange fonds, bateau et espérance de COT : on ne peut pas en tirer la valeur du bateau. Utile surtout comme repère de ce que vaut un emplacement touristique.

**6. Saint-Mammès, 70 000 €** : la plus proche de votre besoin technique. Péniche de 39 m des chantiers Michot, cale non aménagée mais **déjà lestée, avec cornières soudées pour poser un plancher**, logement de marinier (salon, 2 chambres), gare à 10 min, Paris à 45 min en train. Il manque la largeur, l'année, le titre, la coque et la COT.

**7. Longueil-Annel, 75 000 €** : annonce de deux lignes (« Moerbeke 1960, 38 m × 5,10 m, 379 T, équipé commerce, jauge du Rhin 2027 »). La largeur de 5,10 m dépasse les 5,05 m du gabarit Freycinet : à vérifier pour les écluses. Presque aucune information sur le reste.

**8. Dunkerque, 85 000 €** : le point fort décisif est le **certificat communautaire valide jusqu'en novembre 2033**, qui suppose normalement une inspection récente (à demander). Cale non aménagée avec plancher de fer étanche, moteur Scania et deux groupes Lister, logement du marinier de 35 m² et logement avant aménagés. Éloignée de la région parisienne, vendeur peu actif.

**9. Lille (bateau à Péronnes-lez-Antoing), 25 000 €** : péniche de 1920, 38 × 5 m, immobile et jamais sortie de l'eau depuis 2009, sans instruments, à remorquer, et qui doit quitter son emplacement. Le nom de la commune me semble belge : autre autorité de gestion et autres règles, à vérifier. Écartée en l'état.

**10. Auxerre, 38 000 €** : appartement flottant de 135 m² avec terrasse de 40 m² sur un bief privé, très regardé (423 favoris). Le prix est étonnamment bas pour le descriptif : il faut comprendre la navigabilité, le titre, le statut du bief et les charges. La cale est occupée par l'appartement, donc peu compatible avec votre projet.

**11. Saïga, 48 000 €** : péniche de 1951, coque expertisée en 2023, vendue via le courtier H2O Bateau (fiche « Péniche Saïga » sur son site). Le gabarit n'est pas donné (100 m² laisse penser à un bateau plus petit qu'une Freycinet).

## Annonces 12 à 18

**12. Dunkerque, bateau citerne, 75 000 €** : annonce de trois lignes (« peut être transformé en bateau logement », « certificat de l'Union renouvelé »). Aucune dimension, aucun moteur. Une citerne a une cale cloisonnée en cuves, donc une reconversion plus lourde, et il faudrait connaître les cargaisons transportées et le dégazage.

**13. Roubaix, bateau à Vilvoorde (Belgique), 75 000 €** : Freycinet de 38 m construite en 1965 à Thuin, moteur Cummins 257 kW, annoncée en parfait état de navigation, mais **immatriculée comme bateau de plaisance** et située en Belgique. Pour un usage habitation, atelier ou professionnel, il faudra un autre statut et les autorisations correspondantes, et vérifier l'immatriculation et le statut TVA.

**14. Arleux, Jessica, 70 000 €** : c'est la fiche technique la plus complète. Freycinet de 1962 (Forges de Strasbourg), **38,50 × 5,05 m**, certificat de l'Union annoncé valide jusqu'en 2029, plancher de fer, panneaux roulants aluminium, moteur Volvo 380 ch à 8 800 heures, propulseur d'étrave de 160 ch, groupe électrogène Hatz insonorisé de 17 kVA et surtout une **pompe de ballast fixe de 100 t**. Elle reste à documenter sur la coque, la COT et l'emplacement ; elle est dans le Nord.

**15. Douai, 50 000 €** : péniche de 38 × 5 m de 1961, fond changé, moteur Iveco 350 ch, groupe Lister de 15 kVA, plancher de fer, documents valides jusqu'en septembre 2030. L'annonce est classée en « Équipements bateau » avec le bouton « Transaction sécurisée » : pour un bateau de cette taille, il faut un acte de vente et des papiers vérifiés, et une visite avant tout paiement en ligne.

**16. Vigneux-sur-Seine, 155 000 €** : péniche logement de 1937, 90 m² sur deux niveaux avec terrasse de 20 m² (environ 1 722 € par m²). Utile comme repère de prix francilien pour du logement, pas pour votre projet.

**17. Dunkerque, Ebonystar, 60 000 €** : péniche de 1931, 30 m, moteur de 121,3 kW, certificats de coque annoncés à jour. La largeur de 5,28 m est supérieure aux 5,05 m du gabarit Freycinet, ce qui restreint les itinéraires (et le titre de l'annonce dit « 5 m »).

**18. Charleville-Mézières, 80 000 €** : péniche « type plaquet » (terme de l'annonce) de 1954, fond rénové en 1992 à 7 mm, ligne d'arbre et gouvernail refaits en 2009, et **grue de levage de 2 t** embarquée, intéressante pour l'atelier. Gabarit, titre et moteur ne sont pas indiqués.

## Annonces 19 à 21

**19. Saint-Jean-de-Losne, 90 000 € (fiche complète recollée le 22 octobre)** : Freycinet de 38,80 × 5,05 m construite en 1969 à Douai, rivée et soudée. Le dossier est plus solide que je ne le pensais : **certificat communautaire valable jusqu'en 2030**, dernière montée en cale en juin 2023, cales aménageables de **63 m² et 42 m²** (suggestion de plan en annexe), logement du marinier de 26 m² refait à neuf, grue de 1,2 t, bateau basé au port de Saint-Jean-de-Losne. Points faibles : moteur GM 92 de 365 ch à 26 000 heures, pas de propulseur d'étrave, aucune cuve d'eaux noires (WC sanibroyeur) et marquise encore en restauration. L'annonce a été remontée le 20 octobre après un premier dépôt le 13, sans changement de prix : elle ne semble pas avoir trouvé preneur. Visites le week-end sur rendez-vous.

**20. Cercy-la-Tour, 39 000 €** : « beau bateau avec emplacement » dans un village de la Nièvre, ancien magasin d'accastillage, partie isolée, moteur Volvo Penta 380 ch en bon état, 332 favoris, baisse de prix. Aucune dimension. Comme l'emplacement n'est pas transférable de plein droit, il faut le confirmer avec le gestionnaire avant de payer pour lui.

**21. Compiègne, 179 000 €** : annonce d'agence (iad France) classée en vente immobilière, mais pour une péniche, comme l'indique elle-même l'annonce : Freycinet de 38,95 × 5,05 m, entièrement rénovée (pièce de vie de 51 m², terrasse couverte de 40 m², 3 chambres, baignoire à remous), moteur GM 180 ch fonctionnel, dernière expertise de coque en septembre 2019, « emplacement en règle ». Comme la cale est entièrement occupée par le logement, elle convient mal à un atelier ou à un laboratoire ; elle sert surtout de repère de prix pour un Freycinet rénové avec emplacement dans l'Oise. L'emplacement n'est pas cessible de plein droit : « en règle » vaut pour le vendeur, pas pour l'acheteur.

## Lecture du marché (prudente : 21 annonces, prix demandés)

- **C1, Freycinet de 38 à 39 m navigables sans emplacement garanti** (annonces 1, 4, 6, 7, 8, 13, 14, 15, 19 : 9 annonces) : de 50 000 € à 95 000 €, médiane **75 000 €** (la même sans l'annonce de Douai). Cinq annonces sur neuf se placent entre 70 000 et 75 000 €, les autres à 85 000, 90 000 et 95 000 €.
- Le certificat valide ne suffit pas à expliquer l'écart : Dunkerque (certificat jusqu'en 2033) est à 85 000 €, Jessica (jusqu'en 2029) à 70 000 €, Douai (documents jusqu'en 2030) à 50 000 €, Saint-Jean-de-Losne (jusqu'en 2030, montée en cale en 2023) à 90 000 €. Le logement du marinier aménagé, le moteur (Saint-Jean-de-Losne a 26 000 heures pour 90 000 €) et l'état de la coque pèsent aussi.
- **C2, à régulariser** (annonces 2, 3, 9) : de 18 000 € à 48 000 €, selon la date du dernier sondage et la remise en conformité à prévoir.
- **C3, logement ou emplacement annoncé** : 38 000 € (Auxerre), 39 000 € (Cercy-la-Tour), 155 000 € (Vigneux), 160 000 € (Auvers, fonds de commerce). Les deux annonces de province qui mettent en avant un emplacement sont autour de 38 - 39 000 € : l'emplacement semble y peser moins qu'en Île-de-France, où les péniches logement affichées montent à 215 000 - 345 000 €. Deux annonces au gabarit inconnu ne suffisent pas à conclure.
- **Compiègne (annonce 21)** montre l'autre extrême : une Freycinet de 38,95 × 5,05 m entièrement rénovée, avec emplacement annoncé en règle, à 179 000 €. L'écart d'environ 100 000 € avec la médiane des Freycinet navigables non aménagées (75 000 €) mélange la rénovation du logement et l'emplacement : je ne peux pas les séparer avec une seule annonce.
- Les bateaux de gabarit différent ou inconnu (30 m, citerne, type inconnu) sont exclus de la médiane.
- La catégorie C1 peut cacher une valeur d'emplacement dans le prix (COT non transférable de plein droit) : à demander à chaque vendeur.
- Le prix d'achat n'est qu'une partie du budget (expertise, cale sèche éventuelle, remise en conformité électrique, titre de navigation, emplacement). Ces postes sont à chiffrer avec des devis.

## Financement et calendrier (vos contraintes du 17 octobre 2026)

Vos hypothèses : amarrage en Île-de-France pour commencer (vous êtes originaire du Nord), achat à la fin de l'hiver ou au début du printemps 2027, et un prêt d'achat d'au plus 50 000 € plus facile à obtenir qu'un prêt de 70 000 € ou plus, avec un éventuel second prêt pour les travaux. Le seuil de 50 000 € n'est pas un plafond ferme : il sera à voir avec les banques. Je ne suis pas conseiller financier : voici des éléments à faire valider par une banque ou un courtier.

**Répartition des annonces par prix demandé**

| Tranche | Annonces |
| :-- | :-- |
| Jusqu'à 50 000 € | 2 Reims 18 000 · 9 Lille 25 000 · 10 Auxerre 38 000 · 20 Cercy-la-Tour 39 000 · 3 Creil 48 000 (à débattre) · 11 Saïga 48 000 · 15 Douai 50 000 |
| 50 000 à 80 000 € | 17 Ebonystar 60 000 · 1 Paris 70 000 · 6 Saint-Mammès 70 000 · 14 Arleux 70 000 · 7 Longueil-Annel 75 000 · 12 citerne 75 000 · 13 Roubaix 75 000 · 18 Charleville 80 000 |
| Plus de 80 000 € | 8 Dunkerque 85 000 · 19 Saint-Jean-de-Losne 90 000 · 4 Noyon 95 000 · 16 Vigneux 155 000 · 5 Auvers 160 000 · 21 Compiègne 179 000 |

**Ce qu'il faut savoir sur le financement**

- Un bateau est un bien meuble : pas de crédit immobilier classique. Le financement passe par un prêt personnel ou affecté, ou un crédit spécialisé comme le Crédit Maritime. L'hypothèque fluviale existe, mais d'après la Bible (6.1) elle exige une immatriculation, une expertise de coque récente, un titre de navigation et une COT valide : plusieurs bateaux de la liste n'y répondent pas, donc le prêt se ferait sans garantie sur le bateau.
- Votre intuition est raisonnable : un montant plus faible et une durée plus courte passent généralement plus facilement. Ce n'est pas une règle, cela dépend de vos revenus, de votre apport et de la banque, et certains prêts personnels sont plafonnés (à vérifier auprès des établissements).
- Pour le second prêt « travaux », les dispositifs classiques liés au logement (éco-PTZ, MaPrimeRénov) ne s'appliquent pas aux bateaux selon la Bible, et le PAMI est réservé aux activités commerciales déclarées. Il s'agirait donc plutôt d'un deuxième prêt personnel. Son avantage : le montant se chiffre sur devis après l'expertise de coque. Son risque : les deux prêts s'additionnent dans votre taux d'endettement.
- Passer de 70 000 - 75 000 € affichés à moins de 50 000 € demande une remise d'environ 30 %, ce qui est rare sur les bateaux en bon état. Pour rester sous 50 000 €, mieux vaut viser les annonces déjà à ce niveau.
- Le prix d'achat n'est qu'une partie du coût : expertise de coque, assurance, emplacement, convoyage, mise en conformité électrique et titre de navigation. Ces postes doivent entrer dans le montant total à financer.

**Ce que cela change pour les candidats**

- **Annonce 3 (Creil, 48 000 €, à débattre)** : sous le seuil, dans l'Oise (donc proche de l'Île-de-France, à vérifier sur le temps de trajet), coque doublée en 2024 avec plan de sondage. Le second prêt serait destiné à la mise en conformité électrique et au titre de navigation, expiré depuis 2019. L'emplacement reste sous redevance sans titre : à sécuriser avant l'achat.
- **Annonce 15 (Douai, 50 000 €)** : au seuil exact, une négociation sous 50 000 € est envisageable, mais elle est loin de l'Île-de-France et les papiers sont à vérifier.
- **Annonce 6 (Saint-Mammès, 70 000 €)** : en Seine-et-Marne, cale lestée prête à aménager. Un prêt d'achat plus élevé, ou une négociation sérieuse.
- **Annonce 14 (Jessica, 70 000 €)** : la meilleure fiche technique, mais dans le Nord : convoyage en Île-de-France à prévoir.
- **Annonce 1 (Paris 12e, 70 000 €)** : bien placée, mais sans COT, et la zone de Paris relève de HAROPA, où l'emplacement est le point le plus difficile.

**Calendrier (de fin octobre 2026 à mars - avril 2027)**

- Octobre - novembre : demander documents et sondages pour 4 à 5 bateaux, et sonder deux banques (dont le Crédit Maritime) sur le montant et le type de prêt possibles.
- Décembre - février : suivre les prix chaque mois (plusieurs annonces affichent déjà des baisses, comme Cercy-la-Tour) et visiter les bateaux restants. L'hiver est souvent une période plus calme pour les ventes de bateaux, ce qui peut aider la négociation : à vérifier sur les annonces suivies.
- Mars - avril : expertise de coque indépendante avant de signer, puis l'offre.
- Certaines annonces auront disparu d'ici là : prévoir de remplacer les candidats qui se vendent.

## Pour votre projet

Par ordre de proximité avec vos besoins (cale libre, lestage, coque fiable), en tenant compte d'un amarrage initial en Île-de-France :
1. **Annonce 3 (Creil, 48 000 €)** : compatible avec un prêt d'achat proche de 50 000 €, proche de l'Île-de-France, coque récente. Il faut chiffrer la remise en conformité électrique et le titre, et sécuriser l'emplacement.
2. **Annonce 6 (Saint-Mammès, 70 000 €)** : en Île-de-France, cale lestée avec cornières pour un plancher ; peu de données techniques.
3. **Annonce 14 (Arleux, Jessica, 70 000 €)** : gabarit exact, certificat jusqu'en 2029, ballast fixe de 100 t, mais dans le Nord.
4. **Annonce 19 (Saint-Jean-de-Losne, 90 000 €)** : certificat jusqu'en 2030, cale sèche en 2023, deux cales aménageables, logement neuf ; prix élevé, moteur très usé, éloignée de l'Île-de-France.
5. **Annonce 8 (Dunkerque, 85 000 €)** : certificat jusqu'en 2033, cale non aménagée ; éloignée et chère.
6. À creuser ensuite : annonce 15 (Douai, 50 000 €, papiers à vérifier) et annonce 18 (grue de 2 t, gabarit à connaître). L'annonce 21 (Compiègne) sert surtout de repère de prix.

Pour un amarrage en Île-de-France, l'emplacement est probablement une contrainte plus forte que le prix : voir la règle sur la COT en tête de ce document.

## Prochaines étapes

1. Contacter les vendeurs des annonces 3, 6, 14 et 15 avec les questions de `annonces.json` (certificat, dernier sondage et épaisseurs, régime d'occupation).
2. Renseigner le gestionnaire de la voie d'eau de Creil sur la cession ou le maintien de l'emplacement.
3. Sonder deux banques (dont le Crédit Maritime) sur le type et le plafond de prêt possible pour un bateau sans hypothèque.
4. Établir pour chaque candidat un budget total (achat, expertise, assurance, emplacement, conformité, convoyage) avec des devis.
5. Suivre les prix chaque mois et noter les baisses dans `annonces.json`.
6. Regarder la fiche « Péniche Saïga » chez H2O Bateau pour connaître le gabarit.
