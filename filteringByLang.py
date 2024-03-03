import requests

def get_countries_by_language(language_code):
    url = f"https://restcountries.com/v3.1/lang/{language_code}"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
        return None

# Specify the language code (e.g., "eng" for English)
language_code = "eng"

# Fetch countries based on language
result = get_countries_by_language(language_code)

if result:
    # Print the data for each country
    for index, country in enumerate(result):
        print(f"Country {index + 1}: {country}")
else:
    print("No data fetched.")
