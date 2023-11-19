import urllib.parse
url = 'wss://localhost:8765'
params = {'var1': 'lh = 8765', 'var2': 1337}
print(url + urllib.parse.urlencode(params))
