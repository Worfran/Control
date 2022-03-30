import matplotlib.pyplot as plt
 
## Declaramos valores para el eje x
eje_x = ['Python', 'R', 'Node.js', 'PHP'] #unique
 
## Declaramos valores para el eje y
eje_y = [50,20,35,47] #contador 
 
## Creamos Gráfica
plt.bar(eje_x, eje_y)
 
## Legenda en el eje y
plt.ylabel('Cantidad de usuarios')
 
## Legenda en el eje x
plt.xlabel('Lenguajes de programación')
 
## Título de Gráfica
plt.title('Usuarios de lenguajes de programación')
 
## Mostramos Gráfica
plt.show()


