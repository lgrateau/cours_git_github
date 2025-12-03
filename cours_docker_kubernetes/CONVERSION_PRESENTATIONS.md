# Guide de Conversion en Présentations
## PowerPoint et PDF

---

## 🎯 Options de Conversion

Vous avez plusieurs options pour convertir les slides Markdown en présentations PowerPoint ou PDF.

---

## Option 1 : Marp (Recommandé) ⭐

### Installation

```bash
# Via npm
npm install -g @marp-team/marp-cli

# Via Homebrew (macOS)
brew install marp-cli
```

### Conversion en PowerPoint

```bash
# Convertir un module en PPTX
marp module1_introduction_conteneurisation.md -o module1.pptx

# Convertir tous les modules
marp module1_introduction_conteneurisation.md -o module1.pptx
marp module2_docker_commandes_essentielles.md -o module2.pptx
marp module3_docker_avance.md -o module3.pptx
marp module4_kubernetes.md -o module4.pptx
```

### Conversion en PDF

```bash
marp module1_introduction_conteneurisation.md -o module1.pdf --pdf
```

### Avec VS Code

1. Installer l'extension "Marp for VS Code"
2. Ouvrir un fichier .md
3. Cliquer sur l'icône Marp dans la barre d'outils
4. Exporter en PPTX ou PDF

---

## Option 2 : Scripts Automatiques (Le Plus Simple) 🚀

### Script Bash (Linux/macOS)

```bash
# Rendre le script exécutable
chmod +x convert_to_presentations.sh

# Exécuter
./convert_to_presentations.sh
```

### Script Python (Multiplateforme)

```bash
# Exécuter
python3 convert_to_presentations.py

# Ou sur Windows
python convert_to_presentations.py
```

Les scripts vont :
- ✅ Vérifier que Marp est installé
- ✅ Créer le dossier `presentations/`
- ✅ Convertir tous les modules en PPTX
- ✅ Convertir tous les modules en PDF
- ✅ Afficher un résumé des fichiers créés

---

## Option 3 : Pandoc

### Installation

```bash
# macOS
brew install pandoc

# Windows
choco install pandoc

# Linux
sudo apt-get install pandoc
```

### Conversion

```bash
# En PowerPoint
pandoc module1_introduction_conteneurisation.md -o module1.pptx

# En PDF via LaTeX
pandoc module1_introduction_conteneurisation.md -o module1.pdf

# Avec un thème personnalisé
pandoc module1_introduction_conteneurisation.md -o module1.pptx --reference-doc=template.pptx
```

---

## 🎨 Personnalisation des Slides

### Thème Marp Personnalisé

Le fichier `marp-theme.css` contient le thème personnalisé pour Docker & Kubernetes avec :
- Couleurs Docker (bleu #0db7ed) et Kubernetes (bleu #326ce5)
- Emojis Docker 🐳 pour les listes
- Style moderne et professionnel
- Bon contraste pour la lisibilité

### Utiliser le thème

```bash
marp --theme marp-theme.css module1_introduction_conteneurisation.md -o module1.pptx
```

### Ajouter des Directives Marp

En haut de chaque fichier .md, vous pouvez ajouter :

```markdown
---
marp: true
theme: docker-kubernetes
paginate: true
backgroundColor: #fff
---
```

---

## 🚀 Méthode Rapide (Recommandée)

### Étapes Simples

1. **Installer Marp CLI**
   ```bash
   npm install -g @marp-team/marp-cli
   ```

2. **Exécuter le script de conversion**
   ```bash
   # Linux/macOS
   ./convert_to_presentations.sh
   
   # Windows/Multiplateforme
   python convert_to_presentations.py
   ```

3. **Ouvrir les présentations**
   - Les fichiers sont dans le dossier `presentations/`
   - Ouvrir dans PowerPoint et ajuster si nécessaire

---

## 📦 Structure des Fichiers Générés

```
presentations/
├── module1_introduction_conteneurisation.pptx
├── module1_introduction_conteneurisation.pdf
├── module2_docker_commandes_essentielles.pptx
├── module2_docker_commandes_essentielles.pdf
├── module3_docker_avance.pptx
├── module3_docker_avance.pdf
├── module4_kubernetes.pptx
└── module4_kubernetes.pdf
```

---

## 💡 Conseils

### Pour PowerPoint

- ✅ Utiliser Marp pour la conversion automatique
- ✅ Ajuster les images et la mise en page après conversion
- ✅ Vérifier que les tableaux sont bien formatés
- ✅ Ajouter des animations si souhaité

### Pour Google Slides

- ✅ Importer le PPTX généré par Marp
- ✅ Ajuster les polices et couleurs
- ✅ Partager avec les étudiants

### Bonnes Pratiques

- 📝 Garder les fichiers Markdown comme source
- 🔄 Régénérer les PPTX après modifications
- 💾 Versionner les deux formats (MD et PPTX)
- 📤 Partager les PPTX pour la présentation

---

## 🛠️ Dépannage

### Problème : Marp ne s'installe pas

**Solution :**
```bash
# Vérifier Node.js
node --version

# Installer Node.js si nécessaire
# Puis réessayer
npm install -g @marp-team/marp-cli
```

### Problème : Les images ne s'affichent pas

**Solution :**
- Utiliser des chemins relatifs pour les images
- Ajouter l'option `--allow-local-files`
- Ou convertir en PDF puis en PPTX

### Problème : Le formatage est incorrect

**Solution :**
- Ajuster le fichier Markdown
- Utiliser le thème Marp personnalisé (`marp-theme.css`)
- Ou éditer manuellement le PPTX après conversion

### Problème : Erreur "command not found: marp"

**Solution :**
```bash
# Vérifier l'installation
npm list -g @marp-team/marp-cli

# Réinstaller si nécessaire
npm install -g @marp-team/marp-cli

# Vérifier le PATH
echo $PATH
```

---

## 📚 Ressources

- **Marp Documentation :** https://marp.app/
- **Marp CLI GitHub :** https://github.com/marp-team/marp-cli
- **Pandoc Manual :** https://pandoc.org/MANUAL.html
- **Markdown Guide :** https://www.markdownguide.org/

---

## ✅ Checklist de Conversion

- [ ] Installer Marp CLI ou Pandoc
- [ ] Tester la conversion sur un module
- [ ] Vérifier le résultat dans PowerPoint
- [ ] Ajuster le thème si nécessaire
- [ ] Convertir tous les modules avec le script
- [ ] Vérifier les images et tableaux
- [ ] Créer les PDF
- [ ] Partager les présentations

---

## 🎓 Utilisation pour le Cours

### Avant le cours

1. Générer les présentations :
   ```bash
   python convert_to_presentations.py
   ```

2. Vérifier les fichiers dans `presentations/`

3. Copier sur une clé USB ou partager via cloud

### Pendant le cours

- Utiliser les fichiers PPTX pour la présentation
- Les étudiants peuvent suivre avec les PDF
- Les fichiers Markdown restent la référence

### Après le cours

- Mettre à jour les Markdown si nécessaire
- Régénérer les présentations
- Partager les versions mises à jour

---

## 🔄 Workflow Recommandé

```
1. Modifier les fichiers .md
   ↓
2. Exécuter convert_to_presentations.py
   ↓
3. Vérifier les PPTX générés
   ↓
4. Commit dans Git
   ↓
5. Partager avec les étudiants
```

---

**Bonne conversion ! 🎉**

---

## 📞 Support

Pour toute question :
- Laurent Grateau : laurent.grateau@fr.ibm.com
- Nicolas Peulvast : peulvast@fr.ibm.com