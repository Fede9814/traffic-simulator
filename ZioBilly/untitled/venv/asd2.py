from tkinter import Tk, Canvas, Frame, BOTH

"""
def run_periodically(func, ms):
    func()
    root.after(ms, run_periodically, func, ms)

def tick():
    global count
    count += 1
    tick_label.configure(text="count: %d" % count)

count = 0
root = tk.Tk()
tick_label = tk.Label(root, text="")
tick_label.pack(padx=20, pady=20)

run_periodically(tick, 1000)

root.mainloop()
"""
class Veicolo(Frame):

    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):

        # questo è il titolo della finestra: nel nostro caso sarà "Simulatore traffico" per esempio
        self.master.title("Forma del veicolo")
        self.pack(fill=BOTH, expand=1)

        canvas = Canvas(self)
        macchina = canvas.create_rectangle(150,200,170,300, fill='blue')
        canvas.create_line(300, 35, 300, 200, dash=(4, 2))
        canvas.create_line(55, 85, 155, 85, 105, 180, 55, 85)
        canvas.pack(fill=BOTH, expand=1)
        canvas.move(macchina, 30,30)

def main():

    root = Tk()
    ex = Veicolo()
    root.geometry("500x500+300+300")
    root.mainloop()

if __name__ == '__main__':
    main()