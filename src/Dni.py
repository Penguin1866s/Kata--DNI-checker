from src.tableAsignation import tableAsignation
class Dni:
    def __init__(self, stringDni=""):
        self.dni = stringDni
        self.table = tableAsignation().getTable()
        self.LENGHT_DNI = 9
        self.LENGHT_NUMBER_DNI = 8
    
    def getDni(self):
        return self.dni
    
    def getNumberDni(self):
        return self.dni[ : self.LENGHT_NUMBER_DNI]
    
    def getLetterDni(self):
        return self.dni[self.LENGHT_NUMBER_DNI : ]
    
    def calculateLetterDni(self):
        number_to_index = int(Dni(self.dni).getNumberDni()) % len(self.table)
        return self.table[number_to_index]
    
    def checkDni(self):
        if Dni(self.dni).calculateLetterDni() == Dni(self.dni).getLetterDni():
            return True
        else:
            return False
