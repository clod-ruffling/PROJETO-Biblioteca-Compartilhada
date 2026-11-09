leitores = []
proximo_id_leitor = 1

livros = []
proximo_id_livro = 1

# gerenciamento de leitores

def consultar_leitor(id_leitor):
    for leitor in leitores:
        if leitor['id'] == id_leitor:
            return leitor
    return None


def buscar_leitor(nome):
    for leitor in leitores:
        if leitor['nome'].lower() == nome.lower():
            return leitor
    return None


def inserir_leitor(nome):
    global proximo_id_leitor

    if buscar_leitor(nome) != None:
        return None

    leitor = {
        'id': proximo_id_leitor,
        'nome': nome
    }

    leitores.append(leitor)
    proximo_id_leitor += 1
    return leitor


def listar_leitores():
    return leitores


def remover_leitor(id_leitor):
    leitor = consultar_leitor(id_leitor)

    if leitor == None:
        return False

    if livros_por_leitor(id_leitor):
        return False

    leitores.remove(leitor)
    return True

# gerenciamento de livros

def consultar_livro(id_livro):
    for livro in livros:
        if livro[ 'id'] == id_livro:
            return livro
    return None


def livros_por_leitor(id_leitor):
    resultado = []

    for livro in livros:
        if livro['leitor_id'] == id_leitor:
            resultado.append(livro)

    return resultado


def buscar_livro(titulo):
    resultado = []

    for livro in livros:
        if titulo.lower() in livro['titulo'].lower():
            resultado.append(livro)

    return resultado


def inserir_livro(titulo, id_leitor):
    global proximo_id_livro

    leitor = consultar_leitor(id_leitor)

    if leitor == None:
        return None

    # verifica se o leitor ja possui um livro com esse titulo.

    for livro in livros:
        if livro['titulo'].lower() == titulo.lower():
            if livro['leitor_id'] == id_leitor:
                return None

    livro = {
        'id': proximo_id_livro,
        'titulo': titulo,
        'leitor_id': id_leitor
    }

    livros.append(livro)
    proximo_id_livro += 1
    return livro


def listar_livros():
    return livros


def transferir_livro(id_livro, id_novo_leitor):
    livro = consultar_livro(id_livro)
    leitor = consultar_leitor(id_novo_leitor)

    if livro == None or leitor == None:
        return False

    livro['leitor_id'] = id_novo_leitor
    return True


def remover_livro(id_livro):
    livro = consultar_livro(id_livro)

    if livro == None:
        return False

    livros.remove(livro)
    return True

# funções auxiliares

def ler_id(mensagem):
    while True:
        valor = input(mensagem)

        if valor.isdigit():
            return int(valor)

        print('Digite um numero valido.')


def mostrar_leitor(leitor):
    print('ID:', leitor['id'], '- Nome:', leitor['nome'])


def mostrar_livro(livro):
    leitor = consultar_leitor(livro['leitor_id'])

    print('ID:', livro['id'], '- Titulo:', livro['titulo'])

    if leitor != None:
        print('Leitor:', leitor['nome'])
    else:
        print('Leitor nao encontrado.')

# menu de cadastros

def menu_cadastros():
    while True:
        print('\n===== CADASTROS =====')
        print('1 - Cadastrar leitor')
        print('2 - Adicionar livro')
        print('0 - Voltar')

        opcao = input('Escolha: ')

        if opcao == '1':
            nome = input('Nome do leitor: ').strip()

            if nome == '':
                print('Digite um nome.')
            else:
                leitor = inserir_leitor(nome)

                if leitor == None:
                    print('Esse leitor ja esta cadastrado.')
                else:
                    print('Leitor cadastrado! ID:', leitor['id'])

        elif opcao == '2':
            id_leitor = ler_id('ID do leitor:')
            leitor = consultar_leitor(id_leitor)

            if leitor == None:
                print('Leitor nao encontrado.')
            else:
                titulo = input('Titulo do livro: ').strip()

                if titulo == '':
                    print('Digite um titulo.')
                else:
                    livro = inserir_livro(titulo, id_leitor)

                    if livro == None:
                        print('Livro ja cadastrado para esse leitor.')
                    else:
                        print('Livro cadastrado! ID:', livro['id'])

        elif opcao == '0':
            break
        else:
            print('Opcao invalida.')

# menu de consultas

def menu_consultas():
    while True:
        print('\n===== CONSULTAS =====')
        print('1 - Listar leitores e livros')
        print('2 - Consultar livros de um leitor')
        print('3 - Buscar livro pelo titulo')
        print('0 - Voltar')

        opcao = input('Escolha: ')

        if opcao == '1':
            lista = listar_leitores()

            if len(lista) == 0:
                print('Nenhum leitor cadastrado.')
            else:
                for leitor in lista:
                    mostrar_leitor(leitor)
                    lista_livros = livros_por_leitor(leitor['id'])

                    if len(lista_livros) == 0:
                        print('Nenhum livro')
                    else:
                        for livro in lista_livros:
                            print('  -', livro['titulo'])

        elif opcao == '2':
            id_leitor = ler_id('ID do leitor: ')
            leitor = consultar_leitor(id_leitor)

            if leitor == None:
                print('Leitor nao encontrado.')
            else:
                print('Livros de', leitor['nome'])
                lista = livros_por_leitor(id_leitor)

                if len(lista) == 0:
                    print('Esse leitor nao possui livros.')
                else:
                    for livro in lista:
                        mostrar_livro(livro)

        elif opcao == '3':
            titulo = input('Digite o titulo ou parte dele: ')
            lista = buscar_livro(titulo)

            if len(lista) == 0:
                print('Livro nao encontrado.')
            else:
                for livro in lista:
                    mostrar_livro(livro)

        elif opcao == '0':
            break
        else:
            print('Opcao invalida.')

# menu de movimentacoes

def menu_movimentacoes():
    while True:
        print('\n===== MOVIMENTACOES =====')
        print('1 - Transferir livro')
        print('2 - Remover livro')
        print('3 - Remover leitor')
        print('0 - Voltar')

        opcao = input('Escolha: ')

        if opcao == '1':
            id_livro = ler_id('ID do livro: ')
            livro = consultar_livro(id_livro)

            if livro == None:
                print('Livro nao encontrado.')
            else:
                id_leitor = ler_id('ID do novo leitor: ')

                if transferir_livro(id_livro, id_leitor):
                    print('Livro transferido!')
                else:
                    print('Novo leitor nao encontrado.')

        elif opcao == '2':
            id_livro = ler_id('ID do livro:')

            if remover_livro(id_livro):
                print('Livro removido!')
            else:
                print('Livro nao encontrado!')

        elif opcao == '3':
            id_leitor = ler_id('ID do leitor: ')

            if remover_leitor(id_leitor):
                print('Leitor removido!')
            else:
                print('Leitor nao encontrado ou possui livros.')

        elif opcao == '0':
            break
        else:
            print('Opcao invalida.')

# menu principal

def menu_principal():
    while True:
        print('\n=================================')
        print('   BIBLIOTECA COMPARTILHADA')
        print('=================================')
        print('1 - Cadastros')
        print('2 - Consultas')
        print('3 - Movimentacoes')
        print('0 - Sair')

        opcao = input('Escolha: ')

        if opcao == '1':
            menu_cadastros()
        elif opcao == '2':
            menu_consultas()
        elif opcao == '3':
            menu_movimentacoes()
        elif opcao == '0':
            print('Programa encerrado.')
            break
        else:
            print('Opcao invalida.')

menu_principal()
