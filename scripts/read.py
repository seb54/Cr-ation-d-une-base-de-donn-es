import pandas as pd

# Charger le fichier CSV des clients pour vérifier les colonnes
clients_df = pd.read_csv('../_sources/jeu-de-donnees-clients-66fed38c68779376654152.csv')

# Afficher les colonnes présentes dans le fichier CSV
print(clients_df.columns)
