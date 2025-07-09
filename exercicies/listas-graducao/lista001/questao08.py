"""
08- Equação de Segundo Grau: Solicite ao usuário os valores de “a”, “b”, “c” e “x”, em
seguida resolva uma equação quadrática do tipo y = ax2 + bx + c e exiba o valor
de y para o usuário.

"""

valorA= int(input("Digite o valor de (a): "))
valorB= int(input("Digite o valor de (b): "))
valorC = int(input("Digite o valor de (c): "))
valorX = int(input("Digite o valor de (x): "))


equacao = (valorA*(valorX**2)) + (valorB*valorX) + valorC
print(f"A equação {valorA}x{valorX}^2 + {valorB}x{valorX} + {valorC} = {equacao}")