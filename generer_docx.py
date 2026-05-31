"""
Génération des .docx TIPE via Pandoc.
Pandoc gère nativement : markdown, LaTeX $...$, tableaux, gras/italique.
"""

import subprocess
import os
import tempfile

PANDOC = r"C:\Program Files\Pandoc\pandoc.exe"
BASE   = r"C:\Users\samue\Documents\Claude-projet\TIPE-clem"

# Correspondance section → fichier image individuel
# Inséré juste après la ligne de titre de section dans le rapport
GRAPH_SECTIONS = {
    "### IV.1.": "graphique_1_distribution.png",
    "### IV.2.": "graphique_2_cinetique.png",
    "### IV.3.": "graphique_3_oxygene.png",
    "### IV.4.": "graphique_4_abaque.png",
}


def inject_images(md_content):
    """Insère les références d'images après les sections IV.x du rapport."""
    lines = md_content.split('\n')
    result = []
    for line in lines:
        result.append(line)
        for heading, img_file in GRAPH_SECTIONS.items():
            if line.startswith(heading):
                img_path = os.path.join(BASE, img_file).replace('\\', '/')
                if os.path.exists(os.path.join(BASE, img_file)):
                    result.append('')
                    result.append(f'![]({img_path})')
                    result.append('')
    return '\n'.join(result)


def convert(md_path, docx_path, with_images=False):
    with open(md_path, encoding='utf-8') as f:
        content = f.read()

    if with_images:
        content = inject_images(content)

    # Fichier temporaire avec le contenu modifié
    tmp = tempfile.NamedTemporaryFile(
        mode='w', suffix='.md', encoding='utf-8', delete=False,
        dir=BASE  # même dossier → chemins relatifs images OK
    )
    tmp.write(content)
    tmp.close()

    cmd = [
        PANDOC, tmp.name,
        '-o', docx_path,
        '--from=markdown+tex_math_dollars+smart',
        '--standalone',
        '--wrap=none',
    ]

    try:
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)
        size = os.path.getsize(docx_path) // 1024
        print(f"OK  {os.path.basename(docx_path)}  ({size} Ko)")
    except subprocess.CalledProcessError as e:
        print(f"ERREUR {os.path.basename(docx_path)} :\n{e.stderr}")
    finally:
        os.unlink(tmp.name)


# ─── Génération ─────────────────────────────────────────────────────────────

files = [
    ("rapport_TIPE_complet.md",     "rapport_TIPE_complet.docx",     True),
    ("revue_litterature_SO2_vin.md", "revue_litterature_SO2_vin.docx", False),
    ("preparation_oral_jury.md",     "preparation_oral_jury.docx",     False),
]

for md_file, docx_file, imgs in files:
    convert(
        os.path.join(BASE, md_file),
        os.path.join(BASE, docx_file),
        with_images=imgs,
    )

print("\nTous les .docx ont été générés.")
