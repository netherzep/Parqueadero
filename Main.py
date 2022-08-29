from ast import Assert
from tokenize import String
from Parquear import Parquear
from datetime import datetime
from Payment import Payment
from Payment import Payment
import random
Usuarios: Parquear = [0]*2
Pagos: Payment = []
Parq: Parquear
Espacios_Disp = len(Usuarios)


def Decorador_impresion(Funcion):
    

    def Funcionint(*args, **kwargs):
        print("Imprimiendo Lista\n")
        Funcion(*args, **kwargs)
        print("\nLista impresa")
    return Funcionint

    

    

@Decorador_impresion
def printUsers(Lista, detalle: str):

    if detalle == "u":
        print("\n"+"-"*10+"Usuarios usando el parqueadero"+"-"*10+"\n")
    elif detalle == "p":
        print("\n"+"-"*10+"Historial de Pagos"+"-"*10+"\n")

    for user in Lista:
        print(user)
    
    print("\n")
   


def NuevoVehiculo (Espacios_Disp) -> int:
    print("-------------Parquear nuevo Vehiculo-------------")
    Hora_entrada = datetime.now().minute
    print(f"Hora de entrada: {Hora_entrada}")
    Parq = Parquear(input("Digite el nombre del nuevo cliente: \n"), 
            input("Digite el número de identificación del cliente: \n"), 
            input("Digite la placa del Auto: \n"),
            input("Digite el modelo del Auto: \n"),
            int(input("Digite el espacio donde desea parquear el vehiculo: \n")),Espacios_Disp, Hora_entrada)

    
    print(f"El lugar de parqueo para {Parq.getname()} es el: {Parq.GetLugarParqueo()}\n")
    
    Parq.SetEspacios_Disponibles(Espacios_Disp)
    Usuarios[Parq.GetLugarParqueo()-1] = Parq
    printUsers(Usuarios, "u")

    Espacios_Disp -= 1

    return Espacios_Disp

def RetirarVehiculo(Id: str, Usuarios, Espacios_Disp) -> int:
    Parq: Parquear
    for user, Parq in enumerate(Usuarios):
        
        if  Usuarios[user] == None:
            continue
        elif Parq.getId() == Id:
             print(f"\nEl usuario que desea retirar el Vehiculo es: {Parq.getname()} con cédula {Parq.getId()}\n")
             print(f"El tiempo de uso del parqueadero de {Parq.getname()} fue de $: {datetime.now().minute - Parq.GetHoraEntrada()} Minutos")
             Pago = Payment(Parq.getname(),Parq.getname(),datetime.now().minute - Parq.GetHoraEntrada())
             print(f"El costo a pagar por {Pago.getname()} Es: {Pago.GetCosto_Total()}")
             Pagos.append(Pago)
             Usuarios[user] = None
             Espacios_Disp += 1
             printUsers(Usuarios,"u")
             break
        else:
            print("La identificación: "+Id+" No se encuentra registrada")

         
    return Espacios_Disp


if __name__ == '__main__':
    
    print("Bienvenido al parqueadero Diego Llanos\n")
    desicion: str = "y"
    Opcion: int
     
    
    while desicion == "y":
        
        if Espacios_Disp == 0 and desicion != "y":
            print("No hay más espacios en el parqueadro\n")
            desicion = "y"
            break

        Opcion = int(input("Qué desea hacer?\n1.Parquear Carro.\n2.Retirar Carro.\n3.Mostrar Usuarios\n4.Imprimir Pagos\n"))

        if Opcion == 1 and Espacios_Disp !=0:

           print("Espacios Disponibles " + str(Espacios_Disp))
           Espacios_Disp = NuevoVehiculo(Espacios_Disp)
           print(f"\nVehiculo parqueado, espacios disponibles: {Espacios_Disp}\n")
        elif  Opcion == 1 and Espacios_Disp == 0:
            print("No hay espacios disponibles")
            desicion = "y"         

        elif Opcion == 2:

            print("-------------Retirar Vehiculo-------------\n")
            BuscarUsuario = input("Digite la cedula del cliente: \n")
            Espacios_Disp = RetirarVehiculo(BuscarUsuario, Usuarios, Espacios_Disp)
        
            print("Usuario Retirado")
        elif Opcion == 3:
            printUsers(Usuarios, "u")
        elif Opcion == 4:
            printUsers(Pagos, "p")

        desicion = input("Desea continuar  con la ejecución del programa? Y/N? \n")
    
    

    




