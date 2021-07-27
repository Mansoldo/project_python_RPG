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

    except ValueError as erro:
        print('Por favor, digite um número entre 1 e 4')
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


spacing()

print('Bem vindo ao projeto "RPG" textual relacionado com o seção 2 do curso de Python completo.\n'
      'Serão apresentados 5 perguntas relacionadas ao tema, contendo 4 alternativas. No final \n'
      'será exibido a quantidade de questões certas. Para avançar para o módulo 3 do curso, precisará\n'
      'ter um aproveitamento superior a 70%¨.')
spacing()
menu_game()

spacing()

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
            print('Que comece os jogos!')
except:
    pass
