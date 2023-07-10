#import 'clickhouse_connect' - ClickHouse Connect is a suite of Python packages
import clickhouse_connect

#creating a connection with clickhouse server
client = clickhouse_connect.get_client(host='localhost', username='default', password='', database='school')

#creating a table in clickhouse
client.command('CREATE TABLE students (id UInt32, name String, marks Float64) ENGINE MergeTree ORDER BY id')

#insert data to the table
row1 = [101, 'Rahul Harshan', 85.233]
row2 = [102, 'Preethu', 67.04]
row3 = [103, 'Ryan R', 90.04]
data = [row1, row2, row3]
client.insert('students', data, column_names=['id', 'name', 'marks'])

#view data in terminal
result = client.query('SELECT * FROM students')
print(result.result_rows)