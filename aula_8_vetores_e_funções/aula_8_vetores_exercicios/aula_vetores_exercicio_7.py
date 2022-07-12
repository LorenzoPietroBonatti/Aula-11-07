# 7) Ler um conjunto de numeros, armazenando-os em vetor e calcular o quadrado dos
# componentes deste vetor, armazenando o resultado em outro vetor. Os conjuntos tem 5
# elementos cada. Imprimir todos os conjuntos.

conjunto = []

for i in range(5):
    valores = float(input("Insira os valores: "))
    conjunto.append(valores)

conj_quad = []

for i in range(5):
    valor_quad = conjunto[i] ** 2
    conj_quad.append(valor_quad)

print(conjunto)
print(conj_quad)
