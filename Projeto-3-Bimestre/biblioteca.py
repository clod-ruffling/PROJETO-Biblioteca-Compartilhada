leitores = []
proximo_id_leitor = 1

livros = []
proximo_id_livro = 1


# ==========================================
# GERENCIAMENTO DE LEITORES
# ==========================================

def consultar_leitor(id_leitor):
    for leitor in leitores:
        if leitor['id'] == id_leitor:
            return leitor
    return None


def buscar_leitor(nome):
    if not isinstance(nome, str) or nome.strip() == '':
        return None

    for leitor in leitores:
        if leitor['nome'].lower() == nome.strip().lower():
            return leitor
    return None


def inserir_leitor(nome):
    global proximo_id_leitor

    if not isinstance(nome, str) or nome.strip() == '':
        return None

    nome = nome.strip()

    if buscar_leitor(nome) is not None:
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


def editar_leitor(id_leitor, novo_nome):
    leitor = consultar_leitor(id_leitor)

    if leitor is None:
        return False

    if not isinstance(novo_nome, str) or novo_nome.strip() == '':
        return False

    novo_nome = novo_nome.strip()

    outro_leitor = buscar_leitor(novo_nome)

    if outro_leitor is not None and outro_leitor['id'] != id_leitor:
        return False

    leitor['nome'] = novo_nome
    return True


def remover_leitor(id_leitor):
    leitor = consultar_leitor(id_leitor)

    if leitor is None:
        return False

    if livros_por_leitor(id_leitor):
        return False

    leitores.remove(leitor)
    return True


# ==========================================
# GERENCIAMENTO DE LIVROS
# ==========================================

def consultar_livro(id_livro):
    for livro in livros:
        if livro['id'] == id_livro:
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

    if not isinstance(titulo, str) or titulo.strip() == '':
        return resultado

    for livro in livros:
        if titulo.strip().lower() in livro['titulo'].lower():
            resultado.append(livro)

    return resultado


def inserir_livro(titulo, id_leitor):
    global proximo_id_livro

    if not isinstance(titulo, str) or titulo.strip() == '':
        return None

    if not isinstance(id_leitor, int) or id_leitor <= 0:
        return None

    titulo = titulo.strip()

    leitor = consultar_leitor(id_leitor)

    if leitor is None:
        return None

    # Verifica se o leitor já possui um livro com esse título.

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


def editar_livro(id_livro, novo_titulo):
    livro = consultar_livro(id_livro)

    if livro is None:
        return False

    if not isinstance(novo_titulo, str) or novo_titulo.strip() == '':
        return False

    novo_titulo = novo_titulo.strip()

    # Impede títulos duplicados para o mesmo leitor.

    for outro_livro in livros:
        if outro_livro['id'] != id_livro:
            if outro_livro['titulo'].lower() == novo_titulo.lower():
                if outro_livro['leitor_id'] == livro['leitor_id']:
                    return False

    livro['titulo'] = novo_titulo
    return True


def transferir_livro(id_livro, id_novo_leitor):
    livro = consultar_livro(id_livro)
    leitor = consultar_leitor(id_novo_leitor)

    if livro is None or leitor is None:
        return False

    if id_novo_leitor <= 0:
        return False

    # Não permite transferir para o mesmo leitor.

    if livro['leitor_id'] == id_novo_leitor:
        return False

    # Verifica se o novo leitor já possui esse título.

    for outro_livro in livros:
        if outro_livro['titulo'].lower() == livro['titulo'].lower():
            if outro_livro['leitor_id'] == id_novo_leitor:
                return False

    livro['leitor_id'] = id_novo_leitor
    return True


def remover_livro(id_livro):
    livro = consultar_livro(id_livro)

    if livro is None:
        return False

    livros.remove(livro)
    return True


# ==========================================
# FUNÇÕES AUXILIARES E VALIDAÇÕES
# ==========================================

def ler_id(mensagem):
    while True:
        try:
            valor = input(mensagem).strip()

            id_digitado = int(valor)

            if id_digitado <= 0:
                raise ValueError

            return id_digitado

        except ValueError:
            print('Erro: digite um número inteiro positivo.')


def ler_texto(mensagem):
    while True:
        texto = input(mensagem).strip()

        if texto == '':
            print('Erro: este campo não pode ficar vazio.')
        else:
            return texto


def mostrar_leitor(leitor):
    print('ID:', leitor['id'], '- Nome:', leitor['nome'])


def mostrar_livro(livro):
    leitor = consultar_leitor(livro['leitor_id'])

    print('ID:', livro['id'], '- Título:', livro['titulo'])

    if leitor is not None:
        print('Leitor:', leitor['nome'])
    else:
        print('Leitor não encontrado.')


# ==========================================
# MENU DE CADASTROS E EDIÇÕES
# ==========================================

def menu_cadastros():
    while True:
        try:
            print('\n===== CADASTROS =====')
            print('1 - Cadastrar leitor')
            print('2 - Adicionar livro')
            print('3 - Editar leitor')
            print('4 - Editar livro')
            print('0 - Voltar')

            opcao = input('Escolha: ').strip()

            if opcao == '1':
                nome = ler_texto('Nome do leitor: ')
                leitor = inserir_leitor(nome)

                if leitor is None:
                    print('Esse leitor já está cadastrado.')
                else:
                    print('Leitor cadastrado! ID:', leitor['id'])

            elif opcao == '2':
                id_leitor = ler_id('ID do leitor: ')
                leitor = consultar_leitor(id_leitor)

                if leitor is None:
                    print('Leitor não encontrado.')
                else:
                    titulo = ler_texto('Título do livro: ')
                    livro = inserir_livro(titulo, id_leitor)

                    if livro is None:
                        print('Livro já cadastrado para esse leitor.')
                    else:
                        print('Livro cadastrado! ID:', livro['id'])

            elif opcao == '3':
                id_leitor = ler_id('ID do leitor: ')
                leitor = consultar_leitor(id_leitor)

                if leitor is None:
                    print('Leitor não encontrado.')
                else:
                    mostrar_leitor(leitor)
                    novo_nome = ler_texto('Novo nome: ')

                    if editar_leitor(id_leitor, novo_nome):
                        print('Leitor editado com sucesso!')
                    else:
                        print('Não foi possível editar. Nome já cadastrado.')

            elif opcao == '4':
                id_livro = ler_id('ID do livro: ')
                livro = consultar_livro(id_livro)

                if livro is None:
                    print('Livro não encontrado.')
                else:
                    mostrar_livro(livro)
                    novo_titulo = ler_texto('Novo título: ')

                    if editar_livro(id_livro, novo_titulo):
                        print('Livro editado com sucesso!')
                    else:
                        print('Não foi possível editar. Título duplicado para esse leitor.')

            elif opcao == '0':
                break

            else:
                print('Opção inválida.')

        except ValueError:
            print('Erro: valor informado inválido.')


# ==========================================
# MENU DE CONSULTAS
# ==========================================

def menu_consultas():
    while True:
        try:
            print('\n===== CONSULTAS =====')
            print('1 - Listar leitores e livros')
            print('2 - Consultar livros de um leitor')
            print('3 - Buscar livro pelo título')
            print('0 - Voltar')

            opcao = input('Escolha: ').strip()

            if opcao == '1':
                lista = listar_leitores()

                if len(lista) == 0:
                    print('Nenhum leitor cadastrado.')
                else:
                    for leitor in lista:
                        mostrar_leitor(leitor)
                        lista_livros = livros_por_leitor(leitor['id'])

                        if len(lista_livros) == 0:
                            print('Nenhum livro.')
                        else:
                            for livro in lista_livros:
                                print('  -', livro['titulo'])

            elif opcao == '2':
                id_leitor = ler_id('ID do leitor: ')
                leitor = consultar_leitor(id_leitor)

                if leitor is None:
                    print('Leitor não encontrado.')
                else:
                    print('Livros de', leitor['nome'])
                    lista = livros_por_leitor(id_leitor)

                    if len(lista) == 0:
                        print('Esse leitor não possui livros.')
                    else:
                        for livro in lista:
                            mostrar_livro(livro)

            elif opcao == '3':
                titulo = ler_texto('Digite o título ou parte dele: ')
                lista = buscar_livro(titulo)

                if len(lista) == 0:
                    print('Livro não encontrado.')
                else:
                    for livro in lista:
                        mostrar_livro(livro)

            elif opcao == '0':
                break

            else:
                print('Opção inválida.')

        except ValueError:
            print('Erro: valor informado inválido.')


# ==========================================
# MENU DE MOVIMENTAÇÕES
# ==========================================

def menu_movimentacoes():
    while True:
        try:
            print('\n===== MOVIMENTAÇÕES =====')
            print('1 - Transferir livro')
            print('2 - Remover livro')
            print('3 - Remover leitor')
            print('0 - Voltar')

            opcao = input('Escolha: ').strip()

            if opcao == '1':
                id_livro = ler_id('ID do livro: ')
                livro = consultar_livro(id_livro)

                if livro is None:
                    print('Livro não encontrado.')
                else:
                    id_leitor = ler_id('ID do novo leitor: ')

                    if transferir_livro(id_livro, id_leitor):
                        print('Livro transferido com sucesso!')
                    else:
                        print('Não foi possível transferir.')
                        print('Verifique se o leitor existe e se não possui esse livro.')

            elif opcao == '2':
                id_livro = ler_id('ID do livro: ')

                if remover_livro(id_livro):
                    print('Livro removido!')
                else:
                    print('Livro não encontrado.')

            elif opcao == '3':
                id_leitor = ler_id('ID do leitor: ')

                if remover_leitor(id_leitor):
                    print('Leitor removido!')
                else:
                    print('Não foi possível remover.')
                    print('Verifique se o leitor existe ou se ainda possui livros.')

            elif opcao == '0':
                break

            else:
                print('Opção inválida.')

        except ValueError:
            print('Erro: valor informado inválido.')


# ==========================================
# MENU PRINCIPAL
# ==========================================

def menu_principal():
    while True:
        try:
            print('\n=================================')
            print('   BIBLIOTECA COMPARTILHADA')
            print('=================================')
            print('1 - Cadastros')
            print('2 - Consultas')
            print('3 - Movimentações')
            print('0 - Sair')

            opcao = input('Escolha: ').strip()

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
                print('Opção inválida.')

        except ValueError:
            print('Erro: entrada inválida. Tente novamente.')


# ==========================================
# EXECUÇÃO DO PROGRAMA
# ==========================================

menu_principal()
