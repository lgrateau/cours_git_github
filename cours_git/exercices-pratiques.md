# Exercices Pratiques - Git et GitHub
## Pour Ingénieurs en Électronique

---

## 📋 Vue d'ensemble

Ce document contient tous les exercices pratiques du cours, avec des instructions détaillées et des solutions.

---

## Exercice 1 : Installation et Configuration (10 min)

### Objectif
Installer Git et configurer votre environnement de travail.

### Instructions

1. **Installer Git**
   - Windows : Télécharger depuis https://git-scm.com/download/win
   - macOS : `brew install git`
   - Linux : `sudo apt-get install git`

2. **Vérifier l'installation**
   ```bash
   git --version
   ```

3. **Configurer votre identité**
   ```bash
   git config --global user.name "Votre Nom"
   git config --global user.email "votre.email@example.com"
   ```

4. **Configurer l'éditeur (VS Code)**
   ```bash
   git config --global core.editor "code --wait"
   ```

5. **Vérifier la configuration**
   ```bash
   git config --list
   ```

### Validation
- [ ] Git est installé et la version s'affiche
- [ ] Votre nom et email sont configurés
- [ ] L'éditeur est configuré

---

## Exercice 2 : Premier Dépôt Local (10 min)

### Objectif
Créer votre premier dépôt Git et faire des commits.

### Instructions

1. **Créer un dossier de projet**
   ```bash
   mkdir projet-led-blink
   cd projet-led-blink
   ```

2. **Initialiser Git**
   ```bash
   git init
   ```

3. **Créer un fichier README**
   ```bash
   echo "# Projet LED Blink" > README.md
   echo "Un simple projet Arduino pour faire clignoter une LED" >> README.md
   ```

4. **Vérifier le statut**
   ```bash
   git status
   ```

5. **Ajouter le fichier**
   ```bash
   git add README.md
   ```

6. **Faire le premier commit**
   ```bash
   git commit -m "Initial commit: Ajout du README"
   ```

7. **Voir l'historique**
   ```bash
   git log
   ```

### Validation
- [ ] Le dépôt est initialisé (dossier .git existe)
- [ ] Le README est commité
- [ ] L'historique montre votre commit

---

## Exercice 3 : Travailler avec les Branches (15 min)

### Objectif
Créer des branches, faire des modifications et les fusionner.

### Instructions

1. **Créer le fichier principal**
   ```bash
   cat > main.ino << 'EOF'
   void setup() {
     pinMode(LED_BUILTIN, OUTPUT);
   }

   void loop() {
     digitalWrite(LED_BUILTIN, HIGH);
     delay(1000);
     digitalWrite(LED_BUILTIN, LOW);
     delay(1000);
   }
   EOF
   ```

2. **Commiter le fichier**
   ```bash
   git add main.ino
   git commit -m "feat: Ajout du code LED blink de base"
   ```

3. **Créer une branche pour une nouvelle fonctionnalité**
   ```bash
   git checkout -b feature-led-rgb
   ```

4. **Créer un nouveau fichier**
   ```bash
   cat > led_rgb.cpp << 'EOF'
   #include "led_rgb.h"

   void setupRGB() {
     pinMode(RED_PIN, OUTPUT);
     pinMode(GREEN_PIN, OUTPUT);
     pinMode(BLUE_PIN, OUTPUT);
   }

   void setColor(int r, int g, int b) {
     analogWrite(RED_PIN, r);
     analogWrite(GREEN_PIN, g);
     analogWrite(BLUE_PIN, b);
   }
   EOF
   ```

5. **Commiter sur la branche**
   ```bash
   git add led_rgb.cpp
   git commit -m "feat: Ajout support LED RGB"
   ```

6. **Retourner sur main**
   ```bash
   git checkout main
   ```

7. **Créer une autre branche**
   ```bash
   git checkout -b feature-buzzer
   cat > buzzer.cpp << 'EOF'
   #include "buzzer.h"

   void playTone(int frequency, int duration) {
     tone(BUZZER_PIN, frequency, duration);
   }
   EOF
   git add buzzer.cpp
   git commit -m "feat: Ajout support buzzer"
   ```

8. **Fusionner les branches**
   ```bash
   git checkout main
   git merge feature-led-rgb
   git merge feature-buzzer
   ```

9. **Voir l'historique graphique**
   ```bash
   git log --oneline --graph --all
   ```

10. **Supprimer les branches**
    ```bash
    git branch -d feature-led-rgb
    git branch -d feature-buzzer
    ```

### Validation
- [ ] Deux branches ont été créées
- [ ] Les modifications ont été commitées sur chaque branche
- [ ] Les branches ont été fusionnées dans main
- [ ] Les branches ont été supprimées

---

## Exercice 4 : Résoudre un Conflit (15 min)

### Objectif
Créer et résoudre un conflit de fusion.

### Instructions

1. **Créer deux branches qui modifient le même fichier**
   ```bash
   # Branche 1
   git checkout -b version-rapide
   cat > main.ino << 'EOF'
   void setup() {
     pinMode(LED_BUILTIN, OUTPUT);
   }

   void loop() {
     digitalWrite(LED_BUILTIN, HIGH);
     delay(100);  // Clignotement rapide
     digitalWrite(LED_BUILTIN, LOW);
     delay(100);
   }
   EOF
   git commit -am "feat: Clignotement rapide"

   # Retour sur main
   git checkout main

   # Branche 2
   git checkout -b version-lente
   cat > main.ino << 'EOF'
   void setup() {
     pinMode(LED_BUILTIN, OUTPUT);
   }

   void loop() {
     digitalWrite(LED_BUILTIN, HIGH);
     delay(2000);  // Clignotement lent
     digitalWrite(LED_BUILTIN, LOW);
     delay(2000);
   }
   EOF
   git commit -am "feat: Clignotement lent"
   ```

2. **Fusionner la première branche**
   ```bash
   git checkout main
   git merge version-rapide
   ```

3. **Tenter de fusionner la deuxième (conflit !)**
   ```bash
   git merge version-lente
   # CONFLICT!
   ```

4. **Voir les fichiers en conflit**
   ```bash
   git status
   ```

5. **Résoudre le conflit**
   - Ouvrir main.ino dans un éditeur
   - Choisir la version souhaitée ou créer une version hybride
   - Supprimer les marqueurs `<<<<<<<`, `=======`, `>>>>>>>`

6. **Marquer comme résolu**
   ```bash
   git add main.ino
   ```

7. **Finaliser la fusion**
   ```bash
   git commit -m "Merge version-lente: Résolution du conflit"
   ```

8. **Nettoyer**
   ```bash
   git branch -d version-rapide
   git branch -d version-lente
   ```

### Validation
- [ ] Un conflit a été créé
- [ ] Le conflit a été résolu manuellement
- [ ] La fusion a été finalisée

---

## Exercice 5 : Premier Dépôt GitHub (15 min)

### Objectif
Créer un dépôt sur GitHub et pousser votre code.

### Prérequis
- Compte GitHub créé
- Clé SSH configurée (optionnel mais recommandé)

### Instructions

1. **Créer un dépôt sur GitHub**
   - Aller sur https://github.com
   - Cliquer sur "+" → "New repository"
   - Nom : `mon-premier-projet-github`
   - Description : "Mon premier projet avec Git et GitHub"
   - Public
   - Ne pas initialiser avec README (on a déjà un projet local)
   - Créer

2. **Lier le dépôt local au dépôt distant**
   ```bash
   cd projet-led-blink
   git remote add origin git@github.com:votre-username/mon-premier-projet-github.git
   # ou avec HTTPS :
   # git remote add origin https://github.com/votre-username/mon-premier-projet-github.git
   ```

3. **Vérifier le remote**
   ```bash
   git remote -v
   ```

4. **Pousser le code**
   ```bash
   git push -u origin main
   ```

5. **Vérifier sur GitHub**
   - Rafraîchir la page du dépôt
   - Vérifier que tous les fichiers sont présents

6. **Faire une modification locale**
   ```bash
   echo "## Installation" >> README.md
   echo "Télécharger le code et uploader sur Arduino" >> README.md
   git commit -am "docs: Ajout instructions d'installation"
   ```

7. **Pousser la modification**
   ```bash
   git push
   ```

### Validation
- [ ] Le dépôt est créé sur GitHub
- [ ] Le code local est poussé
- [ ] Les modifications sont visibles sur GitHub

---

## Exercice 6 : Collaboration en Équipe (20 min)

### Objectif
Travailler à deux sur un projet avec branches et Pull Requests.

### Instructions (Équipe de 2)

**Personne A (Créateur du projet) :**

1. **Créer un nouveau dépôt sur GitHub**
   - Nom : `projet-collaboratif`
   - Public
   - Initialiser avec README

2. **Ajouter Personne B comme collaborateur**
   - Settings → Collaborators → Add people
   - Entrer le nom d'utilisateur de B

3. **Cloner et créer du contenu**
   ```bash
   git clone git@github.com:personneA/projet-collaboratif.git
   cd projet-collaboratif
   
   cat > sensor.h << 'EOF'
   #ifndef SENSOR_H
   #define SENSOR_H

   float readTemperature();

   #endif
   EOF
   
   git add sensor.h
   git commit -m "feat: Ajout header capteur"
   git push origin main
   ```

**Personne B (Collaborateur) :**

1. **Accepter l'invitation** (email ou notifications GitHub)

2. **Cloner le dépôt**
   ```bash
   git clone git@github.com:personneA/projet-collaboratif.git
   cd projet-collaboratif
   ```

3. **Créer une branche**
   ```bash
   git checkout -b feature-implementation
   ```

4. **Implémenter la fonction**
   ```bash
   cat > sensor.cpp << 'EOF'
   #include "sensor.h"
   #include <DHT.h>

   DHT dht(2, DHT22);

   float readTemperature() {
     return dht.readTemperature();
   }
   EOF
   
   git add sensor.cpp
   git commit -m "feat: Implémentation lecture température"
   ```

5. **Pousser la branche**
   ```bash
   git push -u origin feature-implementation
   ```

6. **Créer une Pull Request sur GitHub**
   - Aller sur le dépôt
   - Cliquer sur "Compare & pull request"
   - Remplir le titre et la description
   - Créer la PR

**Personne A (Review) :**

1. **Examiner la Pull Request**
   - Aller dans l'onglet "Pull requests"
   - Ouvrir la PR de B
   - Examiner les modifications
   - Laisser un commentaire (optionnel)

2. **Merger la Pull Request**
   - Cliquer sur "Merge pull request"
   - Confirmer

3. **Mettre à jour localement**
   ```bash
   git checkout main
   git pull origin main
   ```

**Personne B :**

1. **Mettre à jour et nettoyer**
   ```bash
   git checkout main
   git pull origin main
   git branch -d feature-implementation
   ```

### Validation
- [ ] Les deux personnes ont accès au dépôt
- [ ] Une branche a été créée et poussée
- [ ] Une Pull Request a été créée
- [ ] La PR a été reviewée et mergée
- [ ] Les deux personnes ont le code à jour

---

## Exercice 7 : Projet Complet avec CI/CD (20 min)

### Objectif
Créer un projet Arduino complet avec tests et intégration continue.

### Instructions

1. **Créer la structure du projet**
   ```bash
   mkdir station-meteo-complete
   cd station-meteo-complete
   git init
   ```

2. **Créer platformio.ini**
   ```bash
   cat > platformio.ini << 'EOF'
   [env:uno]
   platform = atmelavr
   board = uno
   framework = arduino
   lib_deps = 
       adafruit/DHT sensor library@^1.4.4
   test_framework = unity
   EOF
   ```

3. **Créer la structure des dossiers**
   ```bash
   mkdir -p src test/test_sensors docs
   ```

4. **Créer le code principal**
   ```bash
   cat > src/main.cpp << 'EOF'
   #include <Arduino.h>
   #include <DHT.h>

   #define DHTPIN 2
   #define DHTTYPE DHT22

   DHT dht(DHTPIN, DHTTYPE);

   void setup() {
     Serial.begin(9600);
     dht.begin();
   }

   void loop() {
     float temp = dht.readTemperature();
     float humidity = dht.readHumidity();
     
     if (!isnan(temp) && !isnan(humidity)) {
       Serial.print("Température: ");
       Serial.print(temp);
       Serial.print("°C, Humidité: ");
       Serial.print(humidity);
       Serial.println("%");
     }
     
     delay(2000);
   }
   EOF
   ```

5. **Créer un test**
   ```bash
   cat > test/test_sensors/test_main.cpp << 'EOF'
   #include <unity.h>

   void test_temperature_range(void) {
       // Test que la température est dans une plage raisonnable
       float temp = 25.0; // Simulé
       TEST_ASSERT_TRUE(temp >= -40.0 && temp <= 80.0);
   }

   void test_humidity_range(void) {
       float humidity = 50.0; // Simulé
       TEST_ASSERT_TRUE(humidity >= 0.0 && humidity <= 100.0);
   }

   void setUp(void) {
       // Initialisation avant chaque test
   }

   void tearDown(void) {
       // Nettoyage après chaque test
   }

   int main(int argc, char **argv) {
       UNITY_BEGIN();
       RUN_TEST(test_temperature_range);
       RUN_TEST(test_humidity_range);
       return UNITY_END();
   }
   EOF
   ```

6. **Créer .gitignore**
   ```bash
   cat > .gitignore << 'EOF'
   .pio/
   .vscode/
   *.pyc
   EOF
   ```

7. **Créer README.md**
   ```bash
   cat > README.md << 'EOF'
   # Station Météo Arduino

   ## Description
   Station météo basée sur Arduino Uno avec capteur DHT22.

   ## Matériel
   - Arduino Uno
   - Capteur DHT22
   - Résistance 10kΩ

   ## Installation
   \`\`\`bash
   pio run
   pio run --target upload
   \`\`\`

   ## Tests
   \`\`\`bash
   pio test
   \`\`\`
   EOF
   ```

8. **Créer GitHub Actions**
   ```bash
   mkdir -p .github/workflows
   cat > .github/workflows/build.yml << 'EOF'
   name: Build and Test

   on:
     push:
       branches: [ main ]
     pull_request:
       branches: [ main ]

   jobs:
     build:
       runs-on: ubuntu-latest
       
       steps:
       - uses: actions/checkout@v3
       
       - name: Cache PlatformIO
         uses: actions/cache@v3
         with:
           path: ~/.platformio
           key: ${{ runner.os }}-pio
       
       - name: Set up Python
         uses: actions/setup-python@v4
         with:
           python-version: '3.x'
       
       - name: Install PlatformIO
         run: |
           python -m pip install --upgrade pip
           pip install platformio
       
       - name: Build firmware
         run: pio run
       
       - name: Run tests
         run: pio test
   EOF
   ```

9. **Commiter tout**
   ```bash
   git add .
   git commit -m "Initial commit: Structure complète du projet"
   ```

10. **Créer le dépôt sur GitHub et pousser**
    ```bash
    # Créer le dépôt sur GitHub d'abord
    git remote add origin git@github.com:votre-username/station-meteo-complete.git
    git push -u origin main
    ```

11. **Vérifier que les Actions s'exécutent**
    - Aller dans l'onglet "Actions" sur GitHub
    - Vérifier que le workflow s'exécute

### Validation
- [ ] Le projet a une structure complète
- [ ] Les tests sont présents
- [ ] Le .gitignore est configuré
- [ ] GitHub Actions est configuré
- [ ] Le workflow s'exécute avec succès

---

## Exercice 8 : Projet Final (25 min)

### Objectif
Créer un projet complet de A à Z avec toutes les bonnes pratiques.

### Cahier des charges

Créer une **station météo complète** avec :
- Lecture de température et humidité (DHT22)
- Affichage sur LCD 16x2
- Logging sur carte SD (optionnel)
- Communication série

### Exigences techniques

- ✅ Dépôt Git avec historique propre
- ✅ README.md complet
- ✅ .gitignore approprié
- ✅ Branches pour fonctionnalités
- ✅ Tests unitaires
- ✅ CI/CD avec GitHub Actions
- ✅ Documentation technique
- ✅ Schéma de câblage (dessin ou description)
- ✅ Release avec tag v1.0.0

### Structure recommandée

```
station-meteo/
├── .github/
│   └── workflows/
│       └── build.yml
├── src/
│   ├── main.cpp
│   ├── sensor.cpp
│   ├── sensor.h
│   ├── display.cpp
│   └── display.h
├── test/
│   └── test_sensors/
│       └── test_main.cpp
├── docs/
│   ├── wiring.md
│   └── api.md
├── .gitignore
├── platformio.ini
├── README.md
├── CHANGELOG.md
└── LICENSE
```

### Étapes suggérées

1. **Initialisation** (5 min)
   - Créer le dépôt local et GitHub
   - Structure de base
   - Premier commit

2. **Développement par fonctionnalités** (15 min)
   - Branche `feature-sensor` : Lecture capteur
   - Branche `feature-display` : Affichage LCD
   - Branche `feature-serial` : Communication série
   - Merger chaque branche après tests

3. **Documentation et tests** (3 min)
   - README complet
   - Tests unitaires
   - Documentation technique

4. **Release** (2 min)
   - Tag v1.0.0
   - Release sur GitHub
   - CHANGELOG

### Validation finale

- [ ] Le projet compile sans erreur
- [ ] Les tests passent
- [ ] La documentation est complète
- [ ] Le dépôt GitHub est propre
- [ ] Une release v1.0.0 existe
- [ ] Le workflow CI/CD fonctionne

---

## Solutions et Corrections

### Exercice 2 - Solution complète

```bash
mkdir projet-led-blink
cd projet-led-blink
git init
echo "# Projet LED Blink" > README.md
echo "Un simple projet Arduino pour faire clignoter une LED" >> README.md
git status
git add README.md
git commit -m "Initial commit: Ajout du README"
git log
```

### Exercice 4 - Résolution de conflit

Fichier résolu (exemple) :
```cpp
void setup() {
  pinMode(LED_BUILTIN, OUTPUT);
}

void loop() {
  digitalWrite(LED_BUILTIN, HIGH);
  delay(500);  // Compromis entre rapide et lent
  digitalWrite(LED_BUILTIN, LOW);
  delay(500);
}
```

---

## Ressources Complémentaires

- **Aide-mémoire Git :** Voir `aide-memoire-git.md`
- **Documentation PlatformIO :** https://docs.platformio.org/
- **Arduino Reference :** https://www.arduino.cc/reference/
- **GitHub Actions :** https://docs.github.com/en/actions

---

**Bon courage avec les exercices ! 🚀**