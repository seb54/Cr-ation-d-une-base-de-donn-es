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

def fetch_clients_with_marketing_consent(conn):
    """
    Récupère les clients qui ont consenti au marketing depuis la base de données.
    
    Paramètres :
    conn (sqlite3.Connection) : Objet de connexion à la base de données SQLite.
    
    Retourne :
    pandas.DataFrame : DataFrame contenant les clients ayant consenti au marketing.
    """
    query = '''
        SELECT Client_ID, Nom, Prenom, Email, Telephone, Date_Naissance, Adresse
        FROM Clients
        WHERE Consentement_Marketing = 1
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
    csv_output_path = '../csv/clients_marketing.csv'
    
    try:
        # Étape 1 : Se connecter à la base de données
        with connect_to_database(db_path) as conn:
            # Étape 2 : Récupérer les clients ayant consenti au marketing
            consent_clients_df = fetch_clients_with_marketing_consent(conn)
            
            # Étape 3 : Afficher les résultats
            if not consent_clients_df.empty:
                print(consent_clients_df)
            else:
                print("Aucun client trouvé avec consentement au marketing.")
            
            # Étape 4 : Exporter les résultats vers un fichier CSV
            export_to_csv(consent_clients_df, csv_output_path)
    except (FileNotFoundError, ConnectionError, RuntimeError, IOError) as e:
        print(f"Erreur : {e}")
    except Exception as e:
        print(f"Une erreur inattendue est survenue : {e}")

if __name__ == "__main__":
    main()