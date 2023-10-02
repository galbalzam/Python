import tkinter as tk
from tkinter import Text
from tkinter import ttk
from tkinter import messagebox

#   global variables
res = 0
firstValue = 0
secondValue = 0
mode = 0
firstValueFilled = False


def convertToInt():
    return int(text.get('1.0', 'end'))


#   functions
def number1():
    checkZero()
    text.insert('1.end', '1')


def number2():
    checkZero()
    text.insert('1.end', '2')


def number3():
    checkZero()
    text.insert('1.end', '3')


def number4():
    checkZero()
    text.insert('1.end', '4')


def number5():
    checkZero()
    text.insert('1.end', '5')


def number6():
    checkZero()
    text.insert('1.end', '6')


def number7():
    checkZero()
    text.insert('1.end', '7')


def number8():
    checkZero()
    text.insert('1.end', '8')


def number9():
    checkZero()
    text.insert('1.end', '9')


def number0():
    checkZero()
    text.insert('1.end', '0')


def plus():
    global firstValue, mode, firstValueFilled
    mode = 1
    firstValue = convertToInt()
    clear()
    print("first Value: ", firstValue)
    firstValueFilled = True


def minus():
    global firstValue, mode, firstValueFilled
    mode = 2
    firstValue = convertToInt()
    clear()
    firstValueFilled = True


def mul():
    global firstValue, mode, firstValueFilled
    mode = 3
    firstValue = convertToInt()
    clear()
    firstValueFilled = True


def divide():
    global firstValue, mode, firstValueFilled
    mode = 4
    firstValue = convertToInt()
    clear()
    print("firstValue mode 4:", firstValue)
    firstValueFilled = True


def equal():
    global secondValue, firstValue, res
    print("firstValueFilled: ", firstValueFilled)
    if firstValueFilled == False:
        firstValue = convertToInt()
    else:
        secondValue = convertToInt()
    clearAll()
    print("second Value: ", secondValue)
    print("first Value: ", firstValue)
    print("Mode: ", mode)

    if mode == 1:
        res = firstValue + secondValue
    elif mode == 2:
        res = firstValue - secondValue
    elif mode == 3:
        res = firstValue * secondValue
    else:
        if secondValue == 0 and firstValueFilled == False:
            secondValue = 1
        try:
            print("***")
            res = firstValue // secondValue
        except:
            # Message
            messagebox.showerror("Error", "Invalid calculation try again")
            reset()
    print("res", res)
    text.insert('1.0', str(res))


def clear():
    # For C button
    text.delete('1.0', 'end')
    text.insert('1.end', '0')


def clearAll():
    text.delete('1.0', 'end')


def checkZero():
    #   get first char value
    #   if first chat value = 0 return true else return false
    num = text.get('1.0', 'end')
    if int(num) == 0:
        clearAll()


def reset():
    # For AC Button
    global res, firstValue, secondValue, mode
    clear()
    res = 0
    firstValue = 0
    secondValue = 0
    mode = 0


root = tk.Tk()

#   root configuration
root.title('Calculator')

width = 280
height = 280
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
#   find the center point
plus_x = int(screen_width / 2 - width / 2)
plus_y = int(screen_height / 2 - height / 2)
root.geometry(f'{width}x{height}+{plus_x}+{plus_y}')
root.resizable(0,0)

#   start here
text = Text(root, height=4)
# number0()
text.insert('1.end', '0')
text.pack()

ttk.Button(root, command=number1, text="1").place(x=10, y=75)
ttk.Button(root, command=number2, text="2").place(x=100, y=75)
ttk.Button(root, command=number3, text="3").place(x=190, y=75)
ttk.Button(root, command=number4, text="4").place(x=10, y=100)
ttk.Button(root, command=number5, text="5").place(x=100, y=100)
ttk.Button(root, command=number6, text="6").place(x=190, y=100)
ttk.Button(root, command=number7, text="7").place(x=10, y=125)
ttk.Button(root, command=number8, text="8").place(x=100, y=125)
ttk.Button(root, command=number9, text="9").place(x=190, y=125)
ttk.Button(root, command=number0, text="0").place(x=10, y=150)
ttk.Button(root, command=plus, text="+").place(x=100, y=150)
ttk.Button(root, command=minus, text="-").place(x=190, y=150)
ttk.Button(root, command=mul, text="*").place(x=10, y=175)
ttk.Button(root, command=divide, text="/").place(x=100, y=175)
ttk.Button(root, command=equal, text="=").place(x=190, y=175)
ttk.Button(root, command=clear, text="C").place(x=10, y=200)
ttk.Button(root, command=reset, text="AC").place(x=100, y=200)

root.mainloop()
