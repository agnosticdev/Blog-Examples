import os, sys, time, json


# Open final artist and replace the genres with a number
with open('final_artist.json') as json_conversion_data:
	conversion_data = json.load(json_conversion_data)
	for obj in conversion_data:

		obj["Latitude"] = float(obj["Latitude"])
		obj["Longitude"] = float(obj["Longitude"])


	with open('final_artist.json', 'w') as outfile:
	    json.dump(conversion_data, outfile)
