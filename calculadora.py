#montando uma calculadora em python
#primeira informação
print("Escolha uma opção: \n digite 1 para adição \n digite 2 para uma subtração \n digite 3 para uma multiplicação \n digite 4 para uma divisão \n digite 5 para sair")

#entrada de dados para o usuario escolher a operação
escolha=input("Escolha uma operação: ")
if escolha > "5":
     print("Por favor, digite uma opção valida!")
     exit()
if escolha=="5":
     print("Ok, tchau") 
     exit()
n1=float(input("Digite o 1 número: "))
n2=float(input("Digite o 2 número: "))
#condições e calculos
if escolha=="1":
    resultado=(n1+n2)
    print(f"o resultado da soma é de {resultado} ")
elif escolha=="2":
    resultado=(n1-n2)
    print(f"O resultado da subtração foi de {resultado}")
elif escolha=="3":
    resultado=(n1*n2)
    print(f"O resultado da multiplicação foi de {resultado}")
elif escolha=="4":
    resultado=(n1/n2)   
    print(f"O resultado da divisão foi de {resultado}")