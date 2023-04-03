# Você estudou muito pra sua prova de lógica de programação e conseguiu terminar
# a prova em 1 hora e 34 minutos. Faça um programa que calcula e exibe o tempo de prova
# decorrido, em minutos e em segundos.

horas = 1
minutos = 34

print(f'Sua prova durou um total de {minutos + (horas*60)} minutos')
print(f'esse tempo em segundos é: {(minutos * 60) + (horas*60*60)}')