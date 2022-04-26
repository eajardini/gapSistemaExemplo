class Clientes():
    def __init__(self, codigo, nome, removido):
        self.codigo = codigo
        self.nome = nome
        self.removido = removido


def cadClientes():
    print("**** Cadastro de Clientes ****")
    codigo = input("Informe o código do cliente: ")
    nome = input("Informe o nome do cliente: ")
    cliente = Clientes(codigo, nome, "n")
    bdCliente.append(cliente)
    print("[main.py|cadClientes]Cliente cadastrado com sucesso!")
    print("  ")


def listarClientes():
    print("**** Listagem de Clientes ****")
    for x in range(len(bdCliente)):
        print("Código:" + bdCliente[x].codigo + " Nome:" + bdCliente[x].nome + " Removido:" + bdCliente[x].removido)

    print("  ")
    print("[main|listarClientes]Listagem completada com sucesso!")
    print("  ")

def atualizarClientes():
    print("**** Atualização de dados de Clientes ****")
    codigo = input("Informe o código do cliente que será alterado: ")
    novoNome = input("Informe o novo nome do cliente: ")
    alterado = "n"
    for x in range(len(bdCliente)):
        if bdCliente[x].codigo == codigo:
            bdCliente[x].nome = novoNome
            alterado = "s"

    print("  ")
    if alterado == "s":
        print("[main|alteraCliente] Cliente alterado com sucesso")
    else:
        print("[main|alteraCliente] Não houve altareção de cliente")
    print("  ")

def removerClientes():
    print("**** Remoção de dados de Clientes ****")
    print("Fazer como exercício")


# Variável que simula uma Banco de Dados
bdCliente = []


