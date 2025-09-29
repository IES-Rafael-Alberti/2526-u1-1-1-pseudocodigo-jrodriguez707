x = input("Escribe un numero entero: ")
while not x.isdigit():
	x = input("Por favor, introduzca un numero entero: ")
x = int(x)
if (x % 2 == 0):
	print("El numero es par")
else:
	print("El numero es impar")
