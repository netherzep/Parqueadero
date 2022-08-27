
class Usuario:
    
    Name: str
    __Id: str
    __Placa: str
    Car_Model: str

    def __init__(self, Name, Id, Placa, Car_Model):
        self.Name = Name
        self.__Id = Id
        self.__Placa = Placa
        self.Car_Model = Car_Model


    def getname(self):
        return self.Name
    
    def setname(self, Name):
        self.Name = Name
    
    def getId(self):
        return self.__Id
    
    def setId(self, Id):
        self.__Id = Id
    
    def getPlaca(self):
        return self.__Placa
    
    def setPlaca(self, Placa):
        self.__Placa = Placa

    def getModelo(self):
        return self.Car_Model
    
    def setModelo(self, Car_Model):
        self.Car_Model = Car_Model

        
    