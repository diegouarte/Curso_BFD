# 1. Leia um número e diga se ele é maior que 10.

entrada = int(input("digite um numero: "))
if entrada >= 10:
    print("esse numero é maior que 10")
elif entrada < 10:
    print("esse numero é menor que 10")

#2. Número positivo ou negativo.

entrada = int(input("digite um numero: "))
if entrada <0:
    print("esse numero eh negativo")  
elif entrada >0:
    print("esse numero eh positivo")

#3. Par ou ímpar.

entrada = int(input("digite um numero: "))
if entrada / 2 == 0:
    print("esse numero eh par")  
elif entrada / 2 == 1:
    print("eesse numero eh impar")

#4. Maior ou menor de idade.

entrada = int(input("digite sua idade "))
if entrada >18:
    print("vc eh maior de idade") 
elif entrada <18:
    print("vc eh menor de idade")

#5. Senha correta. 

n = (input("digite sua senha: "))
if n == "1234":
    print("senha correta")
else:
    print("senha incorreta")

#6. Maior entre dois números.

n1 = int(input("digite um numero: "))
n2 = int(input("digite um numero: "))
if n1 > n2:
    print("o primeiro numero eh maior")
elif n1 < n2:
    print("o segundo numero eh maior")
    
#7. Maior entre três números.

n1 = int(input("digite um numero: "))
n2 = int(input("digite um numero: "))
n3 = int(input("digite um numero: "))
if n1 > n2 & n3:
    print("o primeiro numero he maior")
elif n2 > n3 & n1:
    print("o segundo numero eh maior")
elif n3 > n1 & n2:
    print("o terceiro numero eh maior")

#8. Nota de aluno.

n1 = int(input("nota 1: "))
n2 = int(input("nota 2: "))
if (n1 + n2)/2 >6:
    print("aluno aprovado")
else:
    print("aluno repro")

#9. Classificação por idade.

n1 = int(input("qual a sua idade: "))
if n1 < 16 :
    print("classificacao infantil")
elif n1 > 16 and n1 < 18 :
    print("classificacao juvenil")
elif n1 >= 18:
    print("caldssificacao adulta")
    
#10. Temperatura.

n1 = int(input("qual eh a temperatua: "))
if n1 >=18 and n1 <27:
    print("agradavel")
elif n1 <18:
    print("frio")
elif n1 >=27:
    print("quente")

#11. Turno de estudo.

n1 = int(input("qual horas q vc estuda: "))
if n1 >6 and n1 <12:
    print("manha")
elif n1 >12 and n1 <17:
    print("tarde")
elif n1 >18 and n1 <22:
    print("noite")

#12. Velocidade.

n1 = float(input("qual a velocidade do carro: "))
if n1 > 80:
    print("o carro esta veloz")
elif n1 > 40 and n1 <=80:
    print("o carro esta moderamente veloz")
elif n1 <=40:
    print("o carro esta lento")

#13. Número entre 1 e 100.

n1 = int(input("digite um numero: "))
if n1 >1 and n1 <100:
    print("esse numero esta no intervalo")
else:
    print("nao esta no intervalo")
    
 #14. Iguais ou diferentes.

n1 = int(input("digite um numero: "))
n2 = int(input("digite um numero: "))
if n1 == n2:
    print("os numeros sao iguais")  
else:
    print("nao sao iguais")
    
#15. Vogal ou consoante.

n1 = (input("digite uma letra: "))
if n1 == "a" or n1 == "e" or n1 == "i" or n1 == "o" or n1 == "u":
    print("eh uma vogal")
else:
    print("eh uma consoante")
    
#16. Menor de dois números.

n1 = int(input("digite um numero: "))
n2 = int(input("digite um numero: "))
if n1 < n2:
    print("o primeiro numero eh menor")
else:
    print("o segundo numero eh o menor2")
    