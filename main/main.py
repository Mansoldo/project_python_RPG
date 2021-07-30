# Initial Project

# Menu Game
def menu_game():
    print('|', 20 * '-', 'MENU', 20 * '-', '|')
    print('|', 20 * '-', '1 - JOGAR', 15 * '-', '|')
    print('|', 20 * '-', '2 - INSTRUÇÕES', 10 * '-', '|')
    print('|', 20 * '-', '3 - CRÉDITOS', 12 * '-', '|')
    print('|', 20 * '-', '4 - SAÍDA', 15 * '-', '|')

    # Validation of options
    try:
        option = int(input())
        if option > 4 or option < 1:
            print('Escolha uma opção entre 1 e 4')
            spacing()
            menu_game()

    except ValueError:
        print('Erro de valor: favor inserir um valor entre 1 e 4')
        spacing()
        menu_game()

    if option == 1:
        begin_game()
    elif option == 2:
        instruction()
    elif option == 3:
        creditos()
    else:
        exit()

# Game instructions
def instruction():
    spacing()
    print('Bem vindo ao projeto "game" textual relacionado com o seção 2 do curso de Python completo.\n'
          'Serão apresentados 5 perguntas relacionadas ao tema, contendo 5 alternativas de "a" a "e".\n'
          'Em caso de escolha inexistente, será considerado errado a questão. \n'
          'No final será exibido a quantidade de questões certas. Para avançar para o módulo 3 do \n'
          'curso, precisará ter um aproveitamento superior a 70%¨.')
    spacing()
    select = input('Aperte a tecla "m" de Menu para retornar: ')
    select = select.capitalize()
    if select == 'M':
        spacing()
        menu_game()
    else:
        spacing()
        print('Opção inválida. Para retornar digite a tecla "m".')
        instruction()

# Game creditos for me
def creditos():
    print('Desenvolvedor: Diego Mansoldo \n'
          'Realizador: Diego Mansoldo \n'
          'Roteiro Original: Diego Mansoldo \n'
          'Design de Perguntas: Diego Mansoldo \n'
          'QA: Diego Mansoldo \n'
          'Diretor Executivo: Diego Mansoldo')
    spacing()
    select = input('Aperte a tecla "m" de Menu para retornar: ')
    select = select.capitalize()
    if select == 'M':
        spacing()
        menu_game()
    else:
        spacing()
        print('Opção inválida. Para retornar digite a tecla "m".')
        creditos()

# Adding a function to space
def spacing():
    print()

# Only a text to use in case of error when typing the player's name
def name_question():
    return input('Qual o seu nome? (Limitado a 10 caracteres e apenas letras) ')

# Checking if the name is valid
def name_check(nome):

    valido = True

    for char in nome:
        if char.isdigit():
            valido = False
            break

    if len(nome) > 10 or valido is False:
        return False

    return True

# The questions in a dict
def dictionary_questions():
    perguntas = {
        'Pergunta 1': {
            'pergunta': 'O que a função build-in "startswith" faz?',
            'resposta': {
                'a': 'Verifica o início de uma string',
                'b': 'Verifica o final de uma string',
                'c': 'Inicializa uma variável',
                'd': 'Valida o ínicio da string de acordo com o parâmetro',
                'e': 'Não existe esta função em Python',
            },
            'resposta_certa': 'd'
        },
        'Pergunta 2': {
            'pergunta': 'É possível fazer uso função Switch/Case?',
            'resposta': {
                'a': 'Não existe tal função em nenhuma linguagem',
                'b': 'Ela não existe em Python',
                'c': 'Pode-se usar apenas para substituir If/Else',
                'd': 'Pode ser aplicada apenas em OO',
                'e': 'Sim',
            },
            'resposta_certa': 'b'
        },
        'Pergunta 3': {
            'pergunta': 'É possível utilizar parâmetro nomeado em String Format?',
            'resposta': {
                'a': 'Sim',
                'b': 'Não',
                'c': 'Só é válido passagem de parâmetros normais',
                'd': 'Pode-se utilizar o "f" no início e depois o parãmetro',
                'e': 'Não há como formatar string',
            },
            'resposta_certa': 'a'
        },
        'Pergunta 4': {
            'pergunta': 'Qual o tipo de dado primitivo sai de um "input"?',
            'resposta': {
                'a': 'Int',
                'b': 'Float',
                'c': 'String',
                'd': 'Boolean',
                'e': 'Depende do tipo de entrada',
            },
            'resposta_certa': 'c'
        },
        'Pergunta 5': {
            'pergunta': 'Qual a outra forma de efetuar a contagem de caracteres além de len()?',
            'resposta': {
                'a': '__len__()',
                'b': 'lenght()',
                'c': 'leng()',
                'd': 'lengt()',
                'e': '_len_()',
            },
            'resposta_certa': 'a'
        },
    }
    return perguntas

# validation of questions and answers
def validation(perguntas):
    respostas_corretas = 0

    for pk, pv in perguntas.items():
        print(f'{pk}: {pv["pergunta"]}')
        print('Opções:')
        for rk, rv in pv['resposta'].items():
            print(f'\t({rk}): {rv}')

        usuario_resposta = input('Sua opção: ')
        if usuario_resposta == pv['resposta_certa']:
            respostas_corretas += 1
        print()

    return respostas_corretas

# Game beginning
def begin_game():
    try:
        checking = True

        while checking:
            nome = name_question()
            name_valid = name_check(nome)

            if not name_valid:
                print('Nome inválido! Favor inserir um nome válido')
                spacing()
            else:
                checking = False
                print('Seja bem vindo!!!')
                spacing()
                perguntas = dictionary_questions()
                respostas_certas = validation(perguntas)
                qtd_perguntas = len(perguntas)
                prc_acerto = int(respostas_certas / qtd_perguntas * 100)

                print(f'{nome}, você acertou {respostas_certas} questões de um total de {qtd_perguntas}!')

                msg = 'Você acertou mais de 70%, então pode seguir para o próximo capítulo' \
                    if prc_acerto >= 70 else 'Revise novamente a sessão 2, e refaça o teste'
                print(msg)
                exit()
    except:
        pass

spacing()
menu_game()
spacing()