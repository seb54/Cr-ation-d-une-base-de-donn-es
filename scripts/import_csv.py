import sqlite3
import pandas as pd

# Connexion à la base de données SQLite
conn = sqlite3.connect('../bdd/db.sqlite')
cursor = conn.cursor()

# Charger les fichiers CSV dans des DataFrames pandas
clients_df = pd.read_csv('../_sources/jeu-de-donnees-clients-66fed38c68779376654152.csv')
commandes_df = pd.read_csv('../_sources/jeu-de-donnees-commandes-66fe65226fdb5678959707.csv')

# Insertion des données dans la table Clients
for index, row in clients_df.iterrows():
    cursor.execute('''
        INSERT INTO Clients (Client_ID, Nom, Prenom, Email, Telephone, Date_Naissance, Adresse, Consentement_Marketing)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?) 
        ON CONFLICT(Client_ID) DO UPDATE SET
        Nom = excluded.Nom,
        Prenom = excluded.Prenom,
        Email = excluded.Email,
        Telephone = excluded.Telephone,
        Date_Naissance = excluded.Date_Naissance,
        Adresse = excluded.Adresse,
        Consentement_Marketing = excluded.Consentement_Marketing
    ''', (row['Client_ID'], row['Nom'], row['Prénom'], row['Email'], row['Téléphone'], row['Date_Naissance'], row['Adresse'], row['Consentement_Marketing']))

# Insertion des données dans la table Commandes
for index, row in commandes_df.iterrows():
    cursor.execute('''
        INSERT INTO Commandes (Commande_ID, Date_Commande, Montant_Commande, Client_ID)
        VALUES (?, ?, ?, ?) 
        ON CONFLICT(Commande_ID, Client_ID) DO UPDATE SET
        Date_Commande = excluded.Date_Commande,
        Montant_Commande = excluded.Montant_Commande
    ''', (row['Commande_ID'], row['Date_Commande'], row['Montant_Commande'], row['Client_ID']))

# Commit des changements et fermeture de la connexion
conn.commit()
conn.close()

print("Importation terminée avec succès.")
