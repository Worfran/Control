import numpy as np
import matplotlib.pyplot as plt

file="https://raw.githubusercontent.com/koldunovn/python_for_geosciences/master/Ham_3column.txt"

def reader(file):
    df = np.loadtxt(file)
    return df

def DateIR(year):
    r=year[:,3]
    i=np.argsort(r)
    mini=i[0]
    maxi=i[-1]
    Datem=("IRmin: "+str(r[mini])+" in "+str(int(year[mini,0]))+"-"+str(int(year[mini,1]))+"-"+str(int(year[mini,2])))
    DateM=("IRmax: "+str(r[maxi])+" in "+str(int(year[maxi,0]))+"-"+str(int(year[maxi,1]))+"-"+str(int(year[maxi,2])))
    return Datem +" and "+DateM

def Radiation(year):
    r=year[:,3]
    maxi=np.max(r)
    mini=np.min(r)
    return (mini, maxi)

def anios(df):
    years=[]
    for year in df[:,0]:
        if year not in years:
            years.append(year)
    return years

def Macacosuprema(year,df):
    y=df[df[:,0]==year]
    return Radiation(y)

df=reader(file)

#punto1

y10=df[df[:,0]==2010]
d10=y10[:,2]
r10=y10[:,3]
mean=np.mean(r10)
std=np.std(r10)

plt.figure()
plt.plot(d10,r10, label=DateIR(y10))
plt.xlabel("Day")
plt.ylabel("Radiation")
plt.title("Ionizing radiation")
plt.legend()
plt.savefig("Macaco solar.png")

years=anios(df)
minimos=[]
maximos=[]

for year in years:
    mini,maxi=Macacosuprema(year,df)
    minimos.append(mini)
    maximos.append(maxi)


plt.figure()
plt.plot(years,minimos,color="darkred", label="Minimum")
plt.plot(years,maximos,color="dodgerblue", label="Maximum")
plt.legend()
plt.savefig("Macacosupremo.png")
