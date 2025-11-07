import requests, csv

url = 'https://www.minorplanetcenter.net/iau/MPCORB/CometData.csv'
r = requests.get(url)
with open('data/cometas.csv','wb') as f:
    f.write(r.content)
print('Atualização concluída!')
