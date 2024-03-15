from tkinter import *
from random import randint
from math import sqrt
from time import sleep

HEIGHT = 600
WIDTH = 800

window = Tk()
window.title('Space guardians')
panza = Canvas(window, width=WIDTH, height=HEIGHT, bg='gray')
my_image = PhotoImage(file='background.png')
panza.create_image(0, 0, anchor=NW, image=my_image)
panza.pack()

nava = panza.create_polygon(25, 0, 35, 0, 60, 40, 0,
                            40, fill="Gold", outline="DarkMagenta")
nava2 = panza.create_polygon(
    25, 0, 35, 0, 60, 40, 0, 40, fill="blue", outline="DarkMagenta")
poz_y = HEIGHT - 120
poz_x = WIDTH / 2 - 50
panza.move(nava, poz_x, poz_y)
poz_y2 = HEIGHT - 120
poz_x2 = WIDTH / 2 + 50
panza.move(nava2, poz_x2, poz_y2)

PAS_MISCARE_PIXELI = 25


def nava_move(press):
    if press.keysym == 'Left':
        panza.move(nava, -PAS_MISCARE_PIXELI, 0)
    elif press.keysym == 'Right':
        panza.move(nava, PAS_MISCARE_PIXELI, 0)
    elif press.keysym == 'Up':
        make_shoot()
    elif press.keysym == 'w':
        make_shoot_2()
    elif press.keysym == 'a':
        panza.move(nava2, -PAS_MISCARE_PIXELI, 0)
    elif press.keysym == 'd':
        panza.move(nava2, PAS_MISCARE_PIXELI, 0)


panza.bind_all('<Key>', nava_move)

nava_inamica_nr = list()
nava_inamica_vit = list()


def nave_inamice():
    y = 0
    x = randint(30, WIDTH - 30)
    vit = 1
    nr1 = panza.create_oval(x-20, y-20, x+20, y+20,
                            fill='red', outline='black')
    nava_inamica_nr.append(nr1)
    nava_inamica_vit.append(vit)


def move_nave_inamice():
    for i in range(len(nava_inamica_nr)):
        panza.move(nava_inamica_nr[i], 0, nava_inamica_vit[i])


shoot_nr = list()
shoot_nr2 = list()
shoot_vit = 8


def make_shoot():
    if(len(shoot_nr) < 5):
        pos = panza.coords(nava)
        x = pos[0]
        y = pos[1]
        nr1 = panza.create_oval(
            x-6, y-6, x+6, y+6, fill='yellow', outline='blue')
        shoot_nr.append(nr1)


def make_shoot_2():
    if (len(shoot_nr2) < 5):
        pos = panza.coords(nava2)
        x = pos[0]
        y = pos[1]
        nr1 = panza.create_oval(
            x-6, y-6, x+6, y+6, fill='blue', outline='blue')
        shoot_nr2.append(nr1)


def del_shoot(i):
    panza.delete(shoot_nr[i])
    del shoot_nr[i]


def del_shoot_2(i):
    panza.delete(shoot_nr2[i])
    del shoot_nr2[i]


def clean_shoot():
    for i in range(len(shoot_nr) - 1, -1, -1):
        x, y = coords_shoot(shoot_nr[i])
        if (y < 0):
            del_shoot(i)
    for i in range(len(shoot_nr2) - 1, -1, -1):
        x, y = coords_shoot(shoot_nr2[i])
        if (y < 0):
            del_shoot_2(i)


def coords_nava_inamica(nr_id):
    pos = panza.coords(nr_id)
    x = (pos[0] + pos[2])/2
    y = (pos[1] + pos[3])/3
    return x, y


def move_shoot():
    for i in range(len(shoot_nr)):
        panza.move(shoot_nr[i], 0, -shoot_vit)
    for i in range(len(shoot_nr2)):
        panza.move(shoot_nr2[i], 0, -shoot_vit)


def coords_shoot(nr_id):
    pos = panza.coords(nr_id)
    x = (pos[0] + pos[2])/2
    y = (pos[1] + pos[3])/2
    return x, y


def del_nava_inamica(i):
    panza.delete(nava_inamica_nr[i])
    del nava_inamica_nr[i]


def clean_nava_inamica():
    for i in range(len(nava_inamica_nr)-1, -1, -1):
        x, y = coords_nava_inamica(nava_inamica_nr[i])
        if y > HEIGHT:
            del_nava_inamica(i)


def distance(nr1, nr2):
    x1, y1 = coords_nava_inamica(nr1)
    x2, y2 = coords_shoot(nr2)
    return sqrt((x2 - x1)**2 + (y2 - y1)**2)


def bumm():
    if len(nava_inamica_nr) == 0:
        return
    for i in range(len(nava_inamica_nr) - 1, -1, -1):
        for n in range(len(shoot_nr)-1, -1, -1):
            if distance(nava_inamica_nr[i], shoot_nr[n]) < 26:
                del_nava_inamica(i)
                del_shoot(n)
    if len(nava_inamica_nr) == 0:
        return
    for i in range(len(nava_inamica_nr) - 1, -1, -1):
        for n in range(len(shoot_nr2)-1, -1, -1):
            if distance(nava_inamica_nr[i], shoot_nr2[n]) < 26:
                del_nava_inamica(i)
                del_shoot_2(n)


while True:
    if (randint(1, 200) == 1):
        nave_inamice()
    move_nave_inamice()
    move_shoot()
    clean_shoot()
    clean_nava_inamica()
    bumm()
    window.update()
    sleep(0.002)

mainloop()
