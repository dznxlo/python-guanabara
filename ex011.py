x = float(input('insira a largura da parede em metros:'))
y = float(input('insira a altura da parede em metros:'))
a = x*y
print(f'a parede tem a dimensão de {x:.2f}x{y:.2f} e sua área é de:{a:.2f}m²')
print(f'para pintar essa parede, seram necessários {a/2:.2f}L de tinta')