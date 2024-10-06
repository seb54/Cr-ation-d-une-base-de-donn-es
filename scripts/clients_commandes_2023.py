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

def fetch_clients_with_orders_after_2023(conn):
    """
    Récupère les clients ayant passé des commandes après le 01/01/2023 depuis la base de données.
    
    Paramètres :
    conn (sqlite3.Connection) : Objet de connexion à la base de données SQLite.
    
    Retourne :
    pandas.DataFrame : DataFrame contenant les clients ayant passé des commandes après le 01/01/2023.
    """
    query = '''
        SELECT C.Client_ID, C.Nom, C.Prenom, C.Email, Com.Commande_ID, Com.Date_Commande, Com.Montant_Commande
        FROM Clients C
        JOIN Commandes Com ON C.Client_ID = Com.Client_ID
        WHERE Com.Date_Commande > '2023-01-01'
    '''
    try:
        df = pd.read_sql_query(query, conn)
        return df
    except sqlite3.Error as e:
        raise RuntimeError(f"Échec de l'exécution de la requête : {e}")

def export_to_csv(df, file_path):
    """
    Exporte le DataFrame vers un fichier CSV.
    
    Paramètres :
    df (pandas.DataFrame) : Le DataFrame à exporter.
    file_path (str) : Le chemin pour enregistrer le fichier CSV.
    """
    try:
        df.to_csv(file_path, index=False, encoding='utf-8')
        print(f"Données exportées avec succès vers {file_path}")
    except Exception as e:
        raise IOError(f"Échec de l'exportation des données vers CSV : {e}")

def main():
    """
    Fonction principale pour gérer le flux de travail de la connexion à la base de données,
    la récupération des données des clients et l'exportation vers un fichier CSV.
    """
    db_path = '../bdd/db.sqlite'
    csv_output_path_orders = '../csv/clients_commandes_apres_2023.csv'
    
    try:
        # Étape 1 : Se connecter à la base de données
        with connect_to_database(db_path) as conn:
            # Étape 2 : Récupérer les clients ayant passé des commandes après le 01/01/2023
            orders_after_2023_clients_df = fetch_clients_with_orders_after_2023(conn)
            
            # Étape 3 : Afficher les résultats
            if not orders_after_2023_clients_df.empty:
                print("Clients ayant passé des commandes après le 01/01/2023 :")
                print(orders_after_2023_clients_df)
            else:
                print("Aucun client n'a passé de commande après le 01/01/2023.")
            
            # Étape 4 : Exporter les résultats vers un fichier CSV
            export_to_csv(orders_after_2023_clients_df, csv_output_path_orders)
    except (FileNotFoundError, ConnectionError, RuntimeError, IOError) as e:
        print(f"Erreur : {e}")
    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")

if __name__ == "__main__":
    main()