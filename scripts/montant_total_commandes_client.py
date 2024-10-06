import sqlite3
import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

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
        logging.info("Connexion à la base de données établie avec succès.")
        return conn
    except sqlite3.Error as e:
        raise ConnectionError(f"Échec de la connexion à la base de données : {e}")

def montant_total_commandes_client(conn, client_id):
    """
    Calcule le montant total des commandes d'un client spécifique.
    
    Paramètres :
    conn (sqlite3.Connection) : Objet de connexion à la base de données SQLite.
    client_id (int) : L'ID du client dont on souhaite calculer le montant total des commandes.
    
    Retourne :
    float : Le montant total des commandes du client.
    """
    query = '''
        SELECT SUM(Montant_Commande) as Montant_Total
        FROM Commandes
        WHERE Client_ID = ?
    '''
    try:
        cursor = conn.cursor()
        cursor.execute(query, (client_id,))
        result = cursor.fetchone()
        montant_total = result[0] if result[0] is not None else 0.0
        logging.info(f"Montant total des commandes pour le client ID {client_id} est : {montant_total:.2f} €")
        return montant_total
    except sqlite3.Error as e:
        raise RuntimeError(f"Échec de l'exécution de la requête : {e}")

def main():
    """
    Fonction principale pour gérer le calcul du montant total des commandes d'un client spécifique.
    """
    db_path = '../bdd/db.sqlite'
    
    try:
        # Étape 1 : Se connecter à la base de données
        with connect_to_database(db_path) as conn:
            # Étape 2 : Calculer le montant total des commandes d'un client spécifique
            client_id = int(input("Entrez l'ID du client : "))
            montant_total = montant_total_commandes_client(conn, client_id)
            print(f"Le montant total des commandes pour le client avec l'ID {client_id} est : {montant_total:.2f} €")
    except (FileNotFoundError, ConnectionError, RuntimeError, IOError, ValueError) as e:
        logging.error(f"Erreur : {e}")
        print(f"Erreur : {e}")
    except Exception as e:
        logging.critical(f"Une erreur inattendue est survenue : {e}")
        print(f"Une erreur inattendue est survenue : {e}")

if __name__ == "__main__":
    main()