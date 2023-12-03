# Análisis de la Relación Señal a Ruido (SNR)

## Descripción General

Este repositorio contiene un script en Python para visualizar datos de la Relación Señal a Ruido (*SNR*) a lo largo del tiempo. El análisis está enfocado en los resultados de la maestría para comparaciones futuras.

## Prerrequisitos

Antes de ejecutar el script, asegúrate de que las siguientes bibliotecas estén instaladas:

- pandas
- matplotlib
- seaborn
- numpy

Puedes instalar estos paquetes usando `apt` en este caso para Debian:

```bash
sudo apt update
sudo apt install python3-pandas
```

```bash
sudo apt update 
sudo apt install python3-seaborn
```

## Datos
El script espera un archivo CSV que contenga datos de SNR con marcas de tiempo. Las columnas esperadas son:

- `Timestamp`: La fecha y hora de la medición de SNR.
- `SNR`: El valor de la relación señal-ruido en ese momento.

La ruta al archivo CSV debe proporcionarse como una variable de entorno CSV_PATH.

## Visualizaciones
El script genera cuatro tipos de gráficos:

1. Gráfico de Línea (SNR vs. Tiempo): Muestra la tendencia de los valores de SNR a lo largo del tiempo, útil para observar tendencias generales y fluctuaciones.

2. Gráfico de Dispersión (SNR vs. Tiempo): Representa mediciones individuales de SNR a lo largo del tiempo, útil para identificar valores atípicos y patrones.

3. Histograma (Distribución de SNR): Muestra la distribución de frecuencia de los valores de SNR, útil para comprender la variabilidad y la comunalidad de los niveles de SNR.

4. Boxplot (Estadísticas Resumidas de SNR): Proporciona un resumen estadístico de los datos de SNR, mostrando la mediana, los cuartiles y los valores atípicos.

Cada gráfico se muestra en su propia ventana y puede guardarse para un análisis o informe posterior.

## Uso
Para ejecutar el script, puedes establecer la variable de entorno y ejecutar el archivo Python:

```bash
export CSV_PATH=/ruta/a/tu/archivo/snr_data.csv

python3 Outdoor.py
```

Reemplaza `/ruta/a/tu/archivo/snr_data.csv` con la ruta real a tu archivo `.CSV`.

## Contribuciones
Las contribuciones a este proyecto son bienvenidas. No dudes en enviar solicitudes de extracción o crear incidencias para errores y solicitudes de funcionalidades.
