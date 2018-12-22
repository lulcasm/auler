import functions
from bs4 import BeautifulSoup
import json

# script para cavar aulas do Sala do Saber

idStart = 243225098 #243248604 > progressiva # último id em 21/12/2018

for i in range(idStart, 0, -1):
	
		#inicio = time.time()
	
		url = 'http://player.vimeo.com/video/{}'.format(i)
	
		acessar = requests.get(url).content
		getCode = BeautifulSoup(acessar, 'lxml')

		p = getCode.find('p')
		p = str(p).replace('p', '').replace('<', '').replace('>', '').replace('/', '')

		#print(p)
	
		titulo = getCode.find('title')
		titulo = str(titulo).replace('title', '').replace('<', '').replace('>', '').replace('/', '')

		if titulo == 'Sorry' or titulo == 'Desculpe':

			if p == 'This video does not exist.' or p == 'Este vídeo não existe.':
				print('#{} - não existe'.format(i))

			else:

				print('#{} - vídeo privado'.format(i))

				updateJson('192.168.1.34/aulas.json', [{'id':i}])

		else:
			print('#{} - vídeo publico'.format(i))

		#print(titulo)