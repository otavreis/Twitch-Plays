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
        PressAndHoldKey(G, 1)
    if msg == "right" or msg == "direita": 
        PressAndHoldKey(H, 1)
    if msg == "down" or msg == "re": 
        PressAndHoldKey(F, 1)
    if msg == "up" or msg == "frente": 
        PressAndHoldKey(T, 1)
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

def legoGames(msg):
    if msg == "left" or msg == "esquerda": 
        PressAndHoldKey(A, 1)
    if msg == "right" or msg == "direita": 
        PressAndHoldKey(D, 1)
    if msg == "down": 
        PressAndHoldKey(S, 1)
    if msg == "up": 
        PressAndHoldKey(W, 1)
    if msg == "soco": 
        PressAndHoldKey(H, 0.5)
        PressAndHoldKey(H, 0.5)
        PressAndHoldKey(H, 0.5)
    if msg == "magia":
        PressKeyPynput(J)
    if msg == "solta magia" or msg == "solta":
        ReleaseKeyPynput(J)
    if msg == "troca" or msg == "trocar": 
        PressAndHoldKey(K, 0.5)
    if msg == "pular": 
        PressAndHoldKey(U, 0.5)
    if msg == "pular frente": 
        PressKeyPynput(W)
        PressAndHoldKey(U, 0.5)
        ReleaseKeyPynput(W)
    if msg == "trocar magia": 
        PressAndHoldKey(C, 0.5)

def mineirinho(msg):
    if msg == "pare":
        ReleaseKeyPynput(UP_ARROW)
    if msg == "esq":
        PressAndHoldKey(LEFT_ARROW, 2)
    if msg == "dir":
        PressAndHoldKey(RIGHT_ARROW, 2)
    if msg == "frente":
        PressKeyPynput(UP_ARROW)
    if msg == "re":
        PressAndHoldKey(DOWN_ARROW, 1)
    if msg == "z":
        PressAndHoldKey(Z, 1)
    if msg == "x":
        PressAndHoldKey(X,1)

def gta(msg):
    if msg == "esquerda": 
        PressAndHoldKey(LEFT_ARROW, 2)
    if msg == "esq": 
        PressAndHoldKey(LEFT_ARROW, 0.5)

                # If the chat message is "right", then hold down the D key for 2 seconds
    if msg == "direita": 
        PressAndHoldKey(RIGHT_ARROW, 2)
    if msg == "dir": 
        PressAndHoldKey(RIGHT_ARROW, 0.5)

                # If message is "drive", then permanently hold down the W key
    if msg == "acelerar": 
        ReleaseKeyPynput(DOWN_ARROW) #release brake key first
        PressKeyPynput(UP_ARROW) #start permanently driving

                # If message is "reverse", then permanently hold down the S key
    if msg == "re": 
        ReleaseKeyPynput(UP_ARROW) #release drive key first
        PressKeyPynput(DOWN_ARROW) #start permanently reversing

                # Release both the "drive" and "reverse" keys
    if msg == "parar": 
        ReleaseKeyPynput(UP_ARROW)
        ReleaseKeyPynput(DOWN_ARROW)

    if msg == "freiar": 
        PressAndHoldKey(SPACE, 0.7)
    # if msg == "shoot": 
    #     mouse.press(Button.left)
    #     time.sleep(1)
    #     mouse.release(Button.left)

def braw(msg):
    if msg == "esquerda": 
        PressAndHoldKey(A, 2)
    if msg == "esq": 
        PressAndHoldKey(A, 0.5)
    if msg == "jump": 
        PressAndHoldKey(W, 0.5)
                # If the chat message is "right", then hold down the D key for 2 seconds
    if msg == "direita": 
        PressAndHoldKey(D, 2)
    if msg == "dir": 
        PressAndHoldKey(D, 0.5)

    if msg == "pular dir": 
        PressKeyPynput(D)
        PressAndHoldKey(W, 0.5)
        ReleaseKeyPynput(D)
    if msg == "pular esq": 
        PressKeyPynput(A)
        PressAndHoldKey(W, 0.5)
        ReleaseKeyPynput(A)

    if msg == "atq 1":
        PressKeyPynput(W)
        PressAndHoldKey(X, 0.5)
        ReleaseKeyPynput(W)
    if msg == "atq 2":
        PressKeyPynput(S)
        PressAndHoldKey(X, 0.5)
        ReleaseKeyPynput(S)
    if msg == "atq 3":
        PressKeyPynput(A)
        PressAndHoldKey(X, 0.5)
        ReleaseKeyPynput(A)
    if msg == "atq 4":
        PressKeyPynput(D)
        PressAndHoldKey(X, 0.5)
        ReleaseKeyPynput(D)
                # If message is "drive", then permanently hold down the W key

    if msg == "z": 
        PressAndHoldKey(Z, 0.5)

                # If message is "reverse", then permanently hold down the S key
    if msg == "x": 
        PressAndHoldKey(X, 0.5)
                # Release both the "drive" and "reverse" keys
    if msg == "c": 
        PressAndHoldKey(C, 0.5)
    if msg == "v": 
        PressAndHoldKey(V, 0.5)
    # if msg == "shoot": 
    #     mouse.press(Button.left)
    #     time.sleep(1)
    #     mouse.release(Button.left)

def tetris(msg):
    if msg == "dir" or msg == "d": 
        PressAndHoldKey(D, 0.3)
    if msg == "esq" or msg == "a": 
        PressAndHoldKey(A, 0.3)
    if msg == "w" or msg == "acelerar" or msg == "g":
        PressAndHoldKey(W, 0.3)
    if msg == "s":
        ReleaseKeyPynput(W)
    if msg == "acelerar": 
        PressKeyPynput(W) #start permanently driving
