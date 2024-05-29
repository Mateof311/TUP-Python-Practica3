class Clase:
   atributo_clase = "Hola"   # Accesible desde el exterior
   __atributo_clase = "Hola" # No accesible

   def __mi_metodo(self): # No accesible desde el exterior
       print("Haz algo")
       self.__variable = 0

   def metodo_normal(self): # Accesible desde el exterior
       self.__mi_metodo()

mi_clase = Clase()
mi_clase.__atributo_clase #AttributeError (atributo no accesible)
# mi_clase.__mi_metodo()    #AttributeError (método no accesible)
# print(mi_clase.atributo_clase)
# mi_clase.metodo_normal()
