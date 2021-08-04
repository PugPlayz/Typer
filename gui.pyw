import tkinter as tk
from threading import *
import time
from pynput.keyboard import Key, Controller
keyboard = Controller()

window = tk.Tk()
window.title("Typer")
check = 0

frame1 = tk.Frame(window, width=300, height=400)

label = tk.Label(text="Text2Type")
text = tk.Text(
    width=60,
    height=8,
    )
 
def Timer(text,butText):
    while True:
        global check
        if check == 1:
            check = 0 
            data = text.get('1.0','end-1c')
            i = 6
            while i != 0:
                    i = i - 1
                    butText.set(i)
                    time.sleep(1)
            try:  
                keyboard.type(data)
                butText.set('Write')
            except:
                return('closed')
        else:
            time.sleep(0.3)


def checkSW():
    global check
    check = 1
    print(check)

        
butText = tk.StringVar()
butText.set('Write')
 
button = tk.Button(
    textvariable=butText,
    width=10,
    height=3,
    command=lambda:checkSW(),
)

CC = tk.StringVar()
CC.set(0)
CharCount = tk.Label(textvariable = CC)
label2 = tk.Label(text="Characters")


def Char(text, CC):
    while True:
        try:
            data = text.get("1.0",'end-1c')
            data = len(data)
            CC.set(data)
            time.sleep(0.1)
        except:
            return("exited")

            

def threading():
    t1=Thread(target=Char, args=(text,CC))
    t1._keep_alive = True
    t1.start()
    t2=Thread(target=Timer, args=(text,butText))
    t2.start()       

    

label.pack(pady=8)
text.pack(padx=8)
button.pack(pady=8)
CharCount.pack(side="left")
label2.pack(side="left")


threading()
window.resizable(False, False) 
window.mainloop()



