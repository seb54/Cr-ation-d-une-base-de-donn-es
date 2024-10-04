import sqlite3
import pandas as pd

# Connexion à la base de données SQLite
conn = sqlite3.connect('../bdd/db.sqlite')

# Requête pour sélectionner les clients ayant consenti au marketing
query = '''
    SELECT Client_ID, Nom, Prenom, Email, Telephone, Date_Naissance, Adresse
    FROM Clients
    WHERE Consentement_Marketing = 1
'''

# Exécution de la requête et récupération des résultats dans un DataFrame pandas
consent_clients_df = pd.read_sql_query(query, conn)

# Affichage des résultats
print(consent_clients_df)

# Fermeture de la connexion à la base de données
conn.close()
