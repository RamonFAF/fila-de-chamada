#j1mm1
#05/06/2019

#Programa de chamada em filas

#Importa os módulos necessários.
import random

#Carrega o arquivo com o nome dos alunos.
#arquivo = input('Entre com o nome do arquivo, com a extensão do mesmo >>> ')
chamada = open('lista.txt', 'r') #carrega arquivo, a opção 'r' significa leitura.
conteudo = chamada.readlines() #escreve as linhas que tem no arquivo em uma lista
chamada.close() #fecha o arquio.
NumAlunos = len(conteudo)

#cria as variáveis que representam as cores.
RED   = "\033[1;31m"
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

#Recebe a ordem aleatória para a chamada.
ordem = []
#Gera uma ordem aleatória para a lista de alunos, não permite que números
#iguais entrem na  seleção.
while len(ordem) != len(conteudo):
    aleatorio = random.randrange(NumAlunos)
    if aleatorio not in ordem:
        ordem.append(aleatorio)

#Início da chamada.
print('\n'*50)
ir = input(RED + "\nAPERTE QUALQUER TECLA PARA SEGUIR >>> " )
NomesJaChamados = []
NumChamd = 0
ir = 0
while NumChamd != len(conteudo) :
    NumChamd += 1
    chamar1 = conteudo[ordem[NumChamd]]
    print('\n'*15)
    print("\nO próximo aluno a ser chamado é: " + GREEN + "{}".format(chamar1) + RESET)
    print('\n'*15)
    NomesJaChamados.append(chamar1)
    seguir = input('Digite 1 para ver os nomes chamados ou qualquer tecla para continuar a chamada >>> ')
    if seguir == '1':
        print("\njá foram chamados: "+ BLUE + "{}".format(NomesJaChamados) + RESET)
    ir = input(RED + "\nAPERTE QUALQUER TECLA PARA SEGUIR >>> ")



