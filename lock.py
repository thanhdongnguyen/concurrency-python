import threading
import time
import random

'''
below example is using lock to locked thread when running workerA and workerB.
If not lock thread, both WorkerA and WorkerB will run and change data at variable: counter with WorkerA is incr 
and workerB is decr
'''


lock = threading.Lock()
counter = 0
def workerA():
    global counter
    lock.acquire() 
    try:
        while counter < 10:
            counter += 1 
            print("Worker A is incrementing counter to {}".format(counter))
            sleepTime = random.randint(0, 1)
            time.sleep(sleepTime)
    finally:
        lock.release()

def workerB():
    global counter
    lock.acquire()
    try:
        while counter > -10:
            counter -= 1
            print("Worker B is decrementing counter to {}".format(counter))
            sleepTime = random.randint(0, 1)
            time.sleep(sleepTime)
    finally:
        lock.release()

if __name__ == "__main__":
    t0 = time.time()
    thread1 = threading.Thread(target=workerA)
    thread2 = threading.Thread(target=workerB)
    thread1.start()
    thread2.start()
    thread1.join()
    thread2.join()
    print("Excuting time: {}".format(time.time() - t0))

