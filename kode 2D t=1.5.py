import numpy as np
import matplotlib.pyplot as plt

# Mendefinisikan Variabel
a = 50  # Koefisien Difusivitas Termal baru
panjang = 500  # Panjang plat baru [mm] (0.5 m)
waktu = 1.5  # Waktu simulasi [s]
node = 50  # Jumlah titik grid

dx = panjang / node  # Jarak antar titik grid pada x [mm]
dy = panjang / node  # Jarak antar titik grid pada y [mm]
dt = min(dx**2 / (4 * a), dy**2 / (4 * a))  # Ukuran langkah waktu [s]

u = np.zeros((node, node))  # Suhu awal plat [degC]

# Kondisi batas baru
u[0, :] = 0  # Suhu tepi kiri
u[-1, :] = 100  # Suhu tepi kanan
u[:, 0] = np.linspace(0, 100, node)  # Suhu tepi bawah (variasi linear)
u[:, -1] = np.linspace(0, 100, node)  # Suhu tepi atas (variasi linear)

# Simulasi
counter = 0
while counter < waktu:
    w = u.copy()
    for i in range(1, node - 1):
        for j in range(1, node - 1):
            dd_ux = (w[i-1, j] - 2 * w[i, j] + w[i+1, j]) / dx**2
            dd_uy = (w[i, j-1] - 2 * w[i, j] + w[i, j+1]) / dy**2
            u[i, j] = dt * a * (dd_ux + dd_uy) + w[i, j]

    counter += dt

# Visualisasi distribusi suhu pada t = 1.5 s
fig, ax = plt.subplots()
pcm = ax.pcolormesh(u, cmap=plt.cm.jet, vmin=0, vmax=100)
plt.colorbar(pcm, ax=ax)
ax.set_ylabel("y (cm)")
ax.set_xlabel("x (cm)")
t_mean = np.mean(u)
ax.set_title(f"Distribusi Suhu t: {counter:.3f} s, Suhu rata-rata = {t_mean:.3f}")
plt.show()
