import pandas as pd
import xml.etree.ElementTree as et
from lxml import etree


tree = et.parse('Lote_49399.xml')
raiz = tree.getroot()
""""
print("--------------------")
print(f'raiz: {len(raiz)}')
print(f'raiz filha: {len(raiz[1][0][1])}')
print(raiz[1][0][1].tag)
print("--------------------")
"""
guiasTISS = raiz[1][0][1]

#Remover prefixo no nome da tag
for elem in raiz.iter():
    elem.tag = elem.tag[elem.tag.index('}')+1:]

def lerDados(campos, guia):
    lista = []
    for campo in campos:
        if(len(campo) == 0):
            guia[str(campo.tag)] = str(campo.text)
            print(guia[str(campo.tag)])
            #print(campo.tag, campo.text, len(campo))
        if(len(campo) > 0):
            lerDados(campo, guia)

    return guia

def lerGuias(campos):
    lista = []
    
    for campo in campos:
        guia = {}
        print(campo.tag, campo.text, len(campo))
        if(len(campo) == 0):
            #guia[str(campo.tag)] = str(campo.text)
            print(campo.tag, campo.text, len(campo))
        if(len(campo) > 0):
            guia = lerDados(campo, guia)

        list.append(guia)


#lerDados(guiasTISS)
lerGuias(guiasTISS)
"""guias = lerGuias(guiasTISS)

print('--------GUIA-------')
print(f'Qnt Guias: {len(guias)}')
"""



"""
data = []
df = pd.DataFrame(data)

df.to_csv('xml.csv', index=False, sep=';')
print(df)"""