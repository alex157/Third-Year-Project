import sys
import glob
import json

#Search the path for any JSON files included in the directory
path = 'C:/Users/User/Desktop/Dataset/Last fm dataset/Final/all_data/*.json'
files = glob.glob(path)

#Extract the track_id, artist and title from the JSON file
for name in files:
    with open(name) as f:
        data = f.read()
        jsondata=json.loads(data)
        print (jsondata['track_id'] + ' - ' + jsondata['artist'] + ' - ' + jsondata['title'])
