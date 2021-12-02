# declarando variaveis
num1 = 2
num2 = 5.5

# tipo de dado
print(type(num1))

# manipulando
num3 = num1 + num2
num4 = num1 + 5
print(type(num3))
print(type(num4))

# manipulando
print(num1 ** 5)
print(num2 + 5 / 2)

# verificando
print(5 > 2)
print(2 > 5)

# condição
age = 17

if age >= 18:
  print('Acesso liberado')
else:
  print('Acesso negado')

# cálculos
# https://docs.python.org/3/library/math.html
import math
# raíz quadrada
print(math.sqrt(16))
# fatorial
# 5*4*3*2*1
print(math.factorial(5))
num5 = 20
print(math.factorial(num5))
