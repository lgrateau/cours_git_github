# Présentations PowerPoint et PDF

Ce dossier contient les présentations générées à partir des fichiers Markdown.

## 📊 Fichiers disponibles

Après avoir exécuté le script de conversion, vous trouverez ici :

- `module1_introduction_conteneurisation.pptx` / `.pdf`
- `module2_docker_commandes_essentielles.pptx` / `.pdf`
- `module3_docker_avance.pptx` / `.pdf`
- `module4_kubernetes.pptx` / `.pdf`

## 🚀 Génération des présentations

### Méthode 1 : Script Python (Recommandé)

```bash
# Depuis la racine du projet
python convert_to_presentations.py
```

### Méthode 2 : Script Bash (Linux/macOS)

```bash
# Depuis la racine du projet
chmod +x convert_to_presentations.sh
./convert_to_presentations.sh
```

### Méthode 3 : Manuellement

```bash
# Installer Marp CLI
npm install -g @marp-team/marp-cli

# Convertir chaque module
marp module1_introduction_conteneurisation.md --theme marp-theme.css -o presentations/module1_introduction_conteneurisation.pptx --allow-local-files
marp module2_docker_commandes_essentielles.md --theme marp-theme.css -o presentations/module2_docker_commandes_essentielles.pptx --allow-local-files
marp module3_docker_avance.md --theme marp-theme.css -o presentations/module3_docker_avance.pptx --allow-local-files
marp module4_kubernetes.md --theme marp-theme.css -o presentations/module4_kubernetes.pptx --allow-local-files

# Pour les PDF, ajouter --pdf
marp module1_introduction_conteneurisation.md --theme marp-theme.css -o presentations/module1_introduction_conteneurisation.pdf --allow-local-files --pdf
```

## 📝 Notes

- Les fichiers PPTX et PDF ne sont pas versionnés dans Git (voir `.gitignore`)
- Ils doivent être régénérés après chaque modification des fichiers Markdown
- Les présentations utilisent le thème personnalisé `marp-theme.css`

## 🎨 Personnalisation

Pour modifier le style des présentations, éditez le fichier `marp-theme.css` à la racine du projet.

## 📚 Documentation

Consultez `CONVERSION_PRESENTATIONS.md` pour plus d'informations sur :
- Installation de Marp
- Options de conversion
- Dépannage
- Bonnes pratiques

---

**Cours Docker & Kubernetes - Polytech**