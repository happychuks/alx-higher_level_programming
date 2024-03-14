# Python ORM with MySQL using SQLAlchemy

This repository contains a simple example of using SQLAlchemy as an Object-Relational Mapping (ORM) tool in Python to interact with a MySQL database.

## Installation

1. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
2. Install SQLAlchemy using pip: ```pip install sqlalchemy```
3. Install MySQL connector for Python: ```pip install mysql-connector-python```


## Configuration

1. Make sure you have a MySQL server installed and running. If not, you can download and install it from [MySQL Downloads](https://dev.mysql.com/downloads/).
2. Create a MySQL database for your application.
3. Update the database connection URI in the `config.py` file with your MySQL server details.

## Usage

1. Define your database models by creating Python classes that inherit from `Base` class provided by SQLAlchemy.
2. Use SQLAlchemy's session management to interact with the database. Here's a basic example:

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from your_models_module import Base, YourModelClass

# Create a MySQL database engine
engine = create_engine('mysql+mysqlconnector://username:password@localhost/database_name')

# Create a session maker
Session = sessionmaker(bind=engine)

# Create a session
session = Session()

# Example usage: Inserting data into the database
new_entry = YourModelClass(attribute1=value1, attribute2=value2)
session.add(new_entry)
session.commit()

# Example usage: Querying data from the database
result = session.query(YourModelClass).filter_by(attribute1=value1).all()


## To run this project
1. Ensure mysql server is installed using: ```sudo apt install mysql-server```
2. Test the installation using: ```sudo mysql``` It should open a shell for mysql; then exit with ```quit``` command
3. Start the mysql service using: ```service mysql start``` 
4. Run your scripts: E.g: ```cat 0-select_states.sql | mysql -uroot -p``` and ```./0-select_states.py root root hbtn_0e_0_usa```
5. This will display your query result.

Happy Coding!

