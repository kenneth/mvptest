import os.path
import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('main.html', page_title="", body_id="", messages="whatever",title="home")

settings = {
    "static_path":os.path.join(os.path.dirname(__file__),'static'),
    "template_path":"templates",
}
application = tornado.web.Application([
    (r"/", MainHandler),
], **settings)

if __name__ == "__main__":
    application.listen(8888)
    tornado.ioloop.IOLoop.instance().start()