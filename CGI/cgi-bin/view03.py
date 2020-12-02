#! /usr/bin/env python3
import cgi
import html


form=cgi.FieldStorage()
text1=form.getfirst("author","не задано")
text2=form.getfirst("book","не задано")
text1=html.escape(text1)
text2=html.escape(text2)

print("Content-type: text/html\n")
print("""<!DOCTYPE HTML>
        <html>
        <head>
            <meta charset="cp1251">
            <title>Обработка данных форм</title>
        </head>
        <body>""")

print("<h1>Обработка данных форм!</h1>")
print("<p>text_1: {}</p>".format(text1))
print("<p>text_2: {}</p>".format(text2))

print("""</body>
        </html>""")