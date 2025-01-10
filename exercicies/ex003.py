# dissecando uma variavel - nivel facil

entrada = input("Digite algo: ")
print(f"O tipo é {type(entrada)} \nÉ um número? {entrada.isnumeric()} \nÉ uma letra? {entrada.isalpha()} \nÉ misto? {entrada.isalnum()} \nEstá em maiusculo? {entrada.isupper()} - Em minusculo? {entrada.islower()}")