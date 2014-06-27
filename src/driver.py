from Crawler import PageParser, PostParser, DbWriter
from Queue import Queue

num_threads = 1
max_size = 10
start_url = "http://slickdeals.net/forums/forumdisplay.php?f=9"
domain= "http://slickdeals.net"
page_queue = Queue(maxsize = max_size)
post_queue = Queue(maxsize = max_size)
db_queue   = Queue(maxsize = 100)
url = None
file_name = "data/deal_ratings.txt"
page_parser_threadList = [PageParser.Thread(page_queue, post_queue, domain) for i in xrange(num_threads)]
post_parser_threadList = [PostParser.Thread(post_queue, db_queue) for i in xrange(num_threads)]
db_writer_threadList   = [DbWriter.Thread(db_queue, file_name) for i in xrange(1)]

page_queue.put(start_url, True)
#Start Threads
for thread in page_parser_threadList+post_parser_threadList+db_writer_threadList:
    thread.daemon = True            
    thread.start()

print "All threads started"
for page_num in range(2, 3):
		url = start_url+"&page="+str(page_num)
		page_queue.put(url, True)


print "pages added to the queue"
try:
    print "wait for interrupt"
    while True:
        pass

except KeyboardInterrupt:
    print "End all threads"

