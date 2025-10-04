from tkinter import *

class Calculator:
    def __init__(self):
        self.window = Tk()
        self.window.title("Calculator")
        self.window.geometry("150x200")
        
        # display
        self.display = Entry(self.window)
        self.display.grid(row=0, column=0, columnspan=4, padx=5, pady=5)

        # making buttons
        buttons = ['7','8','9','/','4','5','6','*','1','2','3','-','C','0','=','+']
        row = 1
        col = 0

        for btn in buttons:
            Button(self.window, text=btn, command=lambda x=btn: self.click(x), bg="lightblue").grid(row=row, column=col)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def click(self, key):
        if key == '=':
            try:
                self.display.insert(END,'=' + str(eval(self.display.get())))
            except:
                self.display.insert(END, '=ERROR')
        elif key == 'C':
            self.display.delete(0, END)
        else:
            self.display.insert(END, key)

    def run(self):
        self.window.mainloop()



calc = Calculator()
calc.run()
        
