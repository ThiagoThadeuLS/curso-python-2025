# %%
arquivo = 'data.csv'

with open(arquivo) as open_file:
    lines = open_file.readlines()

for l in lines:
    print(l)
# %%

dados = dict()

chaves = lines[0].strip('\n').split(';')
for chave in chaves:
    dados[chave] = []

# %%

for registro in lines[1:]:
    valores = registro.strip('\n').split(';')

    for i in range(len(valores)):
        dados[chaves[i]].append(valores[i])

dados

# %%

idades = list()
for i in dados['idade']:
    idades.append(int(i))

idades
media = sum(idades) / len(idades)
media