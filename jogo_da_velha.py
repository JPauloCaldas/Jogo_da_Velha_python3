x_ganhou = False
o_ganhou = False
velha = False
jogada = False
ordem = 0
matriz = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]


def verificar_vitoria_x():
    if matriz[0][0] == 'X' and matriz[1][0] == 'X' and matriz[2][0] == 'X' or \
            matriz[0][1] == 'X' and matriz[1][1] == 'X' and matriz[2][1] == 'X' or \
            matriz[0][2] == 'X' and matriz[1][2] == 'X' and matriz[2][2] == 'X' or \
            matriz[0][0] == 'X' and matriz[0][1] == 'X' and matriz[0][2] == 'X' or \
            matriz[1][0] == 'X' and matriz[1][1] == 'X' and matriz[1][2] == 'X' or \
            matriz[2][0] == 'X' and matriz[2][1] == 'X' and matriz[2][2] == 'X' or \
            matriz[0][0] == 'X' and matriz[1][1] == 'X' and matriz[2][2] == 'X' or \
            matriz[0][2] == 'X' and matriz[1][1] == 'X' and matriz[2][0] == 'X':
        return True


# verifica vitória do 'X' após cada jogada de 'X'


def verificar_vitoria_o():
    if matriz[0][0] == 'O' and matriz[1][0] == 'O' and matriz[2][0] == 'O' or \
            matriz[0][1] == 'O' and matriz[1][1] == 'O' and matriz[2][1] == 'O' or \
            matriz[0][2] == 'O' and matriz[1][2] == 'O' and matriz[2][2] == 'O' or \
            matriz[0][0] == 'O' and matriz[0][1] == 'O' and matriz[0][2] == 'O' or \
            matriz[1][0] == 'O' and matriz[1][1] == 'O' and matriz[1][2] == 'O' or \
            matriz[2][0] == 'O' and matriz[2][1] == 'O' and matriz[2][2] == 'O' or \
            matriz[0][0] == 'O' and matriz[1][1] == 'O' and matriz[2][2] == 'O' or \
            matriz[0][2] == 'O' and matriz[1][1] == 'O' and matriz[2][0] == 'O':
        return True


# verifica jogada do 'O' após cada jogada de 'O'


def verificar_velha():
    if matriz[0][0] != "_" and matriz[0][1] != "_" and matriz[0][2] != "_" and \
            matriz[1][0] != "_" and matriz[1][1] != "_" and matriz[1][2] != "_" and \
            matriz[2][0] != "_" and matriz[2][1] != "_" and matriz[2][2] != "_":
        return True


# verifica EMPATE após cada jogada de ambus


def imprimir_tabuleiro(tabuleiro):
    print(f'''     C1    C2     C3

      {tabuleiro[0][0]}  |  {tabuleiro[0][1]}  | {tabuleiro[0][2]}    
L1  _____|_____|_____
      {tabuleiro[1][0]}  |  {tabuleiro[1][1]}  | {tabuleiro[1][2]}   
L2  _____|_____|_____
      {tabuleiro[2][0]}  |  {tabuleiro[2][1]}  | {tabuleiro[2][2]}   
L3       |     |     ''')


# imprime o tabuleiro


tutorial = '''
      BEM VINDO AO JOGO DA VELHA!


========COMO FUNCIONA O JOGO?========
O game foi criado para ser jogado com 2 players.
Ao iniciar o jogo, você e seu amigo decidem quem vai jogar com "X" e que vai jogar com "O".

--------------------------------------------------------------------------------------------

========    COMO JOGAR?     ========
* O tabuleiro é composto por 3 linhas e 3 colunas. 
* O jogador da rodada irá indicar o número da linha e da coluna que deseja jogar. Assim como mostra no exemplo:

EXEMPLO:

Insira o número da LINHA que deseja jogar:  1
Insira o número da COLUNA que deseja jogar: 2

     C1    C2     C3

         |  X  |      
L1  _____|_____|_____
         |     |     
L2  _____|_____|_____
         |     |     
L3       |     |     

-----------------------------------------------------------------------------------------

VAMOS COMEÇAR...


'''

print(tutorial)

primeiro = None

while primeiro != 'O' and primeiro != 'X':
    primeiro = str(input('Digite X ou O e pressione Enter para escolher quem vai começar jogando: ')).strip().upper()
    if primeiro != 'O' and primeiro != 'X':
        print('\nEscolha inválida!\n')

if primeiro == 'X':
    ordem = 0
else:
    ordem = 1

while not x_ganhou and not o_ganhou and not velha:
    if ordem == 0:
        print('\n       AGORA É A VEZ DO X \n')

        while not jogada:

            while True:
                try:
                    linha = int(input('Insira o número da LINHA que você deseja jogar: '))
                    if linha != 1 and linha != 2 and linha != 3:
                        print('\n JOGADA INVÁLIDA! digite um número entre 1 e 3.\n ')
                    else:
                        break
                except ValueError:
                    print('\nJOGADA INVÁLIDA! VOCÊ NÃO DIGITOU UM NÚMERO\n')

            while True:
                try:
                    coluna = int(input('Insira o número da COLUNA que você deseja jogar: '))
                    if coluna != 1 and coluna != 2 and coluna != 3:
                        print('\n JOGADA INVÁLIDA! digite um número entre 1 e 3.\n ')
                    else:
                        break
                except ValueError:
                    print('\nJOGADA INVÁLIDA! VOCÊ NÃO DIGITOU UM NÚMERO\n')

            if matriz[linha - 1][coluna - 1] != "_":
                print('\n       JOGADA INVÁLIDA! \n LOCAL JÁ ESTÁ OCUPADO... \n')

            else:
                matriz[linha - 1][coluna - 1] = 'X'
                jogada = True
            imprimir_tabuleiro(matriz)

        jogada = False
        ordem = ordem + 1

        if verificar_vitoria_x():
            print('BARABÊNS JOGADOR "X" GANHOU \n FIM DE JOGO')
            x_ganhou = True

        if verificar_velha():
            print('NENHUM DOS JOGADORES VENCERAM \n FIM DE JOGO')
            velha = True

    else:
        print('\n       AGORA É A VEZ DO O\n')

        while not jogada:
            while True:
                try:
                    linha = int(input('Insira o número da LINHA que você deseja jogar: '))
                    if linha != 1 and linha != 2 and linha != 3:
                        print('\n JOGADA INVÁLIDA! digite um número entre 1 e 3.\n ')
                    else:
                        break
                except ValueError:
                    print('\nJOGADA INVÁLIDA! VOCÊ NÃO DIGITOU UM NÚMERO\n')

            while True:
                try:
                    coluna = int(input('Insira o número da COLUNA que você deseja jogar: '))
                    if coluna != 1 and coluna != 2 and coluna != 3:
                        print('\n JOGADA INVÁLIDA! digite um número entre 1 e 3.\n ')
                    else:
                        break
                except ValueError:
                    print('\nJOGADA INVÁLIDA! VOCÊ NÃO DIGITOU UM NÚMERO\n')

            if matriz[linha - 1][coluna - 1] != "_":
                print('\n       JOGADA INVÁLIDA! \n LOCAL JÁ ESTÁ OCUPADO... \n')

            else:
                matriz[linha - 1][coluna - 1] = 'O'
                jogada = True
            imprimir_tabuleiro(matriz)

        jogada = False
        ordem = ordem - 1

        if verificar_vitoria_o():
            print('BARABÊNS JOGADOR "O" GANHOU \n FIM DE JOGO')
            o_ganhou = True
        if verificar_velha():
            print('NENHUM DOS JOGADORES VENCERAM \n FIM DE JOGO')
            velha = True
