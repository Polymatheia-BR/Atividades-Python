# As idades das pessoas de um determinado grupo são 10, 12, 15 e 17 anos. Calcule e exiba a 
# média de idade do grupo, e a variação percentual da média das idades caso uma pessoa 
# de 16 anos se junte ao grupo.

media = (10 + 12 + 15 + 17) / 4
nova_media = (10 + 12 + 15 + 16 + 17) / 5
var_percentual = nova_media - media / media

print(f'A média de idade do grupo é: {media}')
print(f'Caso um aluno de 16 anos se junte ao grupo a variação percentual é de: {var_percentual}%')