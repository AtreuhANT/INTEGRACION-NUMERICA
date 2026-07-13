# INTEGRACION-NUMERICA

El problema solicita explicar cómo afectó el "ruido" de los datos experimentales a los métodos de orden superior (Simpson) en comparación con el Trapecio. Desde una perspectiva analítica y matemática, esto es lo que ocurre:

Comportamiento de la Regla del Trapecio (Atenuación): La regla del Trapecio interpola linealmente (polinomios de grado 1) entre pares de puntos adyacentes. Desde un punto de vista de procesamiento de señales, este método actúa de manera similar a un filtro pasa-bajos simple. Las fluctuaciones aleatorias (ruido) entre puntos contiguos tienden a promediarse y compensarse a lo largo de toda el área. No se intenta "seguir" el ruido con precisión, por lo que el método es inherentemente más robusto frente a datos ruidosos.

Comportamiento de los métodos de Simpson (Sobreajuste): Las reglas de Simpson utilizan polinomios de orden superior (grado 2 para Simpson 1/3, grado 3 para Simpson 3/8) para ajustar curvas suaves a través de los datos experimentales (tomando grupos de 3 y 4 puntos respectivamente). Cuando el set de datos incluye ruido aleatorio, los métodos de orden superior cometen el error de intentar trazar un polinomio perfecto que pase exactamente a través de esas perturbaciones y vibraciones mecánicas.

eL sobreajuste polinómico amplifica artificialmente las derivadas altas introducidas por el ruido, induciendo oscilaciones erráticas en la curva interpolada. Como consecuencia, la supuesta "ventaja de precisión" matemática que teóricamente tienen los métodos de Simpson se degrada drásticamente ante datos experimentales ruidosos, pudiendo generar un error mayor o una lectura menos confiable que el simple cálculo lineal que ofrece el Trapecio.
