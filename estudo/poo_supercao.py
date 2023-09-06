class Cachorro:
    def __init__(self, nome, idade):
        self.nome = nome 
        self.idade = idade
        self.__identidade_secreta = "Super Cão" #dois underscores antes do nome do atributo indica ser um atributo privado#

    def latir(self):
        print("Au Au Au")

    def sentar(self):
        print("O {} obedeceu e sentou!".format(self.nome))

    def rolar(self):
        print("O {} odedeceu e rolou, parando de barriga para cima!!".format(self.nome)) 

    def mostrar_identidade_secreta(self):
        print("Olá sou o {}".format(self.__identidade_secreta))

    def __mudar_identidade_secreta(self, nova_identidade): #função privada para alterar um atributo privado, dando mais segurança
        self.__identidade_secreta = nova_identidade

    def atualizar_identidade(self, nova_identidade):
        self.__mudar_identidade_secreta(nova_identidade)

cachorro_1 = Cachorro("Krypto", 3)
cachorro_2 = Cachorro("Jack", 2)

print("O nome dele é {}, e ele possui {} anos".format(cachorro_1.nome, cachorro_1.idade))
cachorro_1.latir()
cachorro_2.sentar()
cachorro_2.rolar()
cachorro_1.mostrar_identidade_secreta()

print(id(cachorro_1))
print(id(cachorro_2))

