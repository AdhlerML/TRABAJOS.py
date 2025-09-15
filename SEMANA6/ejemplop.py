import numpy as np
import matplotlib.pyplot as plt

# Generar datos para el eje x
x = np.linspace(-2 * np.pi, 2 * np.pi, 500)

# Calcular sen(x) y -sen(x)
y1 = np.sin(x)
y2 = -np.sin(x)

# Crear la gráfica
plt.figure(figsize=(10, 6))
plt.plot(x, y1, label='sen(x)', color='blue')
plt.plot(x, y2, label='-sen(x)', color='red')

# Añadir título y etiquetas
plt.title('Funciones seno y su inversa')
plt.xlabel('Ángulo (radianes)')
plt.ylabel('Valor')

# Añadir leyenda y cuadrícula
plt.legend()
plt.grid(True)

# Guardar la gráfica como imagen
plt.savefig('grafico_seno.png')
plt.savefig('grafico_seno.pdf')

# Mostrar la gráfica (opcional)
plt.show()
