# coding=utf-8
import sqlite3


class BancoDeDados:
    """Representa do banco"""

    def __init__(self, nome='banco.db'):
        self.nome, self.conexao = nome, None

    def conecta(self):
        """Conecta passando o nome do arquivo"""
        self.conexao = sqlite3.connect(self.nome)

    def desconecta(self):
        """Desconecta do banco"""
        try:
            self.conexao.close()
        except AttributeError:
            pass

    def createTable(self):
        """Cria as tableas do banco"""
        try:
            cursor = self.conexao.cursor()
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS clientes (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                cpf VARCHAR(11) UNIQUE NOT NULL,
                email TEXT NOT NULL
            );
            """)
        except AttributeError:
            print("Faça a conexão antes de criar as tabelas")

    def inserirCliente(self, nome, cpf, email):
        """Insere cliente """
        try:
            try:
                cursor = self.conexao.cursor()
                cursor.execute(
                    """INSERT INTO clientes (nome, cpf, email) VALUES (?, ?, ?)
                """,(nome, cpf, email))

                self.conexao.commit()
            except sqlite3.IntegrityError:
                print("O CPF %s já está cadastrado" %cpf)
        except AttributeError:
            print("Faça a conexão com o banco")

    def buscarCliente(self, cpf):
        """Busca cliente pelo cpf"""
        try:
            cursor = self.conexao.cursor()
            cursor.execute(
                """SELECT * FROM clientes
            """)
            for linha in cursor.fetchall():
                if linha[2] == cpf:
                    print(linha[1])
                    break
                else:
                    print("CPF não cadastrado")
        except AttributeError:
            print("Faça a conexão com o banco")

    def removerCliente(self, cpf):
        """Remove cliente informando o CPF"""
        try:
            cursor = self.conexao.cursor()
            cursor.execute("""
            DELETE FROM clientes WHERE cpf=?
            """, (cpf,))
            self.conexao.commit()
        except AttributeError:
            print("Faça a conexão com o banco")

    def buscarEmail(self, email):
        try:
            cursor = self.conexao.cursor()
            cursor.execute("""
                SELECT email FROM clientes WHERE email=?
            """, (email,))
            print(cursor.fetchall()[0][0])

        except AttributeError:
            print("Faça a conexão com o banco")
