from tkinter import *
import math

expression = "" #global variable expression

def press(num):
    #function to update expression in the text entry box
    global expression
    expression=expression+str(num)
    disp_eq.set(expression)

def equals():
    try:
        global expression
        if 'π' in expression:
            i=expression.index('π')
            expression=expression[:i]+'math.pi'+expression[i+1:]
        if 'e' in expression:
            i=expression.index('e')
            expression=expression[:i]+'math.e'+expression[i+1:]
        if 'sin' in expression:
            i=expression.index('sin')
            expression=expression[:i]+'math.sin'+expression[i+3:]
        if 'cos' in expression:
            i=expression.index('cos')
            expression=expression[:i]+'math.cos'+expression[i+3:]
        if '√' in expression:
            i=expression.index('√')
            expression=expression[:i]+'math.sqrt'+expression[i+1:]
        if 'tan' in expression:
            i=expression.index('√')
            expression=expression[:i]+'math.tan'+expression[i+1:]
        total=str(eval(expression))
        disp_eq.set(total)
        expression=total
    except:
        disp_eq.set("error")
        expression=""

def clear():
    global expression
    expression=""
    disp_eq.set("")

def clear_last():
    global expression
    expression=expression[:-1]
    disp_eq.set(expression)

def negate():
    global expression
    if expression[0]=='-':
        expression=expression[1:]
    else:
        expression='-'+expression
    disp_eq.set(expression)

if __name__ == "__main__":
    #GUI WINDOW
    gui=Tk()
    gui.configure(background="white")
    gui.title("Calculator")
    gui.geometry("250x210")
    disp_eq=StringVar()
    expression_field=Entry(gui, textvariable=disp_eq)
    expression_field.grid(columnspan=10, ipadx=70)
    disp_eq.set("0")

    #NUMBERS
    button1=Button(gui, text='1', fg='black', bg='azure3', command=lambda: press(1), height=1, width=7)
    button1.grid(row=3, column=0)
    button2 = Button(gui, text='2', fg='black', bg='azure3', command=lambda: press(2), height=1, width=7)
    button2.grid(row=3, column=1)
    button3 = Button(gui, text='3', fg='black', bg='azure3', command=lambda: press(3), height=1, width=7)
    button3.grid(row=3, column=2)
    button4 = Button(gui, text='4', fg='black', bg='azure3', command=lambda: press(4), height=1, width=7)
    button4.grid(row=4, column=0)
    button5 = Button(gui, text='5', fg='black', bg='azure3', command=lambda: press(5), height=1, width=7)
    button5.grid(row=4, column=1)
    button6 = Button(gui, text='6', fg='black', bg='azure3', command=lambda: press(6), height=1, width=7)
    button6.grid(row=4, column=2)
    button7 = Button(gui, text='7', fg='black', bg='azure3', command=lambda: press(7), height=1, width=7)
    button7.grid(row=5, column=0)
    button8 = Button(gui, text='8', fg='black', bg='azure3', command=lambda: press(8), height=1, width=7)
    button8.grid(row=5, column=1)
    button9 = Button(gui, text='9', fg='black', bg='azure3', command=lambda: press(9), height=1, width=7)
    button9.grid(row=5, column=2)
    button0 = Button(gui, text='0', fg='black', bg='azure3', command=lambda: press(0), height=1, width=7)
    button0.grid(row=6, column=1)

    PlusMinus=Button(gui, text='+/-', fg='black', bg='azure3', command=lambda: negate(), height=1, width=7)
    PlusMinus.grid(row=6, column=0)

    plus=Button(gui, text='+', fg='black', bg='azure3', command=lambda: press('+'), height=1, width=7)
    plus.grid(row=5, column=3)
    minus=Button(gui, text='-', fg='black', bg='azure3', command=lambda: press('-'), height=1, width=7)
    minus.grid(row=2, column=3)
    multiply=Button(gui, text='*', fg='black', bg='azure3', command=lambda: press('*'), height=1, width=7)
    multiply.grid(row=3, column=3)
    divide=Button(gui, text='/', fg='black', bg='azure3', command=lambda: press('/'), height=1, width=7)
    divide.grid(row=4, column=3)
    equal=Button(gui, text='=', fg='black', bg='azure3', command=lambda: equals(), height=1, width=7)
    equal.grid(row=6, column=3)

    Clear=Button(gui, text='Clear', fg='black', bg='azure3', command=lambda: clear(), height=1, width=7)
    Clear.grid(row=1, column=3)
    CE=Button(gui, text='CE', fg='black', bg='azure3', command=lambda : clear_last(), height=1, width=7)
    CE.grid(row=1, column=2)

    decimal=Button(gui, text='.', fg='black', bg='azure3', command=lambda: press('.'), height=1, width=7)
    decimal.grid(row=6, column=2)

    l_bracket=Button(gui, text='(', fg='black', bg='azure3', command=lambda: press('('), height=1, width=7)
    l_bracket.grid(row=7, column=0)
    r_bracket=Button(gui, text=')', fg='black', bg='azure3', command=lambda: press(')'), height=1, width=7)
    r_bracket.grid(row=7, column=1)

    root=Button(gui, text='√', fg='black', bg='azure3', command=lambda: press('√'), height=1, width=7)
    root.grid(row=1, column=0)
    pow=Button(gui, text='xⁿ', fg='black', bg='azure3', command=lambda :press('**'), height=1, width=7)
    pow.grid(row=1, column=1)

    pi=Button(gui, text='π', fg='black', bg='azure3', command=lambda: press('π'), height=1, width=7)
    pi.grid(row=7, column=2)
    e=Button(gui, text='e', fg='black', bg='azure3', command=lambda : press('e'), height=1, width=7)
    e.grid(row=7, column=3)

    sin=Button(gui, text='sin', fg='black', bg='azure3', command=lambda: press('sin'), height=1, width=7)
    sin.grid(row=2, column=0)
    cos=Button(gui, text='cos', fg='black', bg='azure3', command=lambda: press('cos'), height=1, width=7)
    cos.grid(row=2, column=1)
    tan=Button(gui, text='tan', fg='black', bg='azure3', command=lambda: press('tan'), height=1, width=7)
    tan.grid(row=2, column=2)

    gui.mainloop() #start the gui