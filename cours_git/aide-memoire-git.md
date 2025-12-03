# Aide-Mémoire Git et GitHub
## Commandes Essentielles pour Ingénieurs en Électronique

---

## 📦 Configuration Initiale

```bash
# Configurer votre identité
git config --global user.name "Votre Nom"
git config --global user.email "votre.email@example.com"

# Configurer l'éditeur
git config --global core.editor "code --wait"

# Vérifier la configuration
git config --list
```

---

## 🚀 Démarrer un Projet

```bash
# Créer un nouveau dépôt
git init

# Cloner un dépôt existant
git clone git@github.com:username/projet.git
git clone https://github.com/username/projet.git
```

---

## 📝 Commandes de Base

```bash
# Voir l'état du dépôt
git status

# Ajouter des fichiers
git add fichier.cpp
git add .                    # Tous les fichiers
git add *.cpp                # Par extension

# Valider les modifications
git commit -m "Message descriptif"
git commit -am "Message"     # add + commit (fichiers suivis)

# Voir l'historique
git log
git log --oneline
git log --oneline --graph --all
```

---

## 🌳 Gestion des Branches

```bash
# Lister les branches
git branch
git branch -a                # Toutes les branches

# Créer une branche
git branch nom-branche

# Changer de branche
git checkout nom-branche
git switch nom-branche       # Git 2.23+

# Créer et changer de branche
git checkout -b nom-branche
git switch -c nom-branche    # Git 2.23+

# Fusionner une branche
git checkout main
git merge nom-branche

# Supprimer une branche
git branch -d nom-branche    # Si fusionnée
git branch -D nom-branche    # Forcer
```

---

## 🔄 Synchronisation avec GitHub

```bash
# Voir les remotes
git remote -v

# Ajouter un remote
git remote add origin git@github.com:user/projet.git

# Pousser vers GitHub
git push origin main
git push -u origin main      # Définir upstream
git push                     # Après avoir défini upstream

# Récupérer depuis GitHub
git pull origin main
git fetch origin             # Sans merge
```

---

## 🔍 Inspection et Comparaison

```bash
# Voir les différences
git diff                     # Non stagées
git diff --staged            # Stagées
git diff main feature        # Entre branches

# Voir un commit
git show abc123
git show HEAD

# Voir qui a modifié quoi
git blame fichier.cpp

# Rechercher dans l'historique
git log --grep="mot-clé"
git log -S "fonction"
```

---

## ↩️ Annuler des Modifications

```bash
# Annuler modifications non stagées
git restore fichier.cpp
git checkout -- fichier.cpp  # Ancienne syntaxe

# Retirer du staging
git restore --staged fichier.cpp
git reset HEAD fichier.cpp   # Ancienne syntaxe

# Annuler le dernier commit (garder modifs)
git reset --soft HEAD~1

# Annuler le dernier commit (supprimer modifs)
git reset --hard HEAD~1

# Créer un commit qui annule
git revert abc123
```

---

## 📦 Git Stash

```bash
# Mettre de côté
git stash
git stash save "Message"

# Lister les stash
git stash list

# Appliquer un stash
git stash apply
git stash pop                # Appliquer et supprimer

# Supprimer un stash
git stash drop stash@{0}
```

---

## 🏷️ Tags

```bash
# Créer un tag
git tag v1.0.0
git tag -a v1.0.0 -m "Version 1.0.0"

# Lister les tags
git tag

# Pousser les tags
git push origin v1.0.0
git push --tags

# Supprimer un tag
git tag -d v1.0.0
git push origin --delete v1.0.0
```

---

## 🔧 Commandes Utiles

```bash
# Renommer un fichier
git mv ancien.cpp nouveau.cpp

# Supprimer un fichier
git rm fichier.cpp

# Nettoyer les fichiers non suivis
git clean -n                 # Voir ce qui serait supprimé
git clean -f                 # Supprimer

# Modifier le dernier commit
git commit --amend

# Voir la configuration
git config --list
git config user.name
```

---

## 🐙 GitHub - Pull Requests

```bash
# Workflow typique
git checkout -b feature-nouvelle
# ... modifications ...
git commit -am "feat: Nouvelle fonctionnalité"
git push -u origin feature-nouvelle
# Créer la PR sur GitHub

# Mettre à jour une PR
git commit -am "fix: Correction suite review"
git push
```

---

## 🔀 Fork et Contribution

```bash
# 1. Fork sur GitHub
# 2. Cloner votre fork
git clone git@github.com:vous/projet.git

# 3. Ajouter l'upstream
git remote add upstream git@github.com:original/projet.git

# 4. Créer une branche
git checkout -b fix-bug

# 5. Faire les modifications et commit
git commit -am "fix: Correction du bug"

# 6. Pousser vers votre fork
git push origin fix-bug

# 7. Créer une PR sur GitHub

# Mettre à jour depuis l'upstream
git fetch upstream
git merge upstream/main
```

---

## 🚫 .gitignore pour Arduino/PlatformIO

```gitignore
# PlatformIO
.pio/
.pioenvs/
.piolibdeps/

# Arduino
*.hex
*.eep
*.elf
*.map
*.o
*.a

# Build
build/
.build/

# IDE
.vscode/
.idea/

# OS
.DS_Store
Thumbs.db

# Secrets
secrets.h
.env
```

---

## 🚫 .gitignore pour KiCad

```gitignore
# KiCad
*.bak
*.kicad_pcb-bak
*-save.kicad_pcb
*.kicad_prl
fp-info-cache

# Gerber
gerber/
*.zip
```

---

## 🔐 Configuration SSH

```bash
# Générer une clé SSH
ssh-keygen -t ed25519 -C "email@example.com"

# Afficher la clé publique
cat ~/.ssh/id_ed25519.pub

# Tester la connexion
ssh -T git@github.com
```

---

## 📋 Messages de Commit

**Format recommandé :**
```
type: Résumé court (50 caractères max)

Description détaillée si nécessaire
- Point 1
- Point 2
```

**Types courants :**
- `feat:` Nouvelle fonctionnalité
- `fix:` Correction de bug
- `docs:` Documentation
- `style:` Formatage
- `refactor:` Refactorisation
- `test:` Tests
- `chore:` Maintenance

**Exemples :**
```bash
git commit -m "feat: Ajout support WiFi ESP32"
git commit -m "fix: Correction lecture capteur DHT22"
git commit -m "docs: Mise à jour du README"
```

---

## 🆘 Résolution de Problèmes

**Conflit de merge :**
```bash
# 1. Voir les fichiers en conflit
git status

# 2. Éditer les fichiers et résoudre
# Supprimer les marqueurs <<<<<<< ======= >>>>>>>

# 3. Marquer comme résolu
git add fichier-resolu.cpp

# 4. Finaliser
git commit
```

**Annuler un merge :**
```bash
git merge --abort
```

**Récupérer un fichier supprimé :**
```bash
git checkout HEAD -- fichier.cpp
```

---

## ⚡ Alias Utiles

```bash
# Configurer des alias
git config --global alias.st status
git config --global alias.co checkout
git config --global alias.br branch
git config --global alias.ci commit
git config --global alias.lg "log --oneline --graph --all"
git config --global alias.last "log -1 HEAD"

# Utilisation
git st
git co main
git lg
```

---

## 🔄 Workflows Recommandés

**Feature Branch Workflow :**
```bash
# 1. Créer une branche
git checkout -b feature-capteur

# 2. Développer
git commit -am "feat: Ajout capteur"

# 3. Pousser
git push -u origin feature-capteur

# 4. Créer une PR sur GitHub

# 5. Après merge, nettoyer
git checkout main
git pull
git branch -d feature-capteur
```

---

## 📚 Ressources

- **Documentation officielle :** https://git-scm.com/doc
- **Pro Git Book (gratuit) :** https://git-scm.com/book/fr/v2
- **GitHub Docs :** https://docs.github.com/
- **Learn Git Branching :** https://learngitbranching.js.org/
- **GitHub Learning Lab :** https://lab.github.com/

---

## 💡 Conseils

✅ **À FAIRE :**
- Commits fréquents et atomiques
- Messages descriptifs
- Branches pour fonctionnalités
- Pull réguliers
- Tests avant merge

❌ **À ÉVITER :**
- Commits de code non fonctionnel sur main
- Messages vagues ("fix", "update")
- Commits de secrets (mots de passe, clés)
- Fichiers compilés dans Git
- Branches trop longues

---

## 🎯 Commandes par Cas d'Usage

**Démarrer un nouveau projet :**
```bash
mkdir mon-projet && cd mon-projet
git init
echo "# Mon Projet" > README.md
git add README.md
git commit -m "Initial commit"
git remote add origin git@github.com:user/projet.git
git push -u origin main
```

**Contribuer à un projet existant :**
```bash
git clone git@github.com:user/projet.git
cd projet
git checkout -b ma-contribution
# ... modifications ...
git commit -am "feat: Ma contribution"
git push -u origin ma-contribution
# Créer une PR sur GitHub
```

**Mettre à jour son fork :**
```bash
git remote add upstream git@github.com:original/projet.git
git fetch upstream
git checkout main
git merge upstream/main
git push origin main
```

---

**Version :** 1.0  
**Dernière mise à jour :** Janvier 2025  
**Licence :** CC BY-SA 4.0