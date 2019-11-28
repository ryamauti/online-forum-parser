import requests

rooturl = 'https://www.hardmob.com.br/'
pageurl = 'forums/407-Promocoes'

req = requests.get(rooturl+pageurl)

def soup_find_all(reqtxt, busca):
    inicios = list()
    z = 1
    while z > 0:
        z = reqtxt.find(busca, z + 10)        
        inicios.append(z)
    return inicios

h3index = soup_find_all(req.text, '<h3 class="threadtitle">')
h3 = list()
for h in range(len(h3index)-1):
    h3.append(req.text[h3index[h]:h3index[h+1]])

ddindex = soup_find_all(req.text, '<span class="time">')
ddtime = list()
for d in range(len(ddindex)-1):
    ddtime.append(req.text[ddindex[d]-20:ddindex[d+1]])

infopagina2 = dict()
regs = len(h3)

for ids in range(regs):
    registro = dict()
    header = h3[ids]
    hrefini = header.find('href') + 6
    hreffim = header.find('?')
    titlini = header[hreffim:].find('>') + 1 + hreffim
    titlfim = header[titlini:].find('</a>') + titlini
    link = header[hrefini:hreffim]
    titulo = header[titlini:titlfim]

    ddtext = ddtime[ids]
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
    registro['link'] = rooturl+link
        
    infopagina2[ids] = registro
    
import json
jd = json.dumps(infopagina2, indent=4)

print(jd)
