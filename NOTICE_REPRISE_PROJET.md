# Notice d'Accompagnement à la Reprise du Projet (Péniche Freycinet)

Salut ! 👋

Si tu lis ces lignes, c’est que tu reprends le flambeau sur le projet technologique et logiciel de notre Péniche Freycinet. Je sais que reprendre le code et l'architecture de quelqu'un d'autre peut faire peur, surtout quand on mélange du code logiciel avec un vrai bateau de 200 tonnes !

Mais respire un grand coup : **tout va bien se passer**. J'ai écrit ce guide spécialement pour toi, en partant du principe que tu maîtrises notre métier et notre projet de vie, mais que le code source, ce n'est pas (encore) ton langage maternel.

Ce document est ta bouée de sauvetage. Garde-le sous la main, il te montrera où chercher, comment lire notre logique, et comment bidouiller sans couler le navire.

---

## 1. Cartographie Mentale (Architecture Globale)

Imagine le système informatique de la péniche comme un grand équipage où chaque membre a un rôle précis :

*   **Les Capteurs (Les Yeux et les Oreilles)** : Dispersés partout dans les cales et les moteurs. Ils surveillent le niveau des cuves, la température des batteries 400V, l'humidité, etc. Ils parlent des langages très basiques (LoRa, N2K, Modbus).
*   **Le Serveur Local Edge (Le Cerveau central)** : C'est notre ordinateur principal (Fanless, durci contre les vibrations). Il fonctionne avec **Home Assistant** (un chef d'orchestre domotique). Il écoute tous les capteurs, stocke l'historique dans une base de données locale, et décide s'il faut déclencher des alarmes.
*   **L'Application Android / Tablette (Le Tableau de Bord)** : C'est ce que tu utilises pour piloter la péniche. L'application (souvent appelée "Client") vient poser des questions au Serveur Central ("Quel est le niveau d'eau de la cuve ?") et affiche de jolis boutons.
*   **Les Scripts Python (Les Assistants Spécialisés)** : Ce sont de petits programmes automatiques. Par exemple, l'un d'eux va lire la météo et la carte des parkings VNF sur internet et la donne au Serveur Central.
*   **ROS 2 (Le Pilote du Sous-marin)** : C'est un système totalement à part, conçu uniquement pour piloter notre petit drone sous-marin qui va inspecter la coque en acier de la péniche.

**La règle d'or (Offline-First) :** Le bateau doit *toujours* fonctionner, même s'il n'y a plus de 4G. Le Cerveau Central est donc *dans* le bateau, pas dans un nuage lointain (le Cloud).

---

## 2. Visite Guidée du Code (Où trouver quoi ?)

Notre dépôt de code est rangé par thèmes. Voici ta carte au trésor à la racine du projet :

*   📁 **`docs/`** : L'encyclopédie du projet. C'est ici que tu trouveras la `BIBLE_TECHNIQUE_PENICHE.md`. Si tu veux relire pourquoi on a choisi de la fonte ou du béton pour alourdir le bateau, c'est là !
*   📁 **`bibliographie/`** : Les textes de loi (VNF, ES-TRIN). Ce sont tous les PDF officiels.
*   📁 **`software/`** : **C'est ici que tu vas passer le plus de temps pour la technique.**
    *   Si tu veux modifier l'outil qui télécharge les cartes VNF, cherche les scripts Python à l'intérieur.
    *   Si tu cherches comment fonctionne l'outil budgétaire ou Home Assistant, la doc `OUTILS_SUIVI_NAVIGATION.md` t'expliquera la démarche.
*   📄 **`prompts_notebook_gemini.md`** : Notre cerveau IA ! Si tu veux modifier les mots-clés qu'on donne à l'IA pour l'aider à trouver des infos sur notre bateau, tu modifies ce fichier.
*   📄 **`MISSING_DOCS.md`** : La liste des courses des fichiers qu'on doit encore télécharger et ranger.

**Exemples pratiques :**
*   *Tu veux changer l'adresse de la base de données VNF ?* $\rightarrow$ Va dans `software/` et ouvre le script Python d'extraction API.
*   *Tu veux ajouter un paragraphe sur les nouvelles réglementations ES-TRIN ?* $\rightarrow$ Va dans `docs/BIBLE_TECHNIQUE_PENICHE.md`.

---

## 3. Les Concepts Clés à retenir (Crash Course)

Pas besoin d'un bac+5 en informatique, voici les 3 concepts magiques pour comprendre nos outils :

1.  **L'architecture Offline-First (Priorité au mode hors-ligne)** :
    L'application de la tablette garde une copie locale des données (grâce à un outil appelé `Jetpack Room DB`). Si la connexion coupe, l'app utilise sa copie locale. Quand le Wi-Fi revient, un "facteur" silencieux (le `WorkManager`) envoie les mises à jour en arrière-plan.
2.  **MQTT (Le système de messagerie des machines)** :
    Quand un capteur (ex: thermomètre moteur) veut envoyer sa température, il ne l'envoie pas directement à ta tablette. Il crie la température dans un tuyau ("Hey, la temp est de 80°C !"). Le Serveur Central écoute ce tuyau, l'enregistre, puis Home Assistant l'affiche. C'est ça le MQTT : un tableau d'affichage numérique.
3.  **Les API (Les guichets d'information)** :
    Quand notre script Python veut connaître les places d'amarrage (EuRIS), il parle à une API. Une API, c'est comme le guichetier d'une gare. On lui demande : *"Donne-moi les places de port"* (c'est la *Requête*), et le guichetier nous donne un ticket avec l'information écrite dessus (la *Réponse*, souvent dans un format lisible par ordinateur appelé JSON).

---

## 4. Le Flux de la Donnée (Anatomie d'une action)

Suivons le cheminement d'une alerte critique : **"Le niveau d'eau de la cuve de phyto-épuration déborde !"**

1.  **Le Capteur (La Bouée)** : Un capteur de flotteur physique dans la cuve des eaux grises se déclenche.
2.  **L'Émission (LoRaWAN)** : Le capteur envoie un micro-message radio (qui passe super bien à travers la coque en acier du bateau) vers le Serveur Central.
3.  **La Réception (Le Cerveau)** : Le Serveur Central (Home Assistant) reçoit le message via son système de tri du courrier (MQTT).
4.  **La Logique de crise (L'Automate)** : Home Assistant regarde ses règles : *"Oh là là, ce capteur est en Alarme Haute !"*. Il décide de couper automatiquement la pompe à eau pour éviter une inondation.
5.  **L'Affichage (La Tablette)** : Home Assistant envoie une notification immédiate à ton réseau local. Ton téléphone et la tablette de la timonerie clignotent en rouge : *"ALERTE : Débordement cuve. Pompe arrêtée."*

---

## 5. Le Guide de Survie (Débogage & Compilation)

Voici ton kit de secours. Si un truc ne marche pas, ne panique pas, c'est normal, c'est de l'informatique.

### A. Si tu modifies un script Python (Outils carto / Navigation)
*   **Pour le lancer** : Ouvre un terminal (l'écran noir) à la racine de `software/` et tape : `python nom_du_script.py`
*   **L'erreur classique** : `ModuleNotFoundError`.
    *   *Signification* : Il te manque un "outil" externe pour faire tourner le script (comme une clé à molette manquante).
    *   *Solution* : Tape `pip install nom_du_module_manquant` pour l'installer.

### B. Si l'application Android ou la Tablette affiche un "Écran Blanc"
1.  Vérifie d'abord que le Wi-Fi du bateau fonctionne.
2.  Vérifie que le "Serveur Central Edge" est allumé et branché (il gère tout).
3.  Ferme l'application de force sur la tablette et relance-la (souvent, ça resynchronise la base de données locale `Room DB`).

### C. Si le serveur "Home Assistant" ne répond plus
*   **Que faire ?** Home Assistant est installé sur le PC durci en soute. Tu peux souvent le redémarrer électriquement, ou si tu as accès à la console, taper la commande de redémarrage (ex: `ha core restart`).
*   **Où regarder si c'est cassé ?** Les erreurs ne mordent pas. Cherche un fichier appelé `home-assistant.log`. Si tu vois des lignes rouges, lis simplement la dernière ligne. Très souvent, elle te dira : "Erreur de mot de passe", "Impossible de joindre le capteur X".

### D. La Règle d'or en cas de crash
**Ne supprime jamais tout pour recommencer à zéro.**
1. Respire.
2. Lis le message d'erreur de haut en bas (souvent la réponse est dans la dernière phrase).
3. Pose la question à ton IA préférée (ou tape l'erreur dans Google).
4. Rappelle-toi que le bateau utilise un système de "snapshots" (des sauvegardes figées dans le temps). On peut toujours revenir au système d'hier si on a vraiment fait une bêtise.

Bon vent et bonne navigation ! Tu vas assurer ! ⚓
