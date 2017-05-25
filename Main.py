import tkinter
from tkinter import *
import xlrd

class construControl:
    def create_window_chapter_0(this):
        this.chapter_0_window = Tk()
        this.chapter_0_window.wm_title(this.cell_0.value)
        this.chapter_0_window.indexes = [7,8,15,16,17,18,19,20,21,22,23,24,25,30,31,32,33,34,35,36,37,38,39,40,41,42]
        this.chapter_0_window.variable = tkinter.StringVar(this.chapter_0_window)
        this.chapter_0_window.variable.set('Selecciona una opción')
        this.chapter_0_window.strings = []
        for i in range(0,len(this.chapter_0_window.indexes)):
            var = this.sheet.cell(this.chapter_0_window.indexes[i] - 1,3).value
            this.chapter_0_window.strings.append(var)
        this.chapter_0_window.drop = tkinter.OptionMenu(this.chapter_0_window,this.chapter_0_window.variable,*this.chapter_0_window.strings,command=this.append_0)
        this.chapter_0_window.drop.grid()
        this.chapter_0_window.cont = 1
        this.chapter_0_window.sum = 0
        this.chapter_0_window.label = Label(this.chapter_0_window,text="Especificacion")
        this.chapter_0_window.label.grid(row=this.chapter_0_window.cont,column=0)
        this.chapter_0_window.input = Label(this.chapter_0_window,text="Cantidad")
        this.chapter_0_window.input.grid(row=this.chapter_0_window.cont,column=1)
        this.chapter_0_window.input = Label(this.chapter_0_window,text="Precio")
        this.chapter_0_window.input.grid(row=this.chapter_0_window.cont,column=2)
        this.chapter_0_window.input = Label(this.chapter_0_window,text="Suma")
        this.chapter_0_window.input.grid(row=this.chapter_0_window.cont,column=3)
        this.chapter_0_window.total = Label(this.chapter_0_window,text="Total = " + str(this.chapter_0_window.sum))
        this.chapter_0_window.total.grid()
        this.chapter_0_window.cont += 1
    def append_0(this,val):
        index = this.getIndex(val)
        print(this.chapter_0_window.label.cget('text'))
        this.chapter_0_window.cont += 1
        this.chapter_0_window.spec = Label(this.chapter_0_window,text=val)
        this.chapter_0_window.spec.grid(row=this.chapter_0_window.cont,column=0,sticky = W)
        this.chapter_0_window.input = Entry(this.chapter_0_window)
        this.chapter_0_window.input.grid(row=this.chapter_0_window.cont,column=1,sticky = W)
        this.chapter_0_window.button = Button(this.chapter_0_window,text='sumar')
        this.chapter_0_window.button.grid(row=this.chapter_0_window.cont,column=1,sticky = E)
        this.chapter_0_window.price = Label(this.chapter_0_window,text=this.sheet.cell(index - 1 ,7).value)
        this.chapter_0_window.price.grid(row=this.chapter_0_window.cont,column=2)
        this.chapter_0_window.sumLab = Label(this.chapter_0_window,text="0")
        this.chapter_0_window.sumLab.grid(row=this.chapter_0_window.cont,column=3)
        this.chapter_0_window.total.destroy()
        this.chapter_0_window.total = Label(this.chapter_0_window,text="Total = " + str(this.chapter_0_window.sum))
        this.chapter_0_window.total.grid()


    def  getIndex(this,string):
        for x in range(0,len(this.chapter_0_window.strings)):
            if string == this.chapter_0_window.strings[x]:
                return this.chapter_0_window.indexes[x]

    def create_window_chapter_1(this):
        t = Tk()
        t.wm_title(t.cell_1.value)

    def create_window_chapter_2(this):
        t = Tk()
        t.wm_title(t.cell_2.value)

    def create_window_chapter_3(this):
        t = Tk()
        t.wm_title(t.cell_3.value)

    def create_window_chapter_4(this):
        t = Tk()
        t.wm_title(t.cell_4.value)

    def create_window_chapter_5(this):
        t = Tk()
        t.wm_title(t.cell_5.value)

    def create_window_chapter_6(this):
        t = Tk()
        t.wm_title(t.cell_6.value)

    def create_window_chapter_7(this):
        t = Tk()
        t.wm_title(t.cell_7.value)

    def create_window_chapter_8(this):
        t = Tk()
        t.wm_title(t.cell_8.value)

    def create_window_chapter_9(this):
        t = Tk()
        t.wm_title(t.cell_9.value)

    def create_window_chapter_10(this):
        t = Tk()
        t.wm_title(t.cell_10.value)

    def create_window_chapter_11(this):
        t = Tk()
        t.wm_title(t.cell_11.value)

    def create_window_chapter_12(this):
        t = Tk()
        t.wm_title(t.cell_12.value)

    def create_window_chapter_13(this):
        t = Tk()
        t.wm_title(t.cell_13.value)

    def create_window_chapter_14(this):
        t = Tk()
        t.wm_title(t.cell_14.value)

    def create_window_chapter_15(this):
        t = Tk()
        t.wm_title(t.cell_15.value)

    def create_window_chapter_16(this):
        t = Tk()
        t.wm_title(t.cell_16.value)

    def create_window_chapter_17(this):
        t = Tk()
        t.wm_title(t.cell_17.value)

    def create_window_chapter_18(this):
        t = Tk()
        t.wm_title(t.cell_18.value)

    def __init__(this,master):
        frame = Frame(master)
        frame.pack()
        this.label = Label(frame, text="ConstruControl v. 1.0")
        this.label.pack()
        this.book = xlrd.open_workbook("Presupuestos/Trabajo final- SAR-NGC-JCM.xlsx", ragged_rows = True)
        this.sheet = this.book.sheet_by_index(8)
        this.chapters = [5,69,90,136,308,383,411,420,438,539,565,879,996,1105,1116,1428,1702,2049,2070,2079]

        this.cell_0 = this.sheet.cell(this.chapters[0],2)
        this.chapter_0 = Button(frame, text=this.cell_0.value,command=this.create_window_chapter_0)
        this.chapter_0.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        this.cell_1 = this.sheet.cell(this.chapters[1],2)
        this.chapter_1 = Button(frame, text=this.cell_1.value,command=this.create_window_chapter_1)
        this.chapter_1.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        this.cell_2 = this.sheet.cell(this.chapters[2],2)
        this.chapter_2 = Button(frame, text=this.cell_2.value,command=this.create_window_chapter_2)
        this.chapter_2.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        this.cell_3 = this.sheet.cell(this.chapters[3],2)
        this.chapter_3 = Button(frame, text=this.cell_3.value,command=this.create_window_chapter_3)
        this.chapter_3.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        this.cell_4 = this.sheet.cell(this.chapters[4],2)
        this.chapter_4 = Button(frame, text=this.cell_4.value,command=this.create_window_chapter_4)
        this.chapter_4.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        this.cell_5 = this.sheet.cell(this.chapters[5],2)
        this.chapter_5 = Button(frame, text=this.cell_5.value,command=this.create_window_chapter_5)
        this.chapter_5.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        this.cell_6 = this.sheet.cell(this.chapters[6],2)
        this.chapter_6 = Button(frame, text=this.cell_6.value,command=this.create_window_chapter_6)
        this.chapter_6.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        this.cell_7 = this.sheet.cell(this.chapters[7],2)
        this.chapter_7 = Button(frame, text=this.cell_7.value,command=this.create_window_chapter_7)
        this.chapter_7.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        this.cell_8 = this.sheet.cell(this.chapters[8],2)
        this.chapter_8 = Button(frame, text=this.cell_8.value,command=this.create_window_chapter_8)
        this.chapter_8.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        this.cell_9 = this.sheet.cell(this.chapters[9],2)
        this.chapter_9 = Button(frame, text=this.cell_9.value,command=this.create_window_chapter_9)
        this.chapter_9.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        this.cell_10 = this.sheet.cell(this.chapters[10],2)
        this.chapter_10 = Button(frame, text=this.cell_10.value,command=this.create_window_chapter_10)
        this.chapter_10.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        this.cell_11 = this.sheet.cell(this.chapters[11],2)
        this.chapter_11 = Button(frame, text=this.cell_11.value,command=this.create_window_chapter_11)
        this.chapter_11.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        this.cell_12 = this.sheet.cell(this.chapters[12],2)
        this.chapter_12 = Button(frame, text=this.cell_12.value,command=this.create_window_chapter_12)
        this.chapter_12.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        this.cell_13 = this.sheet.cell(this.chapters[13],2)
        this.chapter_13 = Button(frame, text=this.cell_13.value,command=this.create_window_chapter_13)
        this.chapter_13.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        this.cell_14 = this.sheet.cell(this.chapters[14],2)
        this.chapter_14 = Button(frame, text=this.cell_14.value,command=this.create_window_chapter_14)
        this.chapter_14.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        this.cell_15 = this.sheet.cell(this.chapters[15],2)
        this.chapter_15 = Button(frame, text=this.cell_15.value,command=this.create_window_chapter_15)
        this.chapter_15.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        this.cell_16 = this.sheet.cell(this.chapters[16],2)
        this.chapter_16 = Button(frame, text=this.cell_16.value,command=this.create_window_chapter_16)
        this.chapter_16.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        this.cell_17 = this.sheet.cell(this.chapters[17],2)
        this.chapter_17 = Button(frame, text=this.cell_17.value,command=this.create_window_chapter_17)
        this.chapter_17.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        this.cell_18 = this.sheet.cell(this.chapters[18],2)
        this.chapter_18 = Button(frame, text=this.cell_18.value,command=this.create_window_chapter_18)
        this.chapter_18.pack(side="top", fill="both", expand=True, padx=10, pady=5)


root = Tk()
Main = construControl(root)
root.mainloop()
