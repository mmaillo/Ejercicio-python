from modelos.alumno import Alumno
from modelos.persona import Persona

import sys

def agregar(numero, bbdd=[]):       
    for i in range(numero):

        nombre = str(input("Introduce un nombre: "))
        apellidos = str(input("Introduce los apellidos: "))
        edad = int(input("Introduce la edad: "))
        asignatura = str(input("Introduce la asignatura: "))

        bbdd.append(Alumno(nombre, apellidos, edad, asignatura))

    return bbdd
            
def mostrar(bbdd):
    for i in bbdd:
        print(i)

def mostrar_adultos(bbdd):
    for i in bbdd:
        #print(persona.mayor_de_edad)
        if  i.mayor_de_edad: 
            print(i)
                
bbdd = [Alumno('Miriam','Maillo',29, 'Inglés'),
        Alumno('Alber','Gomez',26, 'Mate'),
        Alumno('Sonia', 'Perez', 15, 'Lengua'),
        Alumno('Maria', 'Alvarez', 17, 'Física')
       ]
try:
    numero = int(input("Introduce el numero de los alumnos que va a añadir: "))
except ValueError:
    print("Mete valor correcto")
    sys.exit()

bbdd = agregar(numero, bbdd)
mostrar(bbdd)
print("Los mayores de edad son: ")
#mostrar_adultos(bbdd)
    
