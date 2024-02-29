#emprendedor1.py

#Solicita precio de la suscripcion
P = float(input("Ingresa el precio de suscripción (P): "))

# Solicitar el número de usuarios (U)
U = int(input("Ingresa el número de usuarios (U): "))

# Solicitar los gastos totales (GT)
GT = float(input("Ingresa los gastos totales (GT): "))

# Calcular las utilidades
utilidades = P * U - GT

# Muestra las utilidades
print("----------------------------")
print(f"Las utilidades del proyecto son: {utilidades:.2f}")
print("----------------------------")