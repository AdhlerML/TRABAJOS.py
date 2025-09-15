import matplotlib.pyplot as plt
import numpy as np

def aleatorio(n=30):
    """Genera una lista de n números aleatorios entre 0 y 1"""
    return list(np.random.rand(n))
    # genera n números aleatorios y los convierte en una lista
    
ejex = [i for i in range(30)]
ejey = aleatorio(30)
ejey2 = aleatorio(30)

fig,ax = plt.subplots(1,2) # crea una figura y un conjunto de 2 subgráficos en una fila
fig.suptitle("Gráfico de línea") # añade un título a la figura


ax[0].plot(ejex,ejey, 'r-+') # traza una línea en el primer subgráfico con línea roja y marcadores de cruz
ax[0].set_ylabel("Eje Y1") # añade una etiqueta al eje y
ax[0].set_xlabel("Eje X") # añade una etiqueta al eje x
ax[0].legend(['Línea 1']) # añade una leyenda al primer subgráfico
ax[0].set_title("Subgráfico 1") # añade un título al primer subgráfico



ax[1].plot(ejex,ejey2,'ro') # traza una línea en el segundo subgráfico con marcadores de punto azules
ax[1].set_xlabel("Eje X") # añade una etiqueta al eje x
ax[1].set_ylabel("Eje Y2") # añade una etiqueta al eje y
ax[1].set_title("Subgráfico 2") # añade un título al primer subgráfico


plt.show() # muestra la figura