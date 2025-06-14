#Este é o sistema bancário criado para o desafio da DIO
#O desafio consiste em criar um sistema bancário em que:

#Deve possuir 3 funções: Saque, Depósito e Extrato
#O valores retornado em extrato deve ser no formato R$ 100,00
#Cada saque e depósito deve ser armazenado no extrato devidamente identificado
#Exibir mensagens de erro caso o saldo seja insuficiente e demais erros possíveis
#Possuir Menu - E não é necessário possuir usuário

#Fase 2 - adicionar limite diário de 10 transações diárias
#filtrar as operações diárias, se já atingiu 10, bloqueie qualquer operação
#O extrato deve conter data e hora das transações


#Importações
from datetime import datetime

#Saudação:
print("""
++++++++++++++++++++++++++++++++++++      
     Olá! Seja Bem ao PyPay!🌐
O melhor banco digital em Pyhon!🐍
      
+++++++++Version: V2.0++++++++++++++
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
extrato = f""
saques_feitos = 0
transacoes_realizadas = []
LIMITE_SAQUE = 3
LIMITE_TRANSACAO_DIARIA = 10

msg_valor_invalido = "Falha! Informe um valor a partir de R$ 0,01\n"
msg_limite_saque = F"Limite de {LIMITE_SAQUE} saque(s) atingidos!\n"
msg_limite_transacoes = f"Limite de {LIMITE_TRANSACAO_DIARIA} transações diárias excedido\n"

#Definimos while True para fazer um looping
while True:

    opcao = int(input(menu))
    print("")

    #Depósito
    if opcao == 1:
        transacoes_hoje = transacoes_realizadas.count(datetime.now().strftime("%d/%m/%Y"))
        transacoes_excedidas = transacoes_hoje >= LIMITE_TRANSACAO_DIARIA
        if transacoes_excedidas:
             print(msg_limite_transacoes)

        else:
             valor = float(input("Informe o valor que deseja depositar: "))

             if valor > 0:
                  saldo += valor
                  transacoes_realizadas.append(datetime.now().strftime("%d/%m/%Y"))
                  data_atual = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
                  extrato += f"{data_atual} || Depósito || R$ {valor:.2f}\n"
                  print(f"Depósito de R$ {valor:.2f} realizado com sucesso!!\nSaldo atual R$ {saldo:.2f}\n")
                  
             else:     
                  print(msg_valor_invalido)
        
     
     #Saque
    elif opcao == 2:
         transacoes_hoje = transacoes_realizadas.count(datetime.now().strftime("%d/%m/%Y"))
         transacoes_excedidas = transacoes_hoje >= LIMITE_TRANSACAO_DIARIA
         if transacoes_excedidas:
               print(msg_limite_transacoes)

         else:
             valor = float(input("Informe o valor que deseja sacar: ")) 
         
         
             #definindo variáveis limitadoras do saque
             transacoes_hoje = transacoes_realizadas.count(datetime.now().strftime("%d/%m/%Y"))
             transacoes_excedidas = transacoes_hoje >= LIMITE_TRANSACAO_DIARIA
             saldo_insuficiente = valor > saldo
             limite_insuficiente = valor > LIMITE
             saques_excedido = saques_feitos >= LIMITE_SAQUE
         
             #Definindo condicionais de saque - É preciso definir antes os limites, e possíveis erros antes do saque ser autorizado
             if saldo_insuficiente:
                    print(f"Falha! Valor digitado maior que o saldo. Saldo atual R$ {saldo:.2f}\n")
             elif limite_insuficiente:
                    print(f"Falha! Seu limite por saque é de R$ {LIMITE}.\n")
             elif saques_excedido:
                    print(msg_limite_saque)      
                         
                    #Operação de saque    
             elif valor > 0:
                    saldo -= valor
                    transacoes_realizadas.append(datetime.now().strftime("%d/%m/%Y"))
                    data_atual = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
                    extrato += f"{data_atual} || Saque    || R$ {valor:.2f}\n"
                    print(f"Saque de R$ {valor:.2f} realizado com sucesso!!\nSaldo atual R$ {saldo:.2f}\n")
                    saques_feitos += 1
             else:
                  print(msg_valor_invalido)

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
Saldo atual R$ {saldo:.2f}""")
     #definido break para parar o código         
    elif opcao == 0:
         print("""
Muito obrigado por usar o PyPay!🌐
✨Até logo!!✨""")
         break
    
    else:
         print("\n Digite uma opção válida! \n")
    






