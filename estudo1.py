# variavel = definir guardar
    #nome=diego

# print = imprimir, usar aspas
    #print("oi")

# str = textos
    #mensagem = "Olá, mundo!"
    #print(mensagem)

# int = numeros inteiros
    #idade = 28
    #print(idade)

# float = numeros flutuantes 
    #altura = 21,76
    #print(altura)
    # usase : seguido de um numero para defenir as casas decimais

# boolean = True or False ou 0 ou 1
    #a = 10
    #b = 5
    #print(a > b)   # True, porque 10 é maior que 5
    
# round = arredondar 
    #numero = 28,9
    #print(numero)

# mood = % resto que sobra
    #print(10 % 3)   # 1 (pois 10 dividido por 3 dá 3, sobra 1)

# contas basicas = * / - +
    #print(10 + 3)  

# floor division  = // resto inteiro
    #print(10 // 3)  # 3 → inteiro

# if = verifica a primeira condição verdadeira
# elif = verifica outras condições caso a primeira seja falsa
# else = executa se nenhuma condição anterior for verdadeira
    #nota = 75
    #if nota >= 90:
        #print("Parabéns! Você tirou A.")
    #elif nota >= 70:
        #print("Você tirou B. Bom trabalho!")
    #elif nota >= 50:
        #print("Você tirou C. Precisa melhorar.")
    #else:
    # print("Você tirou D. Estude mais!")
    # sempre usar :

# comentarios (#)
    #essa lista
#OU
''' 3x ' no comeco e fim do cod'''

# cls limpar o terminal

# para dizer que algo é exatamente igual se usa (==)
    #nome==diego

# and = ambas situacoes tem q ser True 
    #idade = 15
    #altura = 1.60
        #if idade >= 14 and altura >= 1.50:
            #print("Você pode entrar no brinquedo!")
        #else:
            #print("Você NÃO pode entrar no brinquedo.")

# in = para saber se alguma caractere esta dentro de uma variavel
    #frutas = ["maçã", "banana", "laranja"]
    #if "banana" in frutas:
        #print("Banana está na lista!")

# not in = vai negar, quando vc qr negar algo com proposito
    #numeros = (1, 2, 3, 4)
    #if 5 not in numeros:
        #print("O número 5 não está na tupla.")

# fateamento = determinar pelo numero de caraceteres de onde comecar ate o final -1 
    #texto = "Diego"
    #print(texto[0:4])   # do índice 0 até 3 → 'Die'
    # ex: [4:9] onde ele vai ler a apartir do 4 caractere e ate 10 (10-1=9)
    # ex: [::] se deixa o primeiro espaco em branco ele entende q vai ler do comeco e 2x :: ele vai fatiar 
    # conforme o numero q se coloca depois, ex: [::-1] ele vai fatiar do -1 (ultimo) e de 1 em 1 ate cabar

# for para criar loopin
    #frutas = ["maçã", "banana", "laranja"]
    #for fruta in frutas:
        #print("Eu gosto de", fruta)

# count = encontrar algum caractere dentro de uma variavel 
    #texto = "Glestiano"
    #print(texto.count("a"))   # conta quantas vezes 'a' aparece

# len = quantos caracteres tem dentro dessa variavel
    # texto = "Diego"
    #print(len(texto))

# index = usado para encontrar a posição (índice) da primeira ocorrência 
    #texto = "Diego"
    #print(texto.index("D"))  # índice da letra 'D' = 0
    #print(texto.index("G"))  # índice da letra 'o' = 4

# interpolação em Python é o nome dado às técnicas de inserir valores de variáveis dentro de strings
    #nome = "Diego"
    #idade = 28
    #print("Olá, meu nome é {} e tenho {} anos.".format(nome, idade))
#OU
    #nome = "Diego"
    #idade = 28
    #print(f"Meu nome é {nome} e tenho {idade} anos.")
#OU
    #usando % par marcar e identificar os locais de substituição
    #%s → para string (texto)
    #%d → para inteiro (decimal)
    #%f → para número decimal (float), podendo usar %.2f para limitar casas decimais
        #nome = "Diego"
        #idade = 28
        #print("Meu nome é %s e tenho %d anos."%(nome,idade))

# while = executa um bloco de código repetidamente enquanto uma condição for verdadeira
    #i = 1
    #nome = input("diga seu nome: ")
    #while i <6:
  #  print(nome)
  #  i += 1

# split = dividir uma string em partes criando uma lista com os pedaços 
  #frase=Eu gosto de programar em Python"
    #palavras= frase.split()
       #print(palavras)

# break = serve para interromper um laço (for ou while) antes do fim
#for numero in range(1, 11):
    #if numero == 5:
        #print("Parando no número", numero)
        #break
#print(numero)

  
