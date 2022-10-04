import numpy as np

def Amplitud_De_Transicion(a,b):
    """
    Calcula la probabilidad de transitar de un vector 'a' a un vector 'b' despues de hacer la observacion
    :param a:vector de estado inicial
    :param b:vector de estado final
    :return probabilidad: flotante que representa la probabilidad de transito del vector 'a' al vector 'b'
    """
    distancia_a = np.linalg.norm(a)
    distancia_b = np.linalg.norm(b)
    for i in range(len(a)):                 #Normalizacion Vector_a
        a[i][0] = a[i][0] / distancia_a
        a[i][1] = a[i][1] / distancia_a
    for i in range(len(b)):                 #Normalizacion Vector_b
        b[i][0] = b[i][0] / distancia_b
        b[i][1] = b[i][1] / distancia_b
    bra_b = np.t(b)             # Tranpuesta
    bra_b = np.conj(bra_b)      # Conjugado
    amplitud = np.dot(bra_b,a)      #Amplitud de transicion
    probabilidad = np.linalg.norm(amplitud)**2      #Probabilidad
    return probabilidad

def Media_y_Varianza(m_observable, v_ket):
    """
    Revisa que la matriz observable sea hermitiana, si lo es, calcula la media y la varianza del observable en el estado dado
    :param m_observable: matriz que representa el observable
    :param v_ket: vector de estado inicial
    :return:
    """
    hermitiana = np.t(m_observable)     #Tranpuesta
    hermitiana = np.conj(hermitiana)    #Conjugado
    if hermitiana == m_observable:
        distancia_ket = np.linalg.norm(v_ket)
        for i in range(len(v_ket)):        #Normalizacion Vector_ket
            v_ket[i][0] = v_ket[i][0] / distancia_ket
            v_ket[i][1] = v_ket[i][1] / distancia_ket
        media = np.trace(m_observable)         #Media del observable
        identidad = []
        for i in range(len(m_observable)):          #Creacion de la matriz identidad dependiendo del tamaño de la matriz observable
            identidad.append([])
            for j in range(len(m_observable[0])):
                if i == j:
                    identidad[i].append(1)
                else:
                    identidad[i].append(0)
        m_media = np.multiply(identidad,media)          #Multiplicacion de identidad por la media
        varianza = np.subtract(m_observable,m_media)        #Resta del observable por la media identidad
        varianza = np.dot(varianza,varianza)            #Multiplicaion de la resta por ella misma (al cuadrado)
        varianza = np.trace(varianza)           #Varianza del observable
        return media, varianza
    else:
        return None

def Valores_Probabilidad():


def Dinamica():

