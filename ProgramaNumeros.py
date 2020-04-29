#Alunos: Thiago da Silva e Gabriel Andrade
def main():
  x = int(input(""" 
1 - soma dos números 
2 - média dos números 
3 - maior número 
4 - menor número 
5 - média dos números pares
6 - percentual dos ímpares
O que você deseja fazer: """))
  if x == 1:
    somaNum()
  elif x==2:
    mediaNum()
  elif x==3:
    maiorNumLido()
  elif x==4:
    menorNumLido()
  elif x==5:
    mediaPares()
  elif x==6:
    percentualImpares()
    
def somaNum():
  qtd = int(input("digite a quantidasde de numeros que você quer somar: "))

  soma=0
  cont=0
  while cont < qtd :
    num = int(input("digite um numero: "))
    soma = soma + num
    cont = cont + 1

  print("soma=",soma)

def mediaNum():
    qtd = int(input("Quantos de números que você quer digitar? "))
    n = 0
    num = 0
    soma = 0
    media = 0
    while qtd>0 :
        num = int(input("digite um numero: "))
        soma += num
        n +=1
        qtd -= 1
    media = soma / n
    print("A média dos números lidos é: %.2f" %media)

def maiorNumLido():
    qtd = int(input("Quantos de números que você quer digitar? "))
    num = int(input("Digite o número "))
    maior = num
    qtd -= 1
    while qtd > 0:
        num = int(input("Digite o número: "))
        if num > maior:
            maior = num
        qtd -= 1
    print("O maior número é: %d" %maior)

def menorNumLido():
    qtd = int(input("Quantos de números que você quer digitar? "))
    num = int(input("Digite o número "))
    menor = num
    qtd -= 1
    while qtd > 0:
        num = int(input("Digite o número: "))
        if num < menor:
            menor = num
        qtd -= 1
    print("O menor número é: %d" %menor)

def mediaPares():
    qtd = int(input("Quantos de números que você quer digitar? "))
    n = 0
    num = 0
    soma = 0
    media = 0
    while qtd > 0:
        num = int(input("Digite o número: "))
        if num % 2 == 0:
            soma += num
            n +=1
        qtd -= 1
    media = soma / n
    print("A média dos número pares é: %.2f" %media)

def percentualImpares():
    qtd = int(input("Quantos de números que você quer digitar? "))
    n = qtd
    num = 0
    impares = 0
    porcentagem = 0
    while qtd > 0:
        num = int(input("Digite o número: "))
        if num % 2 != 0:
            impares += 1
        qtd -= 1
    porcentagem = (impares / n)*100
    print("O percentual dos ímpares é: {0:.2f}%".format(porcentagem))

main()
