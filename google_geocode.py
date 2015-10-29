import urllib
import json

#https://maps.googleapis.com/maps/api/geocode/json?address=1600+Amphitheatre+Parkway,+Mountain+View,+CA&key=YOUR_API_KEY

google_key="AIzaSyBim9i4jcLd7KJdZJediqwyQBWaaJCHPWA"
servicecurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

address = "Portland Oregon"

url = servicecurl + urllib.urlencode({'sensor':'false','address':address,'key':google_key})
print 'Retrieving',url
uh = urllib.urlopen(url)
data = uh.read()

print 'Retrieved', len(data),'characters'

try: js = json.loads(str(data))
except: js = None

print (str(data))

#if 'status' not in js or js['status'] != 'OK':
#	print "==== Failure to Retrieve ==="
#	print data

print json.dumps(js,indent=4)

lat = js["results"][0]["geometry"]["location"]["lat"]
lng = js["results"][0]["geometry"]["location"]["lng"]

print 'lat', lat, 'lng',lng
location = js['results'][0]['formatted_address']
print location
