from Crawler import PageParser
from Queue import Queue

num_threads = 1
max_size = 10
start_url = "http://slickdeals.net/forums/forumdisplay.php?f=9"
domain= "http://slickdeals.net"
page_queue = Queue(maxsize = max_size)
post_queue = Queue(maxsize = max_size)
url = None

page_parser_threadList = [PageParser.Thread(page_queue, post_queue) for i in xrange(num_threads)]

page_queue.put(start_url, True)
#Start Threads
for thread in page_parser_threadList:
		thread.start()

for page_num in range(2, 3):
		url = start_url+"&page="+str(page_num)
		page_queue.put(url, True)


try:
    while True:
        print "Wait for all threads to end"

except KeyboardInterrupt:
    for thread in page_parser_threadList:
        thread.stop()
        thread.join()

    print "All thread stopped"



