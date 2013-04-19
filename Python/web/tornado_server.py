#!/usr/bin/env python
#coding:utf-8
from django.conf import settings
import sys
reload(sys)
sys.setdefaultencoding("utf-8")

import logging
logging.basicConfig(level=logging.DEBUG)
import os.path
import tornado.auth
import tornado.escape
import tornado.httpserver
import tornado.ioloop
import tornado.options
from tornado.options import define, options

define("host", default="127.0.0.1", help="run on the given port", type=int)
define("port", default=8888, help="run on the given port", type=int)

from charlotte import app

def main(port=None):
    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(App())
    port = port or options.port
    http_server.listen(port)
    print "port", port
    tornado.ioloop.IOLoop.instance().start()

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1].isdigit():
        port = int(sys.argv[1])
    else:
        port = 8888
    main(port=port)

