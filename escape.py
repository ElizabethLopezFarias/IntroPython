#escape.py
#Cálculo de la velocidad de Escape
print("----------------------------")
#Solicitud de Datos de radio y la constante gravitacional
r = float(input("Ingresa el radio del planeta (en metros): "))
g = float(input("Ingresa la constante gravitacional (en m/s^2): "))
r_km = r * 1000 #conversion a km 
ve = (2 * g * r_km) ** 0.5
print("----------------------------")
print(f"La velocidad de escape es {ve:.1f} [m/s]")
print("----------------------------")