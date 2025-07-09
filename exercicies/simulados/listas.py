"""
1 – (10 pts) Você foi contratado para desenvolver 
um sistema que analisa uma relação de produtos vendidos ao longo de um ano, 
    a respectiva quantidade vendida 
        e o mês em que ocorreu a venda. 
        
Implemente um programa que solicite todas as linhas de registros da planilha ao usuário,
o qual deverá inserir manualmente esses dados. 
Uma vez que esses dados tenham sido inseridos no programa, ele deverá apresentar as seguintes 
informações no terminal: 
a) Qual produto teve a maior quantidade vendida, ao longo dos meses? 
b) Qual o mês com o maior número de vendas? 
c) Qual o produto mais vendido em cada mês? 
d) Quantos produtos tiveram vendas acima de 50 unidades? 
e) Crie uma lista contendo apenas os produtos que venderam 50 ou mais unidades e o mês e exiba essa 
lista.

"""

tam_planilha = int(input("Informe a quantidade de registros: "))

registros_produtos = []

for i in range(1,tam_planilha+1):
        produto = input("Nome do produto: ")
        qtd_venda = int(input("Quantidade vendida: "))
        mes = input("Nome do mês da venda: ")

        registro ={
                "produto": produto,
                "vendas" :qtd_venda,
                "mes": mes

        }

        registros_produtos.append(registro)


#a) Qual produto teve a maior quantidade vendida, ao longo dos meses? 

vendas_totais ={}

vendas_mes ={}


for i in range(len(registros_produtos)):
    indice = registros_produtos[i]
    for registro in indice:
        produto = indice["produto"]
        qtd = indice["vendas"]
        mes = indice["mes"]

        vendas_totais[produto] = qtd
        vendas_mes[mes] = qtd #Ex:maio: 20

maior_venda = 0
prod_maisVendido = ""


for produto in vendas_totais:
    if vendas_totais[produto] > maior_venda:
        maior_venda = vendas_totais[produto]
        prod_maisVendido = produto

maior_vendaMes = 0
mes_maisVendido = ""

for mes in vendas_mes:
    if vendas_mes[mes] >maior_vendaMes:
        maior_vendaMes = vendas_mes[mes] 
        mes_maisVendido = mes

                
        

        
                        

print(registros_produtos)
print(vendas_totais)
print(maior_venda,prod_maisVendido)
print(f"mes:{mes_maisVendido}, qtd:{maior_vendaMes}")
print(vendas_mes)