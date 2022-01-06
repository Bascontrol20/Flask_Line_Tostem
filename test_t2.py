# -*- coding: UTF-8 -*-
import threading
import time

thread_lock = threading.Lock()
threads = []

def print_time( thread_name, delay, counter ):
	while counter:
		time.sleep(delay)
		print(thread_name +":"+str(time.ctime(time.time())))
		counter -= 1

class myThread(threading.Thread):
	def __init__( self, thread_id, name, counter ):
		threading.Thread.__init__( self )
		self.thread_id = thread_id
		self.name = name
		self.counter = counter
	def run( self ):
		print("Starting "+self.name)
		thread_lock.acquire()
		print_time( self.name, self.counter, 5 )
		thread_lock.release()
def main():
	# Create new threads
	thread1 = myThread(1, "Thread-1", 1)
	thread2 = myThread(2, "Thread-2", 2)
	# Start new Threads
	thread1.start()
	#thread2.start()
	# Add threads to thread list
	threads.append(thread1)
	#threads.append(thread2)
	# Wait for all threads to complete
	for t in threads:
		t.join()
	print("Exiting Main Thread")

if __name__=="__main__":
	main()