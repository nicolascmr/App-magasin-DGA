# Application-magasin-DGA

Ce projet est une mini-application de gestion de stocks réalisée dans le cadre d'une candidature pour la DGA.

## Instructions pour le lancement de l'application

### 1. Se placer à la racine du projet pour l'ensemble de la procédure

### 2. Créer un environnement virtuel (si nécessaire sinon passer à l'étape 4) :

```virtualenv -p python3 venv```

### 3. Utiliser l'environnement virtuel :

**Windows**

```.\venv\Scripts\activate```

**Linux**

```source venv/bin/activate```

### 4. Installer les packages avec Pip : 

```pip install -r requirements.txt```

### 5. Intialiser l'application avec un jeu de données par défaut

```flask init-db```

### 6. Lancer le site web de manière locale 

```flask run```

### 7. Se connecter au site web

Aller sur un navigateur et se rendre à l'adresse suivante http://127.0.0.1:5000

## Choix techniques de l'application 

### Technologies utilisées

Pour réaliser cette application web, j'ai choisi d'utiliser le framework Flask au sein de l'écosystème Python. J'ai privilégié cette solution par rapport à d'autres frameworks comme Django, car ces derniers sont souvent trop complets et imposants pour un projet de cette envergure. Flask est un outil léger qui permet de répondre précisément aux besoins d'une mini-application sans ajouter de complexité inutile, tout en restant très simple d'utilisation.

Concernant la gestion des données, j'ai utilisé le système SQLite comme demandé dans le cahier des charges. Je l'ai associé à l'outil SQLAlchemy pour pouvoir communiquer en Python avec cette base de données relationnelle sans avoir à utiliser de requêtes SQL brutes. Ce choix simplifie grandement la maintenance du code et permettrait de changer plus facilement de moteur de base de données si nécessaire à l'avenir.

### Limites connues

L'application présente actuellement quelques limites, notamment le fait qu'elle soit uniquement accessible de manière locale et non en ligne. C'est pour cette raison qu'un système de connexion utilisateur n'a pas été mis en place. Une telle fonctionnalité serait pourtant très utile si l'application devait gérer des aspects plus complexes, comme le suivi de différents stocks sur plusieurs sites ou les procédures de renouvellement des marchandises.

La mise en place d'une authentification permettrait également de donner à chaque employé des accès différents selon ses responsabilités. Pour le moment, le site fonctionne donc sans restriction pour n'importe quel employé local afin de lui permettre d'accéder directement au stock des produits du magasin.

### Améliorations possibles 

Plusieurs perspectives d'évolution sont envisageables pour enrichir cette application. Sur le plan de l'interface, la page d'accueil pourrait accueillir de nouveaux boutons ou un tableau de bord pour rediriger l'utilisateur vers différentes sections du site de manière plus ergonomique.

De plus, si l'objectif devient la gestion de plusieurs points de vente, il serait pertinent de mettre en place un système de sélection de magasin. Cela impliquerait d'ajouter une table dédiée dans la base de données et de créer une association entre les magasins et les produits. Une telle évolution permettrait de visualiser et de gérer les stocks spécifiquement pour chaque site avant toute opération.

### Amélioration réalisée 

En plus des fonctionnalités attendues, j'ai ajouté un outil permettant d'exporter les produits au format CSV. Cette option permet de télécharger la liste complète des stocks ou une sélection précise basée sur les résultats de la barre de recherche.

L'implémentation de cette fonctionnalité est particulièrement pertinente pour un outil de gestion car elle permet à l'utilisateur d'exploiter les données en dehors de l'application. Cela permet la réalisation de schémas ou la conservation d'un historique de l'état des stocks à un instant donné.