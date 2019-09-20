import urllib
import urllib2

with open('demo.py', 'r') as file :
	try:
		for line in file:
			print(line)
	except:
		print('Read file error')
	finally:
		file.close()

req = urllib2.Request('http://python.org')
response = urllib2.urlopen(req)
html = response.read()
print html
