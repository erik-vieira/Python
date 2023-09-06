class ContaCorrente:
    def __init__(self, conta, agencia, nome, cpf, senha, saldo):
        self.conta = conta
        self.agencia = agencia
        self.nome = nome
        self.cpf = cpf
        self.senha = senha
        self.saldo = saldo


    def get_consultar_Conta(self):
        print('conta corrente: {}'.format(self.conta))
        print('Agência: {}'.format(self.agencia))
        print('Nome: {}'.format(self.nome))
        print('CFP: {}'.format(self.cpf))
        print('Saldo em conta: R$ {:.2f}'.format(self.saldo))

    def set_deposito(self):
        deposito = float(input('Qual valor deseja depositar? '))
        if deposito > 0.00:
            self.saldo = deposito + self.saldo
            print("Deposito realizado com sucesso! Seu novo saldo é de R$ {:.2f}".format(self.saldo))
        else:
            print('Seu deposito deve ser maior que zero!')

    def set_sacar(self):
        saque = float(input("Qual valor deseja sacar? "))
        if saque <= self.saldo:
            self.saldo = self.saldo - saque
            print("Saque realizado com sucesso! Seu novo saldo é de R$ {:.2f}".format(self.saldo))
        else:
            print('Saldo insuficiente para saque. Seu saldo é de R$ {:.2f}'.format(self.saldo))

    def cpf02(self):
        cpf02 = input("Informe seu CPF: ")
        if cpf02 == self.cpf:
            cc_02.senha02()
        else:
            print("CPF invalido")

    def senha02(self):
        senha02 = input("Informe sua senha: ")
        if senha02 == self.senha:
            inicio()
        else:
            print("Senha Incorreta")

def inicio():
    print("Selecione a opção desejada?")
    print("[1] - Consultar Conta \n[2] - Deposito \n[3] - Saque \n[4] - Encerrar sessão")
    opcao = int(input(""))
    if opcao == 1:
        cc_02.get_consultar_Conta()
        finalizar()
    elif opcao == 2:
        cc_02.set_deposito()
        finalizar()
    elif opcao == 3:
        cc_02.set_sacar()
        finalizar()
    elif opcao == 4:
        print("Banco Erik agradece!")
        exit()
    elif opcao > 4:
        print("Opção invalida!")
        finalizar()


def finalizar():
    print("Deseja realizar outra operação? ")
    print("[1] - Sim \n[2] - Não")
    opcao2 = int(input(""))
    if opcao2 == 1:
        print("Selecione a opção desejada?")
        print("[1] - Consultar Conta \n[2] - Deposito \n[3] - Saque \n[4] - Encerrar sessão")
        opcao = int(input(""))
        inicio()
    else:
        print("Banco Erik agradece!")
        exit()



cc_01 = ContaCorrente('0123', '0001', 'Erik Viera', '168.478.470-00', '12345', 0.00)
cc_02 = ContaCorrente('0124', '0001', 'Vitória Futro', '497.423.982-70', '0403', 0.00)

print("Bem vindo ao banco Erik")
cc_02.cpf02()