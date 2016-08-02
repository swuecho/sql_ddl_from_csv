sqlite> .mode csv
sqlite> .import ./data/somedata.csv tab1

sqlite3 ex1 --init db.sql
-- Loading resources from db.sql

SQLite version 3.8.2 2013-12-06 14:53:30
Enter ".help" for instructions
Enter SQL statements terminated with a ";"
sqlite> .mode csv
sqlite> .import data/Demographic_Statistics_By_Zip_Code.csv Demographic_Statistics_By_Zip_Code
sqlite> 

