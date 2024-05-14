from datetime import date

#practica ejercicio 1
#USUARIO
class Usuario:
    user_name=(str)
    estado=(bool)
    email=(str)
    password=(str)
    nombre=(str)
    apellido=(str)
    fecha_alta=(date)
    fecha_baja=(date)

    #Al dar de alta un usuario se asigna en fecha_alta la fecha del día y estado True
    def __init__(self,):
        self.estado=True
        self.fecha_alta=date.today()

    #Al validar las credenciales, se retorna verdadero si el usuario y pass ingresado coincide con el
    #user_name y password del usuario; en caso contrario se retorna False
    def validar_credenciales(self,usuario,contra):
        valido= False
        if(usuario==self.user_name and contra==self.password):
            valido=True
        return valido
    #Al dar de baja el usuario, el mismo no se elimina, si no que su estado cambia a False y se le
    #asigna en fecha_baja la fecha del día.
    def baja_usuario(self):
        self.estado=False
        self.fecha_baja=date.today()
