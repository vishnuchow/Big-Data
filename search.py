import redis

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

# Specify the country name to search for
search_country = "North Macedonia"

# Iterate through stored keys to find a match
for key in redis_client.keys("country:*"):
    # Convert the data from string to dictionary
    country_data = eval(redis_client.get(key).decode("utf-8"))

    # Check if the country name matches the search query
    if country_data.get("name", {}).get("common") == search_country:
        print(f"Data for {search_country}:")
        print(country_data)
        break  # Stop searching once a match is found

else:
    print(f"Data for {search_country} not found in Redis.")
