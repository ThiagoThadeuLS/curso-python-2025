# %%

lista = [2, 132, "thadeu", ["ds", "de", "da"], True]

lista[2]
# %%

# pares de chave/valor

dados_thadeu = {
    'sobrenome':'Santos',
    'nome':'thadeu', 
    'filhos':False,
    'formacao':['ensino médio', 'engenharia de software'],
    'cargos':[
        {'nome':'atleta', 'empresa':'MTC'},
        {'nome':'estagiário', 'empresa':'MTC'},
        {'nome':'analista de dados', 'empresa':'MTC'}
    ]
}

# %%
print(dados_thadeu)
print(dados_thadeu['formacao'][-1])
print(dados_thadeu['cargos'][-1]['empresa'])

# %%

dados_thadeu['Estado civil'] = 'casado'
# %%

print(dados_thadeu)

print('chaves:', dados_thadeu.keys())
print('valores:', dados_thadeu.values())
print('items:', dados_thadeu.items())
# %%

for i in [10,20,45,28,"Thadeu"]:
    print(i)

# %%

for i in dados_thadeu:
    print(i, '->',dados_thadeu[i])
# %%

for chave, valor in dados_thadeu.items():
    print(chave, '->', valor)