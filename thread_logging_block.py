import threading

total=0
lock=threading.Lock()
def update(number):
    global total
    #print(threading.currentThread().getName() + '\n')
    lock.acquire()
    try:
        print(threading.currentThread().getName() + '\n')
        total=number
    finally:
        lock.release()
    print(total)

if __name__=='__main__':
    for i in range(10):
        my_thread=threading.Thread(target=update,args=(i,))
        my_thread.start()
