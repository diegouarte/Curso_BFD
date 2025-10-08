# Questão 1: Crie uma string com seu nome e exiba a primeira letra.

nome = "Diego"
print(nome[0])

# Questão 2: Exiba a última letra da string 'Glestiano' usando índice negativo.

print(nome[-1])

# Questão 3: Mostre a terceira letra da string 'nome'.

print(nome[2])

# Questão 4: Usando índice negativo, exiba a penúltima letra de 'nome'.

print(nome[-2])

# Questão 5: Escreva um programa que exiba todas as letras de 'nome' uma por linha.

for c in nome:
    print(c)

# Questão 6: Verifique se a letra 'a' está presente em 'nome'.

print("e" in nome)

# Questão 7: Verifique se a letra 'x' está presente em 'nome'.

print("a" in nome)

# Questão 8: Verifique se a substring 'iano' existe em 'npome'.

print("ego" in nome)

# Questão 9: Verifique se a substring 'tes' existe em 'nome'.

print("Dou" in nome)

# Questão 10: Peça ao usuário uma letra e verifique se ela existe no nome 'nome'.

letra = input("digite um letra: ")
print(letra in nome)

# Questão 11: Verifique se 'z' não está em 'nome'.

print("z" not in nome)

# Questão 12: Verifique se 'G' não está em 'nome'.

print("o" not in nome)

# Questão 13: Escreva um programa que exiba True se 'ano' não estiver em 'nome'.

letra = input("digite um letra: ")
print(letra not in nome)

# Questão 14: Usando 'not in', verifique se 'abc' está ausente em 'nome'.

print("abc" not in nome)

# Questão 15: Verifique se a letra digitada pelo usuário não aparece em 'nome'.

letra = input("digite um letra: ")
print(letra not in nome)

# Questão 16: Mostre apenas as quatro primeiras letras de 'nome'.

print(nome[0:4])

# Questão 17: Exiba apenas as últimas três letras de 'nome'.

print(nome[2:6])

# Questão 18: Pegue os caracteres de índice 2 até 6 de 'nome'.

print(nome[1:4])

# Questão 19: Inverta a string 'nome' usando slicing.

print(nome[1:4])
print(nome[::-1])

# Questão 20: Exiba apenas as letras em posições pares da string 'nome'.

print(nome[::2])

# Questão 21:Conte quantas vezes a letra 'a' aparece em 'nome'.

print(nome.count('e'))

# Questão 22: Peça ao usuário uma letra e diga em qual índice ela aparece pela primeira vez.

letra = input("digite um letra: ")
if letra in nome:
    print(nome.index)

# Questão 23: Verifique se a string 'Gle' aparece no início de 'nome'.

print(nome.find("Di") == 0)

# Questão 24: Verifique se a string 'ano' aparece no final de 'nome'.

print(nome.find("go") == 3)

# Questão 25: Exiba todas as letras de 'Glestiano' acompanhadas de seus índices.

print(f'0 {nome[0]}')
print(f'1 {nome[1]}')
print(f'2 {nome[2]}')
print(f'3 {nome[3]}')
print(f'4 {nome[4]}')

# Questão 26: Crie um programa que verifique se uma palavra digitada pelo usuário está dentro da string 'nome'.

palavra = input("digite uma palavra: ")
if palavra in nome:
    print("está no nome")
else:
   print("não está")

# Questão 27: Escreva um programa que percorra 'nome' e exiba apenas as vogais.

vogais = ["a","e","i","o","u"]
for letra in nome:
    print(nome)
    
# Questão 28: Exiba apenas as consoantes da string 'nome'.


# Questão 29: Pergunte ao usuário uma letra e diga se ela aparece mais de uma vez em 'nome'.

letra = input("escreva uma letra: ")
print(nome.count(letra))

# Questão 30: Verifique se 'Glestiano' é um palíndromo (lido de trás para frente é igual).

nome2 = nome[::-1]
print(nome == nome2)
