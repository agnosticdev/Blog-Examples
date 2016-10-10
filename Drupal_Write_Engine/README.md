# Drupal_Write_Engine

This project was created to work side-by-side with the Node_Read_Engine is the sense that all the data is either
entered or posted into this CMS.  Then once the save, update, or delete occurs the data is then synced with a MongoDB
datastore where it is accessed from the Node_Read_Engine.  Only the necessary data is synced with MongoDB.  This means
that most of the fields Drupal carries on a node are not present in MongoDB.  This was done so Node.js was not 
concerned about the format the data was in, but to simply serve the data as fast as possible.
