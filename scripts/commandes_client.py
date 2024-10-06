import sqlite3
import pandas as pd
import os

def connect_to_database(db_path):
    """
    Établit une connexion à la base de données SQLite.
    
    Paramètres :
    db_path (str) : Le chemin vers le fichier de la base de données SQLite.
    
    Retourne :
    sqlite3.Connection : Objet de connexion à la base de données SQLite.
    """
    if not os.path.exists(db_path):
        raise FileNotFoundError(f"Fichier de base de données non trouvé à : {db_path}")
    try:
        conn = sqlite3.connect(db_path)
        return conn
    except sqlite3.Error as e:
        raise ConnectionError(f"Échec de la connexion à la base de données : {e}")

def fetch_client_orders(conn, client_id):
    """
    Récupère les commandes d'un client spécifique depuis la base de données.
    
    Paramètres :
    conn (sqlite3.Connection) : Objet de connexion à la base de données SQLite.
    client_id (int) : L'ID du client dont on souhaite récupérer les commandes.
    
    Retourne :
    pandas.DataFrame : DataFrame contenant les commandes du client spécifique.
    """
    query = '''
        SELECT Commande_ID, Date_Commande, Montant_Commande
        FROM Commandes
        WHERE Client_ID = ?
    '''
    try:
        df = pd.read_sql_query(query, conn, params=(client_id,))
        return df
    except sqlite3.Error as e:
        raise RuntimeError(f"Échec de l'exécution de la requête : {e}")

def main():
    """
    Fonction principale pour gérer le flux de travail de la connexion à la base de données
    et l'affichage des commandes d'un client spécifique.
    """
    db_path = '../bdd/db.sqlite'
    
    try:
        # Étape 1 : Se connecter à la base de données
        with connect_to_database(db_path) as conn:
            # Étape 2 : Demander l'ID du client à l'utilisateur
            client_id = int(input("Entrez l'ID du client : "))
            
            # Étape 3 : Récupérer les commandes du client
            client_orders_df = fetch_client_orders(conn, client_id)
            
            # Étape 4 : Afficher les résultats
            if client_orders_df.empty:
                print(f"Aucune commande trouvée pour le client avec l'ID {client_id}.")
            else:
                print(f"Commandes pour le client avec l'ID {client_id} :")
                print(client_orders_df)
    except (FileNotFoundError, ConnectionError, RuntimeError, IOError) as e:
        print(f"Erreur : {e}")
    except ValueError:
        print("Erreur : L'ID du client doit être un nombre entier valide.")
    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")

if __name__ == "__main__":
    main()