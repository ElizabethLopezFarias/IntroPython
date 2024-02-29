# Solicitar el precio de suscripción (P)
P = float(input("Ingresa el precio de suscripción (P): "))

# Solicitar el número de usuarios normales (U)
U = int(input("Ingresa el número de usuarios normales (U): "))

# Solicitar los gastos totales (GT)
GT = float(input("Ingresa los gastos totales (GT): "))

# Solicitar las utilidades del año anterior (Uanterior)
Uanterior = float(input("Ingresa las utilidades del año anterior (Uanterior): "))

# Calcular las utilidades actuales
utilidades_actuales = P * U - GT

# Calcular la razón entre las utilidades actuales y las del año anterior
razon_utilidades = utilidades_actuales / Uanterior

print("----------------------------")
print(f"Las utilidades actuales son: {utilidades_actuales:.2f}")
print(f"La razón entre las utilidades actuales y las del año anterior es: {razon_utilidades:.2f}")
print("----------------------------")