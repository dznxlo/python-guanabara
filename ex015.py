d = int(input('insira o número de diárias:'))
k = float(input('insira o valor da rodagem em km:'))
a = (d*60)+(k*0.15)
print(f'o valor do aluguel é de R${a:.2f}')