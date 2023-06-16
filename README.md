# nexusdb

nexusdb is a Python library that provides a simple and lightweight JSON-based database for storing and querying data. It aims to offer an easy-to-use interface while maintaining flexibility and performance.

## Features

- Create and manage databases
- Create and manage tables within databases
- Insert, update, and delete records
- Query records using various conditions
- Perform aggregations
- Create and manage indexes
- Backup and restore databases
- Handle transactions

## Installation

You can install nexusdb using pip:

```shell
pip install nexusdb

```
## Usage

Here's a simple example that demonstrates how to use CrypsDB:

```python

from nexusdb import JSONDatabase

# Initialize the JSONDatabase object
db = JSONDatabase(database_dir="/path/to/database/directory/")

# Create a new database
db.create_database("my_database")

# Create a new table in the database
db.create_table("my_database", "my_table")

# Insert a record into the table
record = {"id": "1", "name": "John Doe", "age": 25}
db.insert_record("my_database", "my_table", record)

# Retrieve a record from the table
retrieved_record = db.get_record("my_database", "my_table", "1")
print(retrieved_record)

# Update a record in the table
updated_fields = {"age": 26}
db.update_record("my_database", "my_table", "1", updated_fields)

# Delete a record from the table
db.delete_record("my_database", "my_table", "1")

# Remove the table from the database
db.remove_table("my_database", "my_table")

# Remove the database
db.remove_database("my_database")

