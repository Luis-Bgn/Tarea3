def modus_ponens_ejemplo(estudiar, buena_calificacion):
    if estudiar:
        return buena_calificacion
    else:
        return "No se puede concluir"

# Premisas
estudiar = True  # Antecedente verdadero
buena_calificacion = "Si"  # Consecuente verdadero

# Aplicación del Modus Ponens
resultado = modus_ponens_ejemplo(estudiar, buena_calificacion)

# Resultado
print("Si decides estudiar:")
print("¿Obtendrás una buena calificación?", resultado)
