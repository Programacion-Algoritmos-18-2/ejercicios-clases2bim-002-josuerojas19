from paquete_archivos.miarchivo import MiArchivo
from paquete_modelo.mimodelo import Persona, OperacionesPersona

m = MiArchivo()
lista = m.obtener_informacion()
lista = [l.split("|") for l in lista]


lista = lista[1:]
lista_personas =[]
for d in lista:
    # print(d)
    p = Persona(d[1], d[2], d[3],d[0],d[4], d[5])
    lista_personas.append(p)

operacion = OperacionesPersona(lista_personas)

print(operacion)
print("El promedio de las notas de la materia X es: ", operacion.obtener_promedio("nota1"))
print("El promedio de las notas de la materia Y es: ", operacion.obtener_promedio("nota2"))
print("Estudiantes con notas menores de 15 en la materia X: ", operacion.obtener_notas_menores("nota1"))
print("Estudiantes con notas menores de 15 en la materia Y: ", operacion.obtener_notas_menores("nota2"))
print("Estudiantes menores con Nombre de inicial J: ", operacion.obtener_nombre_letra_inicial("J"))
print("Estudiantes menores con Nombre de inicial R: ", operacion.obtener_nombre_letra_inicial("R"))