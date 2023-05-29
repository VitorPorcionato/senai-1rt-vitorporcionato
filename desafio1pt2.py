velocidade = float(input("A velocidade é de: "))

valoracima = velocidade - 80
multa = (velocidade - 80)*7 

if velocidade > 80:
    print("O veículo estava {}km/h acima da velocidade, ele foi multado em um valor de: R${:.2f}".format (valoracima,multa))
else:
    print("O veículo estava em velocidade adequada, continue assim")