
class Persona:
    def __init__(self, nombre="", edad=None, dni=None):
        self.nombre = nombre
        self.edad = edad
        self.dni = dni
    
    def set_nombre(self, nombre):
        if type(nombre) != str:
         print("Debe ingresar letras")
        elif (len(nombre) < 3):
            print("El nombre ingresado es demasiado corto")
        self.nombre = nombre
    
    def set_edad(self, edad):
         if type(edad) != int:
                print("Debe ingresar un numero entero")
         elif edad <0 or edad >100:
             print("La edad no es valida.Por favor ingrese edad entre 1 Y 100")
         self.edad = edad
    
    def set_dni(self, dni):
         if type(dni) != int:
           print("Debe ingresar numeros enteros")
           #Intento de evaluar que el DNI tuviera 8 digitos:
         """contador=0 #me dara la cantidad de veces que se realizo la divison (que es la cantidad de digitos del numero ingresado)
       while dni > 0:
           contador+=1
           dni = dni//10 #divide al nuero ingresado hasta dar 0 
           return contador
       if(contador > 8 and contador < 0):
            print("Ingrese numero de 8 digitos")"""
         self.dni = dni
    
    def get_nombre(self):
        return self.nombre
    
    def get_edad(self):
        return self.edad
    
    def get_dni(self):
        return self.dni
    
    def mostrar(self):
        print(f"Nombre: {self.nombre}")
        print(f"Edad: {self.edad}")
        print(f"DNI: {self.dni}")

    def es_mayor_de_edad(self):
        if self.edad >= 18:
           # print("Es mayor de edad")
            return True
        else:
           # print("No es mayor de edad")
            return False


class Cuenta():
    
    titular=Persona()
    cantidad=float

    def __init__(self, titular="", cantidad=None):
        self.titular = titular
        self.cantidad = cantidad
    
    def set_titular(self,titular):
        self.titular=titular  
    
    def set_cantidad(self,cantidad):
        self.cantidad=cantidad 
    
    def get_titutar(self):
        return self.titular
    
    def get_cantidad(self):
        return self.cantidad
    
    def mostrar(self):
        print(f"Titular: {self.titular}")
        print(f"Cantidad: {self.cantidad}")
       
    def ingresar(cantidad):
        if (cantidad > 0 ):
            cantidad=cantidad+cantidad
    
    def retirar(cantidad):
        if (cantidad > 0 ):
            cantidad=cantidad-cantidad

         
class CuentaJoven(Cuenta):
     def __init__(self, titular,cantidad="",bonificacion=""):
        super().__init__(titular,cantidad)
        self.bonificacion = bonificacion

     def set_bonificacion(self,bonificacion,cantidad):
        self.bonificacion= cantidad * (bonificacion/100)
    
     def get_bonificacion(self):
        return self.bonificacion
     
     
     def retirar(cantidad):
        def es_titular_valido ():
         return (Persona().get_edad() < 25 and Persona().es_mayor_de_edad())
        if es_titular_valido == True:
         cantidad -= cantidad 
         print("No puedes retirar dineo. Titular no válido")
         
     def mostrar(self):
          super().mostrar()
          print (f"Bonificacion: {self.bonificacion}")
          print(f"El valor con aumento es {self.cantidad + self.bonificacion}")
        
persona1=Persona()
persona1.nombre= "Jose"
persona1.set_edad(1)
cuenta1=CuentaJoven(Cuenta)
cuenta1.set_titular(persona1.nombre)
cuenta1.set_cantidad(20000)
cuenta1.set_bonificacion(10,250)
cuenta1.mostrar()
cuenta1.get_bonificacion()
     


