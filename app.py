import requests

url = "https://covid-193.p.rapidapi.com/countries"

headers = {
	"x-rapidapi-key": "89d3178d74msh6f8866195c1dbf5p15c0c7jsn524b8fc9692b",
	"x-rapidapi-host": "covid-193.p.rapidapi.com"
}

response = requests.get(url, headers=headers)

print(response.json())