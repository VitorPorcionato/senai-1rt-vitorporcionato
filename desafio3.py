valor = float(input("Insira o salário: R$"))
aumento1 = valor*0.10
aumento2 = valor*0.15
soma1 = valor + aumento1
soma2 = valor + aumento2

if valor > 8250.00:
    print("Seu salário teve um aumento de 10%, seu salário atual é:R${:.2f}".format(soma1))
elif valor <= 8250.00:
    print("Seu salário teve um aumento de 15%, seu salário atual é:R${:.2f}".format(soma2))
