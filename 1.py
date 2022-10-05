"""
Faça um dicionário com o nome de 5 alunos da sala, associados ao número do tênis que cada um calça e exiba esse dicionário na tela.
"""

alunos = {
    'rafinha': 38.5,
    'diogo': 39,
    'eduardo': 36,
    'alexander': 38,
    'otavio': 40
    }

for aluno, pe in alunos.items():
    print(aluno.capitalize(), 'calça', pe)

