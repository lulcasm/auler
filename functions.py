import json
import pip

def install(package):
    if hasattr(pip, 'main'):
        pip.main(['install', package])
    else:
        pip._internal.main(['install', package])

def updateJson(filename, dict_data):
	with open(filename, 'r') as json_data: 
		data = json.load(json_data)

	data.extend(dict_data)

	with open(filename, 'w') as json_data: 
		json.dump(data, json_data)


# Example
if __name__ == '__main__':
    install('bs4')
    install('requests')
    install('lxml')