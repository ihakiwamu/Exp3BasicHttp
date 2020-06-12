import http.server
import socketserver
import socket

host = socket.gethostname()
ip = socket.gethostbyname(host)
print(ip)

port = 8080
Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer((host, port), Handler) as httpd:
    httpd.serve_forever()
    

