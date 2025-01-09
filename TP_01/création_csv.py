import pandas as pd

# Créer un dictionnaire avec les données du fichier CSV
data = {
    'timestamp': [
        '2025-01-05 12:34:56', 
        '2025-01-05 12:35:01', 
        '2025-01-05 12:35:05', 
        '2025-01-05 12:35:10', 
        '2025-01-05 12:36:00'
    ],
    'ip_address': [
        '192.168.1.10', 
        '192.168.1.11', 
        '192.168.1.11', 
        '192.168.1.11', 
        '192.168.1.12'
    ],
    'status': [
        'success', 
        'failed', 
        'failed', 
        'failed', 
        'success'
    ]
}

# Créer un DataFrame pandas à partir du dictionnaire
df = pd.DataFrame(data)

# Sauvegarder le DataFrame en tant que fichier CSV
df.to_csv('logs.csv', index=False)

print("Le fichier logs.csv a été créé avec succès.")
print (df)










