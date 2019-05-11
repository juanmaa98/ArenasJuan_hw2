import numpy as np
import matplotlib.pyplot as plt
import scipy

datos=np.genfromtxt("umax.dat")

w=datos[:,0]
u1=datos[:,1]
u2=datos[:,2]
u3=datos[:,3]

plt.figure()
plt.plot(w,u1,label="u1")
plt.plot(w,u2,label="u2")
plt.plot(w,u3,label="u3")
plt.title("Edificio en sismo")
plt.xlabel("frecuencia angular [rad/s]")
plt.ylabel("Amplitud")
plt.legend()

plt.savefig("uvsw.pdf")


datosw1=np.genfromtxt("uw1.dat")

w1=datosw1[0,0]
t=datosw1[:,1]
u1w1=datosw1[:,2]
u2w1=datosw1[:,3]
u3w1=datosw1[:,4]

plt.figure()
plt.plot(t,u1w1,label="u1")
plt.plot(t,u2w1,label="u2")
plt.plot(t,u3w1,label="u3")
plt.title("Amplitudes en funcion del tiempo para w="+str(w1))
plt.xlabel("tiempo [s]")
plt.ylabel("Amplitud")
plt.legend()

plt.savefig("uw1.pdf")


datosw2=np.genfromtxt("uw2.dat")

w2=datosw2[0,0]
t=datosw2[:,1]
u1w2=datosw2[:,2]
u2w2=datosw2[:,3]
u3w2=datosw2[:,4]

N=len(u1w2)

plt.figure()
plt.plot(t[0:int(N/4)],u1w2[0:int(N/4)],label="u1")
plt.plot(t[0:int(N/4)],u2w2[0:int(N/4)],label="u2")
plt.plot(t[0:int(N/4)],u3w2[0:int(N/4)],label="u3")
plt.title("Amplitudes en funcion del tiempo para w="+str(w2))
plt.xlabel("tiempo [s]")
plt.ylabel("Amplitud")
plt.legend()

plt.savefig("uw2.pdf")

datosw3=np.genfromtxt("uw3.dat")

w3=datosw3[0,0]
t=datosw3[:,1]
u1w3=datosw3[:,2]
u2w3=datosw3[:,3]
u3w3=datosw3[:,4]

N=len(u1w3)

plt.figure()
plt.plot(t[0:int(N/4)],u1w3[0:int(N/4)],label="u1")
plt.plot(t[0:int(N/4)],u2w3[0:int(N/4)],label="u2")
plt.plot(t[0:int(N/4)],u3w3[0:int(N/4)],label="u3")
plt.title("Amplitudes en funcion del tiempo para w="+str(w3))
plt.xlabel("tiempo [s]")
plt.ylabel("Amplitud")
plt.legend()

plt.savefig("uw3.pdf")


datosw4=np.genfromtxt("uw4.dat")

w4=datosw4[0,0]
t=datosw4[:,1]
u1w4=datosw4[:,2]
u2w4=datosw4[:,3]
u3w4=datosw4[:,4]

plt.figure()
plt.plot(t,u1w4,label="u1")
plt.plot(t,u2w4,label="u2")
plt.plot(t,u3w4,label="u3")
plt.title("Amplitudes en funcion del tiempo para w="+str(w4))
plt.xlabel("tiempo [s]")
plt.ylabel("Amplitud")
plt.legend()

plt.savefig("uw4.pdf")

datos=np.genfromtxt("umaxf.dat")

w=datos[:,0]
u1=datos[:,1]
u2=datos[:,2]
u3=datos[:,3]

plt.figure()
plt.plot(w,u1,label="u1")
plt.plot(w,u2,label="u2")
plt.plot(w,u3,label="u3")
plt.title("Edificio en sismo")
plt.xlabel("frecuencia angular [rad/s]")
plt.ylabel("Amplitud")
plt.legend()

plt.savefig("uvswf.pdf")

datosw1=np.genfromtxt("uw1f.dat")

w1=datosw1[0,0]
t=datosw1[:,1]
u1w1=datosw1[:,2]
u2w1=datosw1[:,3]
u3w1=datosw1[:,4]

plt.figure()
plt.plot(t,u1w1,label="u1")
plt.plot(t,u2w1,label="u2")
plt.plot(t,u3w1,label="u3")
plt.title("Amplitudes en funcion del tiempo para w="+str(w1))
plt.xlabel("tiempo [s]")
plt.ylabel("Amplitud")
plt.legend()

plt.savefig("uw1f.pdf")


datosw2=np.genfromtxt("uw2f.dat")

w2=datosw2[0,0]
t=datosw2[:,1]
u1w2=datosw2[:,2]
u2w2=datosw2[:,3]
u3w2=datosw2[:,4]

N=len(u1w2)

plt.figure()
plt.plot(t[0:int(N/4)],u1w2[0:int(N/4)],label="u1")
plt.plot(t[0:int(N/4)],u2w2[0:int(N/4)],label="u2")
plt.plot(t[0:int(N/4)],u3w2[0:int(N/4)],label="u3")
plt.title("Amplitudes en funcion del tiempo para w="+str(w2))
plt.xlabel("tiempo [s]")
plt.ylabel("Amplitud")
plt.legend()

plt.savefig("uw2f.pdf")

datosw3=np.genfromtxt("uw3f.dat")

w3=datosw3[0,0]
t=datosw3[:,1]
u1w3=datosw3[:,2]
u2w3=datosw3[:,3]
u3w3=datosw3[:,4]

N=len(u1w3)

plt.figure()
plt.plot(t[0:int(N/4)],u1w3[0:int(N/4)],label="u1")
plt.plot(t[0:int(N/4)],u2w3[0:int(N/4)],label="u2")
plt.plot(t[0:int(N/4)],u3w3[0:int(N/4)],label="u3")
plt.title("Amplitudes en funcion del tiempo para w="+str(w3))
plt.xlabel("tiempo [s]")
plt.ylabel("Amplitud")
plt.legend()

plt.savefig("uw3f.pdf")


datosw4=np.genfromtxt("uw4f.dat")

w4=datosw4[0,0]
t=datosw4[:,1]
u1w4=datosw4[:,2]
u2w4=datosw4[:,3]
u3w4=datosw4[:,4]

plt.figure()
plt.plot(t,u1w4,label="u1")
plt.plot(t,u2w4,label="u2")
plt.plot(t,u3w4,label="u3")
plt.title("Amplitudes en funcion del tiempo para w="+str(w4))
plt.xlabel("tiempo [s]")
plt.ylabel("Amplitud")
plt.legend()

plt.savefig("uw4f.pdf")

