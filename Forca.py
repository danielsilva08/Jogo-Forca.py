import random

#Cria uma lista de palavras que serão sorteadas.
palavras = ['python', 'programacao', 'computador', 'aula', 'variavel']

#escolha das palavras através do metodo (random.choice(seq))
palavra_sorteada = random.choice(palavras)

#Criamos uma string com traços que representam as letras
palavra_escondida = '-' * len(palavra_sorteada)

#criamos uma lista vazia para armazenar as letras que já foram faladas
letras_adivinhadas = []

max_tentativas = 6

while True:
    #mostra na tela a palavra escondida
    print(palavra_escondida) 
    #pedimos ao jogador para digitar uma letra
    letra = input('Digite uma letra: ')

#verificamos se a letra ja foi digitada
    if letra in letras_adivinhadas:
     print('Você já digitou essa letra. Tente outra por favor')
     continue

#adicionar a letra a lista de letras digitadas
    letras_adivinhadas.append(letra)

#verificar se a letra digita está na palavra sorteada
    if letra in palavra_sorteada:
       #Se a letra está na palavra, atualize a string com traços
       # para mostrar a letra adivinhada
       palavra_escondida = ''.join(letra if letra == palavra_sorteada[indice] else palavra_escondida[indice] for indice in range (len(palavra_sorteada)))
        #lista = []
        #for indice in range(len(palavra_sorteada)):
            #if letra == palavra_sorteada[indice]:
                #lista.append(letra)
           # else:
                #lista.append(palavra_escondida[indice]) 
        #palavra_escondida = ''.join(lista) # se jogador digitou a letra a então teremos = a**a  

#letra não esta na palavra sorteada
    else:
        max_tentativas -= 1
        print(f'Letra não encontrada. Você tem mais {max_tentativas} tentativas')

#Verificamos se o jogador ganhou ou perdeu
    if palavra_escondida == palavra_sorteada:
        print('Parabéns, Você ganhou!!')
        break

    elif max_tentativas == 0:
        print(f'Você perdeu. A palavra era {palavra_sorteada}.')
        break




