import math

t = "%(nombre)s sabe %(idiomas)i idiomas"

v = [{'nombre':'miriam', 'idiomas':5},
     {'nombre':'maria', 'idiomas':3}]

def sustituye (nombre, idiomas):
    print nombre + "sabe" + int(idiomas) + "idiomas"
    for persona in v:
	    sustituye(persona['nombre'], persona['idiomas'])


	