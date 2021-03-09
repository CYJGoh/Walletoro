from tkinter import *
 
calc = Tk()
calc.title('Calculator')
calc.resizable(0,0)
calc.iconbitmap(r'images/money-bag.ico')

 
class Application(Frame):

#Initialise the window
    def __init__(self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)
        self.widgets()
 
    def replace_Text(self, text):
        self.display.delete(0, END)
        self.display.insert(0, text)

#Replace the maths operator to python math operator 
    def calculate(self):
        self.expression=self.display.get()
        self.expression=self.expression.replace('%', '/ 100')
        self.expression=self.expression.replace('x','*')
        self.expression=self.expression.replace('÷','/')
 
        try:
            self.result=eval(self.expression)
            self.replace_Text(self.result)
        except:
            messagebox.showinfo('Invalid Input')

#Add the value entered to the display 
    def append_Display(self, text):
        self.entry_Text=self.display.get()
        self.text_Length= len(self.entry_Text)
 
        if self.entry_Text=='0':
            self.replace_Text(text)
        else:
            self.display.insert(self.text_Length, text)

#Clear button function 
    def clear(self):
        self.replace_Text('0')

#Change colour when user pressed the button
    def enter(self):
        self['background']=self['activebackground']

#Return back the colour to default after pressed
    def leave(self):
        self['background']=self.defaultBackground

#All widgets 
    def widgets(self):

        #Calculator Display
        self.display = Entry(self, font=('Times New Roman', 20), borderwidth=0, relief='raised', justify='right')
        self.display.insert(0, '0')
        self.display.grid(row=0, column=0, columnspan=5)
        
        #Buttons
        self.Button_seven = Button(self, font=('Times New Roman', 16), text='7',fg='black', bg='white', borderwidth=0,
                                   activebackground='grey', command=lambda: self.append_Display('7'))
        self.Button_seven.grid(row=1, column=0, sticky='NWNESWSE')
 
        self.Button_eight = Button(self, font=('Times New Roman', 16), text='8',fg='black', bg='white', borderwidth=0,
                                   activebackground='grey', command=lambda: self.append_Display('8'))
        self.Button_eight.grid(row=1, column=1, sticky='NWNESWSE')
 
        self.Button_nine = Button(self, font=('Times New Roman', 16), text='9',fg='black', bg='white', borderwidth=0,
                                  activebackground='grey', command=lambda: self.append_Display('9'))
        self.Button_nine.grid(row=1, column=2, sticky='NWNESWSE')
 
        self.Button_mul = Button(self, font=('Times New Roman', 16), text='x',fg='white', bg='green3', borderwidth=1,
                                 command=lambda: self.append_Display('x'))
        self.Button_mul.grid(row=1, column=3, sticky='NWNESWSE')
 
        self.Button_clear = Button(self, font=('Times New Roman', 16), text='C',fg='black', bg='lemon chiffon', borderwidth=1,
                                   command=lambda: self.clear())
        self.Button_clear.grid(row=1, column=4, sticky='NWNESWSE')
       
 
        self.Button_four = Button(self, font=('Times New Roman', 16), text='4',fg='black', bg='white', borderwidth=0,
                                  activebackground='grey', command=lambda: self.append_Display('4'))
        self.Button_four.grid(row=2, column=0, sticky='NWNESWSE')
 
        self.Button_five = Button(self, font=('Times New Roman', 16), text='5',fg='black', bg='white', borderwidth=0,
                                  activebackground='grey', command=lambda: self.append_Display('5'))
        self.Button_five.grid(row=2, column=1, sticky='NWNESWSE')
 
        self.Button_six = Button(self, font=('Times New Roman', 16), text='6',fg='black', bg='white', borderwidth=0,
                                 activebackground='grey', command=lambda: self.append_Display('6'))
        self.Button_six.grid(row=2, column=2, sticky='NWNESWSE')
 
        self.Button_div = Button(self, font=('Times New Roman', 16), text='÷',fg='white', bg='green3', borderwidth=1,
                                 command=lambda: self.append_Display('÷'))
        self.Button_div.grid(row=2, column=3, sticky='NWNESWSE')
 
        self.Button_percent = Button(self, font=('Times New Roman', 16), text='%',fg='black', bg='lemon chiffon', borderwidth=1,
                                     command=lambda: self.append_Display('%'))
        self.Button_percent.grid(row=2, column=4, sticky='NWNESWSE')
       
 
        self.Button_one = Button(self, font=('Times New Roman', 16), text='1',fg='black', bg='white', borderwidth=0,
                                 activebackground='grey', command=lambda: self.append_Display('1'))
        self.Button_one.grid(row=3, column=0, sticky='NWNESWSE')
 
        self.Button_two = Button(self, font=('Times New Roman', 16), text='2',fg='black', bg='white', borderwidth=0,
                                 activebackground='grey', command=lambda: self.append_Display('2'))
        self.Button_two.grid(row=3, column=1, sticky='NWNESWSE')
 
        self.Button_three = Button(self, font=('Times New Roman', 16), text='3',fg='black', bg='white', borderwidth=0,
                                   activebackground='grey', command=lambda: self.append_Display('3'))
        self.Button_three.grid(row=3, column=2, sticky='NWNESWSE')
 
        self.Button_sub = Button(self, font=('Times New Roman', 16), text='-',fg='white', bg='green3', borderwidth=1,
                                 command=lambda: self.append_Display('-'))
        self.Button_sub.grid(row=3, column=3, sticky='NWNESWSE')
 
        self.Button_equal = Button(self, font=('Times New Roman', 16), text='=',fg='black', bg='lemon chiffon', borderwidth=1,
                                   command=lambda: self.calculate())
        self.Button_equal.grid(row=3, column=4, sticky='NWNESWSE', rowspan=2)
 
 
        self.Button_zero = Button(self, font=('Times New Roman', 16), text='0',fg='black', bg='white', borderwidth=0,
                                  activebackground='grey', command=lambda: self.append_Display('0'))
        self.Button_zero.grid(row=4, column=0, columnspan=2, sticky='NWNESWSE')
 
        self.Button_decimal = Button(self, font=('Times New Roman', 16), text='.',fg='black', bg='white', borderwidth=0,
                                     activebackground='grey', command=lambda: self.append_Display('.'))
        self.Button_decimal.grid(row=4, column=2, sticky='NWNESWSE')
 
        self.Button_add = Button(self, font=('Times New Roman', 16), text='+',fg='white', bg='green3', borderwidth=1,
                                 command=lambda: self.append_Display('+'))
        self.Button_add.grid(row=4, column=3, sticky='NWNESWSE')

#Driver code 
app=Application(calc).grid()
calc.mainloop()
