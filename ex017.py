from math import hypot
co = float(input('comprimento do cateto oposto:'))
ca = float(input('comprimento do cateto adjacente:'))
print(f'a hipotenusa vai medir: {hypot(co,ca):.2f}')