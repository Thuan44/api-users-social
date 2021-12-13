import psycopg2

# Connect to your postgres DB
conn = psycopg2.connect(
    host="localhost", database="api_users_social", user="postgres", password=""
)

# cur = conn.cursor()

# cur.execute("SELECT * FROM users;")
# print(cur.fetchall())

# conn.commit()


# Close the connection
# conn.close()
