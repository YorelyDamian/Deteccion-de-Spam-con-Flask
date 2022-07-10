import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(
    'D:\\Yorely\Windows\\Octavo Semestre\\Zamora\\Inteligencia Artificial\\proyecto_Spam\\src\\ArchivosCSV\\normal.csv', delimiter=',')
data.head()

y = data['classN']
z = data['classA']


sumy = sum(y)
sumz = sum(z)

can = 125973
por = 1000


divy = sumy / can * 100
divz = sumz / can * 100


print('classN:', sumy)
print('classA:', sumz)

porcentajes = [divy, divz]
nombres = ["Spam", "Normal"]
plt.pie(porcentajes, labels=nombres)

plt.show()
