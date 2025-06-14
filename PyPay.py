#Este é o sistema bancário criado para o desafio da DIO
#O desafio consiste em criar um sistema bancário em que:

#Deve possuir 3 funções: Saque, Depósito e Extrato
#O valores retornado em extrato deve ser no formato R$ 100,00
#Cada saque e depósito deve ser armazenado no extrato devidamente identificado
#Exibir mensagens de erro caso o saldo seja insuficiente e demais erros possíveis
#Possuir Menu - E não é necessário possuir usuário

#Fase 1.5 - adicionar limite diário de 10 transações diárias
#filtrar as operações diárias, se já atingiu 10, bloqueie qualquer operação
#O extrato deve conter data e hora das transações.

#Fase 2 - Usando funções/módulos
#Transformando código com módulos
#Adicionando funções de criar usuário e criar conta.
#A agência sempre será 001
#Cada usuário pode ter mais de uma conta, as contas deve ser sequenciais
#Saque deve receber apenas argumentos por nome
#Função depósito deve receber argumentos somente por posição
#extrato deve receber argumentos por posição e nome
#Armazenar usuários em uma lista, o usuário é composto por: Nome, data de nascimento, cpf e endereço, sendo o endereço logradouro,n,bairro,cidade/UF
#CPF somente números



#Importações
from datetime import datetime
from tracemalloc import stop

#Saudação:
def saudacao():
     print("""
     ++++++++++++++++++++++++++++++++++++      
          Olá! Seja Bem ao PyPay!🌐
     O melhor banco digital em Pyhon!🐍
          
     +++++++++Version: V2.0++++++++++++++
          """)

     #return saudacao()
saudacao()
#Menu:

def menu():
     print("""
     ************************************
                    MENU
     ************************************      

     [1] - 📨 Depósito
     [2] - 💲 Saque
     [3] - 🧾 Ver extrato
     [4] - ➕ Criar usuário
     [5] - 🔷 Criar conta
     [0] - ❌ Sair

     Digite a opção desejada: """, end="")
     return int(input())
     

#Iniciamos definindo valores base para o código
saldo = 0
LIMITE = 500
extrato = f""
saques_feitos = 0
transacoes_realizadas = []
usuarios = []
LIMITE_SAQUE = 3
LIMITE_TRANSACAO_DIARIA = 10
contas = []
AGENCIA = "0001"

msg_valor_invalido = "Falha! Informe um valor a partir de R$ 0,01\n"
msg_limite_saque = F"Limite de {LIMITE_SAQUE} saque(s) atingidos!\n"
msg_limite_transacoes = f"Limite de {LIMITE_TRANSACAO_DIARIA} transações diárias excedido\n"

def depositar(saldo, valor, extrato,/):
     if valor > 0:
          saldo += valor
          transacoes_realizadas.append(datetime.now().strftime("%d/%m/%Y"))
          data_atual = datetime.now().strftime("%d/%m/%Y, %H:%M:%S")
          extrato += f"{data_atual} || Depósito || R$ {valor:.2f}\n"
          print(f"Depósito de R$ {valor:.2f} realizado com sucesso!!\nSaldo atual R$ {saldo:.2f}\n")

     else:     
          print(msg_valor_invalido)

     return saldo, extrato


def sacar(*, saldo, valor, extrato, LIMITE,saques_feitos,LIMITE_SAQUE):
     saldo_insuficiente = valor > saldo
     limite_insuficiente = valor > LIMITE
     saques_excedido = saques_feitos >= LIMITE_SAQUE
     
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

     return saldo, extrato


def mostrar_extrato(saldo,/,*, extrato):
     if extrato == f"":
          print("Nenhuma movimentação realizada!")
     
     else:
          print("************************************")
          print("            Extrato")
          print("************************************")
          print(extrato)
     return saldo, extrato


def novo_usuario(usuarios):
     cpf = input("Informe seu CPF (Apenas números): ")
     usuario = filtrar_usuario(cpf,usuarios)

     if usuario:
          print("Essa conta já existe!")
          return
     
     nome = input("Digite sem nome completo: ")
     nascimento = input("Informe sua data de nascimento (DD-MM-AAAA): ")
     endereco = input("Informe seu endereço (Logradouro, nº - bairro - Cidade/UF): ")

     usuarios.append({"nome":nome, "nascimento": nascimento,"cpf":cpf, "endereco":endereco})

     print("Usuário criado com sucesso!!\n")

def filtrar_usuario(cpf, usuarios):
     usuarios_filtro = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
     return usuarios_filtro[0] if usuarios_filtro else None

     
def nova_conta(AGENCIA, numero_conta, usuario):
     cpf = input("Informe seu CPF: ")
     usuario = filtrar_usuario(cpf, usuarios)

     if usuario:
          print("Conta criada com sucesso!!!")
          return {"AGENCIA": AGENCIA, "numero_conta":numero_conta, "usuario":usuario}

     print("Usuário não encontrado")


#Definimos while True para fazer um looping
while True:

    opcao = int(menu())

    #Depósito
    if opcao == 1:
          transacoes_hoje = transacoes_realizadas.count(datetime.now().strftime("%d/%m/%Y"))
          transacoes_excedidas = transacoes_hoje >= LIMITE_TRANSACAO_DIARIA
          
          if transacoes_excedidas:
               print(msg_limite_transacoes)
          else:     
               valor = float(input("Informe o valor que deseja sacar: "))
               saldo, extrato = depositar(saldo, valor, extrato)


     #Saque
    elif opcao == 2:         
         transacoes_hoje = transacoes_realizadas.count(datetime.now().strftime("%d/%m/%Y"))
         transacoes_excedidas = transacoes_hoje >= LIMITE_TRANSACAO_DIARIA
         if transacoes_excedidas:
               print(msg_limite_transacoes)

         else:
              valor = float(input("Informe o valor que deseja depositar: "))
              saldo, extrato = sacar(
                    saldo=saldo,
                    valor=valor,
                    extrato=extrato,
                    LIMITE=LIMITE,
                    saques_feitos=saques_feitos,
                    LIMITE_SAQUE=LIMITE_SAQUE
                    )
     
    elif opcao == 4:
          novo_usuario(usuarios)

    elif opcao == 5:
         numero_conta = len(contas) + 1
         conta = nova_conta(AGENCIA, numero_conta, usuarios)

         if conta:
              contas.append(conta)
                      

    #Extrato          
    elif opcao == 3:
         saldo, extrato = mostrar_extrato(saldo,extrato=extrato)

    elif opcao == 0:
         print("Até logo!!")
         break
    else:
         print("\n Digite uma opção válida! \n")

    






