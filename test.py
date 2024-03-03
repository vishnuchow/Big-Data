import requests

url = "https://restcountries.com/v3.1/all"

# Specify the number of records you want (in this case, 20)
query_params = {"limit": 20}

response = requests.get(url, params=query_params)

if response.status_code == 200:
    data = response.json()
    # Do something with the data (e.g., print it)
    for index, country in enumerate(data):
        print(f"Record {index + 1}: {country}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
