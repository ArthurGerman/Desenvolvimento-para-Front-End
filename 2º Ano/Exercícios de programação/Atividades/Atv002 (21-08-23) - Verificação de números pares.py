#Lógica Computacional
#Professor: Eduardo Hernandes
#Aluno: Arthur Germano
#Série: 2ºD II
#Data: 21/08/23

#Este exercício tem o objetivo de desenvolver um programa que determine se o número inserido pelo usuário é par.

numero = int(input("Digite o número: "))

if numero%2 == 0 :
  print("-="*10)
  print("O número",numero,"é par.")
else:
  print("-="*20)
  print("O número",numero,"não é par. Ele é ímpar.")