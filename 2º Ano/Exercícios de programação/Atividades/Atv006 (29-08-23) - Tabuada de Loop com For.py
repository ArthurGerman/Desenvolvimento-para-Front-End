#Lógica Computacional
#Professor: Eduardo Hernandes
#Aluno: Arthur Germano
#Série: 2ºD II
#Data: 29/08/23

#Essa atividade consiste num exercício de tabuada utilizando o loop com o comando FOR.

número = int(input("Digite o número que você deseja que seja calculado: "))# Primeira pergunta
print("-="*30)
multiplicador = int(input("Digite o último multiplicador que você deseja: ")) # Segunda pergunta
for contador in range(0,multiplicador+1,1): #Nessa linha, a variável de controle(contador) armazena o primeiro multiplicador(0) até o último multiplicador que o usuário estipular.
    print(número,"x", contador," = ",número*contador) # Nessa linha, o multiplicando que o usuário estipular é repetido quantas vezes for o multiplicador. Após isso é imprimido o range do contador e logo depois, a multiplicação do multiplicando pelo range do contador. Por fim, o programa é finalizado.

