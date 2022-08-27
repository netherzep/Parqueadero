from ast import Assert
from Parquear import Parquear
from datetime import datetime
from Payment import Payment
import random


if __name__ == '__main__':
    
    print("Bienvenido al parqueadero Diego Llanos\n")
    Usuarios: Parquear = []
    Parq: Parquear
    Espacios_Disp = 10
    lugarParqueo: int = 0
    desicion: str = "y"
    Opcion: int
    Tiempo_Uso: datetime
    Contador_espacios = 0
    
    while desicion == "y":
        
        if Espacios_Disp == 0:
            print("No hay más espacios en el parqueadro\n")
            break

        Opcion = int(input("Qué desea hacer?\n1.Parquear Carro.\n2.Retirar Carro.\n"))

        if Opcion == 1:
            
            print("-------------Parquear nuevo Vehiculo-------------\n")
            print("Espacios Disponibles " + str(Espacios_Disp))
            Hora_entrada = datetime.now()
            Parq = Parquear(input("Digite el nombre del nuevo cliente: \n"), 
            input("Digite el número de identificación del cliente: \n"), 
            input("Digite la placa del Auto: \n"),
            input("Digite el modelo del Auto: \n"),Contador_espacios,Espacios_Disp, Hora_entrada)
            Contador_espacios += 1 
            print(f"El lugar de parqueo para {Parq.getname()} es el: {Parq.GetLugarParqueo()+1}")
            Espacios_Disp -= 1
            Parq.SetEspacios_Disponibles(Espacios_Disp)
            print(lugarParqueo)
            Usuarios.append(Parq)
            for users in Usuarios:
                print(users)

        elif Opcion == 2:

            for i in Usuarios:
                print(i)

            print("-------------Retirar Vehiculo-------------\n")

            BuscarUsuario = input("Digite la cedula del cliente: \n")
              
            for user, Parq in enumerate(Usuarios):
                if Parq.getId() == BuscarUsuario:
                    print(f"El usuario que desea retirar el Vehiculo es: {Parq.getname()} con cédula {Parq.getId()}")

        desicion = input("Desea continuar  con la ejecución del programa? Y/N? \n")
    
    

    




