from random import randint
random_number = randint(1,10)
attemps = 1
number = int(input('Pensei em um número de 1 a 10, tente adivinhar qual é:'))
while random_number != number:
    if number > 10:
        print('Número inválido')
    if number > random_number:
        print(f'Quase lá, o número pensado é menor que {number}')
    if number < random_number:
        print(f'Quase lá, o número pensado é maior que {number}')
    print('Mais sorte na próxima...')
    attemps += 1
    number = int(input('Tente novamente:'))
if attemps == 1:
    print(f'Você acertou de primeira!! em apenas {attemps} tentativa, você chegou ao resultado, que era o número {random_number}.')
else:
    print(f'Parabéns!! o número certo era {random_number}, Você chegou ao resultado em {attemps} tentativas!!')
