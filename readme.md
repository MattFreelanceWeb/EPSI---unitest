# Projet UnitTest

Ce projet contient des tests unitaires pour le module de traitement de données.

## Objectif

L'objectif de ce projet est de tester les différentes fonctionnalités du module de traitement de données pour s'assurer de leur bon fonctionnement et de leur conformité aux spécifications.

## Structure du Projet

Le projet est organisé comme suit :

- **traitementDeDonnee.py** : Ce fichier contient les fonctions de traitement de données à tester.
- **test_traitementDeDonnee.py** : Ce fichier contient les tests unitaires pour les fonctions du module de traitement de données.
- **client.txt** : Fichier de données client utilisé pour les tests.

## Fonctions Testées

Les fonctionnalités suivantes du module de traitement de données sont testées :

- `get_file_name` : Récupère le nom du fichier à partir d'un chemin complet.
- `isExisteFile` : Vérifie si un fichier existe.
- `isEmptyFile` : Vérifie si un fichier est vide.
- `checkDataNumberForEachLine` : Vérifie si chaque ligne d'un fichier a le bon nombre de données.
- `process_client_data` : Traite les données client à partir d'un fichier spécifié.

## Exécution des Tests

Pour exécuter les tests unitaires, utilisez la commande suivante :

```bash
pytest
```