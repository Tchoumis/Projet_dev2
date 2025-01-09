import pandas as pd
import matplotlib.pyplot as plt

# II. Charger le fichier CSV
# Remplacez 'incidents_securite.csv' par le chemin vers votre fichier

df = pd.read_csv('C:\\Users\\diginamic\\Projet_dev2\\TP_02\\incidents_securite.csv')


# III. Explorer les données
# Afficher les premières lignes
print("Premières lignes des données :")
print(df.head())
print("***************************************************************")
print(df.info())


#  Obtenir des informations sur les colonnes
print("***************************************************************")
print("\nInformations sur les colonnes :")
print(df.info())

# Résumé statistique
print("***************************************************************")
print("\nRésumé statistique :")
print(df.describe())


print("***************************************************************")
# IV. Nettoyer les données
# Vérifier les valeurs manquantes
print("\nValeurs manquantes par colonne :")
print(df.isnull().sum())


print("***************************************************************")
# Remplacer les valeurs manquantes par 'Inconnu'
df.fillna('Inconnu', inplace=True) #Remplir les valeurs manquantes



# V Analyser les données
# Nombre d'incidents par type
incidents_par_type = df['Type_Incident'].value_counts()
print("\nNombre d'incidents par type :")
print(incidents_par_type)

print("***************************************************************")

#  Distribution par date
df['Date'] = pd.to_datetime(df['Date'])


# Nombre d'incidents par mois
incidents_par_mois = df.groupby(df['Date'].dt.to_period('M')).size()
print("\nNombre d'incidents par mois :")
print(incidents_par_mois)

print("***************************************************************")

# Fréquence des incidents par lieu
incidents_par_lieu = df['Lieu'].value_counts()
print("\nFréquence des incidents par lieu :")
print(incidents_par_lieu)

# Visualiser les données
print("***************************************************************")

#A. Diagramme en barres pour les types d'incidents
# incidents_par_type.plot(kind='bar', title="Nombre d'incidents par type")
# plt.xlabel('Type d\'incident')
# plt.ylabel('Nombre d\'incidents')
# plt.show()
# 
# 
# 
#B. Évolution des incidents dans le temps
# incidents_par_mois.plot(title='Évolution des incidents dans le temps')
# plt.xlabel('Temps (Année, Mois)')
# plt.ylabel('Nombre d\'incidents')
# plt.show()


# Ajuster la taille
plt.figure(figsize=(10, 6))  # Modifier la taille selon vos besoins
incidents_par_type.plot(kind='bar', title="Nombre d'incidents par type")
plt.xlabel('Type d\'incident')
plt.ylabel('Nombre d\'incidents')
plt.xticks(rotation=45)  # Si les étiquettes de l'axe X sont longues, les faire pivoter
plt.tight_layout()  # Ajuste les espacements pour éviter que les étiquettes ne se chevauchent
plt.show()


# Ajuster la taille
plt.figure(figsize=(10, 6))  # Modifier la taille selon vos besoins
incidents_par_mois.plot(title='Évolution des incidents dans le temps')
plt.xlabel('Temps (Année, Mois)')
plt.ylabel('Nombre d\'incidents')
plt.xticks(rotation=45)  # Rotation des étiquettes si nécessaire
plt.tight_layout()  # Ajuste l'espacement automatique
plt.show()


# C. Exporter les résultats dans un fichier CSV
df.to_csv('resultats_analyse.csv', index=False)













































