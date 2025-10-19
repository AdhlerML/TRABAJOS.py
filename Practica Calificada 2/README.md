<p align="center">
  <img src="img/utp.png" alt="Logo UTP" />
</p>

# PRESENTACION DE EVALUACION_UTP 2

Este proyecto realiza la limpieza, transformación, análisis y visualización de datos provenientes de sensores, con el objetivo de generar reportes y gráficos útiles para la evaluación de temperatura.

1. Limpieza de datos

Lee archivos CSV crudos desde DATA/RAW/.
Normaliza los timestamps al formato ISO (YYYY-MM-DDTHH:MM:SS).
Convierte valores con coma decimal a punto.
Detecta y descarta valores nulos o inválidos (NA, null, error, etc.).
Registra estadísticas de calidad: filas totales, válidas, descartes por timestamp y por valor.

2. Transformación

Convierte voltaje a temperatura en grados Celsius usando una fórmula de calibración lineal basada en dos puntos:

V₁ = 0.4V → T₁ = -30°C
V₂ = 5.6V → T₂ = 120°C

T(V) = T₁ + (T₂ - T₁) * (V - V₁) / (V₂ - V₁)


3. KPIs por archivo

Calcula métricas como:

Número de muestras (n)
Mínimo, máximo, promedio de temperatura
Número y porcentaje de alertas (temperatura > umbral configurable)


 4. Visualización

Genera gráficos por archivo:

Línea de temperatura vs tiempo con umbral y alertas
Histograma de distribución de temperatura


Genera un boxplot global por sensor para comparar su comportamiento.

5. Reporte

Crea un archivo CSV consolidado con los KPIs por archivo en Reportes/kpis_por_archivo.csv.

6. Diagramas de flujo

Incluye diagramas en PNG/SVG que explican el flujo general del pipeline y el proceso de limpieza.

