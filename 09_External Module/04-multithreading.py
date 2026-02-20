import threading
import time

def worker(num):
    print(f"{num} Thread : Starting")
    time.sleep(2)
    print(f"{num} Thread : Finished")

threads=[]
for i in range(3):
    thread = threading.Thread(target = worker,args=(i,) )
    threads.append(thread)
    thread.start()
    
for thread in threads:
    thread.join() # Waits for all the threads to finish.
print("All the threads completed.")