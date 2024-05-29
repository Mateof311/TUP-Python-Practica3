from datetime import date

class Usuario:
    def __init__(self,user_name,email,password,nombre,apellido):
        self.__user_name = user_name # user_name protegido {readonly}
        self.estado = True
        self.email = email
        self.password = password
        self.nombre = nombre
        self.apellido = apellido
        self.__fecha_alta = date.today()
        self.fecha_baja = 0

    def dar_de_baja(self):
        self.estado = False
        self.fecha_baja = date.today()
        print("\nUsuario dado de baja\n")

    def validar_credenciales(self, user_name, password):
        return (self.__user_name == user_name) and (self.password == password) and (self.estado)
    
    def mostrar_todo(self):
        print("\n")
        print(f"Usuario: {self.__user_name}")
        print(f"PassWord: {self.password}")
        print(f"Estado {self.estado}")
        print(f"Nombre: {self.nombre}")
        print(f"Apellido: {self.apellido}")
        print(f"Fecha de alta: {self.__fecha_alta}")
        print(f"Fecha de baja: {self.fecha_baja}")

# MAIN
user1 = Usuario("user1", "emanueltcamacho@gmail.com", "contraseña123", "Emanuel", "Camacho")

print("\nContraseña correcta:", user1.validar_credenciales("user1", "contraseña123"))  # True
print("Contraseña incorrecta:", user1.validar_credenciales("user1", "contraseña456"))  # False

user1.mostrar_todo()
user1.dar_de_baja()

print("Credenciales del user1:",user1.validar_credenciales("user1", "contraseña123"))  # False

user1.mostrar_todo()

