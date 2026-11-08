"""Reconstitue les fichiers originaux de la séance 8 après leur transfert.
Sources textuelles et contenus ODT conservés sans modification.
Aucune donnée élève, aucun accès externe dans le site généré.
"""
from pathlib import Path
import base64
import hashlib
import io
import tarfile
from zipfile import ZipFile, ZIP_DEFLATED, ZIP_STORED
import cairosvg

ROOT = Path(__file__).resolve().parent.parent
parts = sorted((ROOT / '.build').glob('source_*.b64'))
if len(parts) != 5:
    raise RuntimeError('Les cinq parties de la séance sont nécessaires.')
encoded = ''.join(p.read_text(encoding='ascii').strip() for p in parts)
payload = base64.b64decode(encoded, validate=True)
expected = 'e6717879508b2d9cb02f7f359a9da8bd4dc0cd610a070e9313b95621f9382338'
if hashlib.sha256(payload).hexdigest() != expected:
    raise RuntimeError('Contrôle d’intégrité du transfert incorrect.')
files = []
with tarfile.open(fileobj=io.BytesIO(payload), mode='r:xz') as source:
    for member in source.getmembers():
        destination = (ROOT / member.name).resolve()
        if not member.isfile() or not destination.is_relative_to(ROOT):
            raise RuntimeError('Entrée inattendue dans les sources.')
        destination.parent.mkdir(parents=True, exist_ok=True)
        stream = source.extractfile(member)
        if stream is None:
            raise RuntimeError('Source manquante.')
        destination.write_bytes(stream.read())
        if not member.name.startswith('.templates/'):
            files.append(member.name)

for name in ('robot_pixel', 'jardin_solaire'):
    svg = ROOT / 'assets' / (name + '.svg')
    png = svg.with_suffix('.png')
    cairosvg.svg2png(bytestring=svg.read_bytes(), write_to=str(png))
    files.append(png.relative_to(ROOT).as_posix())

pictures = {
    'Pictures/A5B40CEE4B5942C8B6F213CD91A96666.png': 'assets/robot_pixel.png',
    'Pictures/D4685765BF9546498A8096C312CE60DB.png': 'assets/jardin_solaire.png',
}
for rel in ('ressources/fiche_depart.odt', 'enseignant/modele_corrige.odt'):
    template = ROOT / '.templates' / rel
    target = ROOT / rel
    target.parent.mkdir(parents=True, exist_ok=True)
    with ZipFile(target, 'w', compression=ZIP_DEFLATED) as new:
        new.writestr('mimetype', (template / 'mimetype').read_bytes(), compress_type=ZIP_STORED)
        for item in sorted(template.rglob('*')):
            if item.is_file() and item.name != 'mimetype':
                new.write(item, item.relative_to(template).as_posix())
        if rel.startswith('enseignant/'):
            for destination, source in pictures.items():
                new.writestr(destination, (ROOT / source).read_bytes())
    with ZipFile(target) as check:
        if check.testzip() is not None:
            raise RuntimeError('Le document ODT est endommagé.')
    files.append(rel)

(ROOT / '.nojekyll').write_text('', encoding='utf-8')
files.append('.nojekyll')
with ZipFile(ROOT / 'Mission-image-6e.zip', 'w', compression=ZIP_DEFLATED) as bundle:
    for rel in sorted(set(files)):
        bundle.write(ROOT / rel, rel)
with ZipFile(ROOT / 'Mission-image-6e.zip') as check:
    if check.testzip() is not None:
        raise RuntimeError('L’archive finale est endommagée.')
print(f'Séance prête : {len(files)} fichiers, archive vérifiée.')
