# "pintando a parede"

largura_p = float(input("Digite a largura da parede: "))
altura_p = float(input("Digite o comprimento da parede: "))

area_p = largura_p * altura_p
qtd_tinta = area_p/ 2

print(f"Sua dimensão é de {largura_p}x{altura_p} e sua área é {area_p}m. A quantidade de tinha que você precisará: {qtd_tinta}L")