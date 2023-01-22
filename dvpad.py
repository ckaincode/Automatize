
a = input().split(" ")
n = len(a)
soma = 0
var = 0

lista_floatada = []
for i in a:
    i = float(i)
    lista_floatada.append(i)

for i in lista_floatada:
    soma += i

media = soma/n

for i in lista_floatada:
    var += ((media - i)**2)

k = (var/(n-1))**(1/2)

print(n)
print(var)
print(media)
print(f'dvpad = {k:.3f}')