import psycopg2

# Connect to your postgres DB
try:
    conn = psycopg2.connect(
        host="localhost", database="api_users_social", user="postgres", password=""
    )

except (Exception, psycopg2.Error) as error:
    print("Error while fetching data from PostgreSQL", error)
