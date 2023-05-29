def adição (nu1,nu2):
    return nu1 +nu2

def subtração (nu1, nu2):
    return nu1 - nu2

def multiplicação (nu1,nu2):
    return nu1 * nu2

def divisão (nu1, nu2):
    if nu2 !=0:
        return nu1 / nu2
    else:
        "Erro: Não é possivel dividir por zero"

nu1 = float(input("Insira um valor: "))
nu2 = float(input("Insira um valor: "))

print('Escolha uma operação')
print("1- Adição")
print("2- Subtração")
print("3- Multiplicação")
print("4- Divisão")

operação = int(input("Escolha uma das operações: "))

if operação == 1:
    result = adição(nu1, nu2)
    print("Resultado: ", result)
elif operação == 2:
    result = subtração(nu1,nu2)
    print("Resultado:", result)
elif operação ==3:
    result = multiplicação(nu1, nu2)
    print("Resultado:", result)
elif operação ==4:
    result = divisão(nu1, nu2)
    print("Resultado:", result)