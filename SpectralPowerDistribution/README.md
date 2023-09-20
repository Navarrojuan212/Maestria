# Simulación de Canal de Comunicación por Luz Visible (Visible Light Commmication - VLC)

## Descripción

Este proyecto presenta una mejora en la implementación de una simulación de un canal VLC (Visible Light Communication) utilizando programación orientada a objetos (OOP). La simulación permite modelar la distribución de la potencia óptica recibida en un ambiente 3D configurado con múltiples LEDs como fuentes de transmisión.

> [!NOTE]  
> El archivo `luminarias.py` es la versión inicial del código, la cual se quiso conservar como un archivo aparte.

## Características

- **Modelado 3D del ambiente**: Define las dimensiones de tu espacio (longitud, ancho y altura) y modela cómo se distribuirá la luz en este espacio.
- **Configuración de LEDs**: Establece las posiciones y las potencias de transmisión de los LEDs individualmente.
- **Visualización de la distribución de potencia**: Visualiza cómo se distribuirá la potencia óptica en el plano receptor.

## Requisitos

- Python 3.6 o superior
- Matplotlib
- NumPy

Puedes instalar las dependencias necesarias con el siguiente comando:

```bash
pip install matplotlib numpy
```

# Uso

## Configuración de Parámetros
Antes de ejecutar la simulación, asegúrate de configurar los parámetros correctamente en el script. Aquí hay una guía rápida sobre cada uno:

`lx`, `ly`, `lz`: Las dimensiones de la sala (en metros).
`h`: La altura de la instalación de los LEDs (en metros).
`leds_positions`: Una lista de tuplas que definen las posiciones (x, y) de cada LED en el techo.
`P_totals`: Una lista que define la potencia total de cada LED (en mW)

## Ejecución
Para ejecutar la simulación, simplemente inicia el script `main.py` (o como hayas nombrado tu archivo Python) en un entorno Python que cumpla con los requisitos previamente mencionados.

```bash
python main.py
```

## Visualización
Una vez que la simulación ha terminado, se generará un gráfico 3D que muestra la distribución de la potencia óptica en el plano receptor.

# Contribuciones
Las contribuciones son bienvenidas. Por favor, crea un `'Issue'` o `'Pull Request'` si deseas contribuir al proyecto.

## Contacto
Para preguntas y comentarios, por favor contáctame en:

[Redes](https://linktr.ee/navarro212)

# Agradecimientos
Agradezco a todos los que contribuyeron a este proyecto y a aquellos que lo utilizan para aprender y construir sobre él.