import pandas as pd
import xml.etree.ElementTree as et
from lxml import etree

tree = et.parse('Lote_49399.xml')
raiz = tree.getroot()

guiasTISS = raiz[1][0][1]
listaGuias = []
guia = {}

#Remover prefixo no nome da tag
for elem in raiz.iter():
    elem.tag = elem.tag[elem.tag.index('}')+1:]

#ler campos de cada guia
def lerDados(campos, guia):
    for campo in campos:
        if(len(campo) == 0):
            guia[str(campo.tag)] = str(campo.text)
            #print(campo.tag, campo.text)
        if(len(campo) > 0):
            lerDados(campo, guia)

#ler nivem das guias, criar guias vazias
def lerGuias(campos):
    for campo in campos:
        guia = {}

        lerDados(campo, guia)

        listaGuias.append(guia)

lerGuias(guiasTISS)

df = pd.DataFrame(listaGuias)

#df.to_csv('xml.csv', index=False, sep=';')
print(df)

print(listaGuias[0])