# %%

# Uma maneira de definir listas
idades = [28, 42, 43, 35, 39, 28, 38]

print(idades)
# %%

thadeu = ['Thiago', 'Thadeu', 21, 'Casado', 18000]

print(thadeu)
# %%
type(thadeu)

# %%

# idade
print(thadeu[2])

# renda
print(thadeu[4])

print(thadeu[0])

# %%

idades = [28, 42, 43, 35, 39, 28, 38]

print('Soma idades:', sum(idades))

print('Quantidade idades:', len(idades))

print('Média idades:', sum(idades) / len(idades))

print('Menor idade:', min(idades))

print('Maior idade:', max(idades))
# %%

thadeu = [
    'Thiago Thadeu', 
    21, 
    True, 
    'Casado', 
    ['Atleta', 'Estagiário', 'ds.junior', 'ds.pl', 'ds.sr'],
    [[300, 500, 700, 900, 1000]],
    ['Mão', 'Quase', 'Larissa']
]

print('Tamanho de thadeu:', len(thadeu))

print(thadeu[-1][-1])
# %%

# primeiros 4 elementos 
thadeu[0:4]
# %%

thadeu[4][-2:]

# %%
# thadeu[ start : stop ]

# %%

salarios = thadeu[5]
print(salarios[0][::2])

# thadeu[ start : stop : step ]
