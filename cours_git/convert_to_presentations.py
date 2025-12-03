#!/usr/bin/env python3
"""
Script de conversion des modules Markdown en présentations PowerPoint
Utilise Marp CLI pour la conversion
"""

import os
import subprocess
import sys
from pathlib import Path

def check_marp_installed():
    """Vérifie si Marp CLI est installé"""
    try:
        result = subprocess.run(['marp', '--version'], 
                              capture_output=True, 
                              text=True)
        return result.returncode == 0
    except FileNotFoundError:
        return False

def convert_to_pptx(input_file, output_dir):
    """Convertit un fichier Markdown en PowerPoint"""
    output_file = output_dir / f"{input_file.stem}.pptx"
    
    try:
        result = subprocess.run(
            ['marp', str(input_file), '--theme', 'marp-theme.css', '-o', str(output_file), '--allow-local-files'],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            return True, output_file
        else:
            return False, result.stderr
    except Exception as e:
        return False, str(e)

def convert_to_pdf(input_file, output_dir):
    """Convertit un fichier Markdown en PDF"""
    output_file = output_dir / f"{input_file.stem}.pdf"
    
    try:
        result = subprocess.run(
            ['marp', str(input_file), '--theme', 'marp-theme.css', '-o', str(output_file), '--allow-local-files', '--pdf'],
            capture_output=True,
            text=True
        )
        
        if result.returncode == 0:
            return True, output_file
        else:
            return False, result.stderr
    except Exception as e:
        return False, str(e)

def main():
    print("🎯 Conversion des modules en présentations PowerPoint")
    print("=" * 50)
    print()
    
    # Vérifier si Marp est installé
    if not check_marp_installed():
        print("❌ Marp CLI n'est pas installé.")
        print()
        print("Pour installer Marp CLI :")
        print("  npm install -g @marp-team/marp-cli")
        print()
        print("Ou avec Homebrew (macOS) :")
        print("  brew install marp-cli")
        print()
        sys.exit(1)
    
    print("✅ Marp CLI détecté")
    print()
    
    # Créer le dossier de sortie
    output_dir = Path('presentations')
    output_dir.mkdir(exist_ok=True)
    
    # Liste des modules à convertir
    modules = [
        'module1_introduction.md',
        'module2_commandes_essentielles.md',
        'module3_collaboration_github.md',
        'module4_pratiques_avancees.md'
    ]
    
    # Convertir en PowerPoint
    print("📊 Conversion en PowerPoint...")
    print()
    
    success_count = 0
    for i, module_name in enumerate(modules, 1):
        module_path = Path(module_name)
        
        print(f"[{i}/{len(modules)}] Conversion de {module_name}...")
        
        if not module_path.exists():
            print(f"  ⚠️  Fichier non trouvé : {module_name}")
            print()
            continue
        
        success, result = convert_to_pptx(module_path, output_dir)
        
        if success:
            print(f"  ✅ Créé : {result}")
            success_count += 1
        else:
            print(f"  ❌ Erreur : {result}")
        
        print()
    
    # Convertir en PDF
    print("📄 Conversion en PDF...")
    print()
    
    pdf_count = 0
    for module_name in modules:
        module_path = Path(module_name)
        
        if not module_path.exists():
            continue
        
        print(f"  Conversion de {module_name} en PDF...")
        
        success, result = convert_to_pdf(module_path, output_dir)
        
        if success:
            print(f"  ✅ Créé : {result}")
            pdf_count += 1
        else:
            print(f"  ❌ Erreur : {result}")
    
    print()
    print("=" * 50)
    print("✨ Conversion terminée !")
    print()
    print(f"Résumé :")
    print(f"  - PowerPoint : {success_count}/{len(modules)} fichiers créés")
    print(f"  - PDF : {pdf_count}/{len(modules)} fichiers créés")
    print()
    print(f"Les présentations sont disponibles dans le dossier '{output_dir}/'")
    print()
    
    # Lister les fichiers créés
    if output_dir.exists():
        files = sorted(output_dir.glob('*'))
        if files:
            print("Fichiers créés :")
            for file in files:
                size = file.stat().st_size / 1024  # Taille en KB
                print(f"  - {file.name} ({size:.1f} KB)")
    
    print()
    print("Pour ouvrir les présentations :")
    print("  - PowerPoint : Ouvrir les fichiers .pptx")
    print("  - PDF : Ouvrir les fichiers .pdf")
    print("  - Google Slides : Importer les fichiers .pptx")
    print()

if __name__ == '__main__':
    main()

# Made with Bob
