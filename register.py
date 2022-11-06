import psycopg2
import datetime
hostname = 'localhost'
database = 'Financials_App'
pwd = 'welcome'
username = 'postgres'
port_id = 5432
conn = None
curr = None

# We create a user class that will hold our user information


class User():
    def __init__(self, first_name, second_name, username, password, email, creation_date):
        self.first_name = first_name
        self.second_name = second_name
        self.username = username
        self.password = password
        self.email = email
        self.creation_date = creation_date


# for testing purposes, we create a user
user1 = User('Josh', 'Smith', "Josh.Smith", "spacecow12345",
             "josh.smith@gmail.com", datetime.datetime.now())

# we  define a finction that takes a user object, connects to the local database and passes information from the python script into the database

# we define a finction that connects to the database, opens a cursor,
# passes information from our user object into the database, and then closes the cursor and the database connection


def register_user(current_user):
    try:
        # connecting to the database
        conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id
        )
        # Activating the cursor
        curr = conn.cursor()
        # insert_script = a template that we will use to insert information into the database
        insert_script = 'INSERT INTO user_login_information ( first_name,second_name,username,password,email,creation_date) VALUES (%s,%s,%s,%s,%s,%s)'

        # insert_value = the values that we will use in our insert_script
        insert_value = (current_user.first_name, current_user.second_name, current_user.username,
                        current_user.password, current_user.email, current_user.creation_date)

        # curr.execute to execute the modifications to the database
        curr.execute(insert_script, insert_value)

        # conn.commit() to apply the changes we just made to the database
        conn.commit()
    except Exception as error:
        print(error)

    finally:
        # we close cursor
        if curr is not None:
            curr.close()

        # we close the database connection
        if conn is not None:
            conn.close()


# we test our function
register_user(user1)
