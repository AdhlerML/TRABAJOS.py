import matplotlib.pyplot as plt
import numpy as np

def aleatorio(n=30):
    """Genera una lista de n números aleatorios entre 0 y 1"""
    return list(np.random.rand(n))
    # genera n números aleatorios y los convierte en una lista

ejex = [i for i in range(30)]
ejey = aleatorio(30)    
ejey2 = aleatorio(30)

fig,ax = plt.subplots(2,2) # crea una figura y un conjunto de 2 subgráficos en dos filas y dos columnas
fig.suptitle("Gráfico de línea") # añade un título a la figura

ax[0,0].plot(ejex,ejey, 'go', label) #