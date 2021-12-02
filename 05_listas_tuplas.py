# tuplas
# tuplas são imutáveis
months = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

print(months)
print(type(months))
print(len(months))
print(months[11])

# listas
# listas são mutáveis
people = ['joao', 'maria', 'pedro', 'helena']
people2 = ['eric', 'flavia', 'li']

print(people)
print(type(people))
print(len(people))
people[1] = 'maírah' # mudar valor da chave
people.append('ricardo') # adicionar valor na lista
people.insert(1, 'paula') # adiciona valor em um índice específico
people.sort() # ordena a lista
people.pop(1) # retirar um elemento indicando um índice
people.remove('paula') # retirar um elemento indicando um valor
allPeople = people + people2 # concatenar listas
print(people)
print(allPeople)