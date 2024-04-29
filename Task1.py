import mysql.connector
#db connection
try:
    connct = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="safertek1"
    )
    #queries
    curnt = connct.cursor()
    curnt.execute('''CREATE TABLE IF NOT EXISTS locations (
                    location_id INT AUTO_INCREMENT PRIMARY KEY,
                    street_address VARCHAR(255),
                    city VARCHAR(255),
                    state_province VARCHAR(255),
                    country_id VARCHAR(2)
                )''')
    curnt.execute('''CREATE TABLE IF NOT EXISTS countries (
                    country_id VARCHAR(2) PRIMARY KEY,
                    country_name VARCHAR(255),
                    region_id VARCHAR(255)
                )''')
    print("Enter Location table data:")
    print()
    staddress = input("Enter street address: ")
    city = input("Enter city: ")
    stprovince = input("Enter state/province: ")
    countryid = input("Enter country code: ")
    print()
    sql = "INSERT INTO locations (street_address, city, state_province, country_id) VALUES (%s, %s, %s, %s)"
    values = (staddress, city, stprovince, countryid)
    curnt.execute(sql, values)
    print("Enter Countries table data:")
    print()
    countryid = input("Enter country ID:")
    countryname = input("Enter country Name:")
    regid  = input("Enter region id:")
    sql = "INSERT INTO countries (country_id, country_name,region_id) VALUES (%s, %s, %s)"
    val = (countryid, countryname, regid)
    curnt.execute(sql, val)
    connct.commit()
    #printing message
    print("Data inserted successfully!")
    print()
    #join condition
    print("==============================================Join Operation======================================================")
    countryname = input("Enter country name to apply join condition on that country name: ")
    curnt.execute('''SELECT l.location_id, l.street_address, l.city, l.state_province, c.country_name, c.country_id
                   FROM locations l
                   JOIN countries c ON l.country_id = c.country_id
                   WHERE c.country_name = %s ''', (countryname,))
    rows = curnt.fetchall()
    for c in rows:
        print(c)
except mysql.connector.Error as errc:
    print("MySQL Error:", errc)
    #closing connection
finally:
    if 'cur' in locals() and curnt is not None:
        curnt.close()
    if 'conn' in locals() and connct is not None:
        connct.close()
