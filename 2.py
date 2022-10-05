'''
Crie um dicionário vazio chamado semana = {} e o complete com uma chave para cada dia útil da semana,
tendo como seu valor uma lista com as aulas que você tem nesse dia no CEAP e exiba esse dicionário na tela.
'''

semana = {}

aulas = [
    ['AP41', 'PR43'],
    ['AE41', 'EM41'],
    ['LP41', 'PR43'],
    ['RL44', 'ET44', 'EF44'],
    ['DS44', 'PJ42']
       ]

# preenchendo o dicionario 
semana['segunda'] = aulas[0]
semana['terça'] = aulas[1]
semana['quarta'] = aulas[2]
semana['quinta'] = aulas[3]
semana['sexta'] = aulas[4]

for dia,aula in semana.items():
    if len(aula) == 2: # se tiver duas aulas no dia
        print(f'na {dia} as aulas são {aula[0]} e {aula[1]}')
    else: # se tiver 3 aulas no dia 
        print(f'na {dia} as aulas são {aula[0]} e {aula[1]} e {aula[2]}')
