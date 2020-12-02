import threading
total=0
lock=threading.RLock()

def a1(number):
    lock.acquire()
    try:
        print('a1 locked')
    finally:
        lock.release()
        print('a1 released')
    return ('a1 done')

def a2(number):
    lock.acquire()
    try:
        print('a2 locked')
    finally:
        lock.release()
        print('a2 released')
    return ('a2 done')

def main():
    with lock:
        res1=a1(1)
        res2=a2(2)
    print(res1)
    print(res2)

if __name__ == '__main__':
    main()