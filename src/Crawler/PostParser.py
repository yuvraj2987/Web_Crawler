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
    
    def __init__(self, input_queue, output_queue):
        self.in_queue = input_queue
        self.out_queue = output_queue
        super(Thread, self).__init__()
		

    def run(self):
        while True:
            try:
                #print "PostPraser Thread started"
                url = self.in_queue.get(True)
                #print "Post:", url
                thread_id = get_thread_id(url)
                #print "thread_id:", thread_id
                html_response = requests.get(url)
                soup = BeautifulSoup(html_response.text)
                div_class_score_tag = soup.find('div', {'class':['vote_score']})
                score_label = div_class_score_tag.label
                score = score_label.contents[0]
                #print "score:", score
                div_class_pad10_tag = soup.find('div', {'class':['pad10']})
                aref_list = div_class_pad10_tag.find_all('a')
                for aref in aref_list:
                    if aref.has_attr('href'):
                        ref_str = aref.get('href')
                        idx = ref_str.find('www+')
                        if idx != -1:
                            deal_url_list = ref_str[idx:].split('+')[:3]
                            deal_url = ".".join(deal_url_list)
                            post_msg = thread_id+"|"+deal_url+"|"+score+"|"+url+"\n"
                            self.out_queue.put(post_msg, True)
                        #idx if ends
                    #href if ends
                # aref for ends
                #print "Post complete"
            except requests.exceptions.RequestException:
                pass


