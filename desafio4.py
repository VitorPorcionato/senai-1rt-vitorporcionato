km = float(input("Insira o valor de kilometros (km) percorrido: "))

preço1 = km*0.50
preço2 = km*0.45

if km <= 200:
    print("O preço da passagem é: R${:.2f}".format(preço1))
else:
    print("O preço da passagem é: R${:.2f}".format(preço2))