import requests
import redis

url = "https://restcountries.com/v3.1/all"

# Specify the number of records you want (in this case, 20)
query_params = {"limit": 20}

response = requests.get(url, params=query_params)

if response.status_code == 200:
    data = response.json()

    # Connect to Redis
    redis_host = "redis-13958.c267.us-east-1-4.ec2.cloud.redislabs.com"
    redis_port = 13958
    redis_db = 0
    redis_password = "xuutN7Z1k1V5GzfHq4Q9VWUJSLFAYFeG"
    redis_client = redis.StrictRedis(
        host=redis_host,
        port=redis_port,
        db=redis_db,
        password=redis_password
    )

    # Insert each country's data into Redis
    for index, country in enumerate(data):
        key = f"country:{index + 1}"  # Use a meaningful key for each country
        value = country
        redis_client.set(key, str(value))  # Convert to string before storing

    print("Data inserted into Redis successfully.")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
