import tkinter as tk
from tkinter import messagebox
import math

class Calculator:
    def __init__(self,root):
        self.root = root
        self.root.title('GUI Calculator')
        self.root.geometry('400x500')
        self.equation = tk.StringVar()

        # Entry Widget for Input
        self.entry = tk.Entry(root,textvariable=self.equation, font=('Arial',20), bd=10,relief='ridge', justify ='right')
        self.entry.grid(row=0, column=0,columnspan=4, ipadx=8, ipady=8)

        # Buttons Layout
        buttons = [
            ('7',1,0),('8',1,1),('9',1,2),('/',1,3),
            ('4',2,0),('5',2,1),('6',2,2),('*',2,3),
            ('1',3,0),('2',3,1),('3',3,2),('-',3,3),
            ('0',4,0),('.',1,1),('+',4,2),('=',4,3),
            ('c',5,0),('sqrt',5,1),('x^2',5,2),('log',5,3),
            ('sin',6,0),('cos',6,1),('tan',6,2),('Exit',1,3)
            ]

        for (text,row,col) in buttons:
            button = tk.Button(root,text=text, font=('Arial',15),padx=20,pady=20,
            command=lambda t=text:self.on_button_click(t))
            button.grid(row=row,column=col, sticky='nsew')

    def on_button_click(self, char):
        if char == '=':
            try:
                self.equation.set(eval(self.equation.get()))
            except:
                messagebox.showerror('error','invalid input')
        elif char == 'c':
            self.equation.set('')
        elif char == 'sqrt':
            try:
                self.equation.set(str(math.sqrt(float(self.equation.get()))))
            except:
                messagebox.showerror('error','invalid input')
        elif char == 'x^2':
            try:
                self.equation.set(str(float(self.equation.get())**2))
            except:
                messagebox.showerror('error','invalid input')
        elif char == 'log': 
            try:
                self.equation.set(str(math.log10(float(self.equation.get()))))
            except:
                messagebox.showerror('error','invalid input')
        elif char in ['sin','cos','tan']:
            try:
                num = float(self.equation.get())
                if char == 'sin':
                    self.equation.set(str(math.sin(math.radians(num))))
                elif char == 'cos':
                   self.equation.set(str(math.cos(math.radians(num))))
                elif char == 'tan':
                   self.equation.set(str(math.tan(math.radians(num))))
            except:
                messagebox.showerror('error','invalid input')
        elif char == 'Exit':
                    self.root.quit()
        else:
                    self.equation.set(self.equation.get() + char)

if __name__ == '__main__':
    root = tk. Tk()
    app = Calculator(root)
    root.mainloop()
                
          
