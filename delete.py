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

# Specify the country name to delete
country_to_delete = "Iraq"

# Iterate through stored keys to find a match
for key in redis_client.keys("country:*"):
    # Convert the data from string to dictionary
    country_data = eval(redis_client.get(key).decode("utf-8"))

    # Check if the country name matches the one to delete
    if country_data.get("name", {}).get("common") == country_to_delete:
        # Delete the record
        redis_client.delete(key)
        print(f"Record for {country_to_delete} deleted.")
        break  # Stop searching once a match is found

else:
    print(f"Record for {country_to_delete} not found in Redis.")
