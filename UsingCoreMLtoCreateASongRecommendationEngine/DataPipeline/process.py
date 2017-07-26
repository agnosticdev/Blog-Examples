# Import needed stdlib and other dependencies
import os, sys, time

complete_content = "" # The string contents of the file
file_lines = [] # A list of lines that the complete_content will be exploded to
new_lines = []



# Open file, read contents into a list to be parsed
try:
	# Open the file and read the contents into a
	with open("artist.txt", 'r') as file:
		complete_content = file.read()

	# Explode or split the string contents to a list
	file_lines = complete_content.split("\n")

except ValueError:
	file_open_errors = "Unexpected error loading file: " + str(sys.exc_info()[0])

	# Write the raised error
	error_raised = "Unexpected error loading file: " + str(sys.exc_info()[0])
	# Display the error to the console
	print(error_raised)
	exit("This program needs an input file to continue. Exiting...")


i = 0
# Loop through each file line and discern what needs to be done with the data
for line in file_lines:
	# {"46.44231", "-93.36586", "Go Fish", "Twin Cities, MN"},
	# Split the line by whitespace so we can parse the line
	command_list = line.split('", "')
	line = ""

	if len(command_list) is not 4:
		continue
	i += 1

	if len(command_list) > 0 and command_list[0] is not None:
		lat = command_list[0]
		lat = lat[:1] + '"Latitude":' + lat[1:]
		line += lat + '", '

	if len(command_list) > 0 and command_list[1] is not None:
		lon = command_list[1]
		line += '"Longitude":"' + lon  + '", '

	if len(command_list) > 1 and command_list[2] is not None:
		art = command_list[2]
		line += '"Artist":"' + art  + '", '

	if len(command_list) > 2 and command_list[3] is not None:
		city = command_list[3]
		line += '"City":"' + city

	line += '\n'
	new_lines.append(line)

# Write the new file
json_file = open("new_artists.json", "w")
for l in new_lines:
	json_file.write(l)

json_file.close()
