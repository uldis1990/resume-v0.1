#Python 3.10.8
import mysql.connector
#from datetime import datetime
# create a connection to the database with SSL/TLS encryption



# data modification function
def create_dict_with_numeric_keys(values_tuple):
    dict_with_numeric_keys = {}
    for index, value in enumerate(values_tuple):
        dict_with_numeric_keys[index] = value
    return dict_with_numeric_keys
  
def convert_tuple_to_dict(tuples_list):
    result_list = []
    for tuple_item in tuples_list:
        dict_item = {}
        for index in range(len(tuple_item)):
            dict_item[index] = tuple_item[index]
        result_list.append(dict_item)
    return result_list
  
# create a cursor object on login or true token for executing queries  
cursor = cnx.cursor()
  
"""Function prototype >> execude(query, (tuple_values))
  to execute query as strings values implement (0),(1),(2)...
  returns list of dic with numeric keys"""
# formats DATE type to specific or defalt =
# format datetime.datetime(2023, 5, 10, 22, 48, 53)  
def execute(query,tuple_values):
    d = create_dict_with_numeric_keys((tuple_values))
    input_string = query
    output_string = ''
    for i in range(len(d)):
      output_string = input_string.replace('(i)', (d.get('i')))
    
    cursor.execute(output_string)
    results = cursor.fetchall()
    return convert_tuple_to_dict(results)


#s='users'
# execute a query
#query = f'SELECT * FROM {s}'
# define a variable to hold the table name
#table_name = 'mytable'

# build a dynamic query with string concatenation
#query = 'SELECT * FROM ' + table_name

query = 'SELECT * FROM users'
cursor.execute(query)

# fetch the results and print them
results = cursor.fetchall()
for row in cursor:
  print(row)
#returns list of tuples 
# close the cursor and connection
cursor.close()
cnx.close()
