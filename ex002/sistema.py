from ex002.liby.interface import *
from ex002.liby.arquivo import *
from time import sleep

usuario = 'usuarioscadastrados.txt'
rotas = 'rotasdisponiveis.txt'
reserv ='reservapassagem.txt'

if not arquivoExiste(usuario):
    criarArquivo(usuario)

if not arquivoExiste(rotas):
    criarArquivo(rotas)

if not arquivoExiste(reserv):
    criarArquivo(reserv)


while True:
    resposta = menu(['Cadastar Usuário', 'Usuários Cadastrados', 'Rotas Disponíveis', 'Reserva de Passagens', 'Visualizar Reservas', 'Cancelamento de Reservas', 'Sair' ])
    if resposta == 1:
        cabeçalho('NOVO CADASTRO')
        nome = str(input('Nome: '))
        cpf = str(input('CPF: '))
        email = str(input('E-mail: '))
        cadastrar(usuario, nome, cpf, email)
    elif resposta == 2:
        lerArquivo(usuario)
    elif resposta == 3:
        lerArquivor(rotas)
    elif resposta == 4:
        cabeçalho('RESERVA DE PASSAGENS')
        rota = int(input('Rota: '))
        origem = str(input('Origem: '))
        destino = str(input('Destino: '))
        partida = str(input('Data de Partida: '))
        volta = str(input('Data de Volta: '))
        reservar(reserv, rota, origem, destino, partida, volta)
    elif resposta == 5:
        lerArq(reserv)
    elif resposta == 6:
        cabeçalho('CANCELAMENTO DE RESERVA')
        input('Qual rota você deseja cancelar? ')
        input('Poderia confirmar o seu nome? ')
        input('Poderia confirmar o seu CPF? ')
        print('Cancelamento realizado com sucesso!!!')
    elif resposta == 7:
        print('\nSaindo do sistema...\n')
        print('Obrigado por voar conosco!!!\n')
        print('Até logo!')
        break
    else:
        print('\033[31mERRO! Digite uma opção válida!\033[m')
    sleep(2.5)
