from tkinter import *
expression = ""

# Function getting buttons pressed
def press(num):
	global expression
	expression = expression + str(num)
	equation.set(expression)

# Function equal button
def EqualButton():
	try:
		global expression
		total = str(eval(expression))
		equation.set(total)
		expression = ""
	except:
		equation.set(" error ")
		expression = ""

# Function cm to inch button
def CmToInchButton():
    global expression
    total = int(expression)/2.54
    equation.set(total)

# Function inch to cm button
def InchToCmButton():
    global expression
    total = int(expression)*2.54
    equation.set(total)

#Function clear button
def ClearButton():
	global expression
	expression = ""
	equation.set(" 0")

# Main code

gui = Tk()
gui.configure(background="light blue")
gui.title("Calculator")
gui.geometry("400x350")
equation = StringVar()
ExpressionInput = Entry(gui, textvariable=equation, background="gold", font="15")
ExpressionInput.grid(columnspan=4, ipadx=50, ipady=10)
equation.set(' 0')

#OffButton = Button(gui, text=' Off ', fg='black', bg='salmon', command=exit, height=2, width=7)
#OffButton.grid(row=0, column=4, padx=10, pady=10)

DotButton = Button(gui, text=' dot ', fg='black', bg='salmon', command=lambda: press('.'), height=2, width=7)
DotButton.grid(row=0, column=4, padx=10, pady=10)

button1 = Button(gui, text=' 1 ', fg='black', bg='tan', command=lambda: press(1), height=2, width=7)
button1.grid(row=2, column=0, padx=10, pady=10)

button2 = Button(gui, text=' 2 ', fg='black', bg='tan', command=lambda: press(2), height=2, width=7)
button2.grid(row=2, column=1, padx=10, pady=10)

button3 = Button(gui, text=' 3 ', fg='black', bg='tan', command=lambda: press(3), height=2, width=7)
button3.grid(row=2, column=2, padx=10, pady=10)

plus = Button(gui, text=' + ', fg='black', bg='lightgrey', command=lambda: press("+"), height=2, width=7)
plus.grid(row=2, column=3, padx=10, pady=10)

minus = Button(gui, text=' - ', fg='black', bg='lightgrey', command=lambda: press("-"), height=2, width=7)
minus.grid(row=2, column=4, padx=10, pady=10)

button4 = Button(gui, text=' 4 ', fg='black', bg='tan', command=lambda: press(4), height=2, width=7)
button4.grid(row=3, column=0, padx=10, pady=10)

button5 = Button(gui, text=' 5 ', fg='black', bg='tan', command=lambda: press(5), height=2, width=7)
button5.grid(row=3, column=1, padx=10, pady=10)

button6 = Button(gui, text=' 6 ', fg='black', bg='tan', command=lambda: press(6), height=2, width=7)
button6.grid(row=3, column=2, padx=10, pady=10)

multiply = Button(gui, text=' * ', fg='black', bg='lightgrey', command=lambda: press("*"), height=2, width=7)
multiply.grid(row=3, column=3, padx=10, pady=10)

divide = Button(gui, text=' \u00F7 ', fg='black', bg='lightgrey', command=lambda: press("/"), height=2, width=7)
divide.grid(row=3, column=4, padx=10, pady=10)

button7 = Button(gui, text=' 7 ', fg='black', bg='tan', command=lambda: press(7), height=2, width=7)
button7.grid(row=4, column=0, padx=10, pady=10)

button8 = Button(gui, text=' 8 ', fg='black', bg='tan', command=lambda: press(8), height=2, width=7)
button8.grid(row=4, column=1, padx=10, pady=10)

button9 = Button(gui, text=' 9 ', fg='black', bg='tan', command=lambda: press(9), height=2, width=7)
button9.grid(row=4, column=2, padx=10, pady=10)

button0 = Button(gui, text=' 0 ', fg='black', bg='tan', command=lambda: press(0), height=2, width=7)
button0.grid(row=4, column=3, padx=10, pady=10)

equal = Button(gui, text=' = ', fg='black', bg='lightgreen', command=EqualButton, height=2, width=7)
equal.grid(row=4, column=4, padx=10, pady=10)

CmToInchButton = Button(gui, text='cm to inch', fg='black', bg='aqua', command=CmToInchButton  , height=2, width=17)
CmToInchButton.grid(row=5, column='0', columnspan=2, padx=10, pady=10)

ClearButton = Button(gui, text='Clear', fg='black', bg='pink', command=ClearButton, height=2, width=7)
ClearButton.grid(row=5, column='2', padx=10, pady=10)

InchToCmButton = Button(gui, text='inch to cm', fg='black', bg='aqua', command=InchToCmButton, height=2, width=17)
InchToCmButton.grid(row=5, column='3', columnspan=2, padx=10, pady=10)

# start the GUI
gui.mainloop()