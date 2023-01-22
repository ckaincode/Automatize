Valores = list(map(float,input().split(" ")))
n = len(Valores)
soma = 0.0


for i in Valores:
    soma += i

media = soma/n
memoria = 0.0 #Memoria para guardar os valores do numerador da variância

for i in Valores:
    memoria += ((media - i)**2)

k = (memoria/(n-1))**(1/2) #Raiz da variância, a qual é o desvio padrão


print(f'Desvio Padrão = {k:.3f}') #Retorna o desvio com três casas dacimais
