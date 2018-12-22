import json

def updateJson(filename, dict_data):
	with open(filename, 'r') as json_data: 
		data = json.load(json_data)

	data.extend(dict_data)

	with open(filename, 'w') as json_data: 
		json.dump(data, json_data)