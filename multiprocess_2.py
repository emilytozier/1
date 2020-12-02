import os
import requests

from multiprocessing import Process, current_process, Lock

def get_req(url):
    proc=os.getpid()
    res=requests.get(url)
    proc_name=current_process().name
    print(res,proc,proc_name)

if __name__=='__main__':
    urls=['https://www.djangoproject.com/weblog/?page={}'.format(i) for i in range(1,5)]
    names=['Proc name {}'.format(i) for i in range(1,5)]
    #print(urls)
    procs=[]

    for i,url in enumerate(urls):
        proc=Process(target=get_req, name=names[i], args=(url,))

        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()
