# 2) Escreva um programa que leia 5 numeros e os armazene em um vetor. Mostre o vetor, o 
# maior elemento e a posição que ele se encontra.

from operator import index


listaaa = []

for i in range(5):
    num = int(input("Insira um valor: "))
    listaaa.append(num)

maior_num = max(listaaa)
print(f"O maior valor é: {maior_num}")

if maior_num in listaaa:
    result = listaaa.index(maior_num)

print(f"O índice é: {result}")
