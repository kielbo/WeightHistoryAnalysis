import sqlite3
from tkinter import *
from tkinter import messagebox
from datetime import date
import matplotlib
matplotlib.use("TkAgg")
from db import Database
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
database = Database("fat.db")
class Grubas:
    
    def __init__(self,window):
        self.window=window 
        self.window.wm_title("G R U B A S") #Tytuł okna
        #################################ETYKIETY##################################
        l1=Label(window,text="Date: ") #Etykieta z napisem
        l1.grid(row=0,column=0) #Umiejscowienie etykiety w interfejsie

        l2=Label(window,text="Weight: ")
        l2.grid(row=1,column=0)

        l2=Label(window,text="Overall cheange: ")
        l2.grid(row=2,column=3)

        l3=Label(window,text="Cheange last: ")
        l3.grid(row=1,column=3)

        l4=Label(window,text="Start Weight: ")
        l4.grid(row=0,column=3)
        today = date.today()
        #l5=Label(window,text=today)
        #l5.grid(row=0,column=1)
        ###########################PRZYCISKI####################################
        b1=Button(window,text="View All",width=12,command=self.command_view_all)
        b1.grid(row=3,column=5)
        b2=Button(window,text="New Entry",width=12,command=self.command_entry)
        b2.grid(row=4,column=5)
        b3=Button(window,text="Update",width=12,command=self.command_update)
        b3.grid(row=5,column=5)
        b4=Button(window,text="Delete entry",width=12,command=self.command_destroy)#Usuwanie zaznaczonej pozycjii
        b4.grid(row=6,column=5)
        b5=Button(window,text="Close",width=12,command=window.destroy)#zamykanie programu funkcja window.destroy()
        b5.grid(row=7,column=5)
        ################################POLA#########################################

        self.weight_var=IntVar()
        self.e1=Entry(window,textvariable=self.weight_var)
        self.e1.grid(row=1,column=1)
        
        self.date=StringVar() 
        self.date.set(today)
        self.e2=Entry(window,textvariable=self.date)
        self.e2.grid(row=0,column=1)
        ###############################LIST##########################################

        self.list1=Listbox(window,height=15,width=20)
        self.list1.grid(row=3,column=3,rowspan=4)
        self.list1.bind("<<ListboxSelect>>",self.get_selected_row) #opisac w komenciku

        sb1=Scrollbar(window)
        sb1.grid(row=3,column=4,rowspan=6)

        #frame1=Frame(window,height=15,width=20)
        #frame1.grid(row=3,column=0,rowspan=4)
        #testowanie wykresu
        self.figure = Figure(figsize=(3,2), dpi=100)#konfiguracja wymiarow wykresu dpi to dots per inches
        plot = self.figure.add_subplot(1,1,1)#Either a 3-digit integer or three separate integers describing the position of the subplot. If the three integers are nrows, ncols, and index in order, the subplot will take the index position on a grid with nrows rows and ncols columns. index starts at 1 in the upper left corner and increases to the right.Pos is a three digit integer, where the first digit is the number of rows, the second the number of columns, and the third the index of the subplot. i.e. fig.add_subplot(235) is the same as fig.add_subplot(2, 3, 5). Note that all integers must be less than 10 for this form to work.If no positional arguments are passed, defaults to (1, 1, 1).In rare circumstances, add_subplot may be called with a single argument, a subplot axes instance already created in the present figure but not in the figure's list of axes.
        self.canvas = FigureCanvasTkAgg(self.figure, window)#ta komenda dopiero tworzy wykres 
        self.canvas.get_tk_widget().grid(row=3, column=1,rowspan=4)
    #----------------------------------------------------------------------------
    def command_entry(self):
        database.insert(self.weight_var.get(),self.date.get())
        self.list1.delete(0,END)
        self.list1.insert(END,self.weight_var.get())

    def command_view_all(self):
        self.list1.delete(0,END)
        for rows in database.view():
            self.list1.insert(END,rows)

    def get_selected_row(self,event):
        """tworzy zmienna globalna z danymi z zaznaczonego rekordu, dodatkowo uzupelnia pola o dane z zaznaczonego rekordu. Funkcja ma byc wykorzystana do funkcji odpowiadającej za przycisk update"""
        global selected_tuple #Deklaracja zmiennej globalnej
        index=self.list1.curselection()[0] # curse selection zwraca nr indexu pozycji na ktora klikna urzytkownik, 
        selected_tuple= self.list1.get(index) #wyciaga zawartość kliknietego wiersza do zmiennej
        #print(selected_tuple)
        #print(self.list1.curselection())
        #dalej wypelniamy pola danymi z kliknietych wierszy
        self.e1.delete(0,END)
        self.e1.insert(END,selected_tuple[2])
        self.e2.delete(0,END)
        self.e2.insert(END,selected_tuple[1])
    
    def command_update(self):
        database.update(selected_tuple[0],self.weight_var.get(),self.date.get())
        messagebox.showinfo("Update","Entry number %s has been updated" % selected_tuple[0])
        self.command_view_all()

    def command_destroy(self):
        confirm = messagebox.askyesno("Confirmation ", "Are you sure that you want to delete selected entry ? ", icon='warning')
        #print(confirm)
        if confirm==True:
           database.delete(selected_tuple[0])
           self.command_view_all()



window=Tk()
Grubas(window)
window.mainloop()
