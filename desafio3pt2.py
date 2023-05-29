num1 = float(input("Primeiro número:"))
num2 = float(input("Segundo número:"))
operação = input("Digite a operação a realizar (+,-,* ou /):")

if operação == "+":
    resultado = num1+ num2
elif operação == "-":
    resultado = num1 - num2
elif operação == "*":
    resultado = num1 * num2
elif operação == "/":
    resultado = num1 / num2
else:
    print("Operação inválida!")
    resultado = 0
print("Resultado: ", resultado)