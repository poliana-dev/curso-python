"""Você foi contratado para desenvolver um sistema que calcula descontos para uma loja de roupas. 
As regras de desconto são as seguintes:

● Se o cliente comprar pelo menos três peças deverá ser aplicado um desconto de 10%; 
● Se o cliente comprar pelo menos quatro peças deverá ser aplicado um desconto de 15% (substituindo 
o desconto de 10%); 
● Se o cliente comprar ao menos uma peça de blazer, deverá ser acrescido mais 5% de desconto, 
independentemente de descontos anteriores existirem ou não. Se não houver desconto anterior, mas 
uma das peças for blazer deve ser aplicado o desconto de 5%. Se for aplicado algum dos descontos 
anteriores, deverá ser acrescido ao desconto o valor de 5% se ao menos uma das peças for blazer. 
Escreva um programa que leia a quantidade peças de roupas a serem compradas e o valor da compra. Deverá 
ser informado também se alguma das peças é um blazer. Em seguida o programa deverá informar o valor final 
da compra. Exemplo: 
"""

print("\t---- Peças disponiveis ----\na. Blazer (400R$)\nb. Camisa social (50 R$)\nc. T-shirt casual (25R$)\nd. Calça (50 R$)\ne. Saia (R$25) ")
pecasCompradas = int(input("Digite a quantidade de peças que você comprou: "))

valor = 500
percentualDesconto = 10/100
percentualDescontoBlazer = 5/100


if (pecasCompradas==3):
    valor -= 400 
    print(f"Valor:{valor}" )
    desconto = (valor * (percentualDesconto))
    valorFinal = valor - desconto
    print(f"Valor final com desconto de 3%: {valorFinal}")


elif pecasCompradas == 4:
    valor -= 250
    percentualDesconto = 15/100
    desconto = (valor * (percentualDesconto))
    valorFinal = valor - desconto
    print(f"Valor final com desconto de 4%: {valorFinal}")

elif pecasCompradas == 5:
    valorFinal = 500
else:
    valorFinal = 500 - 400
    
contemBlazer = input("Você comprou um blazer? (s/n): ")
if contemBlazer =='n':
    print(f"Valor final: {valorFinal}")
elif contemBlazer =='s':
    descontoEspecial = (valorFinal * percentualDescontoBlazer) 
    valorFinal -= descontoEspecial
    print(f"Valor final com desconto especial: {valorFinal}")

else: 
    print("Inválido")


