"""
Crie um programa que leia o salário de uma pessoa e calcule o imposto de renda a
ser pago baseado nas seguintes faixas: até R$ 1.903,98 isento, de R$ 1.903,99 até
R$ 2.826,65 o imposto é de 7,5%, de R$ 2.826,66 até R$ 3.751,05 o imposto é de
15%, de R$ 3.751,06 até R$ 4.664,68 o imposto é de 22,5%, acima de R$ 4.664,68
o imposto é de 27,5%.

"""

salario = float(input("Digite seu salário: "))

if salario <= 1903.98:
    print(f"Seu salário no valor de: {salario} está isento.")

elif salario == 1903.99 or salario <= 2826.65:
    print(f"Seu salario no valor de: {salario} tem um imposto aplicado de 7,5%")
    imposto = salario * (75/10)
    salarioImpostado =  imposto - salario
    print(f"Seu salário com os impostos aplicados é de: {salarioImpostado}")

elif salario == 2826.66 or salario <= 3751.05:
    print(f"Seu salario no valor de: {salario} tem um imposto aplicado de 15%")
    imposto = salario * (15/100)
    salarioImpostado = salario - imposto
    print(f"Seu salário com os impostos aplicados é de:{salarioImpostado}")

elif salario == 3751.06 or salario <= 4664.68:
    print(f"Seu salario no valor de: {salario} tem um imposto aplicado de 22,5%")
    imposto = salario * (22/100)  #tem que corrigir
    salarioImpostado =  salario- imposto
    print(f"Seu salário com os impostos aplicados é de:{salarioImpostado}")





