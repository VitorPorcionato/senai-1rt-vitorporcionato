num1 = float(input("Insira a nota: "))
num2 = float(input("Insira a nota: "))
num3 = float(input("Insira a nota: "))

media = (num1+num2+num3)/3

print("A media do aluno: {:.2f}" .format(media))

if media >= 7:
    print("Resultado final: Aprovado")
else:
    if media > 6:
        print("Resultado final: Recuperação")
    else:
        print("Resultado final: Reprovado")
