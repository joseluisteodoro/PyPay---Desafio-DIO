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
     Olá! Seja Bem ao PyPay!
O melhor banco digital em Pyhon!
      
+++++++++Version: V1.0++++++++++++++
      """)

#Menu:
menu = """
************************************
                MENU
************************************      
     Selecione a opção desejada:

[1] - Depositar
[2] - Sacar
[3] - Extrato
[0] - Sair

"""

#Iniciamos definindo valores base para o código
saldo = 0
LIMITE = 500
extrato = ""
saques_feitos = 0
LIMITE_SAQUE = 3

#Definimos while True para fazer um looping
while True:

    opcao = input(menu)

