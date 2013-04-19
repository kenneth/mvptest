from datetime import datetime
#s='20130119T14:14:56+08:00'
s='20130316T04:09:50+01:00'
#print datetime.strptime(s,"%Y%m%dT%H:%M:%S+08:00")

tmp = s[:len(s)-6]
print datetime.strptime(tmp,"%Y%m%dT%H:%M:%S")
