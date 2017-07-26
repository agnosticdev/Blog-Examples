from sklearn.linear_model import LinearRegression
import pandas as pd
import coremltools

# Create a pandas data frame 
json_data_frame = pd.read_json('final_artist.json')


model = LinearRegression()
model.fit(json_data_frame[["City", "Genre1", "Latitude", "Longitude"]], json_data_frame["Artist"])

coreml_model = coremltools.converters.sklearn.convert(model, ["City", "Genre1", "Latitude", "Longitude"], "Artist")

# Set model metadata
coreml_model.author = 'Matthew Eaton'
coreml_model.license = 'BSD'
coreml_model.short_description = 'Predicts the next artist based upon random music data'

# Set feature descriptions manually
coreml_model.input_description['City'] = 'City where artist is from'
coreml_model.input_description['Genre1'] = 'The genre the artist falls into'
coreml_model.input_description['Latitude'] = 'Latitude of where this artist is from'
coreml_model.input_description['Longitude'] = 'Longitude of where this artist is from'

# Set the output descriptions
coreml_model.output_description['Artist'] = 'Predicted Artist'

# Save the model
coreml_model.save('Artist.mlmodel')


