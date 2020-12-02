import os
import requests

from multiprocessing import Process

def get_req(url):
    res=requests.get(url)
    print(res)

if __name__=='__main__':
    urls=['https://www.djangoproject.com/weblog/?page={}'.format(i) for i in range(1,5)]
    #names=['Proc name {}'.format(i) for i in range(1,5)]
    print(urls)
    procs=[]

    for i,url in enumerate(urls):
        proc=Process(target=get_req, args=(url,))

        procs.append(proc)
        proc.start()

    for proc in procs:
        proc.join()


