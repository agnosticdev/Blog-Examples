import os, sys, time, json

city_list = []

# Open final artist and replace the genres with a number
with open('final_artist.json') as json_city_data:
	city_data = json.load(json_city_data)
	for city_obj in city_data:
		index = 0

		if city_obj['City'] not in city_list:
			city_list.append(city_obj['City'])
			city_obj['City'] = (len(city_list) - 1)
		else:
			city_obj['City'] = city_list.index(city_obj['City'])
		index += 1


	with open('final_artist.json', 'w') as outfile:
	    json.dump(city_data, outfile)


with open('city_list.json', 'w') as outfile:
	json.dump(city_list, outfile)