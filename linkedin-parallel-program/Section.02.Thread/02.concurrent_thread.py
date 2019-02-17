import threading
import time


def func1():
    print(threading.currentThread().getName() + ' is starting')
    time.sleep(2)
    print(threading.currentThread().getName() + ' is exiting')
    return

def func2():
    print(threading.currentThread().getName() + ' is starting')
    time.sleep(2)
    print(threading.currentThread().getName() + ' is exiting')
    return

def func3():
    print(threading.currentThread().getName() + ' is starting')
    time.sleep(2)
    print(threading.currentThread().getName() + ' is exiting')
    return



threads = []

for i in range(1):
    t1 = threading.Thread(
        name='func1',
        target=func1,
    )
    
    t2 = threading.Thread(
        name='func2',
        target=func2,
    )
    
    t3 = threading.Thread(
        name='func3',
        target=func3,
    )
    

    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()