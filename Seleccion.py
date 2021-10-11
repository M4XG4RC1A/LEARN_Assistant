#Funcion para obtener
#Manipule Formats
def Obtain(srcS,index):
    File=open(srcS,"r")
    Lines=File.readlines()
    File.close()
    Result=Lines[index].rstrip("\n")
    Result.strip()
    return Result
    pass
def modify(arch,nom,direc):
    Documento = "C:\\Users\\maxga\\OneDrive\\Documentos\\ActividadesPersonal\\MiniBootCamp\\Contactos\\Contactos.txt"
    DocumentoM = "C:\\Users\\maxga\\OneDrive\\Documentos\\ActividadesPersonal\\MiniBootCamp\\Contactos\\ContactosGoogleMeet.txt"
    DocumentoT = "C:\\Users\\maxga\\OneDrive\\Documentos\\ActividadesPersonal\\MiniBootCamp\\Contactos\\ContactosTeams.txt"
    DocumentoZ = "C:\\Users\\maxga\\OneDrive\\Documentos\\ActividadesPersonal\\MiniBootCamp\\Contactos\\ContactosZoom.txt"
    Guardar = ""
    if Seleccion.get()=="Zoom":
        Guardar=DocumentoZ
    elif Seleccion.get()=="Google Meet":
        Guardar=DocumentoM
    elif Seleccion.get()=="Microsoft Teams":
        Guardar=DocumentoT
        pass
    File=open(Guardar, "r")
    lines=File.readlines()
    File.close()
    File_New=open(Guardar, "w")
    Nuevo=nom+"@"+direc;
    Constante=0
    for l in lines:
        Result=l.split("@")
        Name=Result[0]
        if Name==nom:
            File_New.write(Nuevo+"\n")
            Constante=1
        else:
            l=l.rstrip("\n")            
            File_New.write(l+"\n")
            pass
    pass
    if Constante==0:
        File_New.write(Nuevo)
        pass
    File_New.close()

    File=open(Documento, "r")
    lines=File.readlines()
    File.close()
    Rep=0
    File_New=open(Documento, "w")
    for l in lines:
        Result=l.split("@")
        Name=Result[0]
        if Name==nom:
            Rep=1
        pass
    for l in lines:
        l=l.rstrip("\n")
        File_New.write(l+"\n")
        pass
    Nuevo=nom+"@"+direc;
    if Rep==0:
        File_New.write(Nuevo)
    File_New.close()
    print("Listo")
    EntradaNombre.delete(0,"end")
    EntradaDireccion.delete(0,"end")
    pass

from tkinter import *
import time

Documento = "C:\\Users\\maxga\\OneDrive\\Documentos\\ActividadesPersonal\\MiniBootCamp\\Contactos\\Contactos.txt"
Imagenes = "C:\\Users\\maxga\\OneDrive\\Documentos\\ActividadesPersonal\\MiniBootCamp\\Diseños\\"

root=Tk()
root.title("Registro")
Fondo = PhotoImage(file=Imagenes+"FRegistro.png")
BtnRegistrar = PhotoImage(file=Imagenes+"BRegistrar.png")

Seleccion = StringVar()
Seleccion.set("Zoom")
opciones=["Zoom","Google Meet","Microsoft Teams"]

Words = Frame(root, bg="green", width=400, height=400)
Words.pack() #Start of the Principal Frame with the first Flange Color

Label(Words, image=Fondo).place(relwidth=1,relheight=1)

EntradaNombre = Entry(Words,width=40, font=30)
EntradaNombre.place(x=16,y=196)
EntradaDireccion = Entry(Words,width=40, font=30)
EntradaDireccion.place(x=16,y=130)
opcion=OptionMenu(Words,Seleccion,*opciones)
opcion.config(width=36, font=20)
opcion.place(x=16,y=260)

Registrar = Button(Words, image=BtnRegistrar, command=lambda:modify(Documento,EntradaNombre.get(),EntradaDireccion.get())).place(x=113,y=318)

root.mainloop()