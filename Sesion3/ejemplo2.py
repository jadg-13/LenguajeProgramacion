import math

#calcular el area de un circulo
radio = int(input("Ingrese el radio del circulo: "))
area = math.pi * pow(radio, 2)
#imprimir el resultado con dos decimales usando f"""
print(f"El area del circulo es: {area:.4f}")