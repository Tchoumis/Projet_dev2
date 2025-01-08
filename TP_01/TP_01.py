
import pandas as pd

# Charger les données depuis le fichier CSV
df = pd.read_csv('logs.csv')

# Filtrer uniquement les connexions échouées
failed_logs = df[df['status'] == 'failed']

# Compter le nombre de tentatives échouées par adresse IP
failed_counts = failed_logs.groupby('ip_address').size()

# Convertir le résultat en DataFrame et renommer la colonne
failed_counts_df = failed_counts.reset_index(name='failed_count')

# Détecter les IPs avec plus de 2 tentatives échouées
suspect_ips = failed_counts_df[failed_counts_df['failed_count'] > 2]

# Réinitialiser l'index pour commencer à 1
suspect_ips.index = range(1, len(suspect_ips) + 1)

# Afficher le résultat
print("Adresses IP suspectes :")
print(suspect_ips)
