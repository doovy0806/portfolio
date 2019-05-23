import pymysql

def createTable():
    email = '2'
    password = '1'
    db = pymysql.connect(host ='127.0.0.1', port = 3306, user = 'root',password='mr1035122')
    cursor = db.cursor()
    cursor.execute("SELECT * FROM ZOO.USER AS USER WHERE USER.Email = %s AND User.Password = %s", (email, password))

    # sql_query = "INSERT INTO zoo.USER VALUES(1,1,1)"
    # cursor.execute(sql_query)

    # db.commit()

    result = cursor.fetchall()
    print(len(result))
    # for data in result:
    #     print(data[0])
    db.close()

createTable()
