# alugar carro

days = int(input("Quantidade de DIAS alugados: "))
km = float(input("Quantidade de Km percorridos: "))

pay = (60 * days) +  (0.15 * km)

print(f"O total a pagar é de R${pay}")