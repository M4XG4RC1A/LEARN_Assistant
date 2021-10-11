from tkinter import *
import time
import webbrowser

#Funcion para obtener
def Llamada(srcS,Nombre):
    File=open(srcS,"r")
    Lines=File.readlines()
    File.close()
    Result=Lines[0].rstrip("\n")
    Result=Result.split("@")
    Direccion=Result[1]
    for index in range(len(Lines)):
        Result=Lines[index].rstrip("\n")
        Result=Result.split("@")
        Name=Result[0]
        if(Nombre==Name):
            Direccion=Result[1]
    if Direccion[0:3] != "htt":
    	Direccion="https://"+Direccion
    return Direccion
def MandarLink(Link):
    webbrowser.open(Link)
    pass
def BtnLlama(Nombre):
	Documento = "C:\\Users\\maxga\\OneDrive\\Documentos\\ActividadesPersonal\\MiniBootCamp\\Contactos\\ContactosTeams.txt"
	Direccion=Llamada(Documento,Nombre)
	MandarLink(Direccion)
def Final():
	root.destroy()
	pass
def Destruir():
	root.after(5000,Final())
	pass
def FunAyuda():
	Help = Toplevel(root, width=400, height=400)
	Label(Help, image=FondoAyuda).place(relwidth=1,relheight=1)
	EntradaNombre = Entry(Help,width=40, font=20)
	EntradaNombre.place(x=16,y=199)
	Llama = Button(Help, image=BtnLlamar, command=lambda:BtnLlama(EntradaNombre.get())).place(x=113,y=277)
	pass

Imagenes = "C:\\Users\\maxga\\OneDrive\\Documentos\\ActividadesPersonal\\MiniBootCamp\\Diseños\\"

root=Tk()
root.title("Llamada Microsoft Teams")
Fondo = PhotoImage(file=Imagenes+"FTeams.png")
BtnSalir = PhotoImage(file=Imagenes+"BListo.png")
BtnAyuda = PhotoImage(file=Imagenes+"BAyuda.png")
BtnLlamar = PhotoImage(file=Imagenes+"BLlamar.png")
FondoAyuda = PhotoImage(file=Imagenes+"FAyuda.png")
Words = Frame(root, bg="green", width=400, height=400)
Words.pack() #Start of the Principal Frame with the first Flange Color

Label(Words, image=Fondo).place(relwidth=1,relheight=1)

Cerrar = Button(Words, image=BtnSalir, command=lambda:Final()).place(x=113,y=291)
Ayuda = Button(Words, image=BtnAyuda, command=lambda:FunAyuda()).place(x=113,y=344)

root.mainloop()