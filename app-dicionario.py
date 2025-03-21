import pandas as pd

guias = []
guia = {}

guia["senha"] = "123"
guia["pac"] = "alex"

guias.append(guia)

guia = {}
guia["senha"] = "456"
guia["pac"] = "lillian"

guias.append(guia)

print(f'tamanho: {len(guias)}')

print(f'tamanho: {guias}')