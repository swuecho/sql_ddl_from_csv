import csv
import os
filename = 'data/Demographic_Statistics_By_Zip_Code.csv'
table_name = os.path.splitext(os.path.basename(filename))[0]

with open(filename, 'r') as csvfile:
	reader = csv.reader(csvfile)
	head = reader.next()
	first_line_data = reader.next()

column_names = [ column_name.replace(' ', '_').lower() for column_name in head]

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def data_type(value_str):
	if not is_number(value_str):
		return 'text'
	elif '.' in value_str:
		return 'float'
	else:
		return 'integer'		
	
column_type  = [data_type(i) for i in first_line_data]

#CREATE TABLE table_name
#(
#   column_name  column_type,
#   [...]
#);

ddl_first_line = "CREATE TABLE {0}".format(table_name)
ddl_column_and_type = [ ' '.join([a,b]) for a,b in zip(column_names, column_type)]
ddl = ddl_first_line + "\n(\n  " + ",\n  ".join(ddl_column_and_type) + "\n);"
print(ddl)
