import _thread
import time

def print_time( thread_name, delay ):
	count = 0
	while count < 5:
		time.sleep( delay )
		count += 1
		print(thread_name + str(time.ctime(time.time())))


def main():
	try:
		_thread.start_new_thread( print_time, ("thread-1", 2))
		_thread.start_new_thread( print_time, ("thread-2", 4))
	except:
		print("Error: unable to start thread")
	while True:
		pass

if __name__=="__main__":
	main()