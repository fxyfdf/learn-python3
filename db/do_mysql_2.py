import mysql.connector

# mysql1.py
config = {
    'host': '192.168.20.238',
    'user': 'inceptoruser',
    'password': 'password',
    'port': 3316,
    'database': 'metastore_inceptor1',
    'charset': 'utf8'
}
try:
    cnn = mysql.connector.connect(**config)
except mysql.connector.Error as e:
    print('connect fails!{}'.format(e))
cursor = cnn.cursor()
cursor.execute('show tables;')
print (cursor)
for i in cursor:
    print (i)
'''
try:
    sql_query = 'select name,age from stu ;'
    cursor.execute(sql_query)
    for name, age in cursor:
        print (name, age)
except mysql.connector.Error as e:
    print('query error!{}'.format(e))
finally:
    cursor.close()
    cnn.close()
'''