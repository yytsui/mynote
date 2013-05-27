author: yiyang
comments: true
date: 2008-01-06 22:10:52
layout: post
slug: sustainable-transportation-in-canada-an-example-of-exhibit-map-view
title: 'Sustainable transportation in Canada: An example of Exhibit map view'
wordpress_id: 27
tags: Google Maps,Javascript,Python,Web

In Statistics Canada census, there was the [result of employed labor mode of transportation for different areas in Canada](http://www12.statcan.ca/english/census06/data/highlights/POW/Index.cfm). Although the data is quite straightforward, it would be nice to have a 'map' view for this data which will allow us easy to see the distinction geographically.  It turns out that this is an interesting topic for Google map mashup.

By using [Exhibit 2.0](http://simile.mit.edu/exhibit/), a  Javascript library which makes creating interactive easily, all we left to do is dumping the [raw csv data](http://www12.statcan.ca/english/census06/data/highlights/POW/File.cfm?Lang=E&T=603&GH=8&GF=0&G5=0&SC=9&RPP=100&SR=1&SO=0&O=A&D1=1&D2=1&POF=R) with the latitude and longitude of each location into proper json format.  With [geopy](http://exogen.case.edu/projects/geopy/), [simplejson](http://www.undefined.org/python/) and Python build in module csv, here is an implementation:

    
    
    import csv,re
    from geopy import geocoders
    import simplejson
    
    
    COLUMN = ["geocode","place_of_residence","total_Mode_of_transportation","car_truck_or_van_as_driver","car_truck_or_van_as_passenger","total_Sustainable_transportation","public_transit","walked","bicycle","other"]
    GMAPKEY="Google_Map_API_Key_here"
    
    def transformcsv2json(file,jsonfile='output.js'):
    	reader = csv.reader(open(file))
    	column = COLUMN + ['city','province','latlng','label']
    	items=[]
    	fc = 0
    	def getlatlng(place):
    		# For some unknown reasons, sometimes gecoding fails several times before succeeds
    		for i in range(25):
    			try:
    				g = geocoders.Google(GMAPKEY)
    				place, (lat, lng) = g.geocode(place)
    				latlng = str(lat) + ', ' + str(lng)
    				return latlng
    			except:
    				print "|"*60,"Waring! ", place, " ", i, " times geocoding failed!"
    		raise Exception
    
    	for row in reader:
    		city, province = mapLocationName(row[1])
    		if city and province:
    			place = city + " " + province
    			try:
    				latlng = getlatlng(place)
    				rowplus = row + [city, province, latlng, place]
    				transItem = dict(zip(column,rowplus))
    				items.append(transItem)
    			except:
    				#We take a note of the place whcih fails in geocoding but still keeping on transforing next data row anyway.
    				print "?"*60,"Error! ", place, " ", "geocoding failed!"
    				fc += 1
    
    	print "#"*60, 'total number of geocoding fail: ', fc
    	f = open(jsonfile,'w')
    	f.write(simplejson.dumps({'items':items}, ensure_ascii=False))
    	f.close
    
    def mapLocationName(location):
    	#Statistic Canada province abbreviation is different from google maps
    	mapP = {'Alta.':'AB', 'B.C.':'BC', 'Man.':'MB','N.B.':'NB','N.L.':'NL','N.S.':'NS','N.W.T.':'NT','N.U.':'NU','Ont.':'ON','P.E.I.':'PE.','Que.':'QC','Sask.':'SK','Y.T.':'YT'}
    	try:
    		city, province = location.split(',')
    		province = re.findall(r'\((.*)\)',province)[0]
    		if re.search(r'\/',province): province = province.split('/')[0]
    		province = mapP[province]
    	except ValueError:
    		city = location
    		province = ''
    		print 'Warning! ', location, ' parsing failed'
    
    	return city,province
    		
    
    if __name__ == '__main__':
    	transformcsv2json('placeofresidence.csv','placeofresidence.js')
    
    


[Here](/files/pages/placeofresidence.html) is the result map mashup.
