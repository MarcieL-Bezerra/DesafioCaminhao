#importando módulo do SQlite
import sqlite3

class Banco():

    def __init__(self):
        self.veriferro = sqlite3
        self.conexao = sqlite3.connect('banco.db')
        self.createTable()

    def createTable(self):
        c = self.conexao.cursor()

        c.execute("""create table if not exists controles (
                     idcont integer primary key autoincrement,
                     movimento text,
                     caminhao text,
                     placa text,
                     odometro integer,
                     motorista text,
                     destino text,
                     lacre text,
                     usuario text,
                     data date)""")
        self.conexao.commit()
        c.close()