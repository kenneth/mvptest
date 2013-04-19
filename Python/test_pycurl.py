import pycurl
import cStringIO
 
buf = cStringIO.StringIO()
 
c = pycurl.Curl()
c.setopt(c.URL, 'http://www.douban.com')
c.setopt(c.WRITEFUNCTION, buf.write)
c.perform()
 
print buf.getvalue()
buf.close()