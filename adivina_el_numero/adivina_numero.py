import random
import sys

#################################

def pedir_int():
    dato = input()
    while True:
        try:
            dato = int(dato)
            return dato
        except ValueError:
            print("Ingrese un numero")
            dato = input()


#################################

print("¡Hola! ¿Cómo te llamas?")
nombre = input()

random_number = random.randint(1, 20)
print(f"Bueno {nombre}, estoy pensando un numero entre el 1 y 20")

intentos = 0
print("Intenta adivinar")
eleccion = pedir_int()

while intentos < 6:
    if eleccion < random_number:
        print("Tu estimacion es muy baja")
        intentos += 1
        eleccion = pedir_int()
    elif eleccion > random_number:
        print("Tu estimacion es muy alta")
        intentos += 1
        eleccion = pedir_int()
    else:
        print(f"Buen trabajo {nombre}, has adivinado mi numero en {intentos} intentos")
        sys.exit()


print(f"No lo conseguiste. El numero que estaba pensando era {random_number}. Mejor suerte la proxima")


