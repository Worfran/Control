from matplotlib import colors
import numpy as np
import matplotlib.pyplot as plt
from scipy import signal as sg


def macaco3000(t,pi=np.pi):
    argumento=(t*pi*2)
    factor1=2*np.sin(argumento/50)
    factor2=np.sin(argumento/15)
    factor3=0.5*np.sin(argumento/5)
    return  factor1+factor2+factor3 


#indice a
t=np.arange(1,1001,1)
h=t
size=len(t)
y=macaco3000(t)
n=np.random.normal(0,1,size)
y2=y+n

y3=y
y4=y2
t=t[t<=200]
y=y[y>=-4]
y=y[y<=4]
y2=y2[y2>=-4]
y2=y2[y2<=4]

y=y[:200]
y2=y2[:200]


(f,px)=sg.periodogram(y3)
(f2,px2)=sg.periodogram(y4)

plt.figure()
plt.plot(t,y,color="Blue")
plt.plot(t,y2,color="Black")
plt.ylabel("Periodic signal")
plt.xlabel("Time")
plt.savefig("Macacosignal.png")

plt.figure()
plt.plot(f,px)
plt.savefig("caquismo.png")

plt.figure()
plt.plot(f2,px2)
plt.savefig("caquismo2.png")

