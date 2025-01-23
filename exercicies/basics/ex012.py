# reajuste salarial

salario = float(input("Digite o salário do funcionário: "))
reajuste = salario * 15/100
salario_f = reajuste + salario
print(f"O salario de R${salario}, com 15% de aumento passa a ser: R$ {salario_f:.2f}")