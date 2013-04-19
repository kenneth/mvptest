import datetime
s='Sat, 30 Mar 2013 13:31:19 -0400'
print datetime.datetime.strptime(s,'%a, %d %b %Y %X +%f')
print datetime.datetime.strptime('Mon, 01 Apr 2013 16:00:36 +0000','%a, %d %b %Y %X +%f')
