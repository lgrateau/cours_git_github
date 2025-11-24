# Guide de Conversion en Présentations
## PowerPoint et Google Slides

---

## 🎯 Options de Conversion

Vous avez plusieurs options pour convertir les slides Markdown en présentations PowerPoint ou Google Slides.

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
marp module1_introduction.md -o module1.pptx

# Convertir tous les modules
marp module1_introduction.md -o module1.pptx
marp module2_commandes_essentielles.md -o module2.pptx
marp module3_collaboration_github.md -o module3.pptx
marp module4_pratiques_avancees.md -o module4.pptx
```

### Conversion en PDF

```bash
marp module1_introduction.md -o module1.pdf
```

### Avec VS Code

1. Installer l'extension "Marp for VS Code"
2. Ouvrir un fichier .md
3. Cliquer sur l'icône Marp dans la barre d'outils
4. Exporter en PPTX ou PDF

---

## Option 2 : Pandoc

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
pandoc module1_introduction.md -o module1.pptx

# En PDF via LaTeX
pandoc module1_introduction.md -o module1.pdf

# Avec un thème personnalisé
pandoc module1_introduction.md -o module1.pptx --reference-doc=template.pptx
```

---

## Option 3 : Google Slides (Manuel)

### Méthode 1 : Import Markdown

1. Aller sur https://slides.google.com
2. Créer une nouvelle présentation
3. Extensions → Add-ons → Get add-ons
4. Chercher "Markdown to Slides"
5. Installer et utiliser

### Méthode 2 : Copier-Coller

1. Ouvrir le fichier .md dans VS Code
2. Copier le contenu d'une slide (entre les `---`)
3. Coller dans Google Slides
4. Formater manuellement

---

## Option 4 : Reveal.js (Présentation Web)

### Installation

```bash
npm install -g reveal-md
```

### Utilisation

```bash
# Lancer la présentation dans le navigateur
reveal-md module1_introduction.md

# Exporter en PDF
reveal-md module1_introduction.md --print module1.pdf
```

---

## Option 5 : Script de Conversion Automatique

### Script Bash pour Marp

Créer un fichier `convert_all.sh` :

```bash
#!/bin/bash

# Convertir tous les modules en PPTX
for file in module*.md; do
    output="${file%.md}.pptx"
    echo "Converting $file to $output..."
    marp "$file" -o "$output"
done

echo "Conversion terminée !"
```

Exécuter :
```bash
chmod +x convert_all.sh
./convert_all.sh
```

### Script Python

Créer un fichier `convert_to_pptx.py` :

```python
#!/usr/bin/env python3
import os
import subprocess

modules = [
    "module1_introduction.md",
    "module2_commandes_essentielles.md",
    "module3_collaboration_github.md",
    "module4_pratiques_avancees.md"
]

for module in modules:
    output = module.replace('.md', '.pptx')
    print(f"Converting {module} to {output}...")
    subprocess.run(['marp', module, '-o', output])

print("Conversion terminée !")
```

Exécuter :
```bash
python3 convert_to_pptx.py
```

---

## 🎨 Personnalisation des Slides

### Ajouter un Thème Marp

Créer un fichier `theme.css` :

```css
/* @theme custom */

@import 'default';

section {
  background-color: #f5f5f5;
  font-family: 'Arial', sans-serif;
}

h1 {
  color: #2c3e50;
  border-bottom: 3px solid #3498db;
}

h2 {
  color: #34495e;
}

code {
  background-color: #ecf0f1;
  padding: 2px 5px;
  border-radius: 3px;
}

pre {
  background-color: #2c3e50;
  color: #ecf0f1;
  padding: 20px;
  border-radius: 5px;
}
```

Utiliser le thème :
```bash
marp --theme theme.css module1_introduction.md -o module1.pptx
```

### Ajouter des Directives Marp

En haut de chaque fichier .md, ajouter :

```markdown
---
marp: true
theme: default
paginate: true
backgroundColor: #fff
---
```

---

## 📦 Template PowerPoint Personnalisé

### Créer un Template

1. Ouvrir PowerPoint
2. Créer une présentation avec votre design
3. Sauvegarder comme "template.pptx"
4. Utiliser avec Pandoc :

```bash
pandoc module1_introduction.md -o module1.pptx --reference-doc=template.pptx
```

---

## 🚀 Méthode Rapide (Recommandée)

### Étapes Simples

1. **Installer Marp CLI**
   ```bash
   npm install -g @marp-team/marp-cli
   ```

2. **Convertir tous les modules**
   ```bash
   cd cours_git_github
   marp module1_introduction.md -o presentations/module1.pptx
   marp module2_commandes_essentielles.md -o presentations/module2.pptx
   marp module3_collaboration_github.md -o presentations/module3.pptx
   marp module4_pratiques_avancees.md -o presentations/module4.pptx
   ```

3. **Ouvrir dans PowerPoint et ajuster si nécessaire**

---

## 💡 Conseils

### Pour PowerPoint

- ✅ Utiliser Marp pour la conversion automatique
- ✅ Ajuster les images et la mise en page après conversion
- ✅ Vérifier que les tableaux sont bien formatés
- ✅ Ajouter des animations si souhaité

### Pour Google Slides

- ✅ Importer le PPTX généré par Marp
- ✅ Ou utiliser un add-on Markdown to Slides
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
- Ou convertir en PDF puis en PPTX

### Problème : Le formatage est incorrect

**Solution :**
- Ajuster le fichier Markdown
- Utiliser un thème Marp personnalisé
- Ou éditer manuellement le PPTX après conversion

---

## 📚 Ressources

- **Marp Documentation :** https://marp.app/
- **Pandoc Manual :** https://pandoc.org/MANUAL.html
- **Reveal.js :** https://revealjs.com/
- **Markdown to Slides (Google) :** https://workspace.google.com/marketplace

---

## ✅ Checklist de Conversion

- [ ] Installer Marp CLI ou Pandoc
- [ ] Tester la conversion sur un module
- [ ] Vérifier le résultat dans PowerPoint
- [ ] Ajuster le thème si nécessaire
- [ ] Convertir tous les modules
- [ ] Vérifier les images et tableaux
- [ ] Partager les présentations

---

**Bonne conversion ! 🎉**