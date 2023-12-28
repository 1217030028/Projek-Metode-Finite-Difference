import numpy as np
import matplotlib.pyplot as plt

# Mendefinisikan variabel
a = 500  # Koef. difusivitas termal
panjang = 2500  # Panjang plat
waktu = 1.5
node = 2500  # Jumlah titik grid

dx = panjang / node
dt = 0.5 * dx**2 / a
t_n = int(waktu / dt)
u = np.zeros(node) + 20

# Kondisi batas
u[0] = 0
u[-1] = 100

# Simpan suhu rata-rata pada setiap iterasi waktu
suhu_rata_rata = []

counter = 0
while counter < waktu:
    w = u.copy()
    for i in range(1, node - 1):
        u[i] = (dt * a * (w[i - 1] - 2 * w[i] + w[i + 1]) / dx**2) + w[i]

    suhu_rata_rata.append(np.mean(u))

    print("t: {:.3f} s, Suhu rata-rata: {:.2f} Celcius".format(counter, suhu_rata_rata[-1]))

    counter += dt

# Pastikan panjang array waktu dan suhu_rata_rata sama
panjang_minimal = min(len(np.arange(0, waktu, dt)), len(suhu_rata_rata))
waktu_array = np.arange(0, waktu, dt)[:panjang_minimal]

# Print lengths of arrays for debugging
print("Length of waktu_array:", len(waktu_array))
print("Length of suhu_rata_rata:", len(suhu_rata_rata))

# Plot hubungan suhu rata-rata terhadap waktu
plt.plot(waktu_array, suhu_rata_rata[:panjang_minimal])
plt.xlabel("Waktu (s)")
plt.ylabel("Suhu Rata-rata (Celcius)")
plt.title("Hubungan Suhu Rata-rata terhadap Waktu")
plt.show()
