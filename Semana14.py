# funcion que calcula el promedio de tres notas
# recibe tres notas como parametros
# retorna el promedio de las notas

def calcular_promedio(n1:float, n2:float, n3:float)->float:
    promedio = (n1 + n2 + n3) / 3
    return promedio


# mensaje inicial del programa
print("----------- Sistema de promedio -----------")

# ingreso de datos por teclado
nota1 = float(input("Ingrese la primera nota: "))
nota2 = float(input("Ingrese la segunda nota: "))
nota3 = float(input("Ingrese la tercera nota: "))

# llamada a la funcion
resultado = calcular_promedio(nota1, nota2, nota3)

# mostrar resultado en pantalla
print("El promedio del estudiante es:", resultado)