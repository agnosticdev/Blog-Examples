import os, sys, time, json


with open('final_artist.json') as json_genre_data:
	genre_data = json.load(json_genre_data)
	for genre_obj in genre_data:

		if len(genre_obj['genre']) > 0:
			genre_obj['Genre1'] = genre_obj['genre'][0]
		if len(genre_obj['genre']) > 1:
			genre_obj['Genre2'] = genre_obj['genre'][1]
		if len(genre_obj['genre']) > 2:
			genre_obj['Genre3'] = genre_obj['genre'][2]
		if len(genre_obj['genre']) > 3:
			genre_obj['Genre4'] = genre_obj['genre'][3]
		if len(genre_obj['genre']) > 4:
			genre_obj['Genre5'] = genre_obj['genre'][4]

		del genre_obj['genre']


	with open('final_artist.json', 'w') as outfile:
	    json.dump(genre_data, outfile)

