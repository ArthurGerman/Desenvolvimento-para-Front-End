#Lógica Computacional
#Professor: Eduardo Hernandes
#Aluno: Arthur Germano
#Série: 2ºD II
#Data: 30/08/23

# Esse e

soma = 0.0
contador = 1

while contador <= 4 :
    número = float(input("Digite o número: "))
    soma = soma + número
    contador = contador + 1
média = soma/4
print("-="*15)
print("A média do aluno foi:",média)
if média >=7:
    print("-="*15)
    print("O aluno foi aprovado!!\n")
else:
    print("-="*15)
    print("O aluno foi reprovado.\n")
