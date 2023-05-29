def verificar_par (num):
    if num % 2 == 0:
        return True
    else:
        return False
numero = int(input("Insira um número: "))
numero = verificar_par (numero)
print("Esse número é par: ",numero)