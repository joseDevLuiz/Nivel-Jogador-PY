from time import sleep
print('-'*42)
print('Seja bem-vindo(a) a central de premiação\n Imagino que não tenha sido fácil encarar\ntantos desafio, mas cada vitória te trouxe\n pontos de experiência - é o que chamamos\nde XP - para fazer melhorias ao longo do\n tempo e aumentar seu nível.')
print('-'*42)
print('')
#Tempo de leitura
#sleep(7 )
print('Digite abaixo o seu nome e a quantidade XP adquiridos até aqui')
nomeHeroi = str(input('Digite aqui seu nome: '))
xp = int(input('Digite o total de XP alcançado: '))
if xp <= 1000:
    nivelHeroi = 'Ferro'
elif xp > 1000 and xp <= 2000:
    nivelHeroi = 'Bronze'
elif xp > 2000 and xp <= 5000:
    nivelHeroi = 'Prata'
elif xp > 5000 and xp <= 7000:
    nivelHeroi = 'Ouro'
elif xp > 7000 and xp <= 8000:
    nivelHeroi = 'Platina'
elif xp > 8000 and xp <= 9000:
    nivelHeroi = 'Ascedente'
elif xp > 9000 and xp <= 10000:
    nivelHeroi = 'Imortal'
elif xp > 10000:
    nivelHeroi = 'Radiante'
print(f'{nomeHeroi} com sua pontuação de {xp}xps você agora será nível {nivelHeroi}')
