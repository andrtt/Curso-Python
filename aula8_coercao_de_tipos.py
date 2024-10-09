# Conversão de tipos, coerção
# type convertion, typecasting, coercion
# é o ato de converter um tipo em outro
# tipos imutáveis e primitivos:
# str, int, float, bool
print(1 + 1) # Somou
print('a' + 'b') # Concatenou (Pois Python é uma linguagem dinamica)
# print('1'+ 1) # Isso daria errado.
print(int('1'), type(int('1')))
print(int('1') + 1) # Transformeti a string em int

print(type(float('1') + 1))
print(bool(' '))
print(str(11) + 'b') # Transformei 11 em string e ai concatenou com b