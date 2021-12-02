# declarando variaveis
name = 'eric'
lastname = "li"

Name = 'eric'
nAme = 'eric'
na_me = 'eric'

# tipo de dados
print(type(name))
print(type(lastname))

# concatenação
full_name = name + ' ' + lastname
print(name + lastname)
print(full_name)

# tamanho da variável
print(len(name))

# indices da variável
print(name[0])
print(name[-3])
print(name[-2])
print(name[3])

# acesso a uma série de caracteres
# print(name[0:2])

# iniciais
first_letters = name[0] + lastname[0]
print(first_letters)

# manipulando
empresa = name[0] + lastname + 'tech'
email = name + '.' + lastname + '@' + empresa + '.com'
print(email)