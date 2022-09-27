import numpy as np

def ProbabilidadPosicion (vector_posiciones, posicion):
    """
    :param vector_posiciones: vector que representa las posiciones (1*n)
    :param posicion: entero que representa que posicion que quiere calcular la probabilidad de que la particula este ahi (1-n)
    :return probabilidad: flotante que representa la probabilidad de encontrar la particula segun la posicion
    """
    num = np.sqrt((vector_posiciones[posicion][0]**2)+(vector_posiciones[posicion][1]**2))
    den = 0
    for i in range(len(vector_posiciones)):
        den = den + (np.sqrt((vector_posiciones[i][0]**2)+(vector_posiciones[i][1]**2)))**2
    den = np.sqrt(den)
    probabilidad = (num**2)/(den**2)
    return probabilidad

print(ProbabilidadPosicion([[3,-4],[7,2]],1)) #PruebaPrimeraLibreria

def ProbabilidadSegundoVector (v_posiciones_1, v_posiciones_2, posicion):
    """
        :param v_posiciones_1: vector que representa las posiciones en tiempo 1 (1*n)
        :param v_posiciones_2: vector que representa las posiciones en tiempo 2 (1*n)
        :param posicion: entero que representa que posicion que quiere calcular la probabilidad de que la particula este ahi (1-n)
        :return probabilidad: flotante que representa la probabilidad de encontrar la particula segun la posicion
        """
    vector_posiciones = np.dot(v_posiciones_1, v_posiciones_2)
    num = np.sqrt((vector_posiciones[posicion][0] ** 2) + (vector_posiciones[posicion][1] ** 2))
    den = 0
    for i in range(len(vector_posiciones)):
        den = den + (np.sqrt((vector_posiciones[i][0] ** 2) + (vector_posiciones[i][1] ** 2))) ** 2
    den = np.sqrt(den)
    probabilidad = (num ** 2) / (den ** 2)
    return probabilidad

print(ProbabilidadSegundoVector([[3,-4],[7,2]],[[3,-4],[7,2]],0)) #PruebaSegundaLibreria