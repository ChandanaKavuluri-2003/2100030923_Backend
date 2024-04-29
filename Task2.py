import mysql.connector
#db connection
try:
    connct = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="safertek1"
    )
    currnt = connct.cursor()
    countryname = input("Enter Country name to find: ")
    #queries
    currnt.execute('''SELECT country_id
                   FROM countries
                   WHERE country_name = %s''', (countryname,))
    cid = currnt.fetchone()
    if not cid:
        print("Country not found.")
    else:
        countryid = cid[0]
        currnt.execute('''SELECT location_id, street_address, city, state_province
                       FROM locations
                       WHERE country_id = %s''', (countryid,))
        rows = currnt.fetchall()
        for c in rows:
            print("Country:", countryname)
            print("Location ID:", c[0])
            print("Street Address:", c[1])
            print("City:", c[2])
            print("State/Province:", c[3])
            print()
#mysql error
except mysql.connector.Error as e:
    print("MySQL Error:", e)
#closing connection
finally:
    if 'currnt' in locals() and currnt is not None:
        currnt.close()
    if 'connct' in locals() and connct is not None:
        connct.close()
