#Lógica Computacional
#Professor: Eduardo Hernandes
#Aluno: Arthur Germano
#Série: 2ºD II
#Data: 21/08/23

#Este exercício tem o objetivo de desenvolver um programa que verifique se a senha inserida pelo usuário é válida.

senha = input("Digite a senha: ")

verificação_senha = ("1234")

if senha == verificação_senha:
  print("A senha está correta.")
else:
  print("A senha está errada. Reinicie o programa e tente novamente.")