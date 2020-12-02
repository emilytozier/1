#многопоточный мультипроцессорный загрузчик
import os
import requests


from multiprocessing import Pool



def get_req(url):
    res=requests.get(url)
    name=os.path.basename(url)
    print(res,name)

    with open(name,'wb') as fb:
        for chunk in res.iter_content(1024):
            fb.write(chunk)

def main():
    urls=['https://edu.ifmo.ru/file/pages/494/os_mag_prikladnaya_matematika_i_programmirovanie.pdf']

    with Pool(6) as p:
        p.map(get_req,urls)

if __name__=='__main__':
    main()

if __name__=='__main__':
    urls=['https://www.djangoproject.com/weblog/?page={}'.format(i) for i in range(1,5)]
    pool=Pool(3)
    pool.map(get_req,urls)
