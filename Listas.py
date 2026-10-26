notas = [15, 12, 20, 19, 11, 18, 16, 15, 20, 12]

print(notas[9])
print(notas[5])

print(notas[-1])
print(notas[-2])

# get tamanho da lista

print(len(notas))
print(notas.__len__())

# mostra a lista toda
print(notas)

notas.insert(0, 19)


# add elm a lista

notas.append(15) # add no final

# mostra lista toda
print(notas)

notas.insert(312, 18)

# mostra lista toda
print(notas)

# remover

#por pos
print(notas.pop()) # remove e revolve o último
print(notas)

print(notas.pop(2)) # remove e revolve o elm na posição indicada


# remover por val

print(notas.remove(19)) # remove o valor indicado
print(notas)

notas.append(12)

print(notas)
print(notas.remove(12)) # remove a 1a vez valor indicado aparece

print(notas)

for nota in notas:
    print("Nota:", nota)

def estado(nota : {__ge__}) -> str:
    print("Nota:", nota)

print("---------------------")

notas.sort()
print(notas)

notas.reverse()
print(notas)

notas.extend(notas)
print(notas)


print(notas,index(4))

print(notas.index(4, 7))
print(notas.__contains__(4))
print(4 in notas)


print("---------------------")


nomes = [
    "Afonso", "Mariana", "Pedro", "Catarina", "Rodrigo",
    "Beatriz", "Francisco", "Inês", "Guilherme", "Sofia",
    "Tomás", "Matilde", "Diogo", "Carolina", "João",
    "Margarida", "Rafael", "Leonor", "Duarte", "Rita",
    "Henrique", "Teresa", "Martim", "Cláudia", "Samuel"
]

print(nomes[:5]) # todos os elm do idx 0 até ao 5-1......-> nomes[:n]...-> todos os elm entre o idx 0 e n-1
print(nomes[0:5]) # todos os elm do idx 0 até ao 5-1......-> nomes[m:n]...-> todos os elm entre o idx m e n-1


print(nomes[10:18])

tp = ("valor1", "valor2", "valor3", "valor1", 10, True)

print(tp)
print(tp[0])
print(tp[1])

print(tp.count("valor1"))

print(tp.index("valor1"))

for i in tp:
    print(i)

print("--------------")
aluno = ("Carlos", "Java", 13)

print(aluno[2])

aluno_aux = list[str | int](aluno) # converte o tuplo para lista
aluno_aux[2] = 14 # altera o valor numa lista
aluno = tuple[str | int](aluno_aux) # volta a converter para tuplo

print(aluno[2])

nome, curso, nota = aluno

print(f"O {nome} teve {nota} a {curso}")

aluno2 = ("Jose", "Java", 11)

alunos = aluno + aluno2
print(alunos)

alunos2 = aluno2 * 3
print(alunos2)

target = "Java"
print(target in alunos)















