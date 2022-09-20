import numpy as np

def experimento_canicas(mcambiante, v_estado, cant_clicks):
    """
    :param mcambiante: matriz de abyacencia que corresponde al cambio de posicion de las canicas en las aristas en 1 click (array) (tamaño n*n)
    :param v_estado: vector que representa el estado inicial de las canicas (array) (tamaño 1*n)
    :param cant_clicks: entero que corresponde a la cantidad de clicks del experimento (int)
    :return: Y: vector de posibilidades que tiene las canicas de quedar en determinada arista (tamaño 1*n) [si la matriz y vector no son del mismo tamaño no devolvera el vector]
    """
    if len(mcambiante[0]) == len(v_estado):
        if (cant_clicks == 1):
            Y = np.dot(mcambiante, v_estado)
        else:
            mcambiantek = mcambiante
            for i in range(cant_clicks):
                mcambiantek = np.dot(mcambiantek,mcambiante)
            Y = np.dot(mcambiantek, v_estado)
        return Y
    else:
        return None

def experimento_rendijas_clasico(mcambiante, v_estado, cant_clicks):
    """
    :param mcambiante: matriz de abyacencia que corresponde al cambio de posicion de la bala en las rendijas y blancos en 1 click (array) (tamaño n*n)
    :param v_estado: vector que representa el estado inicial de la bala (array) (tamaño 1*n) [recomendacion: que sea una bala desde la posicion 0]
    :param cant_clicks: entero que corresponde a la cantidad de clicks del experimento (int)
    :return: Y: vector de posibilidades que tiene las bala de quedar en determinada arista (tamaño 1*n) [si la matriz y vector no son del mismo tamaño no devolvera el vector]
    """
    if len(mcambiante[0]) == len(v_estado):
        if (cant_clicks == 1):
            Y = np.dot(mcambiante, v_estado)
        else:
            mcambiantek = mcambiante
            for i in range(cant_clicks):
                mcambiantek = np.dot(mcambiantek,mcambiante)
            Y = np.dot(mcambiantek, v_estado)
        return Y
    else:
        return None

def experimento_rendijas_cuantico(mcambiante, v_estado, cant_clicks):
    """
    :param mcambiante: matriz de abyacencia que corresponde al cambio de posicion de la bala en las rendijas y blancos en 1 click (array) (tamaño n*n)
    :param v_estado: vector que representa el estado inicial de la bala (array) (tamaño 1*n) [recomendacion: que sea una bala desde la posicion 0]
    :param cant_clicks: entero que corresponde a la cantidad de clicks del experimento (int)
    :return: Y: vector de posibilidades que tiene las bala de quedar en determinada arista (tamaño 1*n) [si la matriz y vector no son del mismo tamaño no devolvera el vector]
    """
    if len(mcambiante[0]) == len(v_estado):
        if (cant_clicks == 1):
            Y = np.dot(mcambiante, v_estado)
        else:
            mcambiantek = mcambiante
            for i in range(cant_clicks):
                mcambiantek = np.dot(mcambiantek,mcambiante)
            Y = np.dot(mcambiantek, v_estado)
        return Y
    else:
        return None

def grafico_vectorestado(v_estado):


