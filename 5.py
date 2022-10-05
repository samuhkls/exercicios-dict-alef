'''
Faça com que no programa 2 o usuário pergunte um dia da semana e seu programa mostre na tela as aulas que serão dadas naquele dia, junto com seus horários respectivos.
'''
semana = {}

aulas = [
    {'AP41': "14:10", 'PR43': "16:10"},
    {'AE41': "14:10", 'EM41': "16:10"},
    {'LP41': "14:10", 'PR43': "16:10"},
    {'RL44':"14:10" , 'ET44': "15:00", 'EF44': "16:10"},
    {'DS44':"14:10", 'PJ42':"16:10"}
       ]

# preenchendo o dicionario 
semana['segunda'] = aulas[0]
semana['terça'] = aulas[1]
semana['quarta'] = aulas[2]
semana['quinta'] = aulas[3]
semana['sexta'] = aulas[4]

'''
for dia,aula in semana.items():
    if len(aula) == 2: # se tiver duas aulas no dia
        print(f'na {dia} as aulas são {aula}')
    else:
        print(f'na {dia} as aulas são {aula[0]} e {aula[1]} e {aula[2]}')
'''

'''
resp = input('qual dia voce deseja consultar? ')

if resp.lower() == 'segunda':
'''



