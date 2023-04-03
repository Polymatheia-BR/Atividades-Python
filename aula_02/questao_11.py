# Crie um programa em Python que solicite ao usuário e receba o 
# valor do raio para calcular a área, perímetro e diâmetro de um círculo

PI = 3.14
raio = float(input('Digite o raio do círculo: '))
area = PI * raio**2
perimetro = 2 * PI * raio
diametro = 2 * raio

print(f'A área do círculo é {area}, o perímetro é {perimetro} e o diâmetro {diametro}')