# %%

idades = []


while True:
    idade = input('Entre com a idade: ')

    if idade == "":
        break

    idades.append(int(idade))

media = sum(idades) / len(idades)
minimo = min(idades)
maximo = max(idades)
qtde = len(idades)

print('MÉDIA:', media)
print('MINIMO:', minimo)
print('MÁXIMO:', maximo)
print('QUANTIDADE:', qtde)