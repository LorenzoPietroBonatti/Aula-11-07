# 3) Faça um programa que receba do usuario um vetor com 5 posições. Em seguida, mostre
# o maior e o menor elemento do vetor.

list = []

for i in range(5):
    number = float(input("Inser a number: "))
    list.append(number)

highest_number = max(list)
lowest_number = min(list)

print(f"The highest number is: {highest_number}")
print(f"The lowest number is: {lowest_number}")