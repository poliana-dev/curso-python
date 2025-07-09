'''
10.Tabuada: 
Solicite ao usuário um valor numérico, em seguida, exiba a tabuada de
um número específico (por exemplo, 5). O programa deverá ter como saída:
5x1 = 5; 5x2 = 10; 5x3 = 15; 5x4 = 20; 5x5 = 25; 5x6 = 30; 5x7 = 35; 5x8 = 40; 5x9
= 45; 5x10 = 50;

'''

numero =int(input("Digite um valor númerico inteiro: "))

for multiplicador in range(1,11):
    print(f" {numero} x {multiplicador }= {numero*multiplicador}")