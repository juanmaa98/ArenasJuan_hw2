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

