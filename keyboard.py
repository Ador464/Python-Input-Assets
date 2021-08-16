"""Controls the keyboard and simulate it

Functions:
    release : Release all pressed modificator keys 
    fpress : Press and release a button fastly
    mpress : Press and wait for release of a control key
    mrelease : Release the modificator key pressed by mpress
    type : Type the text received
    mod : Press or release a control key
    combine : Press a key with the modifier
    copy : Copy the selection and return it as a string
    paste : Paste the data on the cursor
    setClipboard : Set the clipboard content
    getClipboard : Get the clipboard content
     
"""

# imports
from pynput.keyboard import Key, Controller as KCon
import pyperclip
import time

# setup
keyboard = KCon()
keyboard.release(Key.ctrl)
keyboard.release(Key.shift)
keyboard.release(Key.alt)
keyboard.release(Key.cmd)

# pre-defs
_mprs = ''
_ctrl = False
_shift = False
_alt = False
_cmd = False
keylist = {
        'backspace':Key.backspace,
        'caps_lock':Key.caps_lock,
        'delete':Key.delete,
        'down':Key.down,
        'end':Key.end,
        'enter':Key.enter,
        'esc':Key.esc,
        'f1':Key.f1,
        'f2':Key.f2,
        'f3':Key.f3,
        'f4':Key.f4,
        'f5':Key.f5,
        'f6':Key.f6,
        'f7':Key.f7,
        'f8':Key.f8,
        'f9':Key.f9,
        'f10':Key.f10,
        'f11':Key.f11,
        'f12':Key.f12,
        'f13':Key.f13,
        'f14':Key.f14,
        'f15':Key.f15,
        'f16':Key.f16,
        'f17':Key.f17,
        'f18':Key.f18,
        'f19':Key.f19,
        'f20':Key.f20,
        'home':Key.home,
        'left':Key.left,
        'page_down':Key.page_down,
        'page_up':Key.page_up,
        'right':Key.right,
        'space':Key.space,
        'tab':Key.tab,
        'up':Key.up,
        'media_play_pause':Key.media_play_pause,
        'media_volume_mute':Key.media_volume_mute,
        'media_volume_down':Key.media_volume_down,
        'media_volume_up':Key.media_volume_up,
        'media_previous':Key.media_previous,
        'media_next':Key.media_next,
        'insert': Key.insert,
        'menu': Key.menu,
        'num_lock': Key.num_lock,
        'pause': Key.pause,
        'print_screen': Key.print_screen,
        'scroll_lock': Key.scroll_lock,
        'cmd': Key.cmd,
        'cmd_l': Key.cmd_l,
        'cmd_r': Key.cmd_r,
        'shift': Key.shift,
        'shift_l': Key.shift_l,
        'shift_r': Key.shift_r,
        'ctrl': Key.ctrl,
        'ctrl_l': Key.ctrl_l,
        'ctrl_r': Key.ctrl_r,
        'alt': Key.alt,
        'alt_l': Key.alt_l,
        'alt_r': Key.alt_r,
        'alt_gr': Key.alt_gr,
    }


### main functions ###
def _keyp(K): # convert some keys to equivalent
    global keylist
    K = str(K)
    try:
        return keylist[K.lower()]
    except KeyError:
        return K

def release():
    """Release all pressed modificator keys 
    """
    time.sleep(0.05)
    keyboard.release(Key.ctrl)
    keyboard.release(Key.shift)
    keyboard.release(Key.alt)
    keyboard.release(Key.cmd)

def fpress(K):
    """Press and release a button fastly

    Args:
        K (string): the key to be pressed
    """
    K = str(K)
    time.sleep(0.05)
    keyboard.press(_keyp(K))
    release()

def mpress(K):
    """Press and wait for release of a control key

    Args:
        K (string): the key to be pressed

    Raises:
        Exception: invalid Key
        Exception: another mpress was not released
    """
    global _mprs
    global _ctrl
    global _shift
    global _alt
    global _cmd
    K = str(K)
    if _mprs == '':
        if K.lower(K) == 'ctrl':
            time.sleep(0.05)
            _mprs = Key.ctrl
            keyboard.press(_mprs)
        elif K.lower(K) == 'shift':
            time.sleep(0.05)
            _mprs = Key.shift
            keyboard.press(_mprs)
        elif K.lower(K) == 'alt':
            time.sleep(0.05)
            _mprs = Key.alt
            keyboard.press(_mprs)
        elif K.lower(K) == 'cmd':
            time.sleep(0.05)
            _mprs = Key.cmd
            keyboard.press(_mprs)
        else:
            raise Exception(K + ' is not a valid modification key')
    else:
        raise Exception('another mpress was not released')

def mrelease():
    """Release the modificator key pressed by mpress
    """
    global _mprs
    time.sleep(0.05)
    keyboard.release(_mprs)
    _mprs = ''

def type(TXT):
    """Type the text received

    Args:
        TXT (string): the text to be writed
    """
    time.sleep(0.05)
    keyboard.type(TXT)
    time.sleep(len(TXT) * 0.05)

def mod(K):
    """Press or release a control key

    Args:
        K (enum): a modificator key as a string
            - see the 'keylist' variable description for more

    Raises:
        Exception: not valid key
    """
    global _mprs
    global _ctrl
    global _shift
    global _alt
    global _cmd
    K = str(K)
    if K.lower() == 'ctrl':
        if _ctrl:
            time.sleep(0.05)
            keyboard.release(Key.ctrl)
            _ctrl = False
        else:
            time.sleep(0.05)
            keyboard.press(Key.ctrl)
            _ctrl = True
    elif K.lower() == 'shift':
        if _shift:
            time.sleep(0.05)
            keyboard.release(Key.shift)
            _shift = False
        else:
            time.sleep(0.05)
            keyboard.press(Key.shift)
            _shift = True
    elif K.lower() == 'alt':
        if _alt:
            time.sleep(0.05)
            keyboard.release(Key.alt)
            _alt = False
        else:
            time.sleep(0.05)
            keyboard.press(Key.alt)
            _alt = True
    elif K.lower() == 'cmd':
        if _cmd:
            time.sleep(0.05)
            keyboard.release(Key.cmd)
            _cmd = False
        else:
            time.sleep(0.05)
            keyboard.press(Key.cmd)
            _cmd = True
    else:
        raise Exception(K + ' is not a valid modification key')

def combine(M, K):
    """Press a key with the modifier

    Args:
        M (enum): a modificator key as a string
            - see the 'keylist' variable description for more
        K (string): 
    """
    time.sleep(0.05)
    mod(M)
    fpress(K)
    mod(M)

def copy():
    """Copy the selection and return it as a string

    Returns:
        [type]: [description]
    """
    time.sleep(0.1)
    keyboard.press(Key.ctrl)
    keyboard.press('c')
    keyboard.release(Key.ctrl)
    time.sleep(0.1)
    return pyperclip.paste()

def paste(txt = ''):
    """Paste the data on the cursor

    Args:
        txt (string, optional): the text to be pasted on cursor. Defaults to clipboard.
    """
    if not(txt == ''):
        pyperclip.copy(txt)
    keyboard.press(Key.ctrl)
    keyboard.press('v')
    keyboard.release(Key.ctrl)

def setClipboard(txt):
    """Set the clipboard content

    Args:
        txt (string): the new content of clipboard
    """
    pyperclip.copy(txt)

def getClipboard(txt):
    """Get the clipboard content

    Args:
        txt (string): the current clipboard content

    Returns:
        (string): the current clipboard content
    """
    return pyperclip.paste()

if __name__ == '__main__':
    print(
        'fpress'
    )
