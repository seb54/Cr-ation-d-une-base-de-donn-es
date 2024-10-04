
# Gestion des Clients et Commandes (Base de données SQLite)

## Description

Ce projet implémente un système de gestion de clients et de commandes en utilisant une base de données **SQLite**. Plusieurs fonctionnalités sont incluses pour manipuler les données, telles que l'importation de données à partir de fichiers CSV, l'affichage des clients selon différents critères.

## Fonctionnalités

1. **Importation de données depuis des fichiers CSV** :  
   - `import_csv.py` permet d'importer les données des clients et des commandes à partir de fichiers CSV dans la base de données SQLite.

2. **Affichage des clients ayant consenti au marketing** :  
   - `afficher_clients_marketing.py` affiche les clients ayant consenti à recevoir des communications marketing.

3. **Affichage des commandes d'un client spécifique** :  
   - `commandes_client.py` permet d'afficher toutes les commandes associées à un client en spécifiant son ID.

4. **Calcul du montant total des commandes d'un client** :  
   - `montant_total_commandes_client.py` calcule le montant total des commandes passées par un client spécifique.

5. **Affichage des clients ayant passé des commandes de plus de 100 euros** :  
   - `clients_commandes_100_plus.py` affiche les clients ayant passé des commandes d'un montant supérieur à 100 euros.

6. **Affichage des clients ayant passé des commandes après le 01/01/2023** :  
   - `clients_commandes_2023.py` affiche les clients ayant passé des commandes après une date spécifique.


## Installation

1. **Cloner le repository** :
   ```bash
   git clone https://github.com/votre-repo/gestion-clients-commandes.git
   ```

2. **Installer les dépendances** :
   Ce projet utilise Python. Vous devez installer les bibliothèques requises en exécutant la commande suivante :
   ```bash
   pip install pandas sqlite3 cryptography
   ```

3. **Configuration de la base de données** :  
   Assurez-vous que votre base de données SQLite est initialisée avec les tables `Clients` et `Commandes`. Vous pouvez trouver le script de création des tables dans le fichier `db_structure.sql`.

## Utilisation

### Importer les données des fichiers CSV

Lancez le script `import_csv.py` pour importer les données des fichiers CSV dans la base de données SQLite :
```bash
python import_csv.py
```

### Afficher les clients ayant consenti au marketing

Pour afficher les clients ayant consenti au marketing, lancez :
```bash
python afficher_clients_marketing.py
```

### Afficher les commandes d'un client spécifique

Pour afficher les commandes d'un client spécifique, exécutez :
```bash
python commandes_client.py
```
Un prompt vous demandera de saisir l'ID du client.

### Calculer le montant total des commandes d'un client

Pour calculer le montant total des commandes passées par un client, exécutez :
```bash
python montant_total_commandes_client.py
```

### Afficher les clients ayant passé des commandes de plus de 100 euros

Exécutez le script suivant pour afficher les clients ayant passé des commandes de plus de 100 euros :
```bash
python clients_commandes_100_plus.py
```

### Afficher les clients ayant passé des commandes après le 01/01/2023

Pour afficher les clients ayant passé des commandes après le 01/01/2023, exécutez :
```bash
python clients_commandes_2023.py
```

---

