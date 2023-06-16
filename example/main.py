from nexusdb import JSONDatabase

# Initialize the JSONDatabase object
db = JSONDatabase(database_dir="/path/to/database/directory/")

# Create a new database
db.create_database("my_database")

# Create a new table in the database
db.create_table("my_database", "my_table")

# Insert records into the table
record1 = {"id": "1", "name": "John Doe", "age": 25}
record2 = {"id": "2", "name": "Jane Smith", "age": 30}
record3 = {"id": "3", "name": "Bob Johnson", "age": 35}

db.insert_record("my_database", "my_table", record1)
db.insert_record("my_database", "my_table", record2)
db.insert_record("my_database", "my_table", record3)

# Retrieve all records from the table
all_records = db.get_all_records("my_database", "my_table")
print("All Records:")
for record in all_records:
    print(record)

# Update a record in the table
updated_fields = {"age": 26}
db.update_record("my_database", "my_table", "1", updated_fields)

# Retrieve a specific record from the table
retrieved_record = db.get_record("my_database", "my_table", "1")
print("Retrieved Record:")
print(retrieved_record)

# Delete a record from the table
db.delete_record("my_database", "my_table", "2")

# Retrieve all records after deletion
all_records = db.get_all_records("my_database", "my_table")
print("All Records after Deletion:")
for record in all_records:
    print(record)

# Remove the table from the database
db.remove_table("my_database", "my_table")

# Remove the database
db.remove_database("my_database")
