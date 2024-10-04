import sqlite3

# Connexion à la base de données SQLite
conn = sqlite3.connect('../bdd/db.sqlite')

# Fonction pour calculer le montant total des commandes d'un client spécifique
def montant_total_commandes_client(client_id):
    # Requête SQL pour calculer la somme des montants des commandes du client
    query = '''
        SELECT SUM(Montant_Commande) as Montant_Total
        FROM Commandes
        WHERE Client_ID = ?
    '''
    
    # Exécution de la requête avec le client_id passé en paramètre
    cursor = conn.cursor()
    cursor.execute(query, (client_id,))
    
    # Récupérer le résultat de la requête
    result = cursor.fetchone()
    montant_total = result[0] if result[0] is not None else 0
    
    print(f"Le montant total des commandes pour le client avec l'ID {client_id} est : {montant_total:.2f} €")

# Appel de la fonction pour le client avec l'ID 61
montant_total_commandes_client(61)

# Fermeture de la connexion à la base de données
conn.close()
