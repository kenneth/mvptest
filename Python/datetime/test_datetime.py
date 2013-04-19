from datetime import datetime
import dateutil.parser
s='20130119T14:14:56+08:00'
print datetime.strptime(s,"%Y%m%dT%H:%M:%S+08:00")
print dateutil.parser.parse(s)
print type(dateutil.parser.parse(s))