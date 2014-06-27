import threading

class Thread(threading.Thread):

    def __init__(self, db_queue, file_name):
        self.queue = db_queue
        self.out_file = file_name
        super(Thread, self).__init__()

    def run(self):
        out_file = self.out_file
        with open(out_file, "w") as fp:
            while True:
                msg = self.queue.get(True)
                #print msg
                fp.write(msg)
            #while ends
        #with statement ends

