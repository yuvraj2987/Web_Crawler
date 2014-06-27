import threading
import requests
from bs4 import BeautifulSoup

def get_thread_id(url):
    """
        Give a url get the thread_id
    """
    url_split_list = url.split('/')
    last_item = url_split_list[-1]
    last_item_list = last_item.split('-')
    if last_item_list is None:
        return str(-1)
    else:
        return last_item_list[0]

class Thread(threading.Thread):
    
    def __init__(self, input_queue, output_queue, domain_name):
        self.in_queue = input_queue
        self.out_queue = output_queue
        self.domain = domain_name
        super(Thread, self).__init__()
		

    def run(self):
        while True:
            try:
                url = self.in_queue.get(True)
                #print url


            except requests.exceptions.RequestException:
                pass


