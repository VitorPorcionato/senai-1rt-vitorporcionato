primeiro = float(input("Insira um valor: "))
segundo = float(input("Insira um valor: "))
terceiro = float(input("Insira um valor: "))

#Achando o maior numero
maior = primeiro 

if (segundo > maior):   #o IF deve propor alguma coisa. É preciso escrever o IF e logo depois colocar a condição analisada. Então, em seguida, o bloco de comandos. 
    maior = segundo
if (terceiro > maior):
    maior = terceiro

print("O número maior é: ", maior)

#Achando o menor numero 
menor = primeiro

if (segundo < menor):
    menor = segundo
if (terceiro < menor):
    menor = terceiro

print("O menor numero é: ",menor)