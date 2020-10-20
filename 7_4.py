#с помощью скрипта на питоне, примените функцию urlopen, 
#затем примените метод read, а затем метод decode со строкой параметром utf-8. 

from urllib.request import urlopen

response = urlopen("file:///C:/Users/User/Documents/Visual%20Studio%202017/DjangoWebProject1/DjangoWebProject1/app/1.html")
html = response.read().decode('utf-8')
print(html)
