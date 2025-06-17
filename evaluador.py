def evaluar_respuestas(respuestas):
    resultados = {}
    for marco, lista in respuestas.items():
        if lista:
            promedio = sum(lista) / len(lista)
            if promedio < 2.5:
                evaluacion = "Deficiente"
            elif promedio < 4:
                evaluacion = "Aceptable"
            else:
                evaluacion = "Óptimo"
            resultados[marco] = {
                "promedio": round(promedio, 2),
                "evaluacion": evaluacion
            }
    return resultados

