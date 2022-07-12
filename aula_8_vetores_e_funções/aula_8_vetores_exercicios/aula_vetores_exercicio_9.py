# 9) Faça um programa que leia um vetor de 8 posições e, em seguida, leia também dois
# valores X e Y quaisquer correspondentes a duas posições no vetor. Ao final seu programa
# deverá escrever a soma dos valores encontrados nas respectivas posições X e Y. Se o usuário
# digitar valores inválidas para X ou Y mostre uma mensagem de erro e peça novos valores até 
# que ambos os valores sejam válidos.

lista = []

for i in range(8):
    elementos = float(input("Insira os elementos: "))
    lista.append(elementos)

for i in range(1):
    x = int(input("Insira X: "))
    y = int(input("Insira Y: "))

    if x < 0 or x > 7:
        print("Erro no valor de X")
        continue

    elif y < 0 or y > 7:
        print("Erro no Y")
        continue

soma = lista[x] + lista[y]

print(f"A soma é igual a: {soma}")
