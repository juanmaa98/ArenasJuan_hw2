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

	return F2,freq2

F1,freq1=TFourier(ft1,t1)
F2,freq2=TFourier(ft2,t2)

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

fourier = np.fft.fft(ft2)
freq=np.fft.fftfreq(len(ft2),d=t2[10]-t2[9])

plt.figure()
plt.subplot(211)
plt.plot(freq[0:int(len(t2)/2-1)],fourier[0:int(len(t2)/2-1)],"-",label="fftfreq")
plt.subplot(212)
plt.plot(freq1,F1,'orange')
plt.title("Suma de las ondas")
plt.xlabel("frecuencia")
plt.ylabel("F")

plt.show()


