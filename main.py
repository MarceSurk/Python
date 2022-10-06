"""texto = "Hola Mundo"
numero1 = 2
numero2 = 2
if numero1 > numero1:
    print("el numero",numero1,"es mayor")
elif numero1==numero2:
    print("Son iguales")
else:
    print("el numero",numero2,"es mayor")
print("fin")

for numero in range(10,0,-1):
    print(numero)
primerArray = [1,2,3,4,5,6]
print(len(primerArray))
for numero in primerArray:
    print(numero)"""
#Hacer un bucle que me diga los numeros > 50 que haya en un Array
"""segundoArray = [22132,23,456,2,135,7]

for numero in segundoArray:
    if numero > 50:
        print(numero)
    else:
        count = count+1
        print(count)
alumnos = ["Luis Angel", "Ignacio", "Lloel"]
#Añadir elementos
alumnos.append("Daniel")
#Borrar dato del Array
alumnos.remove("Daniel")
#Borrar una posicion del Array
alumnos.pop()
for alumno in alumnos:
    print(alumno)

diccionario = {
    "nombre":"Luis Angel",
    "ocupacion": "Trabajar"
}
#Editar un valor del diccionario
diccionario["ocupacion"] = "Administrar"
#Añadir un valor al diccionario
diccionario["Edad"] = 32
#Eliminar un calor del diccionario
diccionario.pop("nombre")
print(diccionario)"""

alumnos =  [
    {
        "nombre":"Guille",
        "edad":18
    },
    {
        "nombre":"Sergio",
        "edad": 20
    }
]
for alumno in alumnos:
    print("la edad de",alumno["nombre"],"es:",alumno["edad"],"años")