import numpy as np
import matplotlib.pyplot as plt

# Updated Variables
a = 50  # Updated Koefisien Difusivitas Termal
panjang = 500  # Updated Panjang plat to 0.5 m [mm]
waktu = 0  # Waktu simulasi [s]
node = 50  # Jumlah titik grid

dx = panjang / node  # Jarak antar titik grid pada x [mm]
dy = panjang / node  # Jarak antar titik grid pada y [mm]
dt = min(dx**2 / (4 * a), dy**2 / (4 * a))  # Ukuran langkah waktu [s]

t_nodes = int(waktu / dt)  # Jumlah iterasi simulasi
u = np.zeros((node, node)) + 20  # Suhu awal plat [degC]

# Updated Boundary Conditions
u[0, :] = 0  # Suhu tepi kiri
u[-1, :] = 100  # Suhu tepi kanan
u[:, 0] = np.linspace(0, 100, node)  # Suhu tepi bawah (variasi linear)
u[:, -1] = np.linspace(0, 100, node)  # Suhu tepi atas (variasi linear)

# Visualization of initial temperature distribution
fig, ax = plt.subplots()
ax.set_ylabel("y (cm)")
ax.set_xlabel("x (cm)")
pcm = ax.pcolormesh(u, cmap=plt.cm.jet, vmin=0, vmax=100)
plt.colorbar(pcm, ax=ax)

# Iteration over time
for counter in range(t_nodes):
    w = u.copy()
    for i in range(1, node - 1):
        for j in range(1, node - 1):
            dd_ux = (w[i-1, j] - 2 * w[i, j] + w[i+1, j]) / dx**2
            dd_uy = (w[i, j-1] - 2 * w[i, j] + w[i, j+1]) / dy**2
            u[i, j] = dt * a * (dd_ux + dd_uy) + w[i, j]

    t_mean = np.mean(u)

    # Update the plot
    pcm.set_array(u.ravel())
    ax.set_title(f"Distribusi Suhu t: {counter * dt:.3f} s, suhu rata-rata = {t_mean:.2f}")

plt.show()
