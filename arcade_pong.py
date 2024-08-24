import turtle

# Ventana de juego
screen = turtle.Screen()
screen.title("Arcade Pong") 
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.tracer(0) # Para que no parpadee la pantalla

# Jugadores
player_one = turtle.Turtle() #Para crear un objeto Turtle
player_one.speed(0) 
player_one.shape("square")
player_one.color("white")
player_one.penup() #Esto evita que dibuje una linea recta al desplazar la pala
player_one.goto(-350, 0)
player_one.shapesize(stretch_wid=5, stretch_len=1)

player_two = turtle.Turtle()
player_two.speed(0)
player_two.shape("square")
player_two.color("white")
player_two.penup()
player_two.goto(350,0)
player_two.shapesize(stretch_wid=5, stretch_len=1)


# Pelota
pelota = turtle.Turtle()
pelota.speed(0)
pelota.shape("square")
pelota.color("white")
pelota.penup()
pelota.goto(0, 0)
pelota.dx = 0.05 #Se mueve cada 0.9 pixeles
pelota.dy = 0.05

# Mover las palas

def playerone_up():
    '''jugador uno arriba'''
    y = player_one.ycor()
    y += 20
    player_one.sety(y)

def playerone_down():
    '''jugador uno abajo'''
    y = player_one.ycor()
    y -= 20
    player_one.sety(y)

def playertwo_up():
    ''' jugador dos arriba'''
    y = player_two.ycor()
    y += 20
    player_two.sety(y)

def playertwo_down():
    '''jugador dos abajo'''
    y = player_two.ycor()
    y -= 20
    player_two.sety(y)

#Asignacion teclas
screen.listen()
screen.onkeypress(playerone_up, "w")
screen.onkeypress(playerone_down, "s")
screen.onkeypress(playertwo_up, "Up") # Con la mayuscula hacemos referencia a la flecha arriba del teclado
screen.onkeypress(playertwo_down, "Down") 


while True: # Bucle principal para que el programa funcione
    screen.update() # Esto hace que se vaya actualizando la pantalla y la tengamos abierta

    pelota.setx(pelota.xcor() + pelota.dx)
    pelota.sety(pelota.ycor() + pelota.dy)

    # Bordes
    if pelota.ycor() > 290: # Cuando llega al borde de la pantalla por arriba, cambia la direccion
        pelota.dy *= -1
    if pelota.ycor() < -290: # Cuando llega al borde por abajo, cambia la direccion
        pelota.dy *= -1

    # Porterias
    if pelota.xcor() > 390: # Si revasa por el lado derecho vuelve al centro
        pelota.goto(0,0)
        pelota.dx *= -1 # Invierte su direccion
    if pelota.xcor() < -390: # Si revasa por el lado izquierdo, vuelve al centro
        pelota.goto(0,0)
        pelota.dx *= -1 # Cambia la direccion

    if ((pelota.xcor() > 340 and pelota.xcor() < 350)
        and (pelota.ycor() < player_two.ycor() + 50
        and pelota.ycor() > player_two.ycor()-50))