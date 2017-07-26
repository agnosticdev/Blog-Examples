import os, sys, time, json

artist_list = []

# Open final artist and replace the genres with a number
with open('final_artist.json') as json_artist_data:
	artist_data = json.load(json_artist_data)
	for artist_obj in artist_data:
		index = 0

		if artist_obj['Artist'] not in artist_list:
			artist_list.append(artist_obj['Artist'])
			artist_obj['Artist'] = (len(artist_list) - 1)
		else:
			artist_obj['Artist'] = artist_list.index(artist_obj['Artist'])
		index += 1


	with open('final_artist.json', 'w') as outfile:
	    json.dump(artist_data, outfile)


with open('artist_list.json', 'w') as outfile:
	json.dump(artist_list, outfile)