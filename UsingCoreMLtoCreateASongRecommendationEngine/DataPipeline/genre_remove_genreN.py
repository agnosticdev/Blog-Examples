import os, sys, time, json


with open('final_artist.json') as json_genre_data:
	genre_data = json.load(json_genre_data)
	for genre_obj in genre_data:

		if 'Genre5' in genre_obj:
			del genre_obj['Genre5']


	with open('final_artist.json', 'w') as outfile:
	    json.dump(genre_data, outfile)