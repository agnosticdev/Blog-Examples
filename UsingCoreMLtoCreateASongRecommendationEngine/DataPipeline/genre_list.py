import os, sys, time, json

genre_list = []


# Open final artist and replace the genres with a number
with open('final_artist.json') as json_genre_data:
	genre_data = json.load(json_genre_data)
	for genre_obj in genre_data:
		index = 0
		for genre in genre_obj['genre']:
			if genre not in genre_list:
				genre_list.append(genre)
				genre_obj['genre'][index] = (len(genre_list) - 1)
			else:
				genre_obj['genre'][index] = genre_list.index(genre)
			index += 1


	with open('final_artist.json', 'w') as outfile:
	    json.dump(genre_data, outfile)


with open('genre_list.json', 'w') as outfile:
	json.dump(genre_list, outfile)