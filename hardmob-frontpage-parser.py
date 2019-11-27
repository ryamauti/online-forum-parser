import requests
from bs4 import BeautifulSoup

rooturl = 'https://www.hardmob.com.br/'
pageurl = 'forums/407-Promocoes'

req = requests.get(rooturl+pageurl)
content = req.content
soup = BeautifulSoup(content, 'html.parser')
h3 = soup.find_all(name='h3')
dd = soup.find_all(name='dd')

ddtime = list()
for d in dd:
    if 'span class="time"' in str(d):
        ddtime.append(d)

infopagina = dict()
regs = len(ddtime)

for ids in range(regs):
    registro = dict()
    header = str(h3[ids].a)
    hrefini = header.find('href') + 6
    hreffim = header.find('?')
    titlini = header.find('>') + 1
    titlfim = header.find('</a>')
    link = header[hrefini:hreffim]
    titulo = header[titlini:titlfim]

    ddtext = str(ddtime[ids])
    diaini = ddtext.find('<dd>') + 4
    diafim = ddtext.find('<span') - 2
    horaini = ddtext.find('time') + 6
    horafim = ddtext.find('</span>')
    dia = ddtext[diaini:diafim]
    hora = ddtext[horaini:horafim]

    registro['id'] = ids
    registro['data'] = dia
    registro['hora'] = hora
    registro['titulo'] = titulo
    registro['link'] = url+link
        
    infopagina[ids] = registro
    
#return infopagina
