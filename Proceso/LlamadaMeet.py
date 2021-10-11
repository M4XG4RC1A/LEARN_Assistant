#Importar Librerias
import sys
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
    return Direccion
def MandarLink(Link):
    webbrowser.open(Link)
    pass

import sys
import webbrowser

Documento = "C:\\Users\\maxga\\OneDrive\\Documentos\\ActividadesPersonal\\MiniBootCamp\\Contactos\\ContactosGoogleMeet.txt"

arreglo = sys.argv
LlamarA = arreglo[1]
print("Llamemos a "+ LlamarA)

Direccion=Llamada(Documento,LlamarA)
MandarLink(Direccion)