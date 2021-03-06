# coding = UTF-8
import turtle
import random
import math


PHI = 360 / 7
R = 50


def gotoxy(x, y): #перемещение в точку
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def draw_circle(r, color): #отрисовка круга
    turtle.fillcolor(color)
    turtle.begin_fill()
    turtle.circle(r)
    turtle.end_fill()

def draw_pistol(base_x, base_y):
    gotoxy(base_x, base_y)
    turtle.circle(80)
    # основной круг
    gotoxy(base_x, base_y + 160)
    draw_circle(5, 'brown')
    # мушка

    for i in range(0, 7): # тут начинается отрисовка барабана
        phi_rad = PHI * i * math.pi / 180.0
        gotoxy(base_x + math.sin(phi_rad) * R, base_y + math.cos(phi_rad) * R + 60)
        draw_circle(22, 'white')

def rotate_pistol(base_x, base_y, start):
    for i in range(start, random.randrange(7, 15)):
        phi_rad = PHI * i * math.pi / 180.0
        gotoxy(base_x + math.sin(phi_rad) * R, base_y + math.cos(phi_rad) * R + 60)
        draw_circle(22, 'brown')
        draw_circle(22, 'white')

    gotoxy(base_x + math.sin(phi_rad) * R, base_y + math.cos(phi_rad) * R + 60)
    draw_circle(22, 'yellow')

    return i % 7




turtle.speed(0)

draw_pistol(50, 20)

answer = ''
start = 0

while answer != 'n':
    answer = turtle.textinput('Проверим твою удачу?', 'y/n')

    if answer == 'y':
        start = rotate_pistol(50, 20, start)

        if start == 0:
            phi_rad = PHI * 0 * math.pi / 180.0
            gotoxy(50 + math.sin(phi_rad) * R, 20 + math.cos(phi_rad) * R + 60)
            draw_circle(22, 'red')
            gotoxy(-150, 250)
            turtle.write('В твоей голове новая дырка. Прощай неудачник!', font=('Arial', 18, 'normal'))

    else:
        pass
