from datetime import datetime

class Oldbank():
    """ Classe responsavel pela movimentacao da conta"""

    def __init__(self):
        self.numeroBanco = '999'
        self.numeroAg = '08'
        self.nomeCliente = None
        self.conta = 9991
        self.saldo = 0

    def cria_conta(self):
        """ método cria conta""" 
        print('Bem Vindo(a) ao sistema de criação de conta!')
        nome = input('Digite seu nome: ')
        self.nomeCliente = nome
        self.conta += 1
    
    def depositar(self):
        """Método de deposito"""
        self.deposito = int(input('Digite o valor de deposito: '))
        if self.deposito > 0:
            self.saldo += self.deposito
        else:
            print('Valor Inválido')
    
    def sacar(self):
        """Metodo de saque"""
        self.saque = int(input('Digite o valor de saque: '))
        if self.saque < self.saldo:
            self.saldo -= self.saque
        else:
            print('Saldo Insuficiente')

    def extrato(self):
        print(f'Data e Hora da consulta: {datetime.now()}')
        print(f'-'*20)
        print(f'Ag: {self.numeroAg} Conta: {self.conta}')
        print(f'Cliente: {self.nomeCliente}')
        print(f'Saldo atual: {self.saldo}')

