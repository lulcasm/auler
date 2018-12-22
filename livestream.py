# -*- coding: utf-8 -*-

import requests
from bs4 import BeautifulSoup
import json
import time
#from win10toast import ToastNotifier

#toaster = ToastNotifier()
 
#PLANO BIXO
 
bixoStart = 8074638 # onde parou no dia 19/12/2018
bixoServer = 22625780
 
#PLANO ENEM
 
#enemStart = 8082190
enemStart = 8473268 # onde parou no dia 17/12/2018
enemServer = 807385
 
#MONITORIAS >>>>> acredito que não vale a pena garimpar, as monitorias aparentemente são deletadas
monitoriaStart = 6993776 # onde parou no dia 19/12/2018
monitoriaServer = 22625789

# PERGUNTAR

qualServidor = int(input('Em qual servidor você quer trabalhar agora? [1: ENEM, 2: BIXO, 3: MONITORIA] '))
qualStart = int(input('A partir de onde? '))
 
### MUDAR QUANDO NECESSÁRIO:
start = qualStart
if qualServidor == 1:
    server = enemServer
elif qualServidor == 2:
    server = bixoServer
else:
    server = monitoriaServer

if server == enemServer:
    arquivo = 'aulas-descomplica.json'
    s = 'ENEM'
elif server == bixoServer:
    arquivo = 'aulas-bixosp.json'
    s = 'BixoSP'
elif server == monitoriaServer:
    arquivo = 'aulas-monitoria.json'
    s = 'Monitorias'

print("************************ SERVIDOR: {} ************************".format(s))

try:
 
    for i in range(start, 9999999):
     
        inicio = time.time()
     
        url = 'https://livestream.com/accounts/{}/events/{}/player'.format(server, i)
     
        acessar = requests.get(url).content
        getCode = BeautifulSoup(acessar, 'lxml')
        code = getCode.find("h1")
     
        print(i)
     
        if code == None:
     
            titulo = getCode.find('title')
     
            aula = {'id':i, 'url':url, 'titulo':titulo.text}
     
            with open(arquivo, 'a') as file:
                dumps = json.dumps(aula)
                file.write(dumps+', \n')
     
            print('{} >>> {}'.format(url, titulo.text))
     
        final = time.time()
     
        resultado = final-inicio
        print('({})'.format(resultado))

        #toaster.show_toast("Auler", "Fez request.")

except KeyboardInterrupt:
    print("Script encerrado.")

except:
    """toaster.show_toast('Auler', 'Algo deu errado :/')"""
    print('Ooh, oh :/')
    raise