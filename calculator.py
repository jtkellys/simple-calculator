from tkinter import *

root = Tk()
root.title("Simple Calculator")

number_input = Entry(root, width=35, borderwidth=5)
number_input.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

values = []


def button_click(number):
    current = number_input.get()
    number_input.delete(0, END)
    number_input.insert(0, str(current) + str(number))


def button_clear():
    number_input.delete(0, END)
    values.clear()
    return values


def button_addition(add):
    x = number_input.get()
    values.append(int(x))
    number_input.delete(0, END)
    global math
    math = "addition"
    return values


def button_sub(sub):
    x = number_input.get()
    values.append(int(x))
    number_input.delete(0, END)
    global math
    math = "subtraction"
    return values


def button_multi(multi):
    x = number_input.get()
    values.append(int(x))
    number_input.delete(0, END)
    global math
    math = "multiplication"
    return values


def button_div(div):
    x = number_input.get()
    values.append(int(x))
    number_input.delete(0, END)
    global math
    math = "division"
    return values


def button_equal(equals):
    x = number_input.get()
    values.append(int(x))
    number_input.delete(0, END)
    if math == "addition":
        equals = str(values[0] + values[1])
        number_input.insert(0, equals)
    elif math == "subtraction":
        equals = str(values[0] - values[1])
        number_input.insert(0, equals)
    elif math == "multiplication":
        equals = str(values[0] * values[1])
        number_input.insert(0, equals)
    elif math == "division":
        equals = str(values[0] / values[1])
        number_input.insert(0, equals)
    else:
        return


# Define Buttons

button_1 = Button(root, text="1", pady=20, padx=40, command=lambda: button_click(1))
button_2 = Button(root, text="2", pady=20, padx=40, command=lambda: button_click(2))
button_3 = Button(root, text="3", pady=20, padx=40, command=lambda: button_click(3))
button_4 = Button(root, text="4", pady=20, padx=40, command=lambda: button_click(4))
button_5 = Button(root, text="5", pady=20, padx=40, command=lambda: button_click(5))
button_6 = Button(root, text="6", pady=20, padx=40, command=lambda: button_click(6))
button_7 = Button(root, text="7", pady=20, padx=40, command=lambda: button_click(7))
button_8 = Button(root, text="8", pady=20, padx=40, command=lambda: button_click(8))
button_9 = Button(root, text="9", pady=20, padx=40, command=lambda: button_click(9))
button_0 = Button(root, text="0", pady=20, padx=40, command=lambda: button_click(0))
button_add = Button(root, text="+", pady=20, padx=36, command=lambda: button_addition("+"))
button_subtract = Button(root, text="-", pady=20, padx=39, command=lambda: button_sub("-"))
button_multiply = Button(root, text="*", pady=20, padx=39, command=lambda: button_multi("*"))
button_divide = Button(root, text="/", pady=20, padx=39, command=lambda: button_div("/"))
button_equals = Button(root, text="=", pady=20, padx=190, command=lambda: button_equal("="))
button_clear = Button(root, text="Clear", pady=20, padx=79, command=button_clear)

# Place buttons on screen

button_1.grid(row=3, column=0)
button_2.grid(row=3, column=1)
button_3.grid(row=3, column=2)
button_add.grid(row=3, column=3)

button_4.grid(row=2, column=0)
button_5.grid(row=2, column=1)
button_6.grid(row=2, column=2)
button_subtract.grid(row=2, column=3)

button_7.grid(row=1, column=0)
button_8.grid(row=1, column=1)
button_9.grid(row=1, column=2)
button_multiply.grid(row=1, column=3)

button_0.grid(row=4, column=0)
button_divide.grid(row=4, column=3)
button_clear.grid(row=4, column=1, columnspan=2)

button_equals.grid(row=5, column=0, columnspan=4)

root.mainloop()
