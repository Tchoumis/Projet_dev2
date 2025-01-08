# Les préréquis:

**TP_01**

`pip install pandas`



**TP_02**

`pip install pandas`

`pip install matplotlib`


# Si vous utilisez un environnement virtuel, activez-le d'abord
# Exemple pour un environnement virtuel sur Windows :
`venv\Scripts\activate`

# Désactiver l'environnement virtuel
`deactivate`


# Mise en place de environnement virtuel

`python -m venv venv`


# Avctiver l'environnement virtuel
`venv\Scripts\activate`

# Ensuite, installez matplotlib

# Utiliser des chaînes brutes (raw string) avec un préfixe r
df = pd.read_csv(r'C:\Users\diginamic\Projet_dev2\TP_02\incidents_securite.csv')

# Utiliser des doubles barres obliques inverses (\\)
Pour éviter l'interprétation des séquences d'échappement
`df = pd.read_csv('C:\\Users\\diginamic\\Projet_dev2\\TP_02\\incidents_securite.csv')`

# Utiliser des barres obliques simples (/)

`df = pd.read_csv('C:/Users/diginamic/Projet_dev2/TP_02/incidents_securite.csv')`
