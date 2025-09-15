import matplotlib.pyplot as plt  #importa la biblioteca matplotlib para gráficos
import numpy as np #importa la biblioteca numpy para cálculos numéricos

def aleatorio(n=30):
    """Genera una lista de n números aleatorios entre 0 y 1"""
    return list(np.random.rand(n)) # genera n números aleatorios y los convierte en una lista
    
ejex = [i for i in range(30)] # crea una lista de números del 1 al 10
ejey = aleatorio(30) # llama a la función aleatorio para generar datos aleatorios
ejey2 = aleatorio(30) # llama a la función aleatorio para generar datos aleatorios
# fig,ax = plt.subplots() # crea una figura y un conjunto de subgráficos
# ax.plot(ejex,ejey) # traza una línea en el gráfico
# plt.plot(ejex,ejey) # traza una línea en el gráfico
# plt.scatter(ejex,ejey,color='red') # añade puntos rojos en las coordenadas (ejex, ejey)

# plt.title("Gráfico de línea") # añade un título al gráfico
plt.xlabel("Eje X") # añade una etiqueta al eje x
plt.ylabel("Eje Y") # añade una etiqueta al eje y


plt.plot(ejex,ejey, 'r-+') # traza una línea en el gráfico con línea roja y marcadores de cruz
plt.plot(ejex,ejey, 'r+') # traza una línea en el gráfico con marcadores de cruz rojos
plt.plot(ejex,ejey2,'bo') # traza una línea en el gráfico


plt.legend(['Línea 1', 'Línea 2', 'Línea 3']) # añade una leyenda al gráfico

    
plt.show() # muestra la figura
