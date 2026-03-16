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

for x in range(4): #griglia di gioco 8x8
    for y in range(4):
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
coox_vecchio = 0
cooy_vecchio = 0
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

def movimento():
    global gioco, coox, cooy, coox_vecchio, cooy_vecchio
    gioco = True
    if coox < 0 or coox > 7:
        gioco = False
    elif cooy < 0 or cooy > 7:
        gioco = False
    if pulsante_ds.value() == 0:
        coox_vecchio = coox
        schermo.fill_rect(
            coox_vecchio * larghezza_cella,
            cooy * altezza_cella,
            larghezza_cella,
            altezza_cella,
            0
        )
        schermo.fill_rect(
            coox * larghezza_cella,
            cooy * altezza_cella,
            larghezza_cella,
            altezza_cella,
            1
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
        coox_vecchio = coox
        schermo.fill_rect(
            coox_vecchio * larghezza_cella,
            cooy * altezza_cella,
            larghezza_cella,
            altezza_cella,
            0
        )
        schermo.fill_rect(
            coox * larghezza_cella,
            cooy * altezza_cella,
            larghezza_cella,
            altezza_cella,
            1
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
        cooy_vecchio = cooy
        schermo.fill_rect(
            coox * larghezza_cella,
            cooy_vecchio * altezza_cella,
            larghezza_cella,
            altezza_cella,
            0
        )
        schermo.fill_rect(
            coox * larghezza_cella,
            cooy * altezza_cella,
            larghezza_cella,
            altezza_cella,
            1
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
        cooy_vecchio = cooy
        schermo.fill_rect(
            coox * larghezza_cella,
            cooy_vecchio * altezza_cella,
            larghezza_cella,
            altezza_cella,
            0
        )
        schermo.fill_rect(
            coox * larghezza_cella,
            cooy * altezza_cella,
            larghezza_cella,
            altezza_cella,
            1
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

cibo_counter = 1

def spawn_cibo():
    global cibo, coox_cibo, cooy_cibo, cibo_counter
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
        cibo_counter = 1
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
    
        
