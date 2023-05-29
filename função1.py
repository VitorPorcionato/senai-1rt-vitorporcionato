largura = float(input("Insira a largura do terreno: "))
comprimento = float(input("Insira o comprimento do terreno: "))
def area(largura, comprimento):
    total = largura * comprimento
    return total


print("A Area total do terreno é:",area(largura,comprimento),"metros")
