import os, sys, time, json

latitude = []
longitude = []

with open('final_artist.json') as json_lat_long_data:
	lat_long_data = json.load(json_lat_long_data)

	
	for obj in lat_long_data:

		if 'Longitude' in obj:
			try:
				i = longitude.index(obj['Longitude'])
				obj['Longitude'] = i
			except:
				i = len(longitude)
				longitude.append(obj['Longitude'])
				obj['Longitude'] = i


		if 'Latitude' in obj:
			try:
				i = latitude.index(obj['Latitude'])
				obj['Latitude'] = i
			except:
				i = len(latitude)
				latitude.append(obj['Latitude'])
				obj['Latitude'] = i


	with open('final_artist.json', 'w') as outfile:
	    json.dump(lat_long_data, outfile)

	with open('latitude_data.json', 'w') as latitude_file:
	    json.dump(latitude, latitude_file)

	with open('longitude_data.json', 'w') as longitude_file:
	    json.dump(longitude, longitude_file)