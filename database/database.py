import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect(
    host="localhost", database="api_users_social", user="postgres", password="shitkat'"
)

conn.close()
