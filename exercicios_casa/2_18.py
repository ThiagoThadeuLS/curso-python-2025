# %%
frases = {}

while True:

    frase = input('Entre com a frase: ')
    if frase == "":
        break

    if frase not in frases:
        frases[frase] = 1
    else:
        frases[frase] += 1 



for chave, valor in frases.items():
    print(f'{chave} -> {valor}')

# %%

frases = {
    'oi': 1,
    'ola': 10,
    'teste': 5,
    'oi tudo bem': 3,
    'test': 2
}

items = list(frases.items())
items.sort(key=lambda x: x[-1], reverse=True)

for i, j in items:
    print(f'{i} -> {j}')