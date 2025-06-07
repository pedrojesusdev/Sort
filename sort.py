from random import randint
comp = randint(1,10)
print(comp)
tentativas = 1
num = int(input('Pensei em um número de 1 a 10, tente adivinhar qual é:'))
while comp != num:
    if num > 10:
        print('Número inválido')
    if num > comp:
        print('Quase lá, o número pensado é menor que {}'.format(num))
    if num < comp:
        print('Quase lá, o número pensado é maior que {}'.format(num))
    print('Mais sorte na próxima...')
    tentativas += 1
    num = int(input('Tente novamente:'))
if tentativas == 1:
    print('Você acertou de primeira!! em apenas {} tentativa, você chegou ao resultado, que era o número {}.'.format(tentativas, comp))
else:
    print('Parabéns!! o número certo era {}, Você chegou ao resultado em {} tentativas!!'.format(comp, tentativas))
 
