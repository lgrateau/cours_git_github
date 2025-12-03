#!/usr/bin/env python3
"""
Générateur de présentations HTML à partir des modules Markdown
Utilise reveal.js pour créer des slides interactives
"""

import re
from pathlib import Path

# Template HTML avec reveal.js
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/dist/reset.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/dist/reveal.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/dist/theme/white.css">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/plugin/highlight/monokai.css">
    <style>
        .reveal {{
            font-size: 24px;
        }}
        .reveal .slides {{
            background: #f5f7fa;
        }}
        .reveal .slides section {{
            background: white;
            border-radius: 8px;
            box-shadow: 0 4px 20px rgba(0,0,0,0.08);
        }}
        .reveal h1 {{
            color: #ffffff;
            background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%);
            font-size: 1.6em;
            margin: -20px -20px 0.5em -20px;
            padding: 20px 20px;
            border-radius: 8px 8px 0 0;
            line-height: 1.2;
            font-weight: bold;
            text-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        .reveal h2 {{
            color: #1e40af;
            font-size: 1.2em;
            margin-bottom: 0.4em;
            padding-bottom: 0.3em;
            border-bottom: 2px solid #3b82f6;
            line-height: 1.2;
            font-weight: 600;
        }}
        .reveal h3 {{
            color: #059669;
            font-size: 1.0em;
            line-height: 1.2;
            font-weight: 600;
        }}
        .reveal p {{
            font-size: 0.8em;
            line-height: 1.5;
            margin-bottom: 0.5em;
            color: #1f2937;
        }}
        .reveal ul, .reveal ol {{
            font-size: 0.75em;
            line-height: 1.4;
        }}
        .reveal li {{
            margin-bottom: 0.3em;
            color: #1f2937;
        }}
        .reveal code {{
            background-color: #fef3c7;
            padding: 2px 6px;
            border-radius: 3px;
            color: #92400e;
            font-size: 0.8em;
            font-weight: 600;
            border: 1px solid #fbbf24;
        }}
        .reveal pre {{
            font-size: 0.5em;
            line-height: 1.3;
            margin: 8px 0;
        }}
        .reveal pre {{
            background-color: #1e293b;
            border-radius: 8px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            border: 1px solid #334155;
        }}
        .reveal pre code {{
            background: transparent;
            color: #e2e8f0;
            padding: 12px;
            border-radius: 5px;
            max-height: 400px;
            overflow: auto;
        }}
        .reveal table {{
            font-size: 0.6em;
            line-height: 1.3;
        }}
        .reveal table th {{
            background: linear-gradient(135deg, #2563eb 0%, #1e40af 100%);
            color: white;
            padding: 8px;
            font-weight: bold;
        }}
        .reveal table td {{
            border: 1px solid #e5e7eb;
            padding: 6px;
            color: #1f2937;
        }}
        .reveal table tr:nth-child(even) {{
            background-color: #f9fafb;
        }}
        .reveal table tr:hover {{
            background-color: #dbeafe;
        }}
        .reveal ul, .reveal ol {{
            text-align: left;
        }}
        .reveal blockquote {{
            background-color: #dbeafe;
            border-left: 4px solid #2563eb;
            padding: 12px 16px;
            font-style: italic;
            font-size: 0.8em;
            border-radius: 4px;
            color: #1e40af;
        }}
        .emoji {{
            font-size: 1.1em;
        }}
        .reveal .slides section {{
            text-align: left;
            height: 100%;
            padding: 20px;
        }}
        .reveal .slides section > h1 {{
            text-align: center;
        }}
        .reveal .slides section > h2 {{
            text-align: left;
        }}
        .reveal strong {{
            color: #1e40af;
            font-weight: bold;
        }}
        .reveal em {{
            color: #059669;
            font-style: italic;
        }}
        .reveal a {{
            color: #2563eb;
            font-weight: 600;
        }}
        .reveal a:hover {{
            color: #1e40af;
        }}
        .reveal ul li::marker {{
            color: #2563eb;
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <div class="reveal">
        <div class="slides">
{slides}
        </div>
    </div>
    <script src="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/dist/reveal.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/plugin/notes/notes.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/plugin/markdown/markdown.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/plugin/highlight/highlight.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/reveal.js@4.5.0/plugin/zoom/zoom.js"></script>
    <script>
        Reveal.initialize({{
            hash: true,
            slideNumber: true,
            transition: 'slide',
            plugins: [ RevealMarkdown, RevealHighlight, RevealNotes, RevealZoom ],
            width: 1200,
            height: 700,
            margin: 0.1,
            minScale: 0.2,
            maxScale: 2.0
        }});
    </script>
</body>
</html>
"""

def parse_markdown_to_slides(content):
    """Parse le contenu Markdown et le convertit en slides HTML"""
    # Séparer par les délimiteurs de slides (---)
    slides_content = content.split('\n---\n')
    
    html_slides = []
    
    for slide_content in slides_content:
        if not slide_content.strip():
            continue
        
        # Convertir le Markdown en HTML basique
        html = convert_markdown_to_html(slide_content.strip())
        
        # Créer une section reveal.js
        html_slides.append(f'            <section>\n{html}\n            </section>')
    
    return '\n'.join(html_slides)

def convert_markdown_to_html(markdown):
    """Convertit le Markdown en HTML"""
    html = markdown
    
    # Titres
    html = re.sub(r'^### (.+)$', r'                <h3>\1</h3>', html, flags=re.MULTILINE)
    html = re.sub(r'^## (.+)$', r'                <h2>\1</h2>', html, flags=re.MULTILINE)
    html = re.sub(r'^# (.+)$', r'                <h1>\1</h1>', html, flags=re.MULTILINE)
    
    # Gras et italique
    html = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html)
    html = re.sub(r'\*(.+?)\*', r'<em>\1</em>', html)
    
    # Code inline
    html = re.sub(r'`([^`]+)`', r'<code>\1</code>', html)
    
    # Blocs de code
    def replace_code_block(match):
        lang = match.group(1) or ''
        code = match.group(2)
        return f'                <pre><code class="language-{lang}">{code}</code></pre>'
    
    html = re.sub(r'```(\w+)?\n(.*?)```', replace_code_block, html, flags=re.DOTALL)
    
    # Listes non ordonnées
    def replace_ul(match):
        items = match.group(0)
        items = re.sub(r'^- (.+)$', r'                    <li>\1</li>', items, flags=re.MULTILINE)
        return f'                <ul>\n{items}\n                </ul>'
    
    html = re.sub(r'(?:^- .+$\n?)+', replace_ul, html, flags=re.MULTILINE)
    
    # Listes ordonnées
    def replace_ol(match):
        items = match.group(0)
        items = re.sub(r'^\d+\. (.+)$', r'                    <li>\1</li>', items, flags=re.MULTILINE)
        return f'                <ol>\n{items}\n                </ol>'
    
    html = re.sub(r'(?:^\d+\. .+$\n?)+', replace_ol, html, flags=re.MULTILINE)
    
    # Tableaux
    def replace_table(match):
        lines = match.group(0).strip().split('\n')
        if len(lines) < 3:
            return match.group(0)
        
        # Header
        headers = [cell.strip() for cell in lines[0].split('|')[1:-1]]
        
        # Rows (skip separator line)
        rows = []
        for line in lines[2:]:
            cells = [cell.strip() for cell in line.split('|')[1:-1]]
            rows.append(cells)
        
        # Build HTML table
        table_html = '                <table>\n'
        table_html += '                    <thead>\n                        <tr>\n'
        for header in headers:
            table_html += f'                            <th>{header}</th>\n'
        table_html += '                        </tr>\n                    </thead>\n'
        table_html += '                    <tbody>\n'
        for row in rows:
            table_html += '                        <tr>\n'
            for cell in row:
                table_html += f'                            <td>{cell}</td>\n'
            table_html += '                        </tr>\n'
        table_html += '                    </tbody>\n                </table>'
        
        return table_html
    
    html = re.sub(r'(?:^\|.+\|$\n?)+', replace_table, html, flags=re.MULTILINE)
    
    # Liens
    html = re.sub(r'\[([^\]]+)\]\(([^\)]+)\)', r'<a href="\2" target="_blank">\1</a>', html)
    
    # Paragraphes
    lines = html.split('\n')
    processed_lines = []
    in_block = False
    
    for line in lines:
        stripped = line.strip()
        if stripped.startswith('<') or not stripped:
            processed_lines.append(line)
            in_block = stripped.startswith('<pre>') or stripped.startswith('<ul>') or stripped.startswith('<ol>') or stripped.startswith('<table>')
        elif not in_block:
            processed_lines.append(f'                <p>{line}</p>')
        else:
            processed_lines.append(line)
    
    return '\n'.join(processed_lines)

def generate_html_presentation(markdown_file, output_file):
    """Génère une présentation HTML à partir d'un fichier Markdown"""
    print(f"  Traitement de {markdown_file.name}...")
    
    # Lire le contenu Markdown
    content = markdown_file.read_text(encoding='utf-8')
    
    # Extraire le titre (première ligne avec #)
    title_match = re.search(r'^# (.+)$', content, re.MULTILINE)
    title = title_match.group(1) if title_match else markdown_file.stem
    
    # Convertir en slides HTML
    slides_html = parse_markdown_to_slides(content)
    
    # Générer le HTML complet
    html = HTML_TEMPLATE.format(title=title, slides=slides_html)
    
    # Écrire le fichier HTML
    output_file.write_text(html, encoding='utf-8')
    
    print(f"  ✅ Créé : {output_file}")

def main():
    print("🎯 Génération des présentations HTML")
    print("=" * 50)
    print()
    
    # Créer le dossier de sortie
    output_dir = Path('presentations_html')
    output_dir.mkdir(exist_ok=True)
    
    # Liste des modules à convertir
    modules = [
        'module1_introduction.md',
        'module2_commandes_essentielles.md',
        'module3_collaboration_github.md',
        'module4_pratiques_avancees.md'
    ]
    
    success_count = 0
    
    for i, module_name in enumerate(modules, 1):
        module_path = Path(module_name)
        
        print(f"[{i}/{len(modules)}] {module_name}")
        
        if not module_path.exists():
            print(f"  ⚠️  Fichier non trouvé : {module_name}")
            print()
            continue
        
        output_file = output_dir / f"{module_path.stem}.html"
        
        try:
            generate_html_presentation(module_path, output_file)
            success_count += 1
        except Exception as e:
            print(f"  ❌ Erreur : {e}")
        
        print()
    
    # Créer un index
    print("📄 Création de l'index...")
    create_index(output_dir, modules)
    print()
    
    print("=" * 50)
    print("✨ Génération terminée !")
    print()
    print(f"Résumé : {success_count}/{len(modules)} présentations créées")
    print()
    print(f"Les présentations sont disponibles dans '{output_dir}/'")
    print()
    print("Pour visualiser :")
    print(f"  1. Ouvrir {output_dir}/index.html dans un navigateur")
    print("  2. Ou ouvrir directement chaque fichier HTML")
    print()
    print("Navigation dans les slides :")
    print("  - Flèches ← → : Slide précédente/suivante")
    print("  - Espace : Slide suivante")
    print("  - ESC : Vue d'ensemble")
    print("  - F : Plein écran")
    print()

def create_index(output_dir, modules):
    """Crée une page d'index pour accéder à toutes les présentations"""
    index_html = """<!DOCTYPE html>
<html lang="fr">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Cours Git et GitHub - Index des Présentations</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            max-width: 1000px;
            margin: 0 auto;
            padding: 40px 20px;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh;
        }
        .container {
            background: white;
            border-radius: 10px;
            padding: 40px;
            box-shadow: 0 10px 40px rgba(0,0,0,0.2);
        }
        h1 {
            color: #2c3e50;
            text-align: center;
            margin-bottom: 10px;
        }
        .subtitle {
            text-align: center;
            color: #7f8c8d;
            margin-bottom: 40px;
        }
        .modules {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
            gap: 20px;
            margin-top: 30px;
        }
        .module-card {
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            border-radius: 8px;
            padding: 30px;
            text-decoration: none;
            color: white;
            transition: transform 0.3s, box-shadow 0.3s;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .module-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 8px 15px rgba(0,0,0,0.2);
        }
        .module-number {
            font-size: 2em;
            font-weight: bold;
            margin-bottom: 10px;
            opacity: 0.9;
        }
        .module-title {
            font-size: 1.2em;
            font-weight: 600;
            margin-bottom: 10px;
        }
        .module-duration {
            font-size: 0.9em;
            opacity: 0.8;
        }
        .info {
            background: #ecf0f1;
            border-left: 4px solid #3498db;
            padding: 15px;
            margin: 30px 0;
            border-radius: 4px;
        }
        .info h3 {
            margin-top: 0;
            color: #2c3e50;
        }
        .shortcuts {
            background: #f8f9fa;
            padding: 20px;
            border-radius: 8px;
            margin-top: 30px;
        }
        .shortcuts h3 {
            color: #2c3e50;
            margin-top: 0;
        }
        .shortcuts ul {
            list-style: none;
            padding: 0;
        }
        .shortcuts li {
            padding: 8px 0;
            border-bottom: 1px solid #dee2e6;
        }
        .shortcuts li:last-child {
            border-bottom: none;
        }
        .shortcuts code {
            background: #e9ecef;
            padding: 2px 8px;
            border-radius: 3px;
            font-family: 'Courier New', monospace;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>🎓 Cours Git et GitHub</h1>
        <p class="subtitle">Pour Ingénieurs en Électronique - Formation de 4 heures</p>
        
        <div class="info">
            <h3>📚 À propos de ce cours</h3>
            <p>Ce cours complet vous permettra de maîtriser Git et GitHub pour vos projets d'électronique et de développement embarqué.</p>
        </div>
        
        <div class="modules">
"""
    
    module_info = [
        ("Module 1", "Introduction et Concepts Fondamentaux", "60 min"),
        ("Module 2", "Commandes Git Essentielles", "60 min"),
        ("Module 3", "Collaboration avec GitHub", "60 min"),
        ("Module 4", "Pratiques Avancées et Cas d'Usage", "60 min")
    ]
    
    for i, (module_name, module_title, duration) in enumerate(module_info, 1):
        html_file = f"module{i}_{'introduction' if i == 1 else 'commandes_essentielles' if i == 2 else 'collaboration_github' if i == 3 else 'pratiques_avancees'}.html"
        index_html += f"""
            <a href="{html_file}" class="module-card">
                <div class="module-number">{module_name}</div>
                <div class="module-title">{module_title}</div>
                <div class="module-duration">⏱️ {duration}</div>
            </a>
"""
    
    index_html += """
        </div>
        
        <div class="shortcuts">
            <h3>⌨️ Raccourcis clavier dans les présentations</h3>
            <ul>
                <li><code>←</code> <code>→</code> : Naviguer entre les slides</li>
                <li><code>Espace</code> : Slide suivante</li>
                <li><code>ESC</code> : Vue d'ensemble de toutes les slides</li>
                <li><code>F</code> : Mode plein écran</li>
                <li><code>S</code> : Mode présentateur (avec notes)</li>
                <li><code>?</code> : Afficher l'aide</li>
            </ul>
        </div>
        
        <div class="info">
            <h3>💡 Conseils</h3>
            <ul>
                <li>Suivez les modules dans l'ordre pour une progression optimale</li>
                <li>Pratiquez les exercices après chaque module</li>
                <li>Consultez l'aide-mémoire Git pour référence rapide</li>
                <li>N'hésitez pas à revenir sur les slides si nécessaire</li>
            </ul>
        </div>
    </div>
</body>
</html>
"""
    
    index_file = output_dir / 'index.html'
    index_file.write_text(index_html, encoding='utf-8')
    print(f"  ✅ Index créé : {index_file}")

if __name__ == '__main__':
    main()

# Made with Bob
