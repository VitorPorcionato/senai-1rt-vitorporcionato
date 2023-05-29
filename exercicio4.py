valor1 = int(input("digite um valor: ")) 
valor2 = int(input("digite um valor: "))

print("Variavel 1: ",valor1)
print("Variavel 2: ",valor2)
print("Invertendo...")

aux = valor2 #usar uma variável auxiliar, a aux. A função dar aux é guardar aquele primeiro valor contido em var2
valor2 = valor1
valor1 = aux

print("Variavel 1: ",valor1)
print("Variavel 2: ",valor2)