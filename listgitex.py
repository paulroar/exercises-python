
print("\n-------------------------------------------------\n")

# 1. Ler uma lista de 5 números inteiros e mostrá-los

lsnum = []

for i in range(1, 6):
    lsnum.append(int(input(f"Digite o {i}º número: ")))

print(f"Números inseridos: {lsnum}")

print("\n-------------------------------------------------\n")

# 2. Ler 10 números reais e mostrá-los na ordem inversa

nunreal = []

for i in range(1, 11):
    nunreal.append(float(input(f"Digite o {i}º número real: ")))

# O [::-1] inverte a lista automaticamente
print(f"Ordem inversa: {nunreal[::-1]}")

print("\n-------------------------------------------------\n")

# 3. Ler 4 notas, mostrar as notas e a média

notas = []

for i in range(1, 5):
    notas.append(float(input(f"Digite a {i}ª nota: ")))

media = sum(notas) / len(notas)

print(f"Notas: {notas}")
print(f"Média: {media:.2f}")

print("\n-------------------------------------------------\n")

# 4. Ler 10 caracteres, contar e imprimir as consoantes

consoantes = []
vogais = "aeiouAEIOU"

for i in range(1, 11):
    char = input(f"Digite o {i}º letra: ")
    if char.isalpha() and char not in vogais:
        consoantes.append(char)

print(f"Total de consoantes: {len(consoantes)}")
print(f"Consoantes encontradas: {consoantes}")

print("\n-------------------------------------------------\n")

# 5. Ler 20 números, separar em pares e ímpares, e imprimir os três

lista = []
par = []
impar = []

for i in range(1, 21):
    num = int(input(f"Digite o {i}º número: "))
    lista.append(num)
    if num % 2 == 0:
        par.append(num)
    else:
        impar.append(num)

print(f"Lista completa: {lista}")
print(f"Pares: {par}")
print(f"Ímpares: {impar}")

print("\n-------------------------------------------------\n")

# 6. Calcular médias de 10 alunos e contar quantos têm média >= 7.0

aprovados = 0

for aluno in range(1, 11):
    print(f"--- Aluno {aluno} ---")
    soma = 0
    for i in range(1, 5):
        soma += float(input(f"Nota {i}: "))

    media = soma / 4
    if media >= 7.0:
        aprovados += 1

print(f"\nNúmero de alunos com média maior ou igual a 7.0: {aprovados}")

print("\n-------------------------------------------------\n")

# 7. Ler 5 números inteiros, mostrar a soma, multiplicação e os números

fullnum = []
soma = 0
multiplicacao = 1

for i in range(1, 6):
    num = int(input(f"Digite o {i}º número: "))
    fullnum.append(num)
    soma += num
    multiplicacao *= num

print(f"Números: {fullnum}")
print(f"Soma: {soma}")
print(f"Multiplicação: {multiplicacao}")

print("\n-------------------------------------------------\n")

# 8. Ler idade e altura de 5 pessoas e imprimir na ordem inversa

idades = []
alturas = []

for i in range(1, 6):
    print(f"--- Pessoa {i} ---")
    idades.append(int(input("Idade: ")))
    alturas.append(float(input("Altura (m): ")))

print("\nDados na ordem inversa:")
for i in range(4, -1, -1):
    print(f"Idade: {idades[i]} anos | Altura: {alturas[i]:.2f}m")

print("\n-------------------------------------------------\n")

# 9. Ler lista A de 10 números e mostrar a soma dos quadrados

lista_a = []

for i in range(1, 11):
    lista_a.append(int(input(f"Digite o {i}º número: ")))

soma_quadrados = sum(n ** 2 for n in lista_a)

print(f"Soma dos quadrados dos elementos: {soma_quadrados}")

print("\n-------------------------------------------------\n")


# 10. Intercalar duas listas de 10 elementos numa terceira de 20

l1 = [input(f"Lista 1 - Elem {i}: ") for i in range(1, 11)]
l2 = [input(f"Lista 2 - Elem {i}: ") for i in range(1, 11)]

l3 = [val for pair in zip(l1, l2) for val in pair]

print(f"Lista intercalada: {l3}")