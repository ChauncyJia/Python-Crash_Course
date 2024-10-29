import threading
import time

def worker():
    print(f"{threading.current_thread().name} Starting")
    time.sleep(0.2)
    print(f"{threading.current_thread().name} Exiting")

def my_service():
    print(f"{threading.current_thread().name} Starting")
    time.sleep(0.3)
    print(f"{threading.current_thread().name} Exiting")


t = threading.Thread(name='my_service',target=my_service)
w = threading.Thread(name='worker',target=worker)
w2 = threading.Thread(target=worker) # use default name

t.start()
w.start()
w2.start()



