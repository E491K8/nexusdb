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

# Example usage:
db = JSONDatabase('my_database')
db.create_collection('my_collection')
db.insert_document('my_collection', {'name': 'John Doe', 'age': 25})
db.find_documents('my_collection', {'age': 25})
db.remove_document('my_collection', 'document_id')
db.create_user('John Doe', 'john@example.com', 'password123', 'admin')
db.remove_user('user_id')
db.block_user('user_id')
db.revoke_user('user_id')
db.update_document('my_collection', 'document_id', {'name': 'Jane Doe'})
db.get_all_documents('my_collection')
db.count_documents('my_collection')
db.drop_collection('my_collection')
db.drop_database()
db.import_database('path_to_database.zip')
db.import_collection('my_collection', 'path_to_collection.zip')
db.export_database('exported_database.zip')
db.export_collection('my_collection', 'exported_collection.zip')

