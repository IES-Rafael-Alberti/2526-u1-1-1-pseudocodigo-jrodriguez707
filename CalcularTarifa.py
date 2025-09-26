horas = input ("Introduzca las horas trabajadas: ")
while not horas.isdigit():
                horas = input ("Introduzca las horas trabajadas, nummeros por favor: ")
tarifa = input ("Introduzca la tarifa de cada hora: ")
while not tarifa .isdigit():
                tarifa = input ("Introduzca la tarifa por hora con numeros por favor: ")
print ("Su salario sera de", int (horas) * int (tarifa))

