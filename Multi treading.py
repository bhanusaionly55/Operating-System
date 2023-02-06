import threading
import time

def worker(num):

    print("Worker %d\n" % num)
    time.sleep(1)
    return

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All threads completed.")
