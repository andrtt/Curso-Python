a = 'A'
b = 'B'
c = 1.1
# A primeira chave {} se refere ao primeiro valor e assim sucessivamente.
string = 'b={nome2} a={nome1} a={nome1} c={nome3:.2f}'
formato = string.format(
    nome1=a, nome2=b, nome3=c)

print(formato)