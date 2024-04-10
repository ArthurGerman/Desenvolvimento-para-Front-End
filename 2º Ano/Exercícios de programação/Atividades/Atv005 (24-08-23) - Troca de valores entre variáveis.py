#Lógica Computacional
#Professor: Eduardo Hernandes
#Aluno: Arthur Germano
#Série: 2ºD II
#Data: 24/08/23

# Este exercício tem por proposta criar um algoritmo que armazene dois valores em duas variáveis, e efetuar uma troca de valores de forma que a variável "A" passe a possuir o valor da variável "B" e que a variável "B" passe a possuir o valor da variável "A" e, por fim apresentar os valores trocados. Para resolver esse problema, precisamos criar uma terceira variável("C") que, para realizar a troca de valores, recebe o valor de "B", depois "B" recebe de "A" e por fim "A" recebe de "C". Fazendo isso, a troca de valores será realizada.


A = 5
B = 10
C = B # Nessa linha, como a variável "C" recebe o valor de "B", "C" agora vale 10
B = A # Nessa linha, como a variável "B" recebe o valor de "A", "B" agora vale 5
A = C # Nessa linha, como a variável "A" recebe o valor de "C", "A" agora vale 10
print("\nO novo valor de A é",A,"e o novo valor de B é",B,".\n")