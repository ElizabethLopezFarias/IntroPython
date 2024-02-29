# Solicitar el precio de suscripción para usuarios normales
print("----------------------------")
P_normal = float(input("Ingresa el precio de suscripción para usuarios normales (P_normal): "))

# Solicitar el número de usuarios normales
U_normal = int(input("Ingresa el número de usuarios normales (U_normal): "))

# Solicitar el precio de suscripción para usuarios premium (50% más que el normal)
P_premium = 1.5 * P_normal

# Solicitar el número de usuarios premium
U_premium = int(input("Ingresa el número de usuarios premium (U_premium): "))

# Solicitar los gastos totales (GT)
GT = float(input("Ingresa los gastos totales (GT): "))

# Calcular las utilidades considerando ambos tipos de usuarios
utilidades = (P_normal * U_normal + P_premium * U_premium) - GT

print("----------------------------")
print(f"Las utilidades del proyecto considerando usuarios normales y premium son: {utilidades:.2f}")
print("----------------------------")