# criado em 21/12/2018

import requests
from bs4 import BeautifulSoup
import json
#from win10toast import ToastNotifier
from functions import updateJson
import urllib.request

#idStart inicial: 243000000
idStart = 243002593 # onde parou em 21/12/2018
idEnd = 243900000

try:

	url = input('URL do arquivo: ')
	arquivoComIds = urllib.request.urlopen(url)
	ler = arquivoComIds.read().decode('utf-8')
	l = ler.splitlines(True)

	for linha in l:

		linha = linha.rstrip()

		url = 'https://player.vimeo.com/video/{}'.format(linha)
		r = requests.get(url, headers={'referer':'https://saladosaber.com.br'})
		status = r.status_code

		print('{} > {}'.format(linha, r.status_code))

		if status == '200' or status == 200:
			updateJson('aulas-ss.json', [{'id':linha, 'url':url}])
			print('{} > {}'.format(linha, url))

	"""for i in range(idStart, idEnd):

		url = 'https://player.vimeo.com/video/{}'.format(i)

		request = requests.get(url, headers={'referer':'https://saladosaber.com.br'}).content

		code = BeautifulSoup(request, 'lxml')
		titulo = code.find('title')
		titulo = str(titulo).replace('title', '').replace('<', '').replace('>', '').replace('/', '')
		p = code.find('p')
		p = str(p).replace('p', '').replace('<', '').replace('>', '').replace('/', '')

		keywords = ['sala', 'saber', 'Sala', 'Saber']

		if any(word in titulo for word in keywords): # nem todos os vídeos captados serão da sala do saber
			with open('aula-sala-do-saber.txt', 'a') as aulas:
				aulas.write('{} - {}\n'.format(url, titulo))
			print('{} > vídeo Sala do Saber'.format(i))

		else:
			if titulo == 'Sorry' or titulo == 'Desculpe':

				if p == 'This video does not exist.' or p == 'Este vídeo não existe.':
					print('{} > não existe'.format(i))

				else:
					print('{} > vídeo privado'.format(i))
					with open('private-videos.json', 'a') as arq:
						arq.write(json.dumps({'id':i})+', \n')
			else:
				print('{} > vídeo público'.format(i))"""

except KeyboardInterrupt:
    print("Script encerrado.")

except:
    #toaster.show_toast('Auler: Sala do Saber', 'Algo deu errado :/')
    print('Ooh, oh :/')
    raise
