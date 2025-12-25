# %%

dados_thadeu = [21, 0, 'casado', 'estudante']
dados_thadeu
# %%

dados_thadeu.append('1234567.2345')
dados_thadeu[0] = 20
dados_thadeu
# %%
# tupla_thadeu = 21, 0, 'casado', 'estudante'
tupla_thadeu = (21, 0, 'casado', 'estudante', ['mão', 'quase', 'larissa'])
tupla_thadeu

print(type(tupla_thadeu))

# %%

print(tupla_thadeu)

# %%
tupla_thadeu[-1].append('nunca')
print(tupla_thadeu)