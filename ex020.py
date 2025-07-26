from random import shuffle
x1 = input('insira o primeiro nome: ')
x2 = input('insira o segundo nome: ')
x3 = input('insira o terceiro nome: ')
x4 = input('insira o quarto nome: ')
lista = [x1, x2, x3, x4]
print(f'a lista: {lista}')
shuffle(lista)
print(f'a lista embaralhada: {lista}')