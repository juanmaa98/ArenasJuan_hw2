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

#Definicion propia de la transformada de fourier
def TFourier(ft,t):
	N=len(ft)
	dt=t[10]-t[9]
	F=np.zeros((N),complex)
	freq=np.zeros((N),float)
	for n in range(0,N):
		for k in range(0,N):
			F[n]+=ft[k]*np.exp(-1j*2*np.pi*k*n/N)
		freq[n]=n/(k*dt)
	F2=F[0:int(N/2)]*2/np.mean(F)
	freq2=freq[0:int(N/2)]

	return F2,freq2,dt

F1,freq1,dt1=TFourier(ft1,t1)
F2,freq2,dt2=TFourier(ft2,t2)

#Se grafican ambas transformadas de fourier
plt.figure()
plt.subplot(2,1,1)
plt.plot(freq2,F2)
plt.title("Senal")
plt.xlabel("frecuencia")
plt.ylabel("F")

plt.subplot(2,1,2)
plt.plot(freq1,F1,'orange')
plt.title("Suma de las ondas")
plt.xlabel("frecuencia")
plt.ylabel("F")

plt.tight_layout()

plt.savefig("transformadasOndas.pdf")
print("Se uso la implementacion propia de la transformada de fourier")

#Espectograma

plt.figure()
plt.specgram(ft1,Fs=int(1/dt1))
plt.xlabel("tiempo")
plt.ylabel("frecuencia")
plt.title("Espectrograma de la suma de ondas")
plt.savefig("EspectroSum.pdf")

plt.figure()
plt.specgram(ft2,Fs=int(1/dt2))
plt.xlabel("tiempo")
plt.ylabel("frecuencia")
plt.title("Espectrograma de las ondas por separado")
plt.savefig("EspectroSignal.pdf")

#Terremoto

ft=np.genfromtxt("temblor.txt")
N=len(ft)
Fs=100
dt=1.0/Fs
t=np.linspace(0,dt*N,N)

plt.figure()
plt.plot(t,ft)
plt.title("Temblor")
plt.xlabel("tiempo [s]")
plt.ylabel("Amplitud")

plt.savefig("temblor.pdf")
