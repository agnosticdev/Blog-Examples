import os, sys, time, json

artists_location_without_genre_list = []
artists_genre_list = []
final_list = []

# Open artist location without genre json
with open('data/artists_location_without_genre.json') as json_location_without_genre_data:
    data = json.load(json_location_without_genre_data)
    artists_location_without_genre_list = data['data']

# Open artist genre json
with open('data/artist_genre.json') as json_artist_genre_data:
    artists_genre_list = json.load(json_artist_genre_data)

for artist in artists_location_without_genre_list:
	for artist_genre in artists_genre_list:
		if artist["Artist"] in artists_genre_list:
			if "genre" not in artist:
				artist["genre"] = artists_genre_list[artist["Artist"]]
				final_list.append(artist)


with open('final_artist.json', 'w') as outfile:
    json.dump(final_list, outfile)