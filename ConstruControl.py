import tkinter as tk
import xlrd

class MainWindow(tk.Frame):
    counter = 0
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        self.label = tk.Label(self, text="ConstruControl v. 1.0")
        self.label.pack(side="top", fill="both", expand=True, padx=100, pady=20)
        self.button = tk.Button(self, text="Crear nuevo proyecto",command=self.create_window_create)
        self.button.pack(side="top", fill="both", expand=True, padx=50, pady=20)
        self.button = tk.Button(self, text="Cargar proyecto",command=self.create_window_load)
        self.button.pack(side="top", fill="both", expand=True, padx=50, pady=0)
        self.label = tk.Label(self, text=" ")
        self.label.pack(side="top", fill="both", expand=True, padx=100, pady=50)
        self.button = tk.Button(self, text="Acerca de...",command=self.create_window_about)
        self.button.pack(side="top", fill="both", expand=True, padx=50, pady=20)
        self.label = tk.Label(self, text="-TILANO, Arturo; VÉLEZ, Tomás")
        self.label.pack(side="top", fill="both", expand=True, padx=100, pady=0)
        self.label = tk.Label(self, text="2017")
        self.label.pack(side="top", fill="both", expand=True, padx=100, pady=0)
        self.label = tk.Label(self, text=" ")
        self.label.pack(side="top", fill="both", expand=True, padx=100, pady=5)

    def quit(self):
        self.root.destroy

    def create_window_create(self):
        t = tk.Toplevel(self)
        t.wm_title("Crear")
        l = tk.Label(t, text="Nuevo")
        l.pack(side="top", fill="both", expand=True, padx=10, pady=0)
        l = tk.Label(t, text="Escriba el nombre del proyecto:")
        l.pack(side="top", fill="both", expand=True, padx=10, pady=0)
        i = tk.Entry(t)
        i.pack(side="top", fill="both", expand=True, padx=10, pady=10)
        l = tk.Label(t, text="Cargar imágen de portada")
        l.pack(side="top", fill="both", expand=True, padx=10, pady=10)
        b = tk.Button(t, text="Aceptar",command=self.create_Main_Layout)
        b.pack(side="left",expand=True, padx=10,pady = 10)
        b = tk.Button(t, text="Atrás")
        b.pack(side="left",expand=True, padx=10,pady = 10)

    def create_window_load(self):
        t = tk.Toplevel(self)
        self.root = tk;
        t.wm_title("Cargar")
        b = tk.Button(t, text="Aceptar",command=self.create_Main_Layout)
        b.pack(side="left",expand=True, padx=10,pady = 10)
        b = tk.Button(t, text="Atrás")
        b.pack(side="left",expand=True, padx=10,pady = 10)

    def create_window_about(self):
        self.counter += 1
        t = tk.Toplevel(self)
        t.wm_title("Window #%s" % self.counter)
        l = tk.Label(t, text="ConstruControl")
        l.pack(side="top", fill="both", expand=True, padx=100, pady=5)
        l = tk.Label(t, text="V.1.0")
        l.pack(side="top", fill="both", expand=True, padx=100, pady=5)
        l = tk.Label(t, text=" ")
        l.pack(side="top", fill="both", expand=True, padx=100, pady=10)
        l = tk.Label(t, text="Creado por:")
        l.pack(side="top", fill="both", expand=True, padx=100, pady=5)
        l = tk.Label(t, text="Arturo Tilano C.")
        l.pack(side="top", fill="both", expand=True, padx=100, pady=5)
        l = tk.Label(t, text="Tomás Vélez G.")
        l.pack(side="top", fill="both", expand=True, padx=100, pady=5)
        l = tk.Label(t, text=" ")
        l.pack(side="top", fill="both", expand=True, padx=100, pady=10)
        l = tk.Label(t, text="Profesor Asesor:")
        l.pack(side="top", fill="both", expand=True, padx=100, pady=5)
        l = tk.Label(t, text="Luis Fernando Botero")
        l.pack(side="top", fill="both", expand=True, padx=100, pady=5)
        l = tk.Label(t, text=" ")
        l.pack(side="top", fill="both", expand=True, padx=100, pady=10)
        l = tk.Label(t, text="Modelación Computacional")
        l.pack(side="top", fill="both", expand=True, padx=100, pady=5)
        l = tk.Label(t, text="Ingeniería Civil")
        l.pack(side="top", fill="both", expand=True, padx=100, pady=5)
        l = tk.Label(t, text="Universidad EAFIT")
        l.pack(side="top", fill="both", expand=True, padx=100, pady=5)
        l = tk.Label(t, text="2017-1")
        l.pack(side="top", fill="both", expand=True, padx=100, pady=5)

    def create_Main_Layout(self):
        t = tk.Toplevel(self)
        t.wm_title("Capítulos")
        book = xlrd.open_workbook("Presupuestos/Trabajo final- SAR-NGC-JCM.xlsx", ragged_rows = True)
        sheet = book.sheet_by_index(8)
        chapters = [5,69,90,136,308,383,411,420,438,539,565,879,996,1105,1116,1428,1702,2049,2070,2079]
        for  i in range(0,len(chapters) - 1):
            cellNum = chapters[i] - 1
            cell = sheet.cell(cellNum,2)
            b = tk.Button(t, text=cell.value)
            b.pack(side="top", fill="both", expand=True, padx=10, pady=5)


if __name__ == "__main__":
    root = tk.Tk()
    main = MainWindow(root)
    main.pack(side="top", fill="both", expand=True)
    root.mainloop()
