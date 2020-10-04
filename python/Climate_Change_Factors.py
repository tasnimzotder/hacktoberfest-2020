import requests
from bs4 import BeautifulSoup
from tabulate import tabulate


def Table(header,rankList):
    return tabulate(rankList, headers=header, tablefmt='grid')


urls=["https://www.worldometers.info/world-population/population-by-country/","https://www.ucsusa.org/resources/each-countrys-share-co2-emissions","https://www.nationmaster.com/country-info/stats/Environment/CFC/Consumption"]


url = urls[0]
source2 = requests.get(url)
soup = BeautifulSoup(source2.content, "html.parser")
top10=[]
for i in range(1,11,1):
    rank=str(i)+"."
    country=(soup.select_one("tbody > tr:nth-child({}) > td:nth-child(2)".format(i))).text
    cur_ppl=(soup.select_one("tbody > tr:nth-child({}) > td:nth-child(3)".format(i))).text
    percentage=(soup.select_one("tbody > tr:nth-child({}) > td:nth-child(12)".format(i))).text
    top10.append([rank,country,cur_ppl,percentage])
print('''\n\n  Top 10 populated countries''')
header=['Rank','Country','Population','World share']
print(Table(header,top10))


url = urls[1]
source = requests.get(url)
soup = BeautifulSoup(source.content, "html.parser")
top10=[]
for i in range(1,11,1):
    rank=str(i)+"."
    country=(soup.select_one("tr:nth-child({}) > td:nth-child(2)".format(i))).text
    emmission=(soup.select_one("tr:nth-child({}) > td:nth-child(3)".format(i))).text
    top10.append([rank,country,emmission])
lastUpdate=soup.select_one("span.date-updated").text
print('\n\n  Top 10 most CO2 emitting countries  ({})'.format(lastUpdate))
header=['Rank','Country','CO2 emissions']
print(Table(header,top10))


url = urls[2]
source = requests.get(url)
soup = BeautifulSoup(source.content, "html.parser")
top10=[]
for i in range(1,11,1):
    rank=str(i)+"."
    country=(soup.select_one(" tr:nth-child({}) > td:nth-child(2) > a > span.full".format(i))).text
    consumption=(soup.select_one("tr:nth-child({}) > td.amount".format(i))).text
    top10.append([rank,country,consumption])
print('\n\n  Top 10 most CFC consuming countries')
header=['Rank','Country','CFC consumption\n(in ODP tons)']
print(Table(header,top10))


top10=[[1,"China",59.80],[2,"United States",37.83],[3,"Germany",14.48],[4,"Brazil",11.85],[5,"Japan",7.99],[6,"Pakistan",6.41],[7,"Nigeria",5.96],[8,"Russia",5.84],[9,"Turkey",5.6],[10,"Egypt",5.46]]
print('\n\n  Top 10 plastic waste producing countries')
header=['Rank','Country','Plastic waste generation\n(million tonnes per year)']
print(Table(header,top10))
