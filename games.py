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
    if msg == "left" or msg == "esquerda": 
        PressAndHoldKey(J, 1)
    if msg == "right" or msg == "direita": 
        PressAndHoldKey(L, 1)
    if msg == "down" or msg == "re": 
        PressAndHoldKey(K, 1)
    if msg == "up" or msg == "frente": 
        PressAndHoldKey(I, 1)
    if msg == "a": 
        PressAndHoldKey(NUMPAD_9, 0.5)
    if msg == "b": 
        PressAndHoldKey(NUMPAD_8, 0.5)
    if msg == "x": 
        PressAndHoldKey(NUMPAD_7, 0.5)
    if msg == "y":
        PressAndHoldKey(NUMPAD_6, 0.5)
    if msg == "z": 
        PressAndHoldKey(NUMPAD_5, 0.5)
    if msg == "l": 
        PressAndHoldKey(NUMPAD_4, 0.5)
    if msg == "r": 
        PressAndHoldKey(NUMPAD_3, 0.5)

