#Este é o sistema bancário criado para o desafio da DIO
#O desafio consiste em criar um sistema bancário em que:

#Deve possuir 3 funções: Saque, Depósito e Extrato
#O valores retornado em extrato deve ser no formato R$ 100,00
#Cada saque e depósito deve ser armazenado no extrato devidamente identificado
#Exibir mensagens de erro caso o saldo seja insuficiente e demais erros possíveis
#Possuir Menu - E não é necessário possuir usuário

#Saudação:
from tkinter import Menu


print("""
++++++++++++++++++++++++++++++++++++      
     Olá! Seja Bem ao PyPay!🌐
O melhor banco digital em Pyhon!🐍
      
+++++++++Version: V1.0++++++++++++++
      """)

#Menu:
menu = """
************************************
                MENU
************************************      

[1] - 📨 Depositar
[2] - 💲 Sacar
[3] - 🧾 Extrato
[0] - ❌ Sair

Selecione a opção desejada: 
"""

#Iniciamos definindo valores base para o código
saldo = 0
LIMITE = 500
extrato = ""
saques_feitos = 0
LIMITE_SAQUE = 3

#Definimos while True para fazer um looping
while True:

    opcao = int(input(menu))
    print("")

    #Depósito
    if opcao == 1:
        valor = float(input("Informe o valor que deseja depositar: "))
        if valor > 0:
           saldo += valor
           extrato += f"Depósito || R$ {valor:.2f}\n"
           print(f"""
Depósito de R$ {valor:.2f} realizado com sucesso!!
Saldo atual R$ {saldo:.2f}""")
        else:
                  print("Falha! Informe um valor a partir de R$ 0,01")
     
     #Saque
    elif opcao == 2:
         valor = float(input("Informe o valor que deseja sacar: "))
         print()
         
         #definindo variáveis limitadoras do saque
         saldo_insuficiente = valor > saldo
         limite_insuficiente = valor > LIMITE
         saques_excedido = saques_feitos >= LIMITE_SAQUE
         
         #Definindo condicionais de saque - É preciso definir antes os limites, e possíveis erros antes do saque ser autorizado
         if saldo_insuficiente:
              print(f"""
Falha! Valor digitado maior que o saldo.
Saldo atual R$ {saldo:.2f}
                  """)
         elif limite_insuficiente:
              print(f"""
Falha! Seu limite por saque é de R$ {LIMITE}.
                  """)
         elif saques_excedido:
              print(f"""
Falha! Número máximo de {LIMITE_SAQUE} saque(s) excedido.
                  """)      
                  
          #Operação de saque    
         elif valor > 0:
              saldo -= valor
              extrato += f"Saque    || R$ {valor:.2f}\n"
              print(f"""
Saque de R$ {valor:.2f} realizado com sucesso!!
Saldo atual R$ {saldo:.2f}
               """)
              saques_feitos += 1

    #Extrato          
    elif opcao == 3:
         if extrato == "":
              print("""
Nenhuma movimentação realizada!
                    """)
         else:
              print(f"""
************************************
                Extrato
************************************ 
{extrato}

************************************ 
Saldo atual R$ {saldo:.2f}
                """)
     #definido break para parar o código         
    elif opcao == 0:
         print("""
Muito obrigado por usar o PyPay!🌐
✨Até logo!!✨""")
         break
    
    else:
         print("\n Digite uma opção válida! \n")
    






