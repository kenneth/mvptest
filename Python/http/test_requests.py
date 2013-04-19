import requests
#r = requests.get('https://github.com/timeline.json')
#r = requests.post("http://httpbin.org/post")
#r = requests.put("http://httpbin.org/put")
#r = requests.delete("http://httpbin.org/delete")
#r = requests.head("http://httpbin.org/get")
#r = requests.options("http://httpbin.org/get")
#r = requests.get('https://api.github.com/user', auth=('user', 'pass'))
#r = requests.get('http://www.42qu.com/')

payload = {'key1': 'value1', 'key2': 'value2'}
r = requests.get("http://httpbin.org/get", params=payload)
print r.url
print r
print r.status_code
print r.headers['content-type']
print r.encoding
print r.text
print r.json()