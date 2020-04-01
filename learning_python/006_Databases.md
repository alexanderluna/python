# Databases

Before working with databases in python we have to install the database we want
to use. Python comes with the **DB-API** which allows us to interact with any
database. However, we need to install the respective drivers for the database
we want to use.

Once we have downloaded the driver we need, we can install it.

```python
python3 setup.py install
```

Now that everything is installed we can go ahead and create our database and
table through the terminal. We can use python to connect programmatically to
our newly created database. For that, we create a database configuration
object that holds all the information needed to connect to our database and
import the database connector.

```python
import mysql.connector

db_config = {
  'host': '127.0.0.1',
  'user': 'our_database_user',
  'password': 'our_database_password',
  'database': 'our_database_name',
}

connection = mysql.connector.connect(**db_config)
cursor = connection.cursor()
```

The cursor allows us to send sql commands to the database and receive responses
back. We can write our first SQL command now.

```python
_sql = """show tables"""
cursor.execute(_sql)
response = cursor.fetchall()
```

To receive a response we can use three different methods on the cursor.

- fetchone: get only the first row
- fetchmany: specify how many rows to get
- fetchall: get all rows

Finally, once we are done we have to close the connection.

```python
cursor.close()
connection.close()
```

> When executing an SQL command that makes changes make sure to commit your
> changes with the connection.commit() method.
