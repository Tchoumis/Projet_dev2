**TP_01**
```sh
pip install pandas
```
**TP_02**
Installez matplotlib
```sh
pip install pandas
```
```sh
pip install matplotlib
```

Si un environnement virtuel, activez-le d'abord
Exemple pour un environnement virtuel sur Windows :

```sh
venv\Scripts\activate
```

Désactiver l'environnement virtuel
```sh
deactivate
```

Mise en place de environnement virtuel
```sh
python -m venv venv
```
Avctiver l'environnement virtuel
```sh
venv\Scripts\activate
```
Utiliser des chaînes brutes (raw string) avec un préfixe r
```sh
df = pd.read_csv(r'C:\Users\diginamic\Projet_dev2\TP_02\incidents_securite.csv')
```
Utiliser des doubles barres obliques inverses (\\)
Pour éviter l'interprétation des séquences d'échappement
```sh
df = pd.read_csv('C:\\Users\\diginamic\\Projet_dev2\\TP_02\\incidents_securite.csv')
```
Utiliser des barres obliques simples (/)
```sh
df = pd.read_csv('C:/Users/diginamic/Projet_dev2/TP_02/incidents_securite.csv')
```
