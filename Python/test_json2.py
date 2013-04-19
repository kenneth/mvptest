import simplejson
data='[{"name":"Column_owner","point":"AKESH2880153908"},{"name":"Column_name","point":"wiken"}]'
locations = simplejson.loads(data)
for location in locations:
    print location["name"]
    print location["point"]
