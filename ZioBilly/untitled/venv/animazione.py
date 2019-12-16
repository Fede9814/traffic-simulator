

class animazione(object):
    def __init__(self):
        animation(macchina1)

def animation(macchina1):
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
