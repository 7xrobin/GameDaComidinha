from Tkinter import *
import mtTkinter as Tkinter
import time
from random import randint
from array import *
from threading import *

# Parametros
N_PRODUTORES = 7
N_CONSUMIDORES = 5
MAX_ITENS = 10
PRODUCAO_POR_PRODUTOR = 3*MAX_ITENS

# Variaveis auxiliares
inicio = 0
final = 0
prateleira = [None] * MAX_ITENS
count = 0


# Semaforos
estrada = Semaphore(value=1)
vazio = Semaphore(value=0)
cheio = Semaphore(value=MAX_ITENS)

def log_produtor(x):
        global count
        global final
        global prateleira
        move_producers_to_table(N_PRODUTORES-1,count)
        count = count+1
        final = (final + 1) % MAX_ITENS
        prateleira[final] = x

def log_consumidor(x):
        global count
        global inicio
        global prateleira
        inicio = (inicio + 1) % MAX_ITENS
        move_consumers_to_table(N_CONSUMIDORES-1,count)
        count = count-1

def produtor():
        for x in range(0, PRODUCAO_POR_PRODUTOR): 
                cheio.acquire()
                estrada.acquire()
                log_produtor(x)
                estrada.release()
                vazio.release()
                time.sleep(2)

def consumidor():
        for x in range (0, (PRODUCAO_POR_PRODUTOR*N_PRODUTORES/N_CONSUMIDORES)):
                vazio.acquire()
                cheio.release()
                estrada.acquire()
                log_consumidor(x)
                estrada.release()
                time.sleep(2)

def move_right(char,times):
        global canvas
	for k in range(0,times):
		canvas.move(char, "20", "0")
		canvas.update()
		time.sleep(0.05)

def move_left(char,times):
	for k in range(0,times):
		canvas.move(char, "-20", "0")
		canvas.update()
		time.sleep(0.05)

def move_up(char,times):
	for k in range(0,times):
		canvas.move(char, "0", "-25")
		canvas.update()
		time.sleep(0.05)

def move_down(char,times):
	for k in range(0,times):
		canvas.move(char, "0", "25")
		canvas.update()
		time.sleep(0.05)

def move_producers_to_table(t,platecount):
	i = randint(0,t)

	move_right(produtores[i],22)

	coords1 = canvas.coords(produtores[i])
	produtores[i] = canvas.delete(produtores[i])
	produtores[i] = canvas.create_image(coords1, image = back)
	move_up(produtores[i],(2*i)+5)
	prato = canvas.create_image(490,50-(3*platecount),image = plate)
	pratos.append(prato)
	time.sleep(1)

	coords1 = canvas.coords(produtores[i])
	produtores[i] = canvas.delete(produtores[i])
	produtores[i] = canvas.create_image(coords1, image = front)
	move_down(produtores[i],(2*i)+5)

	coords1 = canvas.coords(produtores[i])
	produtores[i] = canvas.delete(produtores[i])
	produtores[i] = canvas.create_image(coords1, image = left)
	move_left(produtores[i],22)

	coords1 = canvas.coords(produtores[i])
	produtores[i] = canvas.delete(produtores[i])
	produtores[i] = canvas.create_image(coords1, image = right)

def move_consumers_to_table(t,platecount):
	i = randint(0,t)

	move_left(consumidores[i],22)

	coords1 = canvas.coords(consumidores[i])
	consumidores[i] = canvas.delete(consumidores[i])
	consumidores[i] = canvas.create_image(coords1, image = back)
	move_up(consumidores[i],(2*i)+5)
	pratos[platecount-1] = canvas.delete(pratos[platecount-1])
	pratos.pop()
	time.sleep(1)

	coords1 = canvas.coords(consumidores[i])
	consumidores[i] = canvas.delete(consumidores[i])
	consumidores[i] = canvas.create_image(coords1, image = front)
	move_down(consumidores[i],(2*i)+5)

	coords1 = canvas.coords(consumidores[i])
	consumidores[i] = canvas.delete(consumidores[i])
	consumidores[i] = canvas.create_image(coords1, image = right)
	move_right(consumidores[i],22)

	coords1 = canvas.coords(consumidores[i])
	consumidores[i] = canvas.delete(consumidores[i])
	consumidores[i] = canvas.create_image(coords1, image = left)


root = Tkinter.Tk()
root.geometry("976x642")

canvas = Canvas(root, width=976, height=642)
canvas.pack()

right = PhotoImage(file = 'right.gif')
front = PhotoImage(file = 'front.gif')
back = PhotoImage(file = 'back.gif')
left = PhotoImage(file = 'left.gif')
plate = PhotoImage(file = 'plate.gif')
bg = PhotoImage(file = 'Mapa.gif')


background = canvas.create_image(0, 0, image = bg, anchor="nw")

produtores = []
consumidores = []
pratos = []

# cria personagens
for x in range(0,N_PRODUTORES):
	char = canvas.create_image(50, 200+50*x, image = right)
	produtores.append(char)

for x in range(0,N_CONSUMIDORES):
	char = canvas.create_image(926, 200+50*x, image = left)
	consumidores.append(char)

# inicia threads
Produtor = list()
Consumidor = list()

for x in range(0, N_PRODUTORES):
        Produtor.append(Thread(target=produtor))
        Produtor[x].start()

for x in range(0, N_CONSUMIDORES):
        Consumidor.append(Thread(target=consumidor))
        Consumidor[x].start()

#Text View
text_id= canvas.create_text(10, 10, anchor="nw")
canvas.itemconfig(text_id, text="Hello tkinter girl")
canvas.insert(text_id, 12, "new")

root.mainloop()

for x in Produtor:
        x.join()
for x in Consumidor:
        x.join()
