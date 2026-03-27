from machine import Pin, I2C
import ssd1306
import time
import random

i2c = I2C(0, scl=Pin(22), sda=Pin(21))

schermo = ssd1306.SSD1306_I2C(128, 64, i2c)
pulsante_sx = Pin(4, Pin.IN, Pin.PULL_UP)
pulsante_bs = Pin(5, Pin.IN, Pin.PULL_UP)
pulsante_al = Pin(23, Pin.IN, Pin.PULL_UP)
pulsante_ds = Pin(18, Pin.IN, Pin.PULL_UP)


altezza_cella = 8
larghezza_cella = 16
colonne = 8
righe = 8

for x in range(colonne): #griglia di gioco 8x8
    for y in range(righe):
        schermo.rect(
            x * larghezza_cella,
            y * altezza_cella,
            larghezza_cella,
            altezza_cella,
            0
        )    
    

schermo.show()
time.sleep(1)

coox = 0
cooy = 0

coox_cibo = 0
cooy_cibo = 0

schermo.fill_rect(
    coox * larghezza_cella,
    cooy * altezza_cella,
    larghezza_cella,
    altezza_cella,
    1
)
schermo.show()

#variabili logica limite mappa e cibo
gioco = True
cibo = True

#lista del corpo iniziale dello snake
snake = [(coox, cooy), (0,0)]

def movimento():
    global gioco, coox, cooy, snake
    gioco = True
    #controllo limiti mura
    if coox < 0 or coox > 7:
        gioco = False
    elif cooy < 0 or cooy > 7:
        gioco = False
    #logica di movimento
    #cancella coda
    coda = snake.pop()
    schermo.fill_rect(
        coda[0] * larghezza_cella,
        coda[1] * altezza_cella,
        larghezza_cella,
        altezza_cella,
        0
    )
    
  
    if pulsante_ds.value() == 0:
        schermo.fill_rect(
            coox * larghezza_cella,
            cooy * altezza_cella,
            larghezza_cella,
            altezza_cella,
            0
        )
        coox += 1
        schermo.fill_rect(
            coox * larghezza_cella,
            cooy * altezza_cella,
            larghezza_cella,
            altezza_cella,
            1
        )
        schermo.show()
        time.sleep(0.2)

    elif pulsante_sx.value() == 0:
        schermo.fill_rect(
            coox * larghezza_cella,
            cooy * altezza_cella,
            larghezza_cella,
            altezza_cella,
            0
        )
        coox -= 1
        schermo.fill_rect(
            coox * larghezza_cella,
            cooy * altezza_cella,
            larghezza_cella,
            altezza_cella,
            1
        )
        schermo.show()
        time.sleep(0.2)
    elif pulsante_al.value() == 0:
        schermo.fill_rect(
            coox * larghezza_cella,
            cooy * altezza_cella,
            larghezza_cella,
            altezza_cella,
            0
        )
        cooy -= 1
        schermo.fill_rect(
            coox * larghezza_cella,
            cooy * altezza_cella,
            larghezza_cella,
            altezza_cella,
            1
        )
        schermo.show()
        time.sleep(0.2)
    elif pulsante_bs.value() == 0:
        schermo.fill_rect(
            coox * larghezza_cella,
            cooy * altezza_cella,
            larghezza_cella,
            altezza_cella,
            0
        )
        cooy += 1
        schermo.fill_rect(
            coox * larghezza_cella,
            cooy * altezza_cella,
            larghezza_cella,
            altezza_cella,
            1
        )
        schermo.show()
        time.sleep(0.2)

def spawn_cibo():
    global cibo, coox_cibo, cooy_cibo
    if cibo == True:
        coox_cibo = random.choice(range(0, 7))
        cooy_cibo = random.choice(range(0, 7))
        schermo.rect(
           coox_cibo * larghezza_cella,
           cooy_cibo * altezza_cella,
           larghezza_cella,
           altezza_cella,
           1
        )
        cibo = False
    return None

def controllo_cibo():
    global cibo, coox_cibo, cooy_cibo
    if coox == coox_cibo and cooy == cooy_cibo:
        cibo = True
    return None

while gioco:
    spawn_cibo()
    movimento()
    controllo_cibo()
    
    

schermo.fill(0)
schermo.text("GAME OVER", 28, 28)
schermo.show()


        
