import os, sys, time, json

json_id_genre_list = []
json_id_artist_list = []
final_dict = {}

# Open genre list and read the data in the array to a list
with open('artist_id_genre.json') as json_id_genre_data:
    genre_data = json.load(json_id_genre_data)
    json_id_genre_list = genre_data['data']

# Open artist list and read the data in the array to a list
with open('id_artist.json') as json_artist_genre_data:
	artist_data = json.load(json_artist_genre_data)
	json_id_artist_subset = artist_data['data']


for artist in json_id_artist_subset:
	for genre in json_id_genre_list:
		if artist["id"] == genre["id"]:
			if artist["artist"] in final_dict:
				if (genre["genre"] not in final_dict[artist["artist"]] and 
					len(final_dict[artist["artist"]]) < 6):
					final_dict[artist["artist"]].append(genre["genre"])
			else:
				final_dict[artist["artist"]] = [genre["genre"]]



with open('artist_genre.json', 'w') as outfile:
    json.dump(final_dict, outfile)
