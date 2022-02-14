from Banco import Banco

class DadosBanco(object):

    def __init__(self, idcont = "", movimento = "", caminhao = "",
    placa = "", odometro = "", motorista = "", destino = "", lacre = "", usuario= "", data = ""):
        self.info = {}
        #self.idusuario = idusuario

        self.idcont = idcont
        self.movimento = movimento
        self.caminhao = caminhao
        self.placa = placa
        self.odometro = odometro
        self.motorista = motorista
        self.destino = destino
        self.lacre = lacre
        self.usuario = usuario
        self.data = data


    def insertUser(self):

        banco = Banco()
        try:
            c = banco.conexao.cursor()

            minha_query = """INSERT INTO controles (movimento, caminhao, placa, odometro,motorista, destino, lacre, usuario, data) VALUES (?,?,?,?,?,?,?,?,?)"""

            # Convert data into tuple format
            data_tuple = (self.movimento, self.caminhao, self.placa, self.odometro, self.motorista, self.destino, self.lacre, self.usuario, self.data)

            c.execute(minha_query, data_tuple)



            banco.conexao.commit()
            c.close()


            return " Registrado com sucesso!"
        except:
            return " Atenção: Ocorreu um erro na inserção"

    def selecttodos(self, tb_movimento):
        banco = Banco()


        try:

            c = banco.conexao.cursor()

            c.execute("SELECT * FROM controles ORDER BY data DESC")


            tb_movimento.delete(*tb_movimento.get_children())
            for linha in c:
                self.id = linha[0]
                self.movimento = linha[1]
                self.caminhao = linha[2]
                self.placa = linha[3]
                self.odometro = linha[4]
                self.motorista = linha[5]
                self.destino=linha[6]
                self.lacre=linha[7]
                self.usuario=linha[8]
                self.data=linha[9]



                tb_movimento.insert("","end",values=(self.movimento,self.caminhao,self.placa,self.odometro,self.motorista,self.destino,
                self.lacre,self.usuario,self.data))
                #print(valorTotal)

            c.close()
            return "Atualizado com sucesso!"
        except banco.conexao.Error as error:
            return "Ocorreu um erro na atualização"

