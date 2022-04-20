import datetime
from datetime import date

funcionarios = ({'nome': 'Matheus', 'codigo': '1', 'senha': 'm','nivel': '1'},
                {'nome': 'Rafael', 'codigo': '2', 'senha': 'r', 'nivel': '2'},
                {'nome': 'Lucas', 'codigo': '3', 'senha': 'l', 'nivel': '3'})
estoque = list()
item = dict()

def separador_linha(separador, vezes):
    print(f'{separador * vezes}')

def cabecalho():
    separador_linha('*', 42)
    print(f'Sistema de controle de estoque simples'.center(42))
    print(f'Autor: Michel M. Duarte'.center(42))
    print(f'mmd_rg@hotmail.com'.center(42))
    separador_linha('*', 42)

def buscarNaLista(lista, chave):

    for i in lista:
        print({i[chave]})


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


def menu(nivelPermissao):
    resp = True
    while True:
        if nivelPermissao == '1':
            print(f'Selecione uma operação')
            print(f'1 - Inserir item')
            print(f'2 - Buscar item')
            print(f'3 - Editar item')
            print(f'4 - Remover item')
            op = int(input('Digite uma opção: '))
            if (op < 1 or op > 4):
                print(f' -- Opção inválida! --')
            else:
                break
        elif nivelPermissao == '2':
            print(f'Selecione uma operação')
            print(f'1 - Inserir item')
            print(f'2 - Buscar item')
            print(f'3 - Editar item')
            op = int(input('Digite uma opção: '))
            if (op < 1 or op > 3):
                print(f' -- Opção inválida! --')
            else:
                break
        else:
            print(f'Selecione uma operação')
            print(f'1 - Inserir item')
            print(f'2 - Buscar item')
            op = int(input('Digite uma opção: '))
            if (op < 1 or op > 2):
                print(f' -- Opção inválida! --')
            else:
                break
def encerrar():
    separador_linha('*', 21)
    print(f'Encerrando o programa')
    separador_linha('*', 21)
    return 0
#programa principal
cabecalho()
codUsuario = str(input('Digite o cód. do funcionário: '))
senhaUsuario = str(input('Digite a senha: '))
if(login(codUsuario, senhaUsuario)):
    menu(nivelPermissao)
else:
    encerrar()