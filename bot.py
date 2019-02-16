import time
from PIL import ImageGrab
import pyautogui

# cor_fundo = (247, 247, 247)
# cor_dinossauro = (83, 83, 83)

def capturar_tela():
    tela = ImageGrab.grab()
    return tela


def detectar_cacto(tela):
    for x in range(340, 350):
        for y in range(615, 650):
            cor = tela.getpixel((x, y))
            if cor == (83, 83, 83):
                return True
    return cor

def pular():
    pyautogui.press("up")

print("Inicia em 3 segundos...")
time.sleep(3)

while True:
    tela = capturar_tela()
    if detectar_cacto(tela):
        pular()
