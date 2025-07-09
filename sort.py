from random import randint
print('='*30)
print('''Bem vindo ao jogo do sorteio!!
Tente adivinhar o número de 1 a 10 que o computador pensou.
Ele te dará algumas dicas...
No mais... Boa sorte!''')
print('='*30)
your_choice = int(input('Digite um número de 1 a 10:'))
print('='*30)
if your_choice > 10:
    your_choice = int(input('Número inválido, tente novamente'))
    print('='*30)
computer_choice = randint(1,10)
attemps = 0

while your_choice != computer_choice:
    attemps += 1
    print('Você errou! mais sorte na próxima...')
    if computer_choice > your_choice:
        print(f'O número pensado é maior que {your_choice}')
    elif computer_choice < your_choice:
        print(f'O número pensado é menor que {your_choice}')
    else:
        print('Número inválido')
    print('='*30)
    your_choice = int(input('Tente novamente:'))
    print('='*30)
print(f'''Parabéns,você acertou!!! o número escolhido pelo computador era {computer_choice}.
Você acertou em {attemps} tentativas.''')
