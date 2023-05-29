num1 = int(input("Insira um valor: "))
num2 = int(input("Insira um valor: "))
num3 = int(input("Insira um valor: "))

def maior (num1,num2,num3):
    num = num1, num2, num3 
    return max(num)

print("O maior valor é: ",maior(num1, num2, num3))