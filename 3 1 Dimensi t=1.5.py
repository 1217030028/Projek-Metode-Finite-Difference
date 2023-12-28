import numpy as np
import matplotlib.pyplot as plt

#mendefinisikan variabel
a = 500 #koef. difusivitas termal
panjang = 2500 #panjang plat
waktu = 1.5
node = 2500 #jumlah titik grid

dx = panjang / node
dt = 0.5 * dx**2 / a
t_n = int(waktu / dt)
u = np.zeros(node) + 20

#kondisi batas
u[0] = 0
u[-1] = 100

#visualisasi
fig, ax = plt.subplots()
ax.set_xlabel("x (cm)")
pcm = ax.pcolormesh([u], cmap=plt.cm.jet, vmin=0, vmax=100)
plt.colorbar(pcm, ax=ax)
ax.set_ylim([-2, 3])


counter = 0
while counter < waktu:
    w = u.copy()
    for i in range(1, node-1):
        u[i] = (dt * a * (w[i-1] - 2*w[i] + w[i+1]) / dx**2) + w[i]

    print("t: {:.3f} s, Suhu rata-rata: {:.2f} Celcius".format(counter, np.mean(u)))

    #memperbarui plot
    pcm.set_array([u])
    ax.set_title("Distribusi Suhu pada t: {:.3f} s".format(counter))
    counter += dt
    plt.pause(0.01) #menunda plot untuk animasi
    
plt.show()
