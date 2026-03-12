#Exercício Python 062: Melhore o DESAFIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos. 
# O programa encerrará quando ele disser que quer mostrar 0 termos.


print("-=" * 30)
print("         RAZÃO ARITMÉTRICA COM WHILE")
print("-=" * 30)


primeiro = int(input("primeiro termo:"))
razão = int(input("razão:"))


cont = 1

total = 0

mais = 10

while mais != 0:
    
    total += mais
    while cont <= total: 
                            
            cont = cont + 1 

            print(primeiro, end=" -> ")

            primeiro = primeiro + razão
                
        
    print('PAUSA')

    mais = int(input("quantos caracteres você quer adicionar na sua PA ?"))   

print(f"FIM DO PROGRAMA\n\nForam exibidos um total de {total} termos.")






















# print("=-=" * 50)
# print("SUPER PROGRESSÃO ARITIMÉTRICA")
# print("=-=" * 50)

# primeiro_termo = int(input("Digite aqui o primeiro termo:"))
# razao = int(input("Digite aqui a razão:"))

# cont = 1

# termos_adicionais = 1



# while termos_adicionais != 0:

#     while cont <= 10:

#         if cont <= 9:
            
#             cont += 1
            
#             print(primeiro_termo, end = " -> ")

#             primeiro_termo = primeiro_termo + razao

#         elif cont == 10: 
        
#             cont += 1
            
#             print(primeiro_termo, end = " PAUSA ")

#             primeiro_termo = primeiro_termo + razao

#             termos_adicionais = int(input("\n\nQuer continuar?\nSe sim digite quantos termos adicionais você quer: ")) - 1

#             termo_final = termos_adicionais + cont
        
       
#     if cont <= termo_final - 1:

#         cont += 1
            
#         print(primeiro_termo, end = " -> ")

#         primeiro_termo = primeiro_termo + razao
    
#     elif termo_final == cont:

#         cont += 1
            
#         print(primeiro_termo, end = " PAUSA ")

#         primeiro_termo = primeiro_termo + razao

#         termos_adicionais = int(input("\n\nQuer continuar?\nSe sim digite quantos termos adicionais você quer: ")) - 1

#         termo_final = termos_adicionais + cont

#     else:
       

#         print("FIM DO PROGRAMA")



        
        
           

            
    
    
    

         

  

        



