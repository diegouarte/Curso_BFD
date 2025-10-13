#Questão 01: Escreva um programa que imprima os números de 1 a 10 usando while.

numero = 0
while numero <=10:
    print(numero)
    numero += 1
    
#Questão 02: Faça um programa que imprima os números de 10 a 1 (contagem regressiva) usando while.

numero = 10
while numero >=0:
    print(numero)
    numero -= 1

#Questão 03: Crie um programa que imprima os números pares de 0 a 20 usando while.

numero = 0
while numero <=20:
    print(numero)
    numero += 2

#Questão 04: Escreva um programa que imprima os números ímpares de 1 a 19 usando while.

numero = 1
while numero <20:
    print(numero)
    numero += 2

#Questão 05: Faça um programa que peça ao usuário um número e conte de 1 até ele usando while.

i = 0
numero = int(input("diga um numero: "))
while i <=numero:
   print(i)
i += 1

#Questão 06: Escreva um programa que peça ao usuário uma palavra e a imprima 5 vezes com while.

i = 1
nome = input("diga seu nome: ")
while i <6:
    print(nome)
i += 1

#Questão 07: Faça um programa que imprima a tabuada do número 2 (até 10) usando while.

i = 1
tabuada = 2
while i <=10:
    print(f"{tabuada}x{i} = {tabuada*i}")
    i += 1

#Questão 08: Crie um programa que peça um número e imprima a tabuada dele até 10 com while.

i = 1
tabuada = int(input("diga um numero = "))
while i <=10:
    print(f"{tabuada}x{i} = {tabuada*i}")
    i += 1

#Questão 09: Escreva um programa que peça 5 nomes ao usuário e os imprima um por um usando while.
i = 0
nome = input("diga 5 nomes = ").split()
while i <5:
    print(nome[i])
    i += 1

#Questão 10: Faça um programa que peça ao usuário 5 números e mostre a soma deles usando while.

i = 0
soma = 0
while i <5:
    numero = int(input("diga um numero = "))
    soma += numero
    i += 1
print(soma)

#Questão 11: Escreva um programa que imprima todos os múltiplos de 5 até 50 usando while.

i = 5
while i <51:
    print(i)
    i += 5

#Questão 12: Crie um programa que peça um número e imprima todos os números de 0 até ele usando while.

i = 1
numero = int(input("diga um numero: "))
while i <=numero:
   print(i)
   i += 1

#Questão 13: Faça um programa que peça ao usuário números até ele digitar 0.

i = 1
while True:
    numero = int(input("diga um numero: "))
    if numero == 0:
        break

#Questão 14: Escreva um programa que peça ao usuário uma senha até que ele digite 1234.

while True:
    senha = input("senha: ")
    if senha == "1234":
        print("senha correta")
        break
    else:
        print("senha incorreta")

#Questão 15: Crie um programa que imprima os números de 1 a 100, mas apenas os divisíveis por 10.

i = 10
while i <101:
    print(i)
    i += 10

#Questão 16: Faça um programa que imprima os 20 primeiros números naturais com while.

i = 0
while i <21:
    print(i)
    i += 1

#Questão 17: Escreva um programa que peça uma palavra e mostre suas letras uma por uma usando while.

i = 0
nome = input("diga um nome: ")
while i < (len(nome)):
    print(nome[i])
    i += 1
    
#Questão 18: Crie um programa que peça ao usuário um número e calcule a soma de todos os números de 1 até ele usando while.

i = 0
soma = 0
numero = int(input("diga um numero = "))
while i <=numero:
    soma += i
    i += 1
print(soma)

#Questão 19: Faça um programa que peça números ao usuário até que ele digite um número negativo.

i = 0
while True:
    numero = int(input("diga um numero: "))
    if numero <0:
        break

#Questão 20: Escreva um programa que conte quantas letras existem em uma palavra fornecida pelo usuário usando while.

i = 0
nome = input("diga um nome: ")
while i < (len(nome)):
    print(nome[i])
    i += 1
print(i)

#Questão 21: Crie um programa que imprima os números de 50 a 100 usando while.

i = 50
while i <101:
    print(i)
    i += 1

#Questão 22: Faça um programa que mostre a sequência de 2 em 2 até 30 usando while.

i = 0
while i <31:
    print(i)
    i += 2

#Questão 23: Escreva um programa que peça 10 números ao usuário e mostre apenas os pares usando while.

i = 0
pares = 0
numero = input("diga um numero: ").split()
while i < len(numero):    
    numero2 = int(numero[i])
    if numero2 % 2 == 0:
        print(numero2)
        i += 1
     
#Questão 24: Crie um programa que imprima os 15 primeiros múltiplos de 3 usando while.

i = 0
while i <46:
    print(i)
    i += 3

#Questão 25: Faça um programa que peça notas ao usuário até ele digitar -1, e depois mostre quantas notas foram digitadas.

i = 0
while True:
    nota = int(input("nota: "))
    if nota == -1:
        print(i)
        break
    else:
       i += 1

#Questão 26: Escreva um programa que peça um número e calcule seu fatorial com while.

fatorial = 1
numero = int(input("diga um numero: "))
i = numero
while i > 1:       
    fatorial *= i
    i -= 1
print(fatorial)

#Questão 27: Crie um programa que peça ao usuário uma frase e conte quantas vogais ela possui usando while.
#Questão 28: Faça um programa que peça números ao usuário até que a soma deles seja maior que 50.
#Questão 29: Escreva um programa que peça 5 idades e calcule a média usando while.
#Questão 30: Crie um programa que peça ao usuário números até que ele digite fim e depois mostre todos os números digitados.
