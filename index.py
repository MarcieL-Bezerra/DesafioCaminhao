from tkinter import *
from tkinter import ttk
import tkinter.messagebox as tkMessageBox
import os
from comandos import DadosBanco
from datetime import datetime

#comandos
data_atual = datetime.now()
data_atual = data_atual.strftime('%d/%m/%Y %H:%M')
def saindo():
	result = tkMessageBox.askquestion("", "Confirma a saída?", icon='question')
	if result=='yes':
		os._exit(1)
	else:
		pass

def buscarUsuario():
	#busca no banco moradores e visitantes pelo cpf ou casa ou veiculo
	user = DadosBanco()
	resposta = user.selecttodos(tb_movimento=tb_movimento)

	
	#limpando()
	tkMessageBox.showinfo('Resposta', message=resposta)
def reali_cadstro():
    user = DadosBanco()
    user.movimento = combomov.get()
    user.caminhao = combocamin.get()
    user.placa = txt_placa.get()
    user.odometro = txt_odom.get()
    user.motorista = txt_moto.get()
    user.destino = combodep.get()
    user.lacre = txt_lacre.get()
    user.usuario = txt_usuario.get()
    user.data = data_atual


    resposta = user.insertUser()
    buscarUsuario()
#tela inicial

tinicial = Tk()

tinicial.geometry("900x900+0+0")
tinicial.title("MB - CONTROLE DE FROTA EMPRESA ALFA ")

lbl_bemvindo= Label(tinicial, height=2,bg ='SkyBlue',text= 'Seja Bem-Vindo à ALFA',fg='black',font=('arial',25,'bold'))
lbl_bemvindo.place(relx=0.2, rely = 0.0)

#text e imputs ld esquerdo

lbl_status=Label(tinicial,bd=8, bg ='SkyBlue',text="Movimento", fg='black',font=('arial',9,'bold'))
lbl_status.place(relx=0.1, rely = 0.13)

combomov = ttk.Combobox(tinicial,width=9,values=["Ent","Sai"],font=('arial',14,'bold'))
combomov.place(relx=0.2, rely = 0.13)
combomov.current(0)

lbl_status=Label(tinicial,bd=8, bg ='SkyBlue',text="Caminhão", fg='black',font=('arial',9,'bold'))
lbl_status.place(relx=0.1, rely = 0.18)

combocamin = ttk.Combobox(tinicial,width=9,values=["C1","C2","C3","C4","C5"],font=('arial',14,'bold'))
combocamin.place(relx=0.2, rely = 0.18)
combocamin.current(0)

lbl_dest=Label(tinicial,bd=8, bg ='SkyBlue',text="Destino", fg='black',font=('arial',9,'bold'))
lbl_dest.place(relx=0.1, rely = 0.23)

combodep = ttk.Combobox(tinicial,width=9,values=["Dep1","Dep2","Dep3"],font=('arial',14,'bold'))
combodep.place(relx=0.2, rely = 0.23)
combodep.current(0)

lbl_placa=Label(tinicial,bd=4, bg ='SkyBlue',text="Placa", fg='black',font=('arial',9,'bold'))
lbl_placa.place(relx=0.1, rely = 0.28)

txt_placa = ttk.Entry(tinicial,width=10,font=('arial',14,'bold'))
txt_placa.place(relx=0.2, rely = 0.28)

lbl_odom=Label(tinicial,bd=4, bg ='SkyBlue',text="Odômetro", fg='black',font=('arial',9,'bold'))
lbl_odom.place(relx=0.1, rely = 0.33)

txt_odom = ttk.Entry(tinicial,width=10,font=('arial',14,'bold'))
txt_odom.place(relx=0.2, rely = 0.33)

#text e imputs ld direito

lbl_moto=Label(tinicial,bd=4, bg ='SkyBlue',text="Motorista", fg='black',font=('arial',9,'bold'))
lbl_moto.place(relx=0.4, rely = 0.13)

txt_moto = ttk.Entry(tinicial,width=10,font=('arial',14,'bold'))
txt_moto.place(relx=0.5, rely = 0.13)

lbl_lacr=Label(tinicial,bd=4, bg ='SkyBlue',text="Lacres", fg='black',font=('arial',9,'bold'))
lbl_lacr.place(relx=0.4, rely = 0.18)

txt_lacre = ttk.Entry(tinicial,width=10,font=('arial',14,'bold'))
txt_lacre.place(relx=0.5, rely = 0.18)

lbl_histo=Label(tinicial,bd=4, bg ='SkyBlue',text="Usuario", fg='black',font=('arial',9,'bold'))
lbl_histo.place(relx=0.4, rely = 0.23)

txt_usuario = ttk.Entry(tinicial,width=10,font=('arial',14,'bold'))
txt_usuario.place(relx=0.5, rely = 0.23)

lbl_histo=Label(tinicial,bd=4, bg ='SkyBlue',text="Data", fg='black',font=('arial',9,'bold'))
lbl_histo.place(relx=0.4, rely = 0.28)

txt_data = ttk.Entry(tinicial,width=10,font=('arial',14,'bold'))
txt_data.place(relx=0.5, rely = 0.28)
txt_data.insert(0, data_atual)

#botoes

btnCadastrar = Button(tinicial,text = "Cadastrar",bg='SkyBlue',bd=8,compound = LEFT, fg='black',font=('arial',14,'bold'),command = reali_cadstro)
btnCadastrar.place(relx=0.75, rely = 0.16)

btnSair = Button(tinicial,text = "    Sair     ",bg='SkyBlue',bd=8,compound = LEFT, fg='black',font=('arial',14,'bold'), command = saindo)
btnSair.place(relx=0.75, rely = 0.26)

#TABELA TREEVIEW
global tb_movimento
frame = Frame(tinicial,bg='SkyBlue',bd=2,relief= "solid")
frame.place(relx=0.05, rely = 0.4)
titu_dep=Label(frame,width=25,bd=4,bg='SkyBlue', height=2,text= 'CONTROLE DE FROTA',fg='black',font=('arial',14,'bold'))
titu_dep.pack(side=TOP)

tb_movimento = ttk.Treeview(frame, column=(1,2,3,4,5,6,7,8,9), show='headings', height=10)
tb_movimento.pack(side=LEFT)
#tb_movimento.heading('#0', text='', anchor=CENTER)
#largura e alinhamento das colunas
tb_movimento.column(1, width=100, anchor="center")
tb_movimento.column(2, width=100, anchor="center")
tb_movimento.column(3, width=80, anchor="center")
tb_movimento.column(4, width=100, anchor="center")
tb_movimento.column(5, width=100, anchor="center")
tb_movimento.column(6, width=100, anchor="center")
tb_movimento.column(7, width=100, anchor="center")
tb_movimento.column(8, width=80, anchor="center")
tb_movimento.column(9, width=110, anchor="center")


#cabeçalhos
tb_movimento.heading(1, text='MOVIMENTO')
tb_movimento.heading(2, text='CAMINHÃO')
tb_movimento.heading(3, text='PLACA')
tb_movimento.heading(4, text='ODÔMETRO')
tb_movimento.heading(5, text='MOTORISTA')
tb_movimento.heading(6, text='DESTINO/ORIGEM')
tb_movimento.heading(7, text='LACRES')
tb_movimento.heading(8, text='USUARIO')
tb_movimento.heading(9, text='DATA')

#tb_movimento.bind('<<TreeviewSelect>>', mostraSalientado)

sb = Scrollbar(frame, orient=VERTICAL)
sb.pack(side=RIGHT, fill=Y)
tb_movimento.config(yscrollcommand=sb.set)
sb.config(command=tb_movimento.yview)
style = ttk.Style()
style.theme_use("clam")
style.map("Treeview")
style.configure(".", font=('Helvetica', 10), foreground="blue")
#style.configure("Treeview.Heading", foreground='green')


iniciando = buscarUsuario()
tinicial.mainloop()