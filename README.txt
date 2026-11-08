TICE 6e — SÉANCE 08 — MISSION IMAGE
===================================
Durée : 55 minutes. Prévu pour Firefox + LibreOffice Writer.
Même palette et codes graphiques que « Le Bureau Mystère », sans commande de zoom.

DÉMARRER
1. Extraire tout le ZIP : ne pas ouvrir index.html à l’intérieur de l’archive.
2. Ouvrir index.html dans Firefox. Tout le parcours fonctionne hors ligne.
3. Lire le guide dans enseignant/guide.html pour préparer la séance.

CONTENU
index.html / style.css / script.js : site élève, 5 défis + mission réelle + bilan.
galerie.html : galerie d’images à ouvrir dans Firefox pour glisser vers Writer.
assets/ : images PNG réelles + sources SVG modifiables (800 × 500 pixels).
ressources/fiche_depart.odt : document élève avec texte et emplacements.
ressources/texte_depart.txt : secours texte si nécessaire.
enseignant/guide.html : déroulé, corrections, barème, limites et sources.
enseignant/modele_corrige.odt : exemple de résultat sur une page A4.

GITHUB PAGES
Déposer le CONTENU du dossier à la racine du dépôt ou dans un sous-dossier.
Les chemins sont relatifs. Aucun outil de compilation ni installation requis.
Ne pas ajouter de CDN ni modifier les chemins des images sans modifier les liens.
La publication n’est pas effectuée automatiquement par ce dossier.

ÉVALUATION
1000 points attribués une seule fois par critère réussi (12 critères, 5 domaines).
Le score porte uniquement sur le simulateur. Les erreurs et aides restent visibles.
Le fichier réalisé dans Writer n’est pas analysé par le site.
L’autocontrôle de 7 critères doit être observé/validé par l’enseignant.
Les méthodes accessibles au clic sont distinguées du glisser-déposer.

IMPRESSION
Bouton « Imprimer mon bilan » ou commande d’impression du navigateur : seul le
bilan s’imprime. Format A4 portrait, échelle 100 %, sans en-têtes/pieds de page
ajoutés par le navigateur. La mise en page est prévue pour une page.
Les fonds colorés ne sont pas nécessaires. Une impression en PDF convient aussi.

DONNÉES
Identité facultative. Aucun résultat n’est transmis à un serveur.
La sauvegarde facultative utilise uniquement le navigateur courant.
Sans sauvegarde, fermer/recharger la page fait perdre la progression.
Sur un poste partagé, conserver le bilan puis « Nouvel élève · tout effacer ».
L’export JSON est un relevé des résultats, pas le fichier Writer ni une sauvegarde
importable. Le .odt doit être rendu séparément selon les consignes du professeur.

COMPATIBILITÉ
Les simulations ne nécessitent aucun accès système. Le véritable glissement de
Firefox vers Writer dépend de l’installation ; le tester sur un poste du collège.
Secours : enregistrer le PNG puis Insertion > Image (sans Lier). Cette méthode est
prévue dans la fiche et déclarée dans le bilan.
Ne pas interpréter un succès simulé comme une validation automatique dans Writer.

MODIFIER
Contenus et barème : tableaux de données en tête de script.js.
Palette : variables :root au début de style.css.
Bilan imprimé : bloc @media print à la fin de style.css.
Consignes et objectifs : index.html ; guide : enseignant/guide.html.
