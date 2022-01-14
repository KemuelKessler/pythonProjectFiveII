from ex002.liby.interface import *

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Houve um ERRO na criação do arquivo!')
    else:
        print(f'Arquivo {nome} criado com sucesso!')


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in a:
            dado = linha.split(';')
            dado[2] = dado[2].replace('\n','')
            print(f'Nome: {dado[0]:<12}CPF: {dado[1]:<15}E-mail: {dado[2]:>3}')
    finally:
        a.close()


def lerArquivor(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler o arquivo!')
    else:
        cabeçalho('ROTAS DISPONÍVEIS')
        print(a.read())
    finally:
        a.close()



def lerArq(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('Erro ao ler arquivo!')
    else:
        cabeçalho('VER RESERVAS')
        for linha in a:
            dado = linha.split(';')
            print(f'Rota: {dado[0]:<5}Origem: {dado[1]:<15}Destino: {dado[2]:<15}Partida: {dado[3]:<15}Volta: {dado[4]:>3}')
    finally:
        a.close()

def cadastrar(usuario, nome, cpf, email):
    try:
        a = open(usuario, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{nome};{cpf};{email}\n')
        except:
            print('Houve um ERRO no momento de escrever os dados!')
        else:
            print(f'Novo registro de {nome} adicionado com sucesso!')
            a.close()


def reservar(reserv, rota, origem,destino, partida, volta):
    try:
        a = open(reserv, 'at')
    except:
        print('Houve um ERRO na abertura do arquivo!')
    else:
        try:
            a.write(f'{rota};{origem};{destino};{partida};{volta}\n')
        except:
            print('Houve um ERRO no momento de escrever os dados!')
        else:
            print(f'Cadastro de reserva realizado com sucesso!')
            a.close()