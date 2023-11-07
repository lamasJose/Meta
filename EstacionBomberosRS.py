import random
import math
import time
import copy

cobertura_distritos = {
    1: [1, 2, 4, 5],
    2: [1, 2, 3, 5, 6],
    3: [2, 3, 6, 7],
    4: [1, 4, 5, 8, 10, 11],
    5: [1, 2, 4, 5, 6, 8],
    6: [2, 3, 5, 6, 7, 8, 9],
    7: [3, 6, 7, 9, 13],
    8: [4, 5, 6, 8, 9, 11, 12],
    9: [6, 7, 8, 9, 12, 13],
    10: [4, 10, 11, 14],
    11: [4, 8, 10, 11, 12, 14],
    12: [8, 9, 11, 12, 13, 15],
    13: [7, 9, 12, 13, 15, 16],
    14: [10, 11, 14, 15],
    15: [12, 13, 14, 15, 16],
    16: [13, 15, 16]
}

#INTENTO DE UNIOBJETIVO
# def generarSolucion(solucion_actual):
#     distritos_cubiertos = []
#     nueva_solucion = copy.deepcopy(solucion_actual)
#     while len(distritos_cubiertos) != 16:
#         distrito = random.randrange(len(nueva_solucion))
#         if nueva_solucion[distrito] == 1:
#             nueva_solucion[distrito] = 0
#         else:
#             nueva_solucion[distrito] = 1
#         for pos, valor in enumerate(nueva_solucion):
#             if valor == 1:
#                 distritos_cubiertos.extend(vecindad[pos + 1])
#         distritos_cubiertos = list(set(distritos_cubiertos))
#     return nueva_solucion

def distritosSinEstacion(dicc):
    return (set(cobertura_distritos.keys()) - set(dicc.keys()))

def conversionDiccionarioLista(dicc):
    lista_resultante = []

    for lista_valor in dicc.values():
        lista_resultante.extend(lista_valor)

    return(lista_resultante)

def generarSolucion(solucion_actual):
    nueva_solucion = copy.deepcopy(solucion_actual)
    distrito = random.choice(list(cobertura_distritos.keys()))
    if distrito in nueva_solucion:
        nueva_solucion.pop(distrito)
    else:
        nueva_solucion[distrito] = cobertura_distritos[distrito]

    return nueva_solucion

def recocidoSimulado():
    temperatura = 10000000
    epsilon = 0.00001
    alpha = 0.99
    solucion_actual = copy.deepcopy(cobertura_distritos)

    inicio_tiempo = time.time()

    while temperatura > epsilon:
        for _ in range(100):
            siguiente_solucion = generarSolucion(solucion_actual)

            distritos_cubiertos_sa = conversionDiccionarioLista(solucion_actual)
            distritos_cubiertos_ss = conversionDiccionarioLista(siguiente_solucion)
            distritos_no_cubiertos_sa = 16 - len(set(distritos_cubiertos_sa))
            distritos_no_cubiertos_ss = 16 - len(set(distritos_cubiertos_ss))

            delta = (len(siguiente_solucion)*0.001 + distritos_no_cubiertos_ss) - (len(solucion_actual)*0.001 + distritos_no_cubiertos_sa)
            #delta = siguiente_solucion.count(1) - solucion_actual.count(1)
            
            if delta < 0 or random.uniform(0, 1) < math.exp(-delta / temperatura):
                solucion_actual = siguiente_solucion

        temperatura *= alpha

    tiempo_transcurrido = time.time() - inicio_tiempo
    print(f"Tiempo de ejecución: {tiempo_transcurrido} segundos")

    return solucion_actual

resultado = recocidoSimulado()

# print("Solución Final:")
# print(f"Número de estaciones necesarias: {resultado.count(1)}")
# for pos, valor in enumerate(resultado):
#     if valor == 1:
#         print(f"La estación del distrito {pos + 1} cubre los distritos {vecindad[pos + 1]}")

print("Solución Final:")
print(f"Número de estaciones necesarias: {len(resultado)}")
for clave, valor in resultado.items():
    print(f"La estación del distrito {clave} cubre los distritos {cobertura_distritos[clave]}")
