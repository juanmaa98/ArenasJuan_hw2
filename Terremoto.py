import numpy as np
import matplotlib.pyplot as plt
import scipy

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

#Transformada de fourier usando scipy

F=np.fft.fft(ft)
freq=np.fft.fftfreq(N,d=dt)

plt.figure()
plt.plot(freq[np.where(freq.real>=0)],F[np.where(freq.real>=0)])
plt.title("Transformada de fourier Temblor")
plt.xlabel("frecuencia [Hz]")
plt.ylabel("Amplitud")

plt.savefig("TransformadaTemblor.pdf")

#Espectrograma de la senal

plt.figure()
plt.specgram(ft,Fs=Fs)
plt.xlabel("tiempo [s]")
plt.ylabel("frecuencia [Hz]")
plt.title("Espectrograma de la senal")
plt.savefig("EspecTemblor.pdf")

