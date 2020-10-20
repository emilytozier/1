from urllib.request import urlopen

response = urlopen("file:///C:/Users/User/Documents/Visual%20Studio%202017/DjangoWebProject1/DjangoWebProject1/app/1.html")
html = response.read().decode('utf-8')
print(html)