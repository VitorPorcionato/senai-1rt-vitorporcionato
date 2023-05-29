nota = float(input("Insira a nota do competidor: "))

if nota <= 50:
    print("SUA NOTA FOI: {} , VOCÊ RECEBEU DE PREMIAÇÃO: CERTIFICADO DE PARTICIPAÇÃO".format(nota))
elif nota > 50 and nota <= 60:
    print("SUA NOTA FOI: {} , VOCÊ RECEBEU DE PREMIAÇÃO: CERTIFICADO MENÇÃO HONROSA".format(nota))
elif nota > 60 and nota <=70:
    print("SUA NOTA FOI: {} , VOCÊ RECEBEU DE PREMIAÇÃO: MEDALHA DE BRONZE".format(nota))
elif nota > 70 and nota <=90:
    print("SUA NOTA FOI: {} , VOCÊ RECEBEU DE PREMIAÇÃO: MEDALHA DE PRATA".format(nota))
elif nota > 90:
     print("SUA NOTA FOI: {} , VOCÊ RECEBEU DE PREMIAÇÃO: MEDALHA DE OURO".format(nota))

     