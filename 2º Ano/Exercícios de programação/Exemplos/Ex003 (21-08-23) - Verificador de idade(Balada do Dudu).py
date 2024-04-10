#Algoritmo balada do professor eduardo
#O objetivo é identificar se a idade da pessoa corresponde a 18 anos de idade. Caso o usuário tenha a idade necessária, ele será liberado para entrar. Senão, será impedido.

idade = int(input("Qual a sua idade: ")) #Variável

if idade >= 18:
  print("-="*20)
  print("Você está apto para a balada.")
else:
 print("-="*30)
 print("Você não está liberado por não possuir a idade sufuciente.")