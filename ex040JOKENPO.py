from random import choice
from time import sleep
print('- - - ' * 5)
print(' J O K E N P O ')
print('- - - -' * 5)
print(' PEDRA, PAPEL OU TESOURA?')
jog = str(input('Digite sua escolha: ').upper())
comp = (choice(['PEDRA', 'PAPEL', 'TESOURA']))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('- - - ' * 5)
if jog == 'TESOURA' and comp == 'PAPEL' or jog == 'PAPEL' and comp == 'PEDRA' or jog == 'PEDRA' and comp == 'TESOURA':
    print('Voce escolheu {}. \nEu escolhi {}. \nVOCE VENCEU! '.format(jog, comp))
elif jog == 'PAPEL' and comp == 'TESOURA' or jog == 'PEDRA' and comp == 'PAPEL' or jog == 'TESOURA' and comp == 'PEDRA':
    print('Eu escolhi {}. \nVoce escolheu {}. \nVOCE PERDEU!'.format(comp, jog))
elif jog == comp:
    print('Nos dois escolhemos {}. \n EMPATE!'.format(comp))
print('- - - ' * 5)
