# Tarea FP: Reserva de un asiento en sala de cine

# Matriz de la sala 3x4
asientos = [
    [0, 0, 0, 0],
    [0, 0, 0, 0],
    [0, 0, 0, 0]
]

# Pedir fila y columna al usuario
print("--- Reserva de Asientos ---")
f = int(input("Ingrese fila (0 a 2): "))
c = int(input("Ingrese columna (0 a 3): "))

# Reservar asiento (cambiar 0 por 1)
asientos[f][c] = 1

# Mostrar la sala como una tabla
print("\nEstado de la sala:")
for numerofila in range(len(asientos)):
    for numerocolumna in range(len(asientos[numerofila])):
        print(asientos[numerofila][numerocolumna], end=" ")
    print("") # Salto de línea
    # Fin del programa

