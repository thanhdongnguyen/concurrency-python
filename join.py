import threading
import time


'''
Below function main init with 2 thread: thread1 and thread2. 
Thread1 init with Thread and use function start
Thread2 init with Thread and use both function start and join
After run this file, result is:

Thread 1 Started
Is thread 1 Finished
Thread 2 Started
Thread 1 Finished
Thread 2 Finished
Thread 2 definitely finished


this mean, after thread2 use join, it will block parent thread util thread2 terminated, that mean, thread1 will waiting util thread2 terminated
'''

def ourThread(i):
    print("Thread {} Started".format(i))
    time.sleep(i*2)
    print("Thread {} Finished".format(i))

def main():
    thread1 = threading.Thread(target=ourThread, args=(1,))
    thread1.start()
    print("Is thread 1 Finished")
    
    thread2 = threading.Thread(target=ourThread, args=(2,))
    thread2.start()
    thread2.join()
    print("Thread 2 definitely finished")

if __name__ == "__main__":
    main()
