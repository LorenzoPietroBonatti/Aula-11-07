# 6) Faça um programa que possua um vetor denominado A que armazene 6 numeros inteiros.
# O programa deve executar os seguintes passos:

# (a) Atribua os seguintes valores a esse vetor: 1, 0, 5, -2, -5, 7.
# (b) Armazene em uma variavel a soma entre os valores das posições A[0], 
# A[1] e A[5] do vetor e mostre na tela esta soma.
# (c) Modifique o vetor na posição 4, atribuindo a esta posição o valor 100.
# (d) Mostre na tela cada valor do vetor A, um em cada linha.

A = []

for i in range(6):
    valores = float(input(f"Insira o valor {i + 1}: "))
    A.append(valores)

soma = (A[0] + A[1] + A[5])

print(soma)

A[4] = 100

for i in range(6):
    print(A[i])