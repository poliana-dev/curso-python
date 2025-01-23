# calculando descontos

preco = float(input('Digite o preço do produto: '))
desconto = preco*5/100 # valor abatido do preço
valor = preco - desconto # valor a ser pago
print(f"O produto de {preco}, com 5% de desconto irá valer: {valor}")