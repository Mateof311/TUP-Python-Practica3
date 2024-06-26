
class Materia:
    def __init__(self, nombre, profesor, fecha):
        self.nombre = nombre
        self.profesor = profesor
        #Fecha no puede ser anterior a 2006
        self.fecha_inicio = fecha

    @property
    def fecha_inicio(self):
        #print("Estoy obteniendo la fecha de inicio")
        return self._fecha_inicio
        #self._ lo vuelve un atributo privado

    @fecha_inicio.setter
    #dando permiso para que guarde un nuevo valor en el atributo fecha_inicio
    def fecha_inicio(self, fecha):
        # print("Estoy seteando la fecha de inicio")
        if fecha < 2006:
            self._fecha_inicio = 2006
        else:
            self._fecha_inicio = fecha

class Carrera:
    def __init__(self, nombre):
        self.nombre = nombre
        #Contendrá tuplas (código, materia)
        self.materias = {} 
    # Este método agrega materias a la 
    # colección de materias
    def agregar_materia(self, materia, codigo):
        self.materias[codigo] = materia

#Creamos una carrera y tres materias
carrera1 = Carrera("Ingeniería en Sistemas")
algebra = Materia("Algebra", "Juan Quinteros", 2004)
fisica = Materia("Física", "Pedro Perez", 2012)  
programacion = Materia("Programación", "Lorena Ríos",2022)

#Agregamos las materias a la carrera:
carrera1.agregar_materia(201,algebra)
carrera1.agregar_materia(202,fisica)
carrera1.agregar_materia(203,programacion)

# Veomos la fecha de inicio de dictado de algunas materias:
print(f"La fecha de inicio de {algebra.nombre} es {algebra.fecha_inicio}")
print(f"La fecha de inicio de {fisica.nombre} es {fisica.fecha_inicio}")
print(f"La fecha de inicio de {programacion.nombre} es {programacion.fecha_inicio}")

