import random

def setup():
    size(600,600)
    frameRate(60)
    
class Serpiente:
    
    x = 300
    y = 300
    velocidad = 30
    tamano = 30
    arreglo = [[300,300],[330,300],[360,300],[390,300],[420,300]]
    arreglo_inicial = [[300,300],[330,300]]
    direccion = "izquierda"
    
    def dibujar(s):
        for cuadro in s.arreglo:
            square(cuadro[0],cuadro[1],s.tamano)
            
    def actualizar_cola(s):
        for i in range(len(s.arreglo)-1,0,-1):
            copia = s.arreglo[i-1][:]
            s.arreglo[i][0] = copia[0]
            s.arreglo[i][1] = copia[1]
            
class Comida:
    
    x = 0
    y = 0
    
    def dibujar(s):
        square(s.x,s.y,30)
    
serpiente = Serpiente()
def keyPressed():

    if key == 'w' and serpiente.direccion != "abajo":
        serpiente.direccion = "arriba"
    elif key == 'a' and serpiente.direccion != "derecha":
        serpiente.direccion = "izquierda"
    elif key == 'd' and serpiente.direccion != "izquierda":
        serpiente.direccion = "derecha"
    elif key == 's' and serpiente.direccion != "arriba":
        serpiente.direccion = "abajo"
ultima_dibujada = 1000000
tiempo_de_espera = 500
modo = "jugar"
comida = Comida()
comida.x = ((random.randint(0,600)) // 30) * 30
comida.y = ((random.randint(0,600)) // 30) * 30
def draw():
    global ultima_dibujada,tiempo_de_espera,modo
    background(0)
    if modo == "jugar":
        serpiente.dibujar()
        comida.dibujar()
        if abs(ultima_dibujada - millis()) > tiempo_de_espera:
            if serpiente.direccion == "izquierda":
                serpiente.actualizar_cola()
                serpiente.arreglo[0][0] -= serpiente.velocidad
            elif serpiente.direccion == "derecha":
                serpiente.actualizar_cola()
                serpiente.arreglo[0][0] += serpiente.velocidad
            elif serpiente.direccion == "abajo":
                serpiente.actualizar_cola()
                serpiente.arreglo[0][1] += serpiente.velocidad
            elif serpiente.direccion == "arriba":
                serpiente.actualizar_cola()
                serpiente.arreglo[0][1] -= serpiente.velocidad
            for i in range(len(serpiente.arreglo)):
                if i == 0:
                    continue
                x = serpiente.arreglo[0][0]
                y = serpiente.arreglo[0][1]
                if x ==  serpiente.arreglo[i][0] and y == serpiente.arreglo[i][1]:
                    modo = "perdiste"
                    serpiente.arreglo = serpiente.arreglo_inicial
                    break
            ultima_dibujada = millis()
        if serpiente.arreglo[0][0] == comida.x and serpiente.arreglo[0][1] == comida.y:
            while True:
                x = ((random.randint(0,600)) // 30) * 30
                y = ((random.randint(0,600)) // 30) * 30
                igualdad = 0
                for cuadrado in serpiente.arreglo:
                    if x == cuadrado[0] and y == cuadrado[1]:
                        igualdad += 1
                if igualdad == 0:
                    comida.x = x
                    comida.y = y
                    break
            
    elif modo == "perdiste":
        text("perdiste",200,200)
