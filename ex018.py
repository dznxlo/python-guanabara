from math import sin,cos,tan,radians
x = float(input('insira o ângulo desejado: '))
print(f'o ângulo de {x} tem o seno de {sin(radians(x)):.2f}')
print(f'o ângulo de {x} tem o cosseno de {cos(radians(x)):.2f}')
print(f'o ângulo de {x} tem o tangente de {tan(radians(x)):.2f}')