from datetime import date

class Usuario:
    def __init__(self,user_name,email,password,nombre,apellido):      
        self.__user_name = user_name
        self.__email = email
        self.__password = password
        self.__nombre = nombre
        self.__apellido = apellido
        self.__estado = True
        self.__fecha_alta = date.today()
        self.__fecha_baja = 0

    def __str__(self):
        return 'Usuario: {}, email: {}, Password: {}, Nombre: {}, Apellido {} , Estado {}, Fecha_Alta {}'.format(self.__user_name,self.__email,self.__password,self.__nombre,self.__apellido,self.__estado, self.fecha_alta)

    @property
    def user_name(self):
        return self.__user_name

    @property
    def nombre(self):
        return self.__nombre
    
    @nombre.setter
    def nombre(self, nuevo_nombre):
        print("Modificando nombre...")
        self.__nombre = nuevo_nombre
        print("El nuevo nombre es")
        print(self.__nombre)

    @property
    def apellido(self):
        return self.__apellido
    @apellido.setter
    def apellido(self, nuevo_apellido):
        print("Modificando apellido..")
        self.__apellido = nuevo_apellido
        print("El nuevo apellido es")
        print(self.__apellido)
    
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self,nuevo_password):
        print("Modificando Password")
        self.__password = nuevo_password
        print("Se a modificado la contraseña")
        print(replace = self.__password)

    @property
    def estado(self):
        return self.__estado
    @estado.setter
    def estado(self, nuevo_estado):
        print("El estado se esta modificando")
        self.__estado = nuevo_estado
        print("El estado se cambio a: ")
        print(self.__estado)
    
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, nuevo_email):
        print("Modificando Email ")
        self.__email = nuevo_email
        print("El email nuevo es: ")
        print(self.__email)
   
    @property
    def fecha_alta(self):
        return self.__fecha_alta
    @fecha_alta.setter
    def fecha_alta(self, nueva_fecha_alta):
        print("Modificando la fecha alta: ")
        self.__fecha_alta = nueva_fecha_alta
        
        print("La nueva fecha de alta es: ")
        print(self.__fecha_alta)
    
    @property
    def fecha_baja(self):
        return self.__fecha_baja
    
    @fecha_baja.setter
    def fecha_baja(self, nueva_fecha_baja):
        print("Modificando Fecha de baja.")
        self.__fecha_baja = nueva_fecha_baja
        print("La fecha de baja se modifica a : ")
        print(self.__fecha_baja)
    
    def validar_credenciales(self,usuario:str,contraseña:str)-> bool:
        if usuario == self.user_name and contraseña == self.password:
            return("Usuario logueado correctamente")
        else :
            return("Usuario o Contraseña Incorrectas")
    
   
    def baja_usuario(self)->None:
        self.estado = False
        self.fecha_baja = date.today()


# user_name,email,password,nombre,apellido

usuario1 = Usuario("Jorgitosuarez", "jorgeluis@hotmail.com", "jorgitogamer","Jose", "Luis" )
#print(usuario1)

#print(usuario1.validar_credenciales("Jorgitosuarez","Jorgitogamer"))

#print(usuario1.user_name)
#usuario1.user_name = "LOLA"
#print(usuario1.user_name)

print(usuario1.estado, usuario1.fecha_alta, usuario1.fecha_baja)
usuario1.baja_usuario()
print(usuario1.estado, usuario1.fecha_alta, usuario1.fecha_baja)

