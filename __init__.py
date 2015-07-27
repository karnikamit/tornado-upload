__author__ = 'karnikamit'
from tornado.wsgi import WSGIContainer
from tornado.httpserver import HTTPServer
from tornado.ioloop import IOLoop
from routes import app
import sys


if __author__ == 'karnikamit':
    sys.dont_write_bytecode = True
    http_server = HTTPServer(WSGIContainer(app))
    http_server.listen(7000)
    print 'Running on:', 7000
    IOLoop.instance().start()
