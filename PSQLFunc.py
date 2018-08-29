import psycopg2
from config import config


def create_tables():
    '''Creates base data table for survey'''

    command = (
        """
            CREATE TABLE dataset (
            user_id SERIAL PRIMARY KEY,
            question_1 BOOL NOT NULL)
        """
    )
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(command)
        cur.close()
        conn.commit()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def add_column(column_name):
    """adds column into dataset table for recording additional responses in surveys"""
    sql = """ALTER TABLE dataset ADD COLUMN {} integer;""".format(column_name)
    conn = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.curson()
        cur.execute(sql, (column_name,))
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    print('added table column')


def insert_data(column_name, response):
    """inserts user response into dataset table, generating unique ID"""
    sql = """INSERT INTO dataset({}) VALUES(%s) RETURNING user_id;""".format(column_name)
    conn = None
    user_id = None
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql, (response,))
        user_id = cur.fetchone()[0]
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    print(user_id)
    return user_id


def update_data(user_id, column_name, response):
    """Adds responses to subsequent columns for user continuing the survey. Used when ID != question_1"""
    sql = """UPDATE dataset SET {} = {} WHERE user_ID = {}""".format(column_name, response, user_id)
    conn = None
    if user_id is None:
        print("User_id CANNOT BE NULL WTF???")
    try:
        params = config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        cur.close()
    except(Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
