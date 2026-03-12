#Exercício Python 063: Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros 
# elementos de uma Sequência de Fibonacci. 

#Ex: 0 - 1 - 1 - 2 - 3 - 5 - 8

print("-"*30)
print("         FIBONACCI")
print("-"*30)

numero  = int(input("Quantos Termos da sequência de fibonacci você quer ver ?"))

cont = 3
n1 =   0
n2 =   1

print(n1, "->",n2, end=" ")

while cont <= numero:

    n3 = n1 + n2

    print("->",n3, end=" ")

    n1 = n2

    n2 = n3

    cont += 1

print("-> FIM")


    