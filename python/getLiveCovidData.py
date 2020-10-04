# importing the package covid
# can be installed with pip install covid

from covid import Covid
from tabulate import tabulate

covid= Covid()
print('\n COVID-19 stats in India\n')
# setting a country, here India
country = covid.get_status_by_country_name("india")
table=[]
for i in country:
    if i!="id":
        table.append([i.upper()+"            ",":   "+str(country.get(i))])
print((tabulate(table,tablefmt="plain", colalign=("left",))))
print('\n')