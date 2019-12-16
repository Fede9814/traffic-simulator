from tkinter import *
import time
import semaforo

MLato1 = 50
MLato2 = 50
MLato3 = 0
MLato4 = 0

t = time.time()
T = time.ctime(t)

class macchina(object):
    def __init__(self):
        self.root = Tk()
        self.canvas = Canvas(self.root, width=700, height=700)
        self.canvas.create_line(350, )
        self.canvas.pack()
        self.macchina1 = self.canvas.create_rectangle(MLato1, MLato2, MLato3, MLato4, fill='blue')
        self.canvas.moveto(self.macchina1, x=0, y=180)
        self.canvas.pack()
        self.root.after(0, self.animation)
        self.root.mainloop()

    def animation(self):
        track = 0
        while True:
            x = 5
            y = 0
            if track == 0:
                for i in range(0, 100):
                    time.sleep(0.05)
                    if semaforo.semaforo.stato:
                        self.canvas.move(self.macchina1, x, y)
                        self.canvas.update()
                track = 1
                print("check")
            else:
                for i in range(0, 100):
                    time.sleep(0.05)
                    if semaforo.semaforo.stato:
                        self.canvas.move(self.macchina1, -x, y)
                        self.canvas.update()
                track = 0
            print(track)


macchina()
root.mainloop()
