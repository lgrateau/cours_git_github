#!/bin/bash

# Script de conversion des modules Markdown en présentations PowerPoint
# Utilise Marp CLI pour la conversion

echo "🎯 Conversion des modules en présentations PowerPoint"
echo "=================================================="
echo ""

# Vérifier si Marp est installé
if ! command -v marp &> /dev/null
then
    echo "❌ Marp CLI n'est pas installé."
    echo ""
    echo "Pour installer Marp CLI :"
    echo "  npm install -g @marp-team/marp-cli"
    echo ""
    echo "Ou avec Homebrew (macOS) :"
    echo "  brew install marp-cli"
    echo ""
    exit 1
fi

echo "✅ Marp CLI détecté"
echo ""

# Créer le dossier de sortie
mkdir -p presentations

# Liste des modules à convertir
modules=(
    "module1_introduction_conteneurisation.md"
    "module2_docker_commandes_essentielles.md"
    "module3_docker_avance.md"
    "module4_kubernetes.md"
)

# Compteur
total=${#modules[@]}
current=0

# Convertir chaque module
for module in "${modules[@]}"
do
    current=$((current + 1))
    output="presentations/${module%.md}.pptx"
    
    echo "[$current/$total] Conversion de $module..."
    
    if [ -f "$module" ]; then
        marp "$module" --theme marp-theme.css -o "$output" --allow-local-files
        
        if [ $? -eq 0 ]; then
            echo "  ✅ Créé : $output"
        else
            echo "  ❌ Erreur lors de la conversion de $module"
        fi
    else
        echo "  ⚠️  Fichier non trouvé : $module"
    fi
    
    echo ""
done

# Convertir aussi en PDF
echo "📄 Conversion en PDF..."
echo ""

for module in "${modules[@]}"
do
    output="presentations/${module%.md}.pdf"
    
    if [ -f "$module" ]; then
        echo "  Conversion de $module en PDF..."
        marp "$module" --theme marp-theme.css -o "$output" --allow-local-files --pdf
        
        if [ $? -eq 0 ]; then
            echo "  ✅ Créé : $output"
        fi
    fi
done

echo ""
echo "=================================================="
echo "✨ Conversion terminée !"
echo ""
echo "Les présentations sont disponibles dans le dossier 'presentations/'"
echo ""
echo "Fichiers créés :"
ls -lh presentations/
echo ""
echo "Pour ouvrir les présentations :"
echo "  - PowerPoint : Ouvrir les fichiers .pptx"
echo "  - PDF : Ouvrir les fichiers .pdf"
echo "  - Google Slides : Importer les fichiers .pptx"
echo ""

# Cours Docker & Kubernetes - Polytech

# Made with Bob
