#Lógica Computacional
#Professor: Eduardo Hernandes
#Aluno: Arthur Germano
#Série: 2ºD II
#Data: 22/08/23

# Algoritmo balada do professor eduardo 2.0

# O objetivo desse programa é identificar se a idade do usuário corresponde a 16 anos ou mais. Se a idade dele for igual a 16, ele precisará confirmar que possui uma altorização dos pais para adentrar à Balada. O mesmo se aplica caso o usuário tenha idade igual a 17 porém, se ele tiver 18 anos, não precisa apresentar autorização para entrar. 

print(" + - + - + - + - +  - + ")
print(" - BALADA DO DUDU 2.0 - ")
print(" + - + - + - + - +  - + \n\n")

idade = int(input("Qual a sua idade: ")) #Variável

if idade >= 18: # Essa linha irá checar se o usuário tem 18 anos de idade ou mais.
  print("-="*20)
  print("Você está apto para entrar na balada. Aproveite com responsabilidade :)\n")# Mensagem de confirmação de entrada.
elif idade == 16 or idade == 17:   # Essa linha irá checar se o usuário tem 16 ou 17 anos de idade.
  print("-="*30)

  autorização = input("Você tem autorização dos seus pais(Digite apenas sim ou não em letras minúsculas): ") # Variável de checagem de porte da autorização
  
  if autorização == ("sim"):
    print("-="*30)
    print("Você está liberado para participar da balada.\n")# Mensagem de confirmação.
  else: # Se ele não tiver autorização.
    print("-="*30)
    print("Você não está liberado por não possuir autorização dos seus pais.\n")# Mensagem de negação se a idade do usuário for 16 ou 17 e ele não tiver uma autorização dos pais.
else:
 print("-="*30)
 print("Você não está liberado por não possuir a idade sufuciente.\n")# Mensagem negando a entrada caso a idade for abaixo de 16 anos de idade.