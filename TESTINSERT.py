import psycopg2

try:
   connection = psycopg2.connect(user="postgres",
                                  password="Keyboard25",
                                  host="130.89.229.53",
                                  port="5432",
                                  database="postgres")
   cursor = connection.cursor()
   
   postgres_insert_query="""INSERT INTO dbo.USER_TABLE(ID,USER_FIRSTNAME,USER_LASTNAME,USER_EMAIL,USER_ADRESS,USER_BIRTHDATE) VALUES (%s,%s,%s,%s,%s,%s)"""
   record_to_insert=(1235,'Henk','Jansen','henkjansen@live.nl','Poldermolen 78,Hoorn, Nederland','1995-10-30')
   cursor.execute(postgres_insert_query,record_to_insert)
   connection.commit()
   count=cursor.rowcount
   print(count,"record inserted succesfully")
except (Exception, psycopg2.Error) as error :
    if(connection):
        print("Failed to insert record into mobile table", error)

finally:
    #closing database connection.
    if(connection):
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")
