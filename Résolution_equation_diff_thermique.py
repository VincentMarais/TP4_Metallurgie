import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Paramètres
Lx, Ly = 100, 100  # dimensions du domaine
D = 50.2  # coefficient de diffusion
dx = 2.0  # pas spatial
dt = 0.01  # pas temporel
n_steps = 1000  # nombre d'étapes temporelles

# Initialisation
T = np.zeros((Lx, Ly))  # température initiale
source_x, source_y = Lx // 2, Ly//2  # position de la source de chaleur
T[source_x, source_y] = 50  # température à la source

# Création de la figure
fig, ax = plt.subplots()
cax = ax.imshow(T, origin='lower', cmap='hot', interpolation='gaussian')
cbar = fig.colorbar(cax, label='Température')
txt = plt.text(5, 5, f'Temps = 0.00s', color='white')

def update(num):
    global T
    for step in range(10):  # Mettre à jour 10 fois pour une meilleure animation
        T_new = T.copy()
        for i in range(1, Lx-1):
            for j in range(1, Ly-1):
                T_new[i, j] = T[i, j] + D * dt * ((T[i+1, j] - 2*T[i, j] + T[i-1, j]) / dx**2 + (T[i, j+1] - 2*T[i, j] + T[i, j-1]) / dx**2)
        T = T_new

    cax.set_data(T)
    cax.autoscale()
    txt.set_text(f'Temps = {num*10*dt:.2f}s')
    return cax, txt

ani = animation.FuncAnimation(fig, update, frames=n_steps//10, repeat=False)
plt.show()
