import os
import time

def inserir_numero():
    # Solicitando número ao usuário
    numero = int(input('Insira um número:'))

    if numero % 2 == 0:
        print('o número é par.\n')
    else:
        print('O número é ímpar.\n')
def digitar_idade():
    idade = int(input('Sua idade é:'))

    if idade <= 12:
            print('Criança\n')
    elif 13 <= idade <= 18:
            print('Adolescente\n')
    else:
            print('Adulto\n')
def digitar_login():

    # Definindo valores esperados   
    usuario_correto = 'Samuel'
    senha_correta = '1234'
    tentativas = 3

    for tentativa in range(tentativas):
        usuario = input('Digite o seu nome de usuário: ')
        senha = input('Digite sua senha: ')

        if usuario == usuario_correto and senha == senha_correta:
            print(f'\nAcesso permitido! Bem-vindo, {usuario}.\n')
            return  # sai da função
        else:
            restantes = tentativas - tentativa - 1
            print(f'\nAcesso negado! Usuário ou senha incorretos. ({restantes} tentativas restantes)\n')

    print('Número máximo de tentativas excedido. Programa encerrado.')
    quit()
    
def digitar_coordenadas():

    # Solicita as coordenadas do ponto
    x = float(input('\nDigite a coordenada x: '))
    y = float(input('Digite a coordenada y: '))

    # Verifica em qual quadrante o ponto está
    if x > 0 and y > 0:
        print('\nPrimeiro quadrante')
    elif x < 0 and y > 0:
        print('\nSegundo quadrante')
    elif x < 0 and y < 0:
        print('\nTerceiro quadrante')
    elif x > 0 and y < 0:
        print ('\nQuarto quadrante')
    else:
        print('O ponto está localizado no eixo ou origem.')

def finalizar_programa():
    while True:
        finalizar = input('\nDeseja finalizar o programa? (s/n): ').strip().lower()
        if finalizar == 's':
            print('Programa finalizado.')
            time.sleep(1.5)
            os.system('cls' if os.name == 'nt' else 'clear')
            quit()
        elif finalizar == 'n':
            os.system('cls' if os.name == 'nt' else 'clear')
            main()  # reinicia o programa do começo
        else:
            print('Você não escolheu uma das opções. Tente novamente.')


def main():
    inserir_numero()       # executa a verificação par/ímpar
    digitar_idade()        # executa a verificação de faixa etária
    digitar_login()        # executa a verificação de 
    digitar_coordenadas()  # executa a verificação do quadrante do plano cartesiano
    finalizar_programa()   # finaliza ou reinicia o programa

if __name__ == '__main__':
    main()