x=[]
datos=[10,20,30,40,50,60]
for dato in datos:
    print(dato)


alumnos=[]
for i in range(0,5):
        nombre=input("Introduce el nombre:")
        alumnos.append(nombre)
        print(alumnos)

#20/10/2026
# Litzy Danari Hernández Arguelles
cantidad=0
while cantidad ==0:
    x=int(input("cantidad de materias:"))
    if x < 0 or x > 8:
        print("introduce un numero entre 1 y 7")
    else:
        print("la cantidad es correcta")
        cantidad =x 

materias=[]
calificaciones=[]
for i in range(0,5):
    materia=input("introduce el nombre de la materia:")
    materias.append(materia)
    calificacion=int(input("introduce la calificacion:"))
    calificaciones.append(calificacion)
    print(materias)
    print(calificaciones)
    kardex=list(zip(materias , calificaciones))
    print(kardex)
