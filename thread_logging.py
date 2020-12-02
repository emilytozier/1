import threading
import requests
from bs4 import BeautifulSoup as BS
import logging
import time

class MyThread(threading.Thread):
    def __init__(self,number,logger):
        threading.Thread.__init__(self)
        self.number=number
        self.logger=logger
    def run(self):
        logger.debug('read function')
        read(self.number, self.logger)


def get_logger():
    logger=logging.getLogger('example')
    logger.setLevel(logging.DEBUG)

    log_file=logging.FileHandler('example.log')
    log_format='%(asctime)s - %(threadName)s - %(message)s'
    log_formatter=logging.Formatter(log_format)

    log_file.setFormatter(log_formatter)
    logger.addHandler(log_file)
    return logger

def read(number,Logger):
    print(threading.currentThread().getName()+'\n')
    time.sleep(5)
    page=requests.get('https://www.djangoproject.com/weblog/?page={}'.format(number))
    res=BS(page.text,features='lxml').h1
    print(res)

if __name__=='__main__':
    logger=get_logger()
    thread_names=['Alfa','Gamma','Beta','Omega','Zetta','Ipsylon']
    for i in range(1,6):
        my_thread=MyThread(i,logger)
        my_thread.setName(thread_names[i])
        my_thread.start()

    for i in range(1,6):
        my_thread.join()