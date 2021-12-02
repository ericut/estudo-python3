# exercício listas e tuplas
months = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro')

birthday = input('Data de nascimento (dd-mm-aaaa):')
birthMonth = int(birthday[3:5]) - 1

birthMonthLiteral = months[birthMonth]

print('Você nasceu no mês de ' + birthMonthLiteral)