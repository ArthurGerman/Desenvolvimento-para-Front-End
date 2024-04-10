#Lógica Computacional
#Professor: Eduardo Hernandes
#Aluno: Arthur Germano
#Série: 2ºD II
#Data: 21/08/23

#Este exercício tem por objetivo criar um programa que determine se um ano é bissexto

ano = int(input("Digite o ano para saber se ele é bissexto ou não: "))
if ano % 4 == 0 and not ano % 100 == 0 or ano % 400 == 0:
    print("-="*20)
    print("O ano que você digitou é bissexto.")
else:
    print("-="*20)
    print("O ano não é bissexto.")