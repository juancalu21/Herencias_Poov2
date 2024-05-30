
class Persona:
    
    def __init__(self,documento,nombreCompleto) :
        
        self.__documento = documento
        self.__nombreCompleto = nombreCompleto
        
        
    def get_documento(self):
        return self.__documento
    
    def set_documento(self, value):
        self.__documento = value    
    
    def get_nombreCompleto(self):
        return self.__nombreCompleto
    
    def set_nombreCompleto(self, value):
        self.__nombreCompleto = value 
        
    def informacion():
        persona1 = Persona("","")
        documento = int(input("Ingrese el documento"))
        persona1.set_documento(documento)
        
        nombre = int(input("Ingrese el Nombre completo"))
        persona1.set_nombreCompleto(nombre)
        

class Aprendiz(Persona):
    
    def __init__(self, documento, nombreCompleto, ficha, programa):
        super().__init__(documento, nombreCompleto)
        self.__ficha = ficha
        self.__programa = programa
    
    def get_ficha(self):
        return self.__ficha
    
    def set_ficha(self, value):
        self.__ficha = value        
    
    def get_programa(self):
        return self.__programa
    
    def set_programa(self, value):
        self.__programa = value    
    
    
class EtapaLectiva(Aprendiz):
    
    def __init__(self, documento, nombreCompleto, ficha, programa, numeroTrimestre, fechaInicio, fechaTerminacion):
        super().__init__(documento, nombreCompleto, ficha, programa)
        self.__numeroTrimestre = numeroTrimestre
        self.__fechaInicio = fechaInicio
        self.__fechaTerminacion = fechaTerminacion
    
    def get_numeroTrimestre(self):
        return self.__numeroTrimestre
    
    def set_numeroTrimestre(self, value):
        self.__numeroTrimestre = value  
    
    def get_fechaInicio(self):
        return self.__fechaInicio
    
    def set_fechaInicio(self, value):
        self.__fechaInicio = value  
    
    def get_fechaTerminacion(self):
        return self.__fechaTerminacion
    
    def set_fechaTerminacion(self, value):
        self.__fechaTerminacion = value  
    
    def informacion():
        
        LectivaInfo = EtapaLectiva(0,"",0,"","","","")
        
        documento = int(input("Ingrese el documento: "))
        LectivaInfo.set_documento(documento)
        
        nombre = str(input("Ingrese el Nombre completo: "))
        LectivaInfo.set_nombreCompleto(nombre)
        
        ficha = int(input("Ingrese el ficha completo: "))
        LectivaInfo.set_ficha(ficha)        

        programa = str(input("Ingrese el programa: "))
        LectivaInfo.set_programa(programa)

        numeroTrimestre = str(input("Ingrese el numero del Trimestre: "))
        LectivaInfo.set_numeroTrimestre(numeroTrimestre)

        fechaInicio = str(input("Ingrese la fecha de inicio de la etapa lectiva: "))
        LectivaInfo.set_fechaInicio(fechaInicio)

        fechaTerminacion = str(input("Ingrese la fecha de finalizacion de la etapa lectiva: "))
        LectivaInfo.set_fechaTerminacion(fechaTerminacion)

Persona.informacion()
EtapaLectiva.informacion()