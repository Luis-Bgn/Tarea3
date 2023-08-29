def modus_tollens(p, q):
    if not q:
        return not p
    else:
        return "No se puede concluir"

# Premisas
p_false = False  # Antecedente falso
q_false = False  # Consecuente falso
q_true = True  # Consecuente verdadero

# Aplicación del Modus Tollens
resultado_false = modus_tollens(p_false, q_false)
resultado_true = modus_tollens(p_false, q_true)

# Resultados
print("Si la consecuente es falsa:")
print("Resultado con antecedente falso:", resultado_false)
print("Resultado con antecedente verdadero:", resultado_true)
