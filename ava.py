import urllib
import json as m_json

mySites = ['github.com', 'stackoverflow.com', 'pastebin.com']

for i in mySites:
	#print i
	query = "inurl:" + i + " " + "paddypower"
	#print query
	query = urllib.urlencode ( { 'q' : query } )
	#print query
	response = urllib.urlopen ( 'http://ajax.googleapis.com/ajax/services/search/web?rsz=8&v=1.0&' + query ).read()
	#print response
	json = m_json.loads ( response )
	results = json [ 'responseData' ] [ 'results' ]
	print "# Found #"
	for result in results:
	    title = result['title']
	    url = result['url']   # was URL in the original and that threw a name error exception
	    print ( title + '; ' + url )

