#можно использовать для работы с любыми web страницами с использованием BS
import threading
import requests
from bs4 import BeautifulSoup as BS



def read(number):
    print(threading.currentThread().getName()+'\n')
    page=requests.get('https://www.djangoproject.com/weblog/?page={}'.format(number))
    res=BS(page.text,features='lxml').h1
    print(res)

if __name__=='__main__':
    for i in range(1,6):
        my_thread=threading.Thread(target=read,args=(i,))
        my_thread.start()

    for i in range(1,6):
        my_thread.join()