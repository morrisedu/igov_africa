import requests

def get_discontinued(year):
    url = "https://vpic.nhtsa.dot.gov/api/vehicles/getmodelsformakeyear/make/honda/modelyear/" + year + "?format=json"

    data = requests.get(url)

    return data.json()