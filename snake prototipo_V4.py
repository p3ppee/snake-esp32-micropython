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
pulsante_reset = Pin(12, Pin.IN, Pin.PULL_UP)


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
perso = True

#lista del corpo iniziale dello snake
snake = [(0,0), (0,0)]

#direzione iniziale
direzione = (1,0)

def spostamento(x, y, colore):
    schermo.fill_rect(
        x * larghezza_cella,
        y * altezza_cella,
        larghezza_cella,
        altezza_cella,
        colore
    )

def movimento():
    global direzione ,perso ,new_cox ,new_coy
    
    if pulsante_ds.value() == 0 and direzione != (-1, 0):
        direzione = (1,0)
    elif pulsante_sx.value() == 0 and direzione != (1,0):
        direzione = (-1,0)
    elif pulsante_bs.value() == 0 and direzione != (0,-1):
        direzione = (0,1)
    elif pulsante_al.value() == 0 and direzione != (0,1):
        direzione = (0,-1)
    
    #nuova testa
    new_cox = snake[0][0] + direzione[0]
    new_coy = snake[0][1] + direzione[1]
    #controllo se si colpisce da solo
    if (new_cox, new_coy) in snake:
        perso = False
    snake.insert(0, (new_cox, new_coy))
    
    if new_cox < 0 or new_cox >= colonne or new_coy < 0 or new_coy >= righe:
        perso = False   
    
    
    #rimozione coda
    if cibo == False:
        coda = snake.pop()
        spostamento(coda[0], coda[1], 0)
        
    spostamento(new_cox, new_coy, 1)
    schermo.show()
    
    
    
    
    
def spawn_cibo():
    global cibo, coox_cibo, cooy_cibo
    if cibo == True:
        while True:
            coox_cibo = random.choice(range(0, 7))
            cooy_cibo = random.choice(range(0, 7))
            if (coox_cibo, cooy_cibo) in snake:
                continue
            else:
                schermo.rect(
                   coox_cibo * larghezza_cella,
                   cooy_cibo * altezza_cella,
                   larghezza_cella,
                   altezza_cella,
                   1
                )
                cibo = False
                break
    return None

def controllo_cibo():
    global cibo, coox_cibo, cooy_cibo
    if new_cox == coox_cibo and new_coy == cooy_cibo:
        cibo = True
    return None

while True:
    while gioco:
        movimento()
        spawn_cibo()
        controllo_cibo()
        time.sleep(0.2)
        if perso == False:
            schermo.fill(0)
            schermo.text("GAME OVER", 28, 28)
            schermo.show()
            if pulsante_reset.value() == 0:
                schermo.fill(0)
                schermo.show()
                perso = True
                coox = 0
                cooy = 0
                direzione = (1, 0)
                snake = [(0, 0)]
                cibo = True
                schermo.fill(0)
                for x, y in snake:
                    schermo.fill_rect(
                        x * larghezza_cella,
                        y * altezza_cella,
                        larghezza_cella,
                        altezza_cella,
                        1
                    )
                schermo.show()
                break
            else:
                time.sleep(0.1)
                continue
            time.sleep(1)
            break

    

        
        
        

    



