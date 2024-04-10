#Lógica Computacional
#Professor: Eduardo Hernandes
#Aluno: Arthur Germano
#Série: 2ºD II
#Data: 21/08/23

#Este programa calcula a média de três notas e verifica se o aluno foi aprovado(média >= 7)

primeira_nota = float(input("Digite a primeira nota: "))
print("-="*20)
segunda_nota = float(input("Digite a segunda nota: "))
print("-="*20)
terceira_nota = float(input("Digite a terceira nota: "))
print("-="*20)
média = ((primeira_nota + segunda_nota + terceira_nota)/3)
if média >= 7:
  print("Parabéns, você foi aprovado. Sua média foi",média)
else:
  print("Que pena :( Você não foi aprovado. Sua média foi",média)