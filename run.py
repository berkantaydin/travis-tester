import requests

i = 0
while i < 100000:
r = requests.get('http://graph.facebook.com/%s' % i)
i += 1
print(r.text)