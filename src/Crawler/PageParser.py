import threading
import requests
from bs4 import BeautifulSoup


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
                #process url
                html_response = requests.get(url)
                if html_response is None:
                    continue
                soup = BeautifulSoup(html_response.text)
                if soup is None:
                    continue
                aref_list = soup.find_all('a')
                if aref_list is None:
                    continue

                for aref in aref_list:
                    if aref.has_key('id') and re.match(r'thread_title_*', aref.get('id')):
                        if aref.has_key('href'):
                            out_url = self.domain+str(aref.get('href'))
                            self.out_queue.put(out_url, True)
                        #href if ends
                    #aref if ends

            except requests.exceptions.RequestException:
                pass


