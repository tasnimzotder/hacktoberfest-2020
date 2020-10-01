# importing the package covid
# can be installed with pip install covid

from covid import Covid
covid= Covid()

# setting a country, here India
india = covid.get_status_by_country_name("india")
print(india)