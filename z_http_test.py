import http.client

# https://docs.python.org/3/library/http.client.html

conn = http.client.HTTPConnection("192.168.2.1")
conn.request("HEAD", "/")
res = conn.getresponse()
print(res.status, res.reason)

data = res.read()
print(len(data))
