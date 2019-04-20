import numpy as np
import matplotlib.pyplot as plt
import scipy


#Se almacenan los datos de los dos archivos
datos1=np.genfromtxt("signalSuma.dat")
t1=datos1[:,0]
ft1=datos1[:,1]

datos2=np.genfromtxt("signal.dat")
t2=datos2[:,0]
ft2=datos2[:,1]

#Se grafican ambas ondas
plt.figure()
plt.subplot(2,1,1)
plt.plot(t2,ft2)
plt.title("Senal")
plt.xlabel("tiempo")
plt.ylabel("f(t)")

plt.subplot(2,1,2)
plt.plot(t1,ft1,'orange')
plt.title("Suma de las ondas")
plt.xlabel("tiempo")
plt.ylabel("f(t)")


plt.tight_layout()


plt.savefig("ondas.pdf")
