a = input().split(' ')
lista_de_notas = []

for i in a:
    if ',' in i:
        j = i[0]+'.'+i[2]+i[3]
        j = float(j)
        lista_de_notas.append(j)

soma = 0

for _ in lista_de_notas:
    soma += _

k = len(lista_de_notas)

print(soma/k)