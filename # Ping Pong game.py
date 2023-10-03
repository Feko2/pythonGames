# Ping Pong game
import pygame
from pygame.locals import *
import random as rd
from pygame import mixer

pygame.init()
mixer.init()

pantalla = pygame.display.set_mode((1000, 750))
pygame.display.set_caption("Ping Pong")


class Paleta():
    def __init__(self, posx, pantalla):
        if posx == 0:  # izquierda
            self.posx = 100
        else:
            self.posx = 850

        self.posy = 400
        self.color = (255, 255, 255)  # blanco
        self.score = 0
        self.vel = 50
        self.figura = pygame.Rect(self.posx, self.posy, 20, 200)
        pygame.draw.rect(pantalla, self.color, self.figura)

    def moverArriba(self):
        self.posy -= self.vel
        self.figura.top = self.posy

    def moverAbajo(self):
        self.posy += self.vel
        self.figura.top = self.posy

    def respawn(self):
        self.posy = 400
        self.figura.top = 400


class Pelota():
    def __init__(self, pantalla):
        self.vel = 10
        self.posx = 500
        self.posy = 500
        self.direccionx = rd.randint(0, 1)
        self.direcciony = rd.randint(0, 1)
        self.color = (255, 255, 255)  # blanco
        self.figura = pygame.Rect(self.posx, self.posy, 20, 20)
        pygame.draw.rect(pantalla, self.color, self.figura)
        self.color1 = 0
        self.color2 = 0
        self.color3 = 0

        if self.direccionx == 0:  # izquierda
            self.dirx = -1
        else:
            self.dirx = 1

        if self.direcciony == 0:  # arriba
            self.diry = -1
        else:
            self.diry = 1

    def colision(self, p1, p2):
        if self.dirx == 1:  # derecha
            self.posx += self.vel
        else:  # izquierda
            self.posx -= self.vel

        if self.diry == 1:  # esta bajando
            self.posy += self.vel
            if self.posy >= 750:
                self.diry = -1
        else:  # esta subiendo
            self.posy -= self.vel
            if self.posy <= 0:
                self.diry = 1

        self.figura.left = self.posx
        self.figura.top = self.posy

        if self.figura.colliderect(p1.figura):
            self.dirx = 1
            self.vel += 0.5

        if self.figura.colliderect(p2.figura):
            self.dirx = -1
            self.vel += 0.5

    def respawn(self):
        self.posx, self.posy = 500, 500
        self.vel = 10

    def fondo(self):
        self.color1 = rd.randint(0, 255)
        self.color2 = rd.randint(0, 255)
        self.color3 = rd.randint(0, 255)


def escribe(string, size, pos):
    fuente = pygame.font.Font(pygame.font.get_default_font(), size)
    texto = fuente.render(string, False, (255, 255, 255))
    textoRect = texto.get_rect()
    textoRect.center = pos
    return texto, textoRect


corriendo = True

p1 = Paleta(0, pantalla)
p2 = Paleta(1, pantalla)
pelota = Pelota(pantalla)
reloj = pygame.time.Clock()

while corriendo:

    for evento in pygame.event.get():
        if evento.type == QUIT:
            corriendo = False
            break
        if (evento.type == KEYDOWN and evento.key == K_ESCAPE):
            corriendo = False
            break

       # if(evento.type == KEYDOWN and evento.key == K_UP):
        # if(evento.type == KEYDOWN and evento.key == K_DOWN):
          #  p2.moverAbajo()
        #if(evento.type == KEYDOWN and evento.key == K_w):
         #   p1.moverArriba()
        #if(evento.type == KEYDOWN and evento.key == K_s):
         #   p1.moverAbajo()


        #teclas = {'K_UP': True, 'K_DOWN': False, 'K_SPACE': False}
    teclas = pygame.key.get_pressed()
    if teclas[K_UP]:
            p2.moverArriba()
    if teclas[K_DOWN]:
            p2.moverAbajo()
    if teclas[K_w]:
            p1.moverArriba()
    if teclas[K_s]:
            p1.moverAbajo()



    pelota.colision(p1, p2)

    if pelota.posx <= 0:
        pelota.respawn()
        p1.respawn()
        p2.respawn()
        p2.score += 1
        print(f"Jugador 1: {p1.score} | Jugador 2: {p2.score}")

    if pelota.posx >= 1000:
        pelota.respawn()
        p1.respawn()
        p2.respawn()
        p1.score += 1
        print(f"Jugador 1: {p1.score} | Jugador 2: {p2.score}")

    pantalla.fill((0, 0, 0))
    pygame.draw.rect(pantalla, p1.color, p1.figura)
    pygame.draw.rect(pantalla, p2.color, p2.figura)
    pygame.draw.rect(pantalla, pelota.color, pelota.figura)
    scores, scoresR = escribe(
        f"P1: {p1.score} | P2: {p2.score}", 50, (500, 150))
    pantalla.blit(scores, scoresR)
    pygame.display.update()
    reloj.tick(30)

pygame.quit()
