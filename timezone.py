import clickhouse_connect

#create a connection with the clickhouse server
client = clickhouse_connect.get_client(host='localhost', port=8123, user='default', password='', database='ezworks')


#creating a table in clickhouse and integrationg it with an existing mysql server 
client.command("CREATE TABLE time_zone (abbreviation String,zone_name String,time_start String)ENGINE = MySQL('localhost','db_name','zone_time','username','Password')")

print("Table created successfully!")

#insert data into the clickhouse table. It will also reflect in mysql table.
client.command("INSERT INTO ezworks.time_zone (abbreviation, zone_name, time_start) VALUES ('KER', 'Kerala', '+5.30');")
print("Data added successfully!")

#printing the data i click house table
data = client.command('SELECT * FROM time_zone')
print("data >> ", data)