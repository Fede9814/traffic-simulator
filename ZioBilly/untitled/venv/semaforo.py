import time

class semaforo(object):
    stato = True
    def __init__(self):
        self.condizione(self.stato)

    @staticmethod
    def condizione(stato):
        for i in range(10):
            if stato == True:
                stato = False
                start_time = time.time()
                time.sleep(1)
                elapsed_time = time.time() - start_time
            else:
                stato = True
                start_time = time.time()
                time.sleep(4)
                elapsed_time = time.time() - start_time
            print(stato, elapsed_time)


