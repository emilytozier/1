from http.server import BaseHTTPRequestHandler
from http.server import HTTPServer
import socketserver
import sys
class ServerWorking(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type','text.html')
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Питон работает</title></head>", "cp1251"))
        self.wfile.write(bytes("<body><h1>Питон работает</h1>", "cp1251"))
        self.wfile.write(bytes("<p> %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))

serv_adress=('',8000)
serv=HTTPServer(serv_adress,ServerWorking)
serv.serve_forever()

