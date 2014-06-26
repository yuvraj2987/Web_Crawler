import threading
import requests
from bs4 import BeautifulSoup

class Thread(Threading.Thread):
    
    def __init__(self, input_queue, output_queue, domain_name):
        self.in_queue = input_queue
        self.out_queue = output_queue
        self.domain = domain_name
        super(Thread, self).__init__()

    def run(self):

        while True:
            try:
                url = self.in_queue.get(True)
                print url

            except requests.exceptions.RequestException:
                pass


