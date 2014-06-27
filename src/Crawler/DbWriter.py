import threading

class Thread(threading.Thread):

    def __init__(self, db_queue):
        self.queue = db_queue
        super(Thread, self).__init__()


    def run(self):
        while True:
            msg = self.queue.get(True)
            print msg
