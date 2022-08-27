from datetime import datetime

class Payment:
    costo_min: int = 80
    Name: str
    Id: str
    Tiempo_uso: datetime

    def __init__(self, Name, Id, Tiempo_uso):
        self.Name = Name
        self.Id = Id
        self.Tiempo_uso = Tiempo_uso

    def GetCosto_Total(self):
        return self.Tiempo_uso*self.costo_min
        