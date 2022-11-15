import random

IMÁGENES_AHORCADO = ['''
   +---+
   |   |
       |
       |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
       |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''', '''
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========''', '''
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
 =========''','''
   +----+
   |    |
  [O    |
  /|\   |
  / \   |
        |
 ==========''', '''
   +----+
   |    |
  [O]   |
  /|\   |
  / \   |
        |
 ==========''']

palabras = {'Colores':'rojo naranja amarillo verde azul añil violeta blanco negro marron'.split(),
'Formas':'cuadrado triangulo rectangulo circulo elipse rombo trapezoide chevron pentagono hexagono heptagono octogono'.split(),
'Frutas':'manzana naranja limon lima pera sandia uva pomelo cereza banana melon mango fresa tomate'.split(),
'Animales':'murcielago oso castor gato pantera cangrejo ciervo perro burro pato aguila pez rana cabra sanguijuela leon lagarto mono alce raton nutria buho panda piton conejo rata tiburon oveja mofeta calamar tigre pavo tortuga comadreja ballena lobo wombat cebra'.split()}

""" palabras = 'hormiga babuino tejon murcielago oso castor camello gato almeja cobra pantera coyote cuervo ciervo perro burro pato aguila huron zorro rana cabra ganso halcon leon lagarto llama topo mono alce raton mula salamandra nutria buho panda loro paloma piton conejo carnero rata cuervo rinoceronte salmon foca tiburon oveja mofeta perezoso serpiente araña cigüeña cisne tigre sapo trucha pavo tortuga comadreja ballena lobo wombat cebra'.split()"""
# palabras = palabras = 'rojo naranja amarillo verde azul añil violeta blanco negro marron'.split()
# palabras = 'cuadrado triangulo rectangulo circulo elipse rombo trapezoide chevron pentagono hexagono heptagono octogono'.split()
# palabras = 'manzana naranja limon lima pera sandia uva pomelo cereza banana melon mango fresa tomate'.split()


############ FUNCIONES ####################
def obtener_palabra_al_azar(diccionario_de_palabras):
      clave_de_palabras = random.choice(list(diccionario_de_palabras.keys()))
      indice_de_palabra = random.randint(0, len(diccionario_de_palabras[clave_de_palabras]) - 1)
      return [diccionario_de_palabras[clave_de_palabras][indice_de_palabra], clave_de_palabras]
      

def mostrar_tablero(IMÁGENES_AHORCADO, letras_incorrectas, letras_correctas, palabra_secreta):
      print(IMÁGENES_AHORCADO[len(letras_incorrectas)])
      print()

      print('Letras incorrectas:', end=' ')
      for letra in letras_incorrectas:
          print(letra, end=' ')
      print()

      espacios_vacios = '_' * len(palabra_secreta)

      for i in range(len(palabra_secreta)): 
         if palabra_secreta[i] in letras_correctas:
             espacios_vacios = espacios_vacios[:i] + palabra_secreta[i] + espacios_vacios[i+1:]

      for letra in espacios_vacios:
         print(letra, end=' ')
      print()

def obtener_intento(letras_probadas):
      while True:
            print('Adivina una letra:')
            intento = input()
            intento = intento.lower()
            if len(intento) != 1:
                  print('Por favor, introduce una letra.')
            elif intento in letras_probadas:
                  print('Ya has probado esa letra. Elige otra.')
            elif intento not in 'abcdefghijklmnñopqrstuvwxyz':
                  print('Por favor ingresa una LETRA.')
            else:
                  return intento

def jugar_de_nuevo():
     print('¿Quieres jugar de nuevo? (sí o no)')
     return input().lower().startswith('s')


################# PROGRAMA #######################
print('A H O R C A D O')
letras_incorrectas = ''
letras_correctas = ''
palabra_secreta, clave_secreta = obtener_palabra_al_azar(palabras)
juego_terminado = False

while True:
      print(f"La palabra secreta pertenece al conjunto: {clave_secreta}")
      mostrar_tablero(IMÁGENES_AHORCADO, letras_incorrectas, letras_correctas, palabra_secreta)

      intento = obtener_intento(letras_incorrectas + letras_correctas)
      if intento in palabra_secreta:
            letras_correctas += intento

            encontrado_todas_las_letras = True
            for i in range(len(palabra_secreta)):
                  if palabra_secreta[i] not in letras_correctas:
                        encontrado_todas_las_letras = False
                        break
            if encontrado_todas_las_letras:
                  print(f'¡Sí! ¡La palabra secreta es {palabra_secreta}! ¡Has ganado!')
                  juego_terminado = True

      else:
            letras_incorrectas += intento

            if len(letras_incorrectas) == len(IMÁGENES_AHORCADO) - 1:
                  mostrar_tablero(IMÁGENES_AHORCADO, letras_incorrectas, letras_correctas, palabra_secreta)
                  print(f"Te has quedado sin intentos \nDespues de {str(len(letras_incorrectas))} intentos fallidos, y {str(len(letras_correctas))} aciertos, la palabra era {palabra_secreta}")
                  juego_terminado = True
      
      if juego_terminado:
            if jugar_de_nuevo():
                  letras_incorrectas = ""
                  letras_correctas = ""
                  juego_terminado = False
                  palabra_secreta, clave_secreta = obtener_palabra_al_azar(palabras)
            else:
                  break