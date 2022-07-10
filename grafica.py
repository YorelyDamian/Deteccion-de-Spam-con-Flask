import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(
    'D:\\Yorely\Windows\\Octavo Semestre\\Zamora\\Inteligencia Artificial\\proyecto_Spam\\ArchivosCSV\\normal.csv', delimiter=',')
data.head()
w = data['id']
x = data['src_bytes']
y = data['classN']
z = data['classA']

sumw = sum(w)
sumx = sum(x)
sumy = sum(y)
sumz = sum(z)

can = 125973
por = 1000

divw = sumw / can / por
divx = sumx / can / por
divy = sumy / can * 100
divz = sumz / can * 100

print('duration:', divw)
print('src_bytes:', divx)
print('classN:', sumy)
print('classA:', sumz)

porcentajes = [divw, divx, divy, divz]
nombres = ["Duration", "src_Bytes", "Spam", "Normal"]
plt.pie(porcentajes, labels=nombres)

plt.show()
