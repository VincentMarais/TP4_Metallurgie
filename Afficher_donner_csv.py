import matplotlib.pyplot as plt
import pandas as pd

# Lire les données CSV dans un DataFrame
data = pd.read_csv("donnees.csv")

# Extraire les colonnes x et y du DataFrame
x = data["x"]
y = data["y"]

# Créer un graphique à partir des données
plt.figure(figsize=(8, 6))
plt.plot(x, y, label="Données")
plt.xlabel("Axe X")
plt.ylabel("Axe Y")
plt.title("Tracé de données à partir d'un fichier CSV")
plt.legend()
plt.grid(True)

# Afficher le graphique
plt.show()
