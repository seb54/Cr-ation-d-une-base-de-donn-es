import sqlite3
import pandas as pd

# Connexion à la base de données SQLite
conn = sqlite3.connect('../bdd/db.sqlite')

# Fonction pour afficher les commandes d'un client spécifique
def afficher_commandes_client(client_id):
    # Requête SQL pour sélectionner les commandes du client
    query = '''
        SELECT Commande_ID, Date_Commande, Montant_Commande
        FROM Commandes
        WHERE Client_ID = ?
    '''
    
    # Exécution de la requête avec le client_id passé en paramètre
    commandes_df = pd.read_sql_query(query, conn, params=(client_id,))
    
    # Affichage des résultats
    if commandes_df.empty:
        print(f"Aucune commande trouvée pour le client avec l'ID {client_id}.")
    else:
        print(f"Commandes pour le client avec l'ID {client_id} :")
        print(commandes_df)

# Exemple d'utilisation : Afficher les commandes pour un client avec l'ID 1
client_id = int(input("Entrez l'ID du client : "))
afficher_commandes_client(client_id)

# Fermeture de la connexion à la base de données
conn.close()
