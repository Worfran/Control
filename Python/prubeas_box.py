import pandas as pd
import numpy as np

df = pd.DataFrame(np.random.rand(1,5), columns=["A", "B", "C", "D", "E"])

print(df)

print(np.random.rand(1,5))


matriz=[]
#recorrido total
for i in range (len(matriz)):
    for j in range(len(matriz[0])):
        # celdas continuas
        persona=0
        for h in range(i-1,i+2):
            for k in range(j-1,j+2):
                if h >0 and h < len(matriz):
                    if k > 0 and k:
                        personas += matriz[h][k]