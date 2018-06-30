from wsgiref.simple_server import make_server

from hello import application

httpd = make_server('',9000,application)
print "Server httpp on port 9000..."
httpd.serve_forever()
