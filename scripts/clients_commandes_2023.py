import sqlite3
import pandas as pd

# Connexion à la base de données SQLite
conn = sqlite3.connect('../bdd/db.sqlite')

# Requête SQL pour sélectionner les clients ayant passé des commandes après le 01/01/2023
query = '''
    SELECT C.Client_ID, C.Nom, C.Prenom, C.Email, Com.Commande_ID, Com.Date_Commande, Com.Montant_Commande
    FROM Clients C
    JOIN Commandes Com ON C.Client_ID = Com.Client_ID
    WHERE Com.Date_Commande > '2023-01-01'
'''

# Exécution de la requête et récupération des résultats dans un DataFrame pandas
clients_commandes_2023_df = pd.read_sql_query(query, conn)

# Affichage des résultats
if clients_commandes_2023_df.empty:
    print("Aucun client n'a passé de commande après le 01/01/2023.")
else:
    print("Clients ayant passé des commandes après le 01/01/2023 :")
    print(clients_commandes_2023_df)

# Fermeture de la connexion à la base de données
conn.close()
