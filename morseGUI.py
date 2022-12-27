
import RPi.GPIO as GPIO, time
import tkinter as tk

window = tk.Tk()
window.title("Morse Code")



LED = 5
unit = .2


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED, GPIO.OUT)

def close():
    GPIO.output(LED, False)
    window.destroy()

# blinks a dot
def dot():
    GPIO.output(LED, True)
    time.sleep(unit)
    GPIO.output(LED, False)
    time.sleep(unit)

# blinks a dash
def dash():
    GPIO.output(LED, True)
    time.sleep(unit*3)
    GPIO.output(LED, False)
    time.sleep(unit)

    
def newChar():
    time.sleep(unit*3)
    
MORSE_CODE_DICT = { 'A':'.-', 'B':'-...','C':'-.-.', 'D':'-..', 'E':'.','F':'..-.', 'G':'--.', 'H':'....','I':'..', 'J':'.---', 'K':'-.-','L':'.-..', 'M':'--', 'N':'-.','O':'---', 'P':'.--.', 'Q':'--.-','R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..','1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.','0':'-----', ', ':'--..--', '.':'.-.-.-','?':'..--..', '/':'-..-.', '-':'-....-','(':'-.--.', ')':'-.--.-'}


def encrypt():
    message = textEntry.get()
    morse_code = ''
    if len(message)>12:
        print("entered string has more than 12 elements kindly try again")
        return
    # this for loop will keep on scanning the letters and converting it into the morse code
    for i in message:
            #this code will look up the dictionary and add the corresponding value.
            morse_code += MORSE_CODE_DICT[i.upper()] + ' '

    for i in morse_code:
        if i == '.':
            dot()
        elif i == '-':
            dash()
        elif i==' ':
            newChar()

            

textEntry = tk.Entry(window)
textEntry.grid(row = 0, column = 1)
convertButton = tk.Button(window, text="Convert", command=encrypt, bg= 'green', height=1, width= 24)
convertButton.grid(row=3, column=1)
Exit = tk.Button(window, text = 'Exit', command = close, bg = 'red', height= 1, width = 24)
Exit.grid(row=5, column = 1)


window.mainloop()
