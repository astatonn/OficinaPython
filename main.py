from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from func import verb_to_be


      
class verbo_to_be():
    def getVerbo (self, sujeito):
        self.verbo = verb_to_be(sujeito)

        Label (self.root, text=self.verbo).grid(row=2,column =1,padx=10,pady=10)

    def __init__(self):
        self.root = Tk()
        self.root.title('APLICAÇÃO VERBO TO BE')
        self.root.geometry('300x300')

        Label (self.root, text='Insira o pronome').grid(row=0,column = 0, columnspan = 2)

        Label (self.root, text='Verbo').grid(row=1,column = 0,padx=10,pady=10)
        self.sujeito = Entry (self.root)
        self.sujeito.grid(row=1, column=1)

        Label (self.root, text='Verbo To be: ').grid(row=2,column = 0,padx=10,pady=10)  


        Button(self.root, text='Enviar', command= lambda : self.getVerbo(self.sujeito.get())).grid(row=3, column=1,padx=15,pady=15)

        self.root.mainloop()

if __name__ == '__main__':
    verbo_to_be ()

