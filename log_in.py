import psycopg2
import numpy as np
import pandas as pd
from register import User
email_input = "John.Johnson@gmail.com"
password_input = "spaceco8264"

# we define a function that checks if the email-password combination inputed exists in the database


def check_credentials(login_email, login_password):
    hostname = 'localhost'
    database = 'Financials_App'
    pwd = 'welcome'
    username = 'postgres'
    port_id = 5432
    conn = None
    curr = None
    try:
        # connecting to the database
        conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id
        )
        # creating the cursor
        curr = conn.cursor()
        # checking if there are entries in the database for the email/password combination we want to test
        curr.execute(
            f"SELECT * FROM user_login_information WHERE email='{login_email}' AND password='{login_password}'")
        # fetching all the results given by the query
        all_users = curr.fetchall()
        # turning results into a pandas dataframe to work more easily with them
        users_table = pd.DataFrame(data=all_users,
                                   columns=["user_id", "first_name", "second_name", "username", "password", "email", "creation_date"])
        users_table.set_index(['user_id'])
        # if the email/password combination exists in the dataframe, the function will return True, if it doesn't, it will return false
        # this is determined by using the len() function on the dataframe resulted from the query present in the cursor
        if len(users_table) == 1:
            return True
        else:
            return False
    except Exception as error:
        print(error)
    finally:
        # close the cursor
        if curr is not None:
            curr.close()
    # close the database connection
        if conn is not None:
            conn.close()

# we define a function that returns the user's data if the password/email combination entered is correct


def get_user_data(login_email, login_password):
    hostname = 'localhost'
    database = 'Financials_App'
    pwd = 'welcome'
    username = 'postgres'
    port_id = 5432
    conn = None
    curr = None
    try:
        # connecting to the database
        conn = psycopg2.connect(
            host=hostname,
            dbname=database,
            user=username,
            password=pwd,
            port=port_id
        )
        # opening the cursor
        curr = conn.cursor()
        # running check_credentials for the selecte email address an password
        if check_credentials(login_email, login_password) == True:
            curr.execute(
                f"SELECT * FROM user_login_information WHERE email='{login_email}' AND password='{login_password}'")
            all_users = curr.fetchall()
            users_table = pd.DataFrame(data=all_users,
                                       columns=["user_id", "first_name", "second_name", "username", "password", "email", "creation_date"])
            users_table.set_index(['user_id'])
            # creating a current_user object and importing the data from database where email/password combination matches
            current_user = User(users_table['first_name'].iloc[0],
                                users_table['second_name'].iloc[0],
                                users_table['username'].iloc[0],
                                users_table['password'].iloc[0],
                                users_table['email'].iloc[0],
                                users_table['creation_date'].iloc[0])
            print(current_user.first_name)
        else:
            print("user not found")
    except Exception as error:
        print(error)
    finally:
        # closing he cursor
        if curr is not None:
            curr.close()
    # closing database connection
        if conn is not None:
            conn.close()


get_user_data(email_input, password_input)
