# Mission image · TICE 6e · Séance 8

Séance de 55 minutes : insérer, redimensionner et placer des images dans LibreOffice Writer.

Cette séance reprend la charte graphique du **Bureau Mystère**, sans commande de zoom. Elle comprend des défis interactifs, une mission réelle dans Writer, des aides, un bilan détaillé et une feuille d’impression A4.

## Télécharger et démarrer

**[Télécharger la séance complète, prête à utiliser](./Mission-image-6e.zip?raw=true)**

Extraire tout le ZIP, puis ouvrir `index.html` dans Firefox. Le site fonctionne aussi hors ligne : aucune dépendance externe obligatoire et aucun compte élève.

Le ZIP comprend le site, la galerie, les images, les documents Writer et le guide professeur. L’autre option **Code → Download ZIP** télécharge l’ensemble du dépôt, y compris les fichiers techniques de transfert.

## Publication GitHub Pages

Les fichiers sont prêts à la racine du dépôt. La mise en ligne du site nécessite l’activation de GitHub Pages :

1. Ouvrir **Settings → Pages**.
2. Dans **Build and deployment**, choisir **Deploy from a branch**.
3. Sélectionner **main** et **/(root)**, puis **Save**.

L’adresse attendue après publication est : https://vincent-belhaire.github.io/Mission-image-6e/

La page **Settings → Pages** indique l’état et l’adresse de publication.

## Contenu

- `index.html`, `style.css`, `script.js` : parcours élève et bilan imprimable.
- `galerie.html`, `assets/` : galerie Firefox et images pédagogiques.
- `ressources/fiche_depart.odt` : document élève à compléter dans Writer.
- `enseignant/modele_corrige.odt` et `enseignant/guide.html` : modèle et accompagnement enseignant.
- `README.txt` : mode d’emploi détaillé.
- `Mission-image-6e.zip` : archive prête à utiliser.

Les dossiers `.build` et `.github` ont servi au transfert contrôlé des fichiers. Ils ne sont pas nécessaires au fonctionnement local de la séance et ne sont pas inclus dans le ZIP prêt à utiliser.

## Évaluation et impression

Le score porte sur le simulateur. Le travail effectué dans LibreOffice n’est pas analysé automatiquement : l’autocontrôle élève doit être confirmé par l’enseignant.

Le bouton **Imprimer mon bilan** n’imprime que le bilan : A4 portrait, échelle 100 %, sans les en-têtes et pieds de page ajoutés par le navigateur. La feuille de style dédiée à l’impression est conservée dans `style.css`.

## Données

L’identité est facultative. Aucun résultat n’est envoyé à un serveur. La sauvegarde éventuelle reste dans le navigateur de l’élève. Sur un poste partagé, utiliser **Nouvel élève · tout effacer** après conservation du bilan.
