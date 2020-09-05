from pynput.mouse import Button, Controller
from KeyBoardMap import *
from Commands import *


# Fallguys Commands
def fallguys(msg):
    if msg == "left" or msg == "esquerda" : 
        PressAndHoldKey(A, 2)

    if msg == "right" or msg == "direita": 
        PressAndHoldKey(D, 2)

    if msg == "forward" or msg == "frente": 
        ReleaseKeyPynput(S) 
        PressKeyPynput(W) 
                    
    if msg == "back" or msg == "re": 
        ReleaseKeyPynput(W) 
        PressKeyPynput(S)
    if msg == "stop" or msg== "parar": 
        ReleaseKeyPynput(W)
        ReleaseKeyPynput(S)

    if msg == "jump" or msg == "pular": 
        PressAndHoldKey(SPACE, 1.0)

    if msg == "dive" or msg == "mergulhar": 
        PressAndHoldKey(LEFT_CONTROL, 0.7)
                    
    if msg == "jump grab":
        PressKeyPynput(LEFT_SHIFT)
        PressAndHoldKey(SPACE, 2.5)

    if msg == "grab" or msg == "agarrar" :
        if vef == 0:
            PressKeyPynput(LEFT_SHIFT)
            vef = 1
        elif vef == 1:
            ReleaseKeyPynput(LEFT_SHIFT)

def marioParty(msg):
    print("teste")
