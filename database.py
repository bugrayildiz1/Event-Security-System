import psycopg2

conn = psycopg2.connect(
    database = "postgres",
    user="postgres",
    password="Keyboard25",
    host="130.89.229.53",
    port= "5432"

)

print("connected to postgreSQL DB")