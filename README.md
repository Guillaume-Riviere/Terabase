# TeraCodex - Base de Données du Jeu Tera

TeraCodex est une application web permettant de rechercher et d'afficher diverses données du jeu Tera à partir de fichiers JSON. L'application inclut des fonctionnalités de recherche, de filtrage et de pagination, ainsi qu'une modale pour afficher les détails des éléments.

## Fonctionnalités

- Recherche d'éléments par nom ou description.
- Filtrage des éléments par ID.
- Affichage des détails des éléments dans une modale.
- Pagination des résultats de recherche.
- Indicateur de chargement pendant la recherche.

## Prérequis

- Un serveur web pour servir les fichiers HTML, CSS et JavaScript.
- Les fichiers JSON contenant les données du jeu doivent être disponibles dans le répertoire `Data/`.

## Installation

1. Clonez le dépôt :
    ```bash
    git clone https://github.com/BrendonDesvaux/teracodex.git
    ```

2. Placez les fichiers JSON dans le répertoire `Data/`.

3. Ouvrez le fichier `index.html` dans un navigateur web avec LiveServeur.

## Structure du Projet

- `index.html` : Le fichier HTML principal contenant la structure de l'application.
- `style.css` : Le fichier CSS principal pour le style de l'application.
- `item.css` : Le fichier CSS pour les styles spécifiques aux éléments.
- `Data/` : Le répertoire contenant les fichiers JSON avec les données du jeu.

## Utilisation

1. Ouvrez `index.html` dans un navigateur web.
2. Utilisez la barre de recherche pour rechercher des éléments par nom ou description.
3. Cochez la case "Search by ID" pour rechercher des éléments par ID.
4. Cliquez sur un élément dans les résultats de recherche pour afficher les détails dans une modale.
5. Utilisez le bouton "Load More" pour afficher plus de résultats.

## Code JavaScript

Le code JavaScript est inclus dans le fichier `index.html` et gère les fonctionnalités suivantes :

- Chargement des données des éléments à partir des fichiers JSON.
- Recherche et filtrage des éléments.
- Affichage des résultats de recherche.
- Gestion de la modale pour afficher les détails des éléments.
- Indicateur de chargement pendant la recherche.

## Contribuer

Les contributions sont les bienvenues ! Veuillez suivre les étapes suivantes pour contribuer :

1. Fork le dépôt.
2. Créez une branche pour votre fonctionnalité (`git checkout -b feature/ma-fonctionnalité`).
3. Commitez vos modifications (`git commit -am 'Ajoute une nouvelle fonctionnalité'`).
4. Poussez votre branche (`git push origin feature/ma-fonctionnalité`).
5. Ouvrez une Pull Request.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.
