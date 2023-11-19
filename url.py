import urllib.parse
url = 'wss://example.com/somepage/?'
params = {'var1': 'some data', 'var2': 1337}
print(url + urllib.parse.urlencode(params))
