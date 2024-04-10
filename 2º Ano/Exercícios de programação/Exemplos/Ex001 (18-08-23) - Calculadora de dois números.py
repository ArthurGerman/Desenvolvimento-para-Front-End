#Lógica Computacional
#Aluno: Arthur Germano
#Professor: Eduardo Hernandes
#Data: 18/08/23
#Programa desenvolvido para o cálculo da soma, subtração, multiplicação e divisão de dois números

print("Olá mundo!. Isto é uma calculadora.")
print("-="*17)
Primeiro_número = int(input("Digite o primeiro número: ")) #Inserção do primeiro número
print("-="*14)
Segundo_número = int(input("Digite o segundo número: ")) #Inserção dos segundo número
print("-="*14)

soma = Primeiro_número + Segundo_número   #Declaração de variáveis
subtração = Primeiro_número - Segundo_número
multiplicação = Primeiro_número * Segundo_número
divisão = Primeiro_número / Segundo_número

print("A soma dos dois números é", soma,"\nA subtração é",subtração,"\nA multiplicação é",multiplicação,"\nA a divisão é",divisão,".")