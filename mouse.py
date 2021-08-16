"""Controls the mouse and simulate it

Functions:
    getPosition : Return current position of the mouse
    getX : Return current X position of mouse
    getY : Return current Y position of mouse
    setPosition : Set current position of the mouse
    setX : Set current X position of the mouse
    setY : Set current Y position of the mouse
    move : moves mouse relative to current position
    fclick : Click a mouse button
    click : Click and hold a mouse button
    release : Release all mouse buttons current pressed
        
"""

# imports
from pynput.mouse import Button, Controller as MCon
import time

# setup
mouse = MCon()
buttonlist = {
    'unknown':Button.unknown,
    'left':Button.left,
    'middle':Button.middle,
    'right':Button.right
    }

# pre-defs
lst = []

# def functions
def _buttonp(K): # convert some keys to equivalent
    global buttonlist
    K = str(K)
    try:
        return buttonlist[K.lower()]
    except KeyError:
        return K

### main functions ###
def getPosition():
    """Return current position of the mouse

    Returns:
        (tuple): the X and Y current position of mouse
    """
    return mouse.position

def getX():
    """Return current X position of mouse

    Returns:
        (integer): the X position of the mouse
    """
    return mouse.position[0]
    
def getY():
    """Return current Y position of mouse

    Returns:
        (integer): the Y position of the mouse
    """
    return mouse.position[1]

def setPosition(pos):
    """Set current position of the mouse

    Args:
        pos (tuple): the X and Y position of mouse
    """
    time.sleep(0.05)
    mouse.position = pos

def setX(X):
    """Set current X position of the mouse

    Args:
        X (integer): the X position of mouse
    """
    time.sleep(0.05)
    pos = (X, mouse.position[1])
    mouse.position = pos

def setY(Y):
    """Set current Y position of the mouse

    Args:
        Y (integer): the Y position of mouse
    """
    time.sleep(0.05)
    pos = (mouse.position[0], Y)
    mouse.position = pos
    
def move(desl):
    """moves mouse relative to current position

    Args:
        desl (tuple): the X and Y translation
    """
    time.sleep(0.05)
    mouse.move(desl[0], desl[1])

def scroll(sy, sx=0):
    """Scrolls the mouse

    Args:
        sy (integer): Scrolls pixels Vertically
        sx (integer, optional): Scrolls pixels Horizontally. Defaults to 0.
    """
    mouse.scroll(sx, sy)

def fclick(K):
    """Click a mouse button

    Args:
        K (enum): the button to be clicked
            - left: left mouse button
            - right: right mouse button
            - middle: middle mouse button
            - unknown: other mouse buttons
    """
    time.sleep(0.05)
    mouse.click(_buttonp(K))
    time.sleep(0.05)
    mouse.release(_buttonp(K))

def click(K):
    """Click and hold a mouse button

    Args:
        K (enum): the button to be clicked
            - left: left mouse button
            - right: right mouse button
            - middle: middle mouse button
            - unknown: other mouse buttons
    """
    global lst
    time.sleep(0.05)
    lst.append(_buttonp(K))
    mouse.press(_buttonp(K))

def release():
    """Release all mouse buttons current pressed
    """
    global lst
    for i in lst:
        mouse.release(i)
    lst = []