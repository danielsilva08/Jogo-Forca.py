import random

#Cria uma lista de palavras que serão sorteadas.
palavras = ['python', 'programacao', 'computador', 'aula', 'variavel']

#escolha das palavras através do metodo (random.choice(seq))
palavra_sorteada = random.choice(palavras)

#Criamos uma string com traços que representam as letras
palavra_escondida = '-' * len(palavra_sorteada)
palavra_escondida

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
letas_adivinhadas.append(letra)

#verificar se a letra digita está na palavra sorteada



