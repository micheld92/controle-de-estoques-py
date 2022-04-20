import datetime
from datetime import date

funcionarios = ({'nome': 'Matheus', 'codigo': '1', 'senha': 'm','nivel': '1'},
                {'nome': 'Rafael', 'codigo': '2', 'senha': 'r', 'nivel': '2'},
                {'nome': 'Lucas', 'codigo': '3', 'senha': 'l', 'nivel': '3'})
#original estoque = list()
item = dict()

estoque = ({'descricao': 'paracetamol', 'fabricante': 'neoquimica', 'codigo': 0, 'lote': 'a192', 'quantidade': 100, 'dataEntrada': '12', 'horaEntrada': '16'},
           {'descricao': 'aspirina', 'fabricante': 'bayer', 'codigo': 1, 'lote': 'b123', 'quantidade': 12, 'dataEntrada': '22', 'horaEntrada': '19'},
           {'descricao': 'coristina', 'fabricante': 'ache', 'codigo': 2, 'lote': 'c123', 'quantidade': 1212, 'dataEntrada': '22', 'horaEntrada': '19'})


codigo = int(0)
nivelPermissao = ''
def separador_linha(separador, vezes):
    print(f'{separador * vezes}')

def cabecalho():
    separador_linha('*', 42)
    print(f'Sistema de controle de estoque simples'.center(42))
    print(f'Autor: Michel M. Duarte'.center(42))
    print(f'mmd_rg@hotmail.com'.center(42))
    separador_linha('*', 42)

def criaItem():
    resp = True
    while resp:
        des = str(input('Descrição: ').upper())
        fab = str(input('Fabricante: ').upper())
        lot = str(input('Lote: '))
        qtd = int(input('Quantidade: '))

        insereNoEstoque(des, fab, lot, qtd)

        while True:
            resp = str(input('Deseja adicionar mais itens? (S/N) ')).upper()[0]
            if resp in 'SN':
                break
            print('Resposta inválida')
        if resp == 'N':
            resp = False

def insereNoEstoque(descricao, fabricante, lote, quantidade):
    global codigo
    item['descricao'] = str(descricao)
    item['fabricante'] = str(fabricante)
    item['codigo'] = codigo
    item['lote'] = str(lote)
    item['quantidade'] = int(quantidade)
    item['dataEntrada'] = '{}/{}/{}'.format(date.today().day, date.today().month, date.today().year)
    item['horaEntrada'] = datetime.datetime.now().strftime('%H:%M')
    estoque.append(item.copy())
    codigo += 1


def buscarNoEstoque():
    global indice
    item_buscado = str(input('Digite a descrição ou codigo do item: '))
    if (item_buscado[0:3].isnumeric()):#verifica se os 3 primeiros digitos são numéricos
        chave = 'codigo'
        item_buscado = int(item_buscado)
    else:
        chave = 'descricao'
    print(chave)
    for i in estoque:
        if item_buscado == i[chave]:
            print(f'Descrição: {i["descricao"]}')
            indice = estoque.index(i)
            print(indice)

def verificaExistencia(cod=-1):
    #verificar quantidade, se maior que 0 executar
    resp = str(input('\nO item já existe no estoque, deseja adicionar assim mesmo? (s/n)  ')).upper()[0]
    if resp == 'N':
        return 0 #deverá reexibir o menu
    print(f'executa os procedimentos de adicao aos itens ja existentes')

def listarTodos():
    separador_linha('*', 30)
    if (len(estoque) == 0):
        print(f'O estoque está vazio!')
        return 0
    '''for i in estoque:
        print(f'Descrição: {i["descricao"]}')
        print(f'Fabricante: {i["fabricante"]}')
        print(f'Lote: {i["lote"]}')
        print(f'Quantidade: {i["quantidade"]}')
        print(f'Data de entrada: {i["dataEntrada"]}')
        print(f'Hora de entrada: {i["horaEntrada"]}')
        separador_linha('*', 30)'''
def editarItem():
    print('editar item')

def login(codUsu, senhaUsu):
    global nivelPermissao
    for i in funcionarios:
        if (codUsu in {i["codigo"]} and senhaUsu in {i["senha"]}):
            nivelPermissao = i["nivel"]
            print("Autenticado como:")
            print(f'Usuário: {i["nome"]}\n'
                  f'Código: {i["codigo"]}\n'
                  f'Permissão nivel {nivelPermissao}\n')
            return True
    else:
        print(f'Usuário não encontrado!')
    return False

def selecionaOperacao(nivelPermissao, opcao):
    if nivelPermissao == '1':
        if opcao == 1:
            return criaItem()
        elif opcao == 2:
            return buscarNoEstoque()
        elif opcao == 3:
            return editarItem()
        elif opcao == 4:
            return removerItem()
        elif opcao == 5:
            return listarTodos()
    elif nivelPermissao == '2':
        if opcao == 1:
            return criaItem()
        elif opcao == 2:
            return buscarNoEstoque()
        elif opcao == 3:
            return ditarItem()
        elif opcao == 4:
            return listarTodos()
    else:
        if opcao == 1:
            return buscarNoEstoque()
        elif opcao == 2:
            return listarTodos()

def menu(nivel_permissao):
    while True:
        if nivel_permissao == '1':
            print(f'Selecione uma operação')
            print(f'1 - Inserir item')
            print(f'2 - Buscar item')
            print(f'3 - Editar item')
            print(f'4 - Remover item')
            print(f'5 - Listar todos os itens')
            print(f'0 - SAIR')
            op = int(input('Digite uma opção: '))
            selecionaOperacao('1', op)
            if (op < 0 or op > 5):
                print(f'\n -- Opção inválida! --\n')
            if op == 0:
                resp = str(input('\nTEM CERTEZA QUE DESEJA ENCERRAR O SISTEMA? s/n ')).upper()[0] #pega o primeiro caractere
                if resp == 'S':
                    encerrar()
        elif nivel_permissao == '2':
            print(f'Selecione uma operação')
            print(f'1 - Inserir item')
            print(f'2 - Buscar item')
            print(f'3 - Editar item')
            print(f'4 - Listar todos os itens')
            print(f'0 - Sair')
            op = int(input('Digite uma opção: '))
            if (op < 0 or op > 4):
                print(f' -- Opção inválida! --')
            else:
                break
        else:
            print(f'Selecione uma operação')
            print(f'1 - Buscar item')
            print(f'2 - Listar todos os itens')
            print(f'0 - Sair')
            op = int(input('Digite uma opção: '))
            if (op < 0 or op > 2):
                print(f' -- Opção inválida! --')
            else:
                break

def encerrar():
    separador_linha('*', 42)
    print(f'Encerrando o programa'.center(42))
    separador_linha('*', 42)
    exit()


#programa principal
cabecalho()

codUsuario = '1'#str(input('Digite o cód. do funcionário: '))
senhaUsuario = 'm'#str(input('Digite a senha: '))
if(login(codUsuario, senhaUsuario)):
    menu(nivelPermissao)
else:
    encerrar()
