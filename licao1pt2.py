while True:
    valor = int(input("Insira um número: "))
    analise = valor%2

    if valor < 0:
        print("\nNumero negativo")
        break
    elif analise == 0:
        print("Numero par")
    elif analise > 0:
        print("Numero Impar")