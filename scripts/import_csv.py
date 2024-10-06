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

def validate_clients_data(clients_df):
    """
    Valide les données des clients pour s'assurer qu'elles contiennent les colonnes nécessaires.
    
    Paramètres :
    clients_df (pandas.DataFrame) : DataFrame contenant les données des clients.
    
    Retourne :
    bool : True si les données sont valides, sinon lève une exception.
    """
    required_columns = ['Client_ID', 'Nom', 'Prénom', 'Email', 'Téléphone', 'Date_Naissance', 'Adresse', 'Consentement_Marketing']
    for column in required_columns:
        if column not in clients_df.columns:
            raise ValueError(f"La colonne requise '{column}' est manquante dans les données des clients.")
    logging.info("Validation des données des clients réussie.")
    return True

def validate_orders_data(commandes_df):
    """
    Valide les données des commandes pour s'assurer qu'elles contiennent les colonnes nécessaires.
    
    Paramètres :
    commandes_df (pandas.DataFrame) : DataFrame contenant les données des commandes.
    
    Retourne :
    bool : True si les données sont valides, sinon lève une exception.
    """
    required_columns = ['Commande_ID', 'Date_Commande', 'Montant_Commande', 'Client_ID']
    for column in required_columns:
        if column not in commandes_df.columns:
            raise ValueError(f"La colonne requise '{column}' est manquante dans les données des commandes.")
    logging.info("Validation des données des commandes réussie.")
    return True

def insert_clients_data(conn, clients_df):
    """
    Insère les données des clients dans la table Clients.
    
    Paramètres :
    conn (sqlite3.Connection) : Objet de connexion à la base de données SQLite.
    clients_df (pandas.DataFrame) : DataFrame contenant les données des clients.
    """
    cursor = conn.cursor()
    try:
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
        logging.info("Insertion des données des clients réussie.")
    except sqlite3.Error as e:
        raise RuntimeError(f"Échec de l'insertion des données des clients : {e}")

def insert_orders_data(conn, commandes_df):
    """
    Insère les données des commandes dans la table Commandes.
    
    Paramètres :
    conn (sqlite3.Connection) : Objet de connexion à la base de données SQLite.
    commandes_df (pandas.DataFrame) : DataFrame contenant les données des commandes.
    """
    cursor = conn.cursor()
    try:
        for index, row in commandes_df.iterrows():
            cursor.execute('''
                INSERT INTO Commandes (Commande_ID, Date_Commande, Montant_Commande, Client_ID)
                VALUES (?, ?, ?, ?)
                ON CONFLICT(Commande_ID, Client_ID) DO UPDATE SET
                Date_Commande = excluded.Date_Commande,
                Montant_Commande = excluded.Montant_Commande
            ''', (row['Commande_ID'], row['Date_Commande'], row['Montant_Commande'], row['Client_ID']))
        logging.info("Insertion des données des commandes réussie.")
    except sqlite3.Error as e:
        raise RuntimeError(f"Échec de l'insertion des données des commandes : {e}")

def main():
    """
    Fonction principale pour gérer le flux de travail de la connexion à la base de données
    et l'insertion des données des clients et des commandes.
    """
    db_path = '../bdd/db.sqlite'
    clients_csv_path = '../_sources/jeu-de-donnees-clients-66fed38c68779376654152.csv'
    commandes_csv_path = '../_sources/jeu-de-donnees-commandes-66fe65226fdb5678959707.csv'
    
    try:
        # Étape 1 : Charger les fichiers CSV dans des DataFrames pandas
        clients_df = pd.read_csv(clients_csv_path)
        commandes_df = pd.read_csv(commandes_csv_path)
        
        # Étape 2 : Valider les données des fichiers CSV
        validate_clients_data(clients_df)
        validate_orders_data(commandes_df)
        
        # Étape 3 : Se connecter à la base de données
        with connect_to_database(db_path) as conn:
            # Étape 4 : Insérer les données des clients dans la base de données
            insert_clients_data(conn, clients_df)
            
            # Étape 5 : Insérer les données des commandes dans la base de données
            insert_orders_data(conn, commandes_df)
            
            # Étape 6 : Commit des changements
            conn.commit()
            logging.info("Toutes les transactions ont été validées avec succès.")
    except (FileNotFoundError, ConnectionError, RuntimeError, IOError, ValueError) as e:
        logging.error(f"Erreur : {e}")
        print(f"Erreur : {e}")
    except Exception as e:
        logging.critical(f"Une erreur inattendue est survenue : {e}")
        print(f"Une erreur inattendue est survenue : {e}")

if __name__ == "__main__":
    main()