#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial.

#Ex: 5! = 5 x 4 x 3 x 2 x 1 = 120

numero = int(input("digite um número para calcular seu fatorial:"))

num_indice = numero

num_fatorial = numero

while num_indice  > 0 :

    if num_indice > 1:

        num_fatorial -= 1

        numero = numero * num_fatorial

        print(num_indice ,"x ", end="")

        num_indice -= 1

    else:
        
        numero = numero * num_fatorial

        print(num_indice,"=", numero, end="")

        num_indice -= 1

print(f"\n\nO Resultado do calculo fatorial é: {numero}")









