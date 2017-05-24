import tkinter as tk
import xlrd

class MainWindow(tk.Frame):
    counter = 0
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.label = tk.Label(self, text="ConstruControl v. 1.0")
        book = xlrd.open_workbook("Presupuestos/Trabajo final- SAR-NGC-JCM.xlsx", ragged_rows = True)
        self.sheet = book.sheet_by_index(8)
        self.chapters = [5,69,90,136,308,383,411,420,438,539,565,879,996,1105,1116,1428,1702,2049,2070,2079]

        self.cell_0 = self.sheet.cell(self.chapters[0],2)
        self.chapter_0 = tk.Button(self, text=self.cell_0.value,command=self.create_window_chapter_0)
        self.chapter_0.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        self.cell_1 = self.sheet.cell(self.chapters[1],2)
        self.chapter_1 = tk.Button(self, text=self.cell_1.value,command=self.create_window_chapter_1)
        self.chapter_1.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        self.cell_2 = self.sheet.cell(self.chapters[2],2)
        self.chapter_2 = tk.Button(self, text=self.cell_2.value,command=self.create_window_chapter_2)
        self.chapter_2.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        self.cell_3 = self.sheet.cell(self.chapters[3],2)
        self.chapter_3 = tk.Button(self, text=self.cell_3.value,command=self.create_window_chapter_3)
        self.chapter_3.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        self.cell_4 = self.sheet.cell(self.chapters[4],2)
        self.chapter_4 = tk.Button(self, text=self.cell_4.value,command=self.create_window_chapter_4)
        self.chapter_4.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        self.cell_5 = self.sheet.cell(self.chapters[5],2)
        self.chapter_5 = tk.Button(self, text=self.cell_5.value,command=self.create_window_chapter_5)
        self.chapter_5.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        self.cell_6 = self.sheet.cell(self.chapters[6],2)
        self.chapter_6 = tk.Button(self, text=self.cell_6.value,command=self.create_window_chapter_6)
        self.chapter_6.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        self.cell_7 = self.sheet.cell(self.chapters[7],2)
        self.chapter_7 = tk.Button(self, text=self.cell_7.value,command=self.create_window_chapter_7)
        self.chapter_7.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        self.cell_8 = self.sheet.cell(self.chapters[8],2)
        self.chapter_8 = tk.Button(self, text=self.cell_8.value,command=self.create_window_chapter_8)
        self.chapter_8.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        self.cell_9 = self.sheet.cell(self.chapters[9],2)
        self.chapter_9 = tk.Button(self, text=self.cell_9.value,command=self.create_window_chapter_9)
        self.chapter_9.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        self.cell_10 = self.sheet.cell(self.chapters[10],2)
        self.chapter_10 = tk.Button(self, text=self.cell_10.value,command=self.create_window_chapter_10)
        self.chapter_10.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        self.cell_11 = self.sheet.cell(self.chapters[11],2)
        self.chapter_11 = tk.Button(self, text=self.cell_11.value,command=self.create_window_chapter_11)
        self.chapter_11.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        self.cell_12 = self.sheet.cell(self.chapters[12],2)
        self.chapter_12 = tk.Button(self, text=self.cell_12.value,command=self.create_window_chapter_12)
        self.chapter_12.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        self.cell_13 = self.sheet.cell(self.chapters[13],2)
        self.chapter_13 = tk.Button(self, text=self.cell_13.value,command=self.create_window_chapter_13)
        self.chapter_13.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        self.cell_14 = self.sheet.cell(self.chapters[14],2)
        self.chapter_14 = tk.Button(self, text=self.cell_14.value,command=self.create_window_chapter_14)
        self.chapter_14.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        self.cell_15 = self.sheet.cell(self.chapters[15],2)
        self.chapter_15 = tk.Button(self, text=self.cell_15.value,command=self.create_window_chapter_15)
        self.chapter_15.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        self.cell_16 = self.sheet.cell(self.chapters[16],2)
        self.chapter_16 = tk.Button(self, text=self.cell_16.value,command=self.create_window_chapter_16)
        self.chapter_16.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        self.cell_17 = self.sheet.cell(self.chapters[17],2)
        self.chapter_17 = tk.Button(self, text=self.cell_17.value,command=self.create_window_chapter_17)
        self.chapter_17.pack(side="top", fill="both", expand=True, padx=10, pady=5)

        self.cell_18 = self.sheet.cell(self.chapters[18],2)
        self.chapter_18 = tk.Button(self, text=self.cell_18.value,command=self.create_window_chapter_18)
        self.chapter_18.pack(side="top", fill="both", expand=True, padx=10, pady=5)

    def create_window_chapter_0(self):
        chapter_0 = tk.Toplevel(self)
        chapter_0.wm_title(self.cell_0.value)
        chapter_0.indexes = [7,8,15,16,17,18,19,20,21,22,23,24,25,30,31,32,33,34,35,36,37,38,39,40,41,42]
        variable = tk.StringVar()
        variable.set("Selecciona una opción")
        chapter_0.strings = []
        for i in range(0,len(chapter_0.indexes)):
            var = self.sheet.cell(chapter_0.indexes[i] - 1,3).value
            chapter_0.strings.append(var)
        chapter_0.drop = tk.OptionMenu(chapter_0,variable,*chapter_0.strings,command=self.act)
        chapter_0.drop.grid(row=0, column=2)
    def act(self,value):
        print(self.value)

    def create_window_chapter_1(self):
        t = tk.Toplevel(self)
        t.wm_title(self.cell_1.value)

    def create_window_chapter_2(self):
        t = tk.Toplevel(self)
        t.wm_title(self.cell_2.value)

    def create_window_chapter_3(self):
        t = tk.Toplevel(self)
        t.wm_title(self.cell_3.value)

    def create_window_chapter_4(self):
        t = tk.Toplevel(self)
        t.wm_title(self.cell_4.value)

    def create_window_chapter_5(self):
        t = tk.Toplevel(self)
        t.wm_title(self.cell_5.value)

    def create_window_chapter_6(self):
        t = tk.Toplevel(self)
        t.wm_title(self.cell_6.value)

    def create_window_chapter_7(self):
        t = tk.Toplevel(self)
        t.wm_title(self.cell_7.value)

    def create_window_chapter_8(self):
        t = tk.Toplevel(self)
        t.wm_title(self.cell_8.value)

    def create_window_chapter_9(self):
        t = tk.Toplevel(self)
        t.wm_title(self.cell_9.value)

    def create_window_chapter_10(self):
        t = tk.Toplevel(self)
        t.wm_title(self.cell_10.value)

    def create_window_chapter_11(self):
        t = tk.Toplevel(self)
        t.wm_title(self.cell_11.value)

    def create_window_chapter_12(self):
        t = tk.Toplevel(self)
        t.wm_title(self.cell_12.value)

    def create_window_chapter_13(self):
        t = tk.Toplevel(self)
        t.wm_title(self.cell_13.value)

    def create_window_chapter_14(self):
        t = tk.Toplevel(self)
        t.wm_title(self.cell_14.value)

    def create_window_chapter_15(self):
        t = tk.Toplevel(self)
        t.wm_title(self.cell_15.value)

    def create_window_chapter_16(self):
        t = tk.Toplevel(self)
        t.wm_title(self.cell_16.value)

    def create_window_chapter_17(self):
        t = tk.Toplevel(self)
        t.wm_title(self.cell_17.value)

    def create_window_chapter_18(self):
        t = tk.Toplevel(self)
        t.wm_title(self.cell_18.value)




if __name__ == "__main__":
    root = tk.Tk()
    main = MainWindow(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()
