from database import BancoDeDados

if __name__ == "__main__":
    banco = BancoDeDados()
    banco.conecta()
    banco.createTable()
    banco.inserirCliente("Mateus", "11111111111", "mateus@gmail.com")
    banco.inserirCliente("Tatiane", "22222222222", "tatiane@gmail.com")
    banco.removerCliente("11111111111")
    banco.buscarCliente("11111111111")
    banco.buscarEmail("tatiane@gmail.com")
    banco.desconecta()



