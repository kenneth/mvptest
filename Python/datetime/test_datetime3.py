from time import gmtime, strftime
print strftime("%a, %d %b %Y %H:%M:%S +0000", gmtime())

from datetime import datetime
dt = datetime.now()
print dt.strftime('%Y-%m-%d %H:%M:%S %z')
s='Sat, 30 Mar 2013 13:31:19 -0400'
print datetime.strptime(s,"%a, %d %b %Y %H:%M:%S -0400")
#print datetime.strptime(s,"%a, %d %b %Y %H:%M:%S %z")