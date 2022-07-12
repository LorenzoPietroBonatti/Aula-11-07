# 5) Ler um vetor com 5 nomes de pessoas, após pedir que o usuário digite um nome qualquer 
# de pessoa. Escrever a mensagem “ACHEI”, se o nome estiver armazenado no vetor de nomes ou 
# “NÃO ACHEI” caso contrário.

nomes = ["João" , "Pedro", "Anna", "Gabriela", "Marya"]

nome = str(input("Insira um nome: "))

nome_uppercase = nome.capitalize()

print(nome_uppercase)

if nome_uppercase in nomes:
    print("Achei")

else:
    print("Não achei")