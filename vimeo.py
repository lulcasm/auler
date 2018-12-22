# -*- coding: utf-8 -*-

from functions import updateJson
from bs4 import BeautifulSoup
import json
import requests

# script para cavar aulas do Sala do Saber

idStart = int(input('Coloque o ID: '))#243194357 #243248604 > progressiva # último id em 21/12/2018
tipo = int(input('Progressivo (1) ou decressivo (2)? '))

if tipo == 1:
	tip = range(idStart, 400000000)
else:
	tip = range(idStart, 0, -1)

for i in tip:
	
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

				updateJson('aulas.json', [{'id':i}])

		else:
			print('#{} - vídeo publico'.format(i))

		#print(titulo)
