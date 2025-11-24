# Instructions d'Utilisation du Cours
## Git et GitHub pour Ingénieurs en Électronique

---

## 🎉 Félicitations !

Vous disposez maintenant d'un cours complet de 4 heures sur Git et GitHub, spécialement conçu pour les ingénieurs en électronique.

---

## 📂 Structure des Fichiers

Voici ce qui a été créé pour vous :

```
cours_git_github/
├── README.md                          # Vue d'ensemble du cours
├── SOMMAIRE.md                        # Navigation complète
├── INSTRUCTIONS.md                    # Ce fichier
│
├── Modules (Markdown source)
├── module1_introduction.md            # Module 1 (60 min)
├── module2_commandes_essentielles.md  # Module 2 (60 min)
├── module3_collaboration_github.md    # Module 3 (60 min)
├── module4_pratiques_avancees.md      # Module 4 (60 min)
│
├── Documents de support
├── aide-memoire-git.md                # Aide-mémoire des commandes
├── exercices-pratiques.md             # 8 exercices avec solutions
├── guide-formateur.md                 # Guide pour les formateurs
│
├── Présentations HTML (✨ NOUVEAU)
├── presentations_html/
│   ├── index.html                     # Page d'accueil
│   ├── module1_introduction.html
│   ├── module2_commandes_essentielles.html
│   ├── module3_collaboration_github.html
│   └── module4_pratiques_avancees.html
│
└── Scripts de conversion
    ├── generate_html_slides.py        # Générateur HTML
    ├── convert_to_presentations.sh    # Conversion PPTX (Bash)
    └── convert_to_presentations.py    # Conversion PPTX (Python)
```

---

## 🚀 Démarrage Rapide

### Pour les Étudiants

**1. Visualiser les présentations HTML**

```bash
# Ouvrir la page d'accueil dans votre navigateur
open cours_git_github/presentations_html/index.html

# Ou sur Linux
xdg-open cours_git_github/presentations_html/index.html

# Ou sur Windows
start cours_git_github/presentations_html/index.html
```

**2. Suivre le cours**

- Commencez par le Module 1
- Suivez les modules dans l'ordre (1 → 2 → 3 → 4)
- Faites les exercices pratiques après chaque module
- Consultez l'aide-mémoire quand nécessaire

**3. Navigation dans les slides**

- **Flèches ← →** : Naviguer entre les slides
- **Espace** : Slide suivante
- **ESC** : Vue d'ensemble de toutes les slides
- **F** : Mode plein écran
- **S** : Mode présentateur (avec notes)
- **?** : Afficher l'aide

### Pour les Formateurs

**1. Préparer la formation**

```bash
# Lire le guide formateur
cat cours_git_github/guide-formateur.md

# Tester les présentations
open cours_git_github/presentations_html/index.html
```

**2. Pendant la formation**

- Utiliser les présentations HTML en mode plein écran
- Suivre le planning suggéré dans le guide formateur
- Faire des démonstrations en direct
- Encourager la participation aux exercices

**3. Après la formation**

- Partager les ressources avec les étudiants
- Collecter les feedbacks
- Organiser un suivi

---

## 📊 Formats Disponibles

### 1. Présentations HTML (Recommandé) ✨

**Avantages :**
- ✅ Interactives et modernes
- ✅ Fonctionnent dans n'importe quel navigateur
- ✅ Pas d'installation nécessaire
- ✅ Navigation fluide
- ✅ Mode présentateur intégré
- ✅ Vue d'ensemble des slides

**Utilisation :**
```bash
# Ouvrir l'index
open presentations_html/index.html

# Ou ouvrir un module spécifique
open presentations_html/module1_introduction.html
```

### 2. Fichiers Markdown (Source)

**Avantages :**
- ✅ Faciles à éditer
- ✅ Versionnables avec Git
- ✅ Lisibles en texte brut
- ✅ Convertibles en d'autres formats

**Utilisation :**
```bash
# Lire avec un éditeur Markdown
code module1_introduction.md

# Ou dans VS Code avec prévisualisation
# Ctrl+Shift+V (Windows/Linux)
# Cmd+Shift+V (macOS)
```

### 3. PowerPoint (Optionnel)

Si vous avez besoin de fichiers PowerPoint :

```bash
# Installer Marp CLI
npm install -g @marp-team/marp-cli

# Convertir tous les modules
cd cours_git_github
./convert_to_presentations.sh

# Ou avec Python
python3 convert_to_presentations.py
```

Les fichiers PPTX seront créés dans `presentations/`

---

## 🎯 Parcours d'Apprentissage

### Niveau Débutant (0-2h)

**Objectif :** Comprendre les bases de Git

1. **Module 1** : Introduction et concepts (60 min)
   - Lire les slides
   - Faire l'exercice 1 : Installation
   - Faire l'exercice 2 : Premier dépôt

2. **Module 2** : Commandes essentielles (60 min)
   - Lire les slides
   - Faire l'exercice 3 : Branches
   - Faire l'exercice 4 : Résolution de conflits

**Résultat :** Vous savez créer un dépôt, faire des commits, et gérer des branches.

### Niveau Intermédiaire (2-3h)

**Objectif :** Collaborer avec GitHub

3. **Module 3** : Collaboration GitHub (60 min)
   - Lire les slides
   - Faire l'exercice 5 : Premier dépôt GitHub
   - Faire l'exercice 6 : Collaboration en équipe

**Résultat :** Vous savez utiliser GitHub pour collaborer.

### Niveau Avancé (3-4h)

**Objectif :** Appliquer les bonnes pratiques

4. **Module 4** : Pratiques avancées (60 min)
   - Lire les slides
   - Faire l'exercice 7 : Projet avec CI/CD
   - Faire l'exercice 8 : Projet final

**Résultat :** Vous maîtrisez les workflows professionnels.

---

## 📚 Ressources Complémentaires

### Documents Inclus

1. **[aide-memoire-git.md](aide-memoire-git.md)**
   - Toutes les commandes Git essentielles
   - Exemples pratiques
   - Résolution de problèmes
   - À garder sous la main !

2. **[exercices-pratiques.md](exercices-pratiques.md)**
   - 8 exercices progressifs
   - Instructions détaillées
   - Solutions et corrections
   - Projet final complet

3. **[guide-formateur.md](guide-formateur.md)**
   - Planning détaillé
   - Conseils pédagogiques
   - Gestion des problèmes
   - Évaluation des acquis

### Ressources Externes

**Documentation officielle :**
- Git : https://git-scm.com/doc
- GitHub : https://docs.github.com/
- Pro Git Book (gratuit) : https://git-scm.com/book/fr/v2

**Tutoriels interactifs :**
- Learn Git Branching : https://learngitbranching.js.org/
- GitHub Learning Lab : https://lab.github.com/
- Katacoda Git : https://www.katacoda.com/courses/git

**Communautés :**
- Stack Overflow : Tag [git]
- Reddit : r/git
- GitHub Community : https://github.community/

---

## 🛠️ Personnalisation

### Modifier les Slides

1. **Éditer les fichiers Markdown**
   ```bash
   code module1_introduction.md
   ```

2. **Régénérer les présentations HTML**
   ```bash
   python3 generate_html_slides.py
   ```

3. **Vérifier le résultat**
   ```bash
   open presentations_html/index.html
   ```

### Ajouter du Contenu

**Ajouter une slide :**
```markdown
---

## Nouveau Titre

Votre contenu ici

- Point 1
- Point 2

```bash
# Exemple de code
git status
```
```

**Ajouter un exercice :**
Éditer `exercices-pratiques.md` et ajouter votre exercice.

---

## 💡 Conseils d'Utilisation

### Pour une Formation en Présentiel

1. **Avant le cours :**
   - Tester les présentations HTML
   - Vérifier la connexion Internet
   - Préparer les exemples de code
   - Imprimer l'aide-mémoire (optionnel)

2. **Pendant le cours :**
   - Utiliser le mode plein écran (touche F)
   - Faire des démonstrations en direct
   - Encourager les questions
   - Respecter les pauses

3. **Après le cours :**
   - Partager le lien vers les présentations
   - Envoyer l'aide-mémoire
   - Organiser un suivi

### Pour une Formation en Ligne

1. **Préparation :**
   - Partager le lien des présentations HTML
   - Tester le partage d'écran
   - Préparer les breakout rooms

2. **Pendant la session :**
   - Partager l'écran avec les slides
   - Utiliser le chat pour les questions
   - Faire des pauses plus fréquentes (toutes les 45 min)

3. **Suivi :**
   - Enregistrer la session
   - Partager les ressources
   - Créer un groupe de discussion

### Pour l'Auto-Formation

1. **Planification :**
   - Bloquer 4 heures dans votre agenda
   - Préparer votre environnement de travail
   - Installer Git avant de commencer

2. **Apprentissage :**
   - Suivre les modules dans l'ordre
   - Faire TOUS les exercices
   - Prendre des notes
   - Ne pas hésiter à revenir en arrière

3. **Pratique :**
   - Créer vos propres projets
   - Contribuer à l'open source
   - Utiliser Git quotidiennement

---

## 🔧 Dépannage

### Les présentations HTML ne s'affichent pas correctement

**Solution :**
- Utiliser un navigateur moderne (Chrome, Firefox, Safari, Edge)
- Vérifier que JavaScript est activé
- Essayer un autre navigateur

### Les blocs de code ne sont pas colorés

**Solution :**
- Vérifier la connexion Internet (les bibliothèques sont chargées depuis un CDN)
- Rafraîchir la page (Ctrl+F5 ou Cmd+Shift+R)

### Je veux modifier le style des présentations

**Solution :**
Éditer le fichier `generate_html_slides.py` et modifier la section `<style>` dans `HTML_TEMPLATE`.

### Je veux générer des PDF

**Solution :**
```bash
# Avec Marp
marp module1_introduction.md -o module1.pdf

# Ou imprimer depuis le navigateur
# Ouvrir la présentation HTML → Ctrl+P → Enregistrer en PDF
```

---

## 📊 Statistiques du Cours

**Contenu créé :**
- ✅ 4 modules complets (125 slides)
- ✅ 8 exercices pratiques avec solutions
- ✅ 1 aide-mémoire complet (50+ commandes)
- ✅ 1 guide formateur détaillé
- ✅ 4 présentations HTML interactives
- ✅ 1 page d'index élégante

**Formats disponibles :**
- ✅ Markdown (source éditable)
- ✅ HTML (présentations interactives)
- ✅ PowerPoint (via conversion)
- ✅ PDF (via conversion)

**Durée totale :** 4 heures
**Niveau :** Débutant à Intermédiaire
**Public :** Étudiants ingénieurs en électronique

---

## ✅ Checklist de Démarrage

### Avant de Commencer

- [ ] Git est installé sur votre ordinateur
- [ ] Vous avez un compte GitHub
- [ ] Vous avez un éditeur de texte (VS Code recommandé)
- [ ] Vous avez ouvert les présentations HTML
- [ ] Vous avez lu le README.md

### Pendant le Cours

- [ ] Module 1 complété
- [ ] Exercices 1-2 réalisés
- [ ] Module 2 complété
- [ ] Exercices 3-4 réalisés
- [ ] Module 3 complété
- [ ] Exercices 5-6 réalisés
- [ ] Module 4 complété
- [ ] Exercices 7-8 réalisés

### Après le Cours

- [ ] Aide-mémoire consulté
- [ ] Projet personnel créé sur GitHub
- [ ] Contribution à un projet open source
- [ ] Git utilisé quotidiennement

---

## 🎓 Certification

### Critères de Validation

Pour valider le cours :
- ✅ Présence aux 4 modules (ou auto-formation complète)
- ✅ Participation aux exercices
- ✅ Projet final réalisé (exercice 8)
- ✅ Quiz final > 70% (optionnel)

### Compétences Acquises

Après ce cours, vous serez capable de :
- ✅ Utiliser Git pour versionner vos projets
- ✅ Collaborer efficacement avec GitHub
- ✅ Gérer des branches et résoudre des conflits
- ✅ Appliquer les bonnes pratiques professionnelles
- ✅ Mettre en place CI/CD pour vos projets

---

## 📞 Support

### Questions sur le Contenu

- Consulter l'aide-mémoire
- Relire les slides
- Chercher sur Stack Overflow
- Demander au formateur

### Problèmes Techniques

- Vérifier la documentation Git
- Consulter GitHub Docs
- Poser une question sur Stack Overflow

### Suggestions d'Amélioration

Ce cours est un document vivant. Vos suggestions sont les bienvenues :
- Corrections de typos
- Améliorations pédagogiques
- Nouveaux exercices
- Exemples supplémentaires

---

## 🚀 Prochaines Étapes

### Immédiatement

1. Ouvrir `presentations_html/index.html`
2. Commencer par le Module 1
3. Faire l'exercice 1 (Installation)

### Cette Semaine

1. Compléter les 4 modules
2. Faire tous les exercices
3. Créer un projet sur GitHub

### Ce Mois

1. Utiliser Git quotidiennement
2. Contribuer à un projet open source
3. Partager vos connaissances

### Long Terme

1. Maîtriser les workflows avancés
2. Devenir référent Git dans votre équipe
3. Former d'autres personnes

---

## 🎉 Bon Apprentissage !

Vous avez maintenant tout ce qu'il faut pour maîtriser Git et GitHub. N'oubliez pas :

- 💪 La pratique est essentielle
- 🤝 N'hésitez pas à demander de l'aide
- 🌟 Contribuez à l'open source
- 📚 Continuez à apprendre

**Bonne chance avec Git et GitHub ! 🚀**

---

**Version :** 1.0  
**Dernière mise à jour :** Janvier 2025  
**Licence :** CC BY-SA 4.0  
**Créé avec ❤️ pour les ingénieurs en électronique**