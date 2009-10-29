import httplib, os, urlparse

def http_connection(url):
  components = list(urlparse.urlparse(url))

  if 'https' == components[0]:
    return httplib.HTTPSConnection(components[1])

  return httplib.HTTPConnection(components[1])

url = os.environ['PATH_INFO'][1:] + '?' + os.environ['QUERY_STRING']

conn = http_connection(url)
conn.request('GET', url, None, None)
response = conn.getresponse()

print 'Access-Control-Allow-Origin: *'

print 'Status: ' + str(response.status) + ' ' + response.reason

for header in response.getheaders():
  print header[0] + ': ' + header[1]

print

print response.read()
