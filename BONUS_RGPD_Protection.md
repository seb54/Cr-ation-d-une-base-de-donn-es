# Identification des Données Sensibles selon le RGPD et Solutions de Protection

## 1. Introduction

Le **RGPD** (Règlement Général sur la Protection des Données) impose aux entreprises et aux organisations la responsabilité de protéger les données personnelles identifiables (DPI) des individus. Dans le cadre de ce projet, nous identifions les données sensibles présentes dans notre base de données et proposons des solutions conformes au RGPD pour assurer leur protection, telles que le chiffrement et la pseudonymisation.

## 2. Identification des Données Sensibles

Les **données sensibles** sont définies par le RGPD comme toute information permettant d'identifier une personne ou de porter atteinte à sa vie privée. Voici les types de données sensibles que nous avons identifiées dans notre base de données :

- **Nom et Prénom** : informations permettant l'identification directe.
- **Email** : information personnelle utilisée pour la communication.
- **Numéro de téléphone** : permet une identification et un contact direct.
- **Adresse** : localisation physique des personnes.
- **Consentement Marketing** : informations sur le choix des utilisateurs de recevoir des communications commerciales.

### Exemple de champs dans notre base de données SQLite :
- Nom : `Nom`
- Prénom : `Prenom`
- Email : `Email`
- Téléphone : `Telephone`
- Adresse : `Adresse`
- Consentement au Marketing : `Consentement_Marketing`

## 3. Solutions pour Protéger les Données Sensibles

### 3.1 Chiffrement des Données

Le **chiffrement** consiste à rendre les données illisibles sans une clé de déchiffrement appropriée. Il est recommandé de chiffrer les données sensibles telles que les emails, les numéros de téléphone, et les adresses. Voici un exemple de chiffrement en Python utilisant la bibliothèque `cryptography` :

```python
from cryptography.fernet import Fernet

# Générer une clé de chiffrement (à stocker de manière sécurisée)
key = Fernet.generate_key()
cipher_suite = Fernet(key)

# Exemple de chiffrement d'un email
email = "julien.clement@gmail.com"
encrypted_email = cipher_suite.encrypt(email.encode())
```

### 3.2 Pseudonymisation des Données

La **pseudonymisation** consiste à remplacer les informations personnelles identifiables par des pseudonymes afin de réduire les risques en cas de violation des données. Cela permet d'assurer qu'une personne ne puisse pas être identifiée directement à partir des données stockées.

Exemple de pseudonymisation des noms avec un hachage SHA-256 :

```python
import hashlib

def pseudonymize(value):
    return hashlib.sha256(value.encode()).hexdigest()

nom = "Julien Clement"
pseudonymized_nom = pseudonymize(nom)
print(pseudonymized_nom)
```

### 3.3 Anonymisation des Données

L'**anonymisation** est un processus irréversible où les données ne peuvent plus être associées à une personne spécifique. Cela est particulièrement utile lorsque les informations personnelles n'ont plus besoin d'être conservées après utilisation.

### 3.4 Gestion des Accès

Pour protéger les données sensibles, il est essentiel de limiter l'accès aux informations personnelles. Il est recommandé de mettre en place un système de **contrôle d'accès basé sur les rôles** (RBAC) afin que seules les personnes autorisées puissent accéder à certaines données.

### 3.5 Suppression des Données (Droit à l'oubli)

En vertu du **droit à l'oubli** (Article 17 du RGPD), les utilisateurs peuvent demander la suppression complète de leurs données personnelles. Il est important de développer des mécanismes pour supprimer ou anonymiser les données à la demande.

## 4. Conclusion

L'identification et la protection des données sensibles sont essentielles pour respecter le RGPD et garantir la confidentialité des utilisateurs. En mettant en place des solutions de **chiffrement**, de **pseudonymisation**, et de **contrôle d'accès**, nous réduisons les risques d'exposition des données sensibles et assurons une meilleure protection en cas de violation de la sécurité.

### Références

- [CNIL - Le RGPD expliqué](https://www.cnil.fr/fr/reglement-europeen-protection-donnees)
- [Documentation sur l'anonymisation](https://www.cnil.fr/fr/technologies/lanonymisation-de-donnees-personnelles)

