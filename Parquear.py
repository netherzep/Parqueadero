from Usuario import Usuario
from datetime import datetime

class Parquear(Usuario):
    
    Lugar_Parqueo: int
    Espacios_Disponibles: int
    Hora_entrada: datetime

    def __init__(self, Name, Id, Placa, Car_Model, Lugar_Parqueo, Espacios_Disponibles, Hora_entrada):
        super().__init__(Name, Id, Placa, Car_Model)
        self.Lugar_Parqueo = Lugar_Parqueo
        self.Espacios_Disponibles = Espacios_Disponibles
        self.Hora_entrada = Hora_entrada


    def __repr__(self):
        return f"Nombre: {self.Name}, Id: {Usuario.getId(self)}, Placa: {Usuario.getPlaca(self)}, Modelo: {self.Car_Model}, Hora entrada: {self.Hora_entrada}, Lugar de parqueo: {self.Lugar_Parqueo}"

    def SetEspacios_Disponibles(self, Espacios_Disponibles:int):
        self.Espacios_Disponibles = Espacios_Disponibles

    def GetEspacios_Dispobles(self):
        return self.Espacios_Disponibles

    def GetLugarParqueo(self):
        return self.Lugar_Parqueo
    
    def GetHoraEntrada(self):
        return self.Hora_entrada

    def getId(self):
        return super().getId()

    
