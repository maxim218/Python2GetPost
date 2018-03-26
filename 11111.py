import random

import urllib
import urllib2

######################################################################

def getRandNumber(n):
	r = int(random.random() * 1000) % n
	return r

def getRandChar():
	s = "abcdefghijklmnopqrstuvwxyz"
	n = len(s)
	v = getRandNumber(n)
	c = s[v]
	return str(c)

def getRandString(n):
	s = ""
	for i in range(0,n):
		s = s + getRandChar()
	return s

######################################################################

def assertEqual(valueReal, valueNormal):
	message = ""
	if(valueNormal != valueReal):
		message += "\n"
		message += "----------------------------------------------"
		message += "\n"
		message += "Result not correct:"
		message += "\n"
		message += "Normal result: " + str(valueNormal);
		message += "\n"
		message += "Real result: " + str(valueReal);
		message += "\n\n"
		raise Exception(message)
	else:
		message += "\n"
		message = "----------------------------"
		message += "\n"
		message += "Test OK"
		message += "\n"
		message += "Normal and Real value: " + str(valueReal);
		message += "\n\n"
		print(message)

######################################################################

def getUrl(s):
	url = 'http://localhost:5000/' + s + '/' + getRandString(25)
	return url

def sendGet(s):
	url = getUrl(s)
	data = urllib.urlopen(url).read()
	return data

def sendPost(s, body):
	headers = { 'User-Agent' : 'python urllib2' }
	data = body
	url = getUrl(s)
	req = urllib2.Request(url, data, headers)
	response = urllib2.urlopen(req)
	result = response.read()
	return result


######################################################################


n = 0

while(True):
	n += 1
	nam = "t1Au" + str(n)
	pas = "t1Ap" + str(n)
	assertEqual(  sendPost("registrate_user", '{"loginField":"' + nam + '","passwordField":"' + pas + '"}') ,  "__YES__"  );
	assertEqual(  sendPost("registrate_user", '{"loginField":"' + nam + '","passwordField":"' + pas + '"}') ,  "__NO__"  );
	assertEqual(  sendPost("registrate_user", '{"loginField":"' + nam + '","passwordField":"' + pas + '"}') ,  "__NO__"  );
	assertEqual(  sendPost("registrate_user", getRandString(24) ) ,  "__JSON_ERROR__"  );
	print(nam, pas)







	



