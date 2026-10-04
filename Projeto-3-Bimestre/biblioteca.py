leitores = []
livros = []
responsaveis = []

while True:

    print('=================================')
    print('      BIBLIOTECA COMPARTILHADA')
    print('=================================')
    print('1 - Cadastrar leitor')
    print('2 - Adicionar livro')
    print('3 - Listar leitores e livros')
    print('4 - Consultar livros de um leitor')
    print('5 - Transferir livro')
    print('0 - Sair')
    print('=================================')

    opcao = input('Escolha uma opção: ')

    # cadastra leitor

    if opcao == '1':
        nome = input('Digite o nome do leitor: ')
        if nome in leitores:
            print('Esse leitor já está cadastrado.')
        else:
            leitores.append(nome)
            print('Leitor cadastrado com sucesso.')

    # adiciona livros

    elif opcao == '2':
        nome = input('Digite o nome do leitor: ')
        if nome not in leitores:
            print('Leitor não encontrado.')
        else:
            titulo = input('Digite o título do livro: ')
            if titulo in livros:
                print('Esse livro já está cadastrado.')
            else:
                livros.append(titulo)
                responsaveis.append(nome)
                print('Livro adicionado com sucesso.')

    # lista dos leitores e livros

    elif opcao == '3':
        print()
        print('========== BIBLIOTECA ==========')
        if len(leitores) == 0:
            print('Nenhum leitor cadastrado.')
        else:
            for leitor in leitores:
                print()
                print('Leitor:', leitor)
                print('Livros:')
                tem_livro = False
                for i in range(len(livros)):

                    if responsaveis[i] == leitor:
                        print('-', livros[i])
                        tem_livro = True
                if tem_livro == False:
                    print('- Nenhum livro')

    # consulta livros

    elif opcao == '4':
        nome = input('Digite o nome do leitor: ')
        if nome not in leitores:
            print('Leitor não encontrado.')
        else:
            print()
            print('========== LIVROS DE', nome.upper(), '==========')
            tem_livro = False
            for i in range(len(livros)):
                if responsaveis[i] == nome:
                    print('-', livros[i])
                    tem_livro = True
            if tem_livro == False:
                print('Esse leitor não possui livros.')

    # transfere livro

    elif opcao == '5':
        leitor_atual = input('Digite o nome do leitor atual: ')
        if leitor_atual not in leitores:
            print('Leitor não encontrado.')
        else:
            titulo = input('Digite o título do livro: ')
            encontrado = False
            for i in range(len(livros)):
                if livros[i] == titulo and responsaveis[i] == leitor_atual:
                    novo_leitor = input('Digite o nome do novo leitor: ')
                    if novo_leitor in leitores:
                        responsaveis[i] = novo_leitor
                        print('Livro transferido com sucesso.')
                    else:
                        print('Novo leitor não encontrado.')
                    encontrado = True
            if encontrado == False:
                print('Livro não encontrado para esse leitor.')

    # saida e opção invalida

    elif opcao == '0':
        print('Programa encerrado.')
        break
    else:
        print('Opção inválida.')