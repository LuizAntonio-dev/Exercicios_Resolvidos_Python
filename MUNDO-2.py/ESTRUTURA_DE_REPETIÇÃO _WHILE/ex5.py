# Refaça o DESAFIO 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.


print("-=" * 30)
print("         RAZÃO ARITMÉTRICA COM WHILE")
print("-=" * 30)


primeiro = int(input("primeiro termo:"))
razão = int(input("razão:"))


cont = 0

#print(primeiro,end=" -> ")
       
while cont < 10: 
        
        if cont < 9:
                
            cont = cont + 1 

            print(primeiro, end=" -> ")

            primeiro = primeiro + razão
        else:

            cont = cont + 1 

            print(primeiro, end=" FIM ")

            primeiro = primeiro + razão
        
    