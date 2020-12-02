#процессы выполняются по порядку и выводятся с id
import os
import requests


from multiprocessing import Process, current_process

from multiprocessing import Lock, RLock

#lock=threading.Lock()
def get_req(url,lock):
    lock.acquire()
    try:
        proc=os.getpid()
        res=requests.get(url)
        proc_name=current_process().name
        print(res,proc,proc_name)
    finally:
        lock.release()

if __name__=='__main__':
    lock=RLock()
    urls=['https://www.djangoproject.com/weblog/?page={}'.format(i) for i in range(1,5)]
    names=['Proc name {}'.format(i) for i in range(1,5)]
    #print(urls)
    procs=[]

    for i,url in enumerate(urls):
        proc=Process(target=get_req, name=names[i], args=(url,lock,))
        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()
