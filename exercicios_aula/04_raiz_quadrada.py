# Faça um programa que receba um número inteiro
# e calcule a raiz quadrada e exiba o resultado.

numero = int(input('Entre com um número inteiro para calcular a sua raiz quadarda: '))

raiz = numero ** (1/2)
raiz = round(raiz, 4)

print('A raiz quadrada de', numero, 'é:', raiz)