import pymysql
import config

def mysql_get_mydb():
    try:
        database = pymysql.connect(
            host=config.host,
            user=config.user,
            passwd=config.passwd,
            db=config.db
        )
    finally:
        return database

create_skarr_quotes = """
    CREATE TABLE skarr_quotes(
        id INT AUTO_INCREMENT PRIMARY KEY,
        quote VARCHAR(100)
    )
"""

def create_table():
    db = mysql_get_mydb()
    cursor = db.cursor()

    with cursor:
        cursor.execute(create_skarr_quotes)
        db.commit()

seed_db = """
INSERT INTO skarr_quotes(quote)
VALUES
    ("Timmy, I'm fixing my sleeping schedule tonight."),
    ("Boo fukin hoo")
"""

def seed():
    db = mysql_get_mydb()
    cursor = db.cursor()

    with cursor:
        cursor.execute(seed_db)
        db.commit()

def add_quote_to_db(formatted_quote):
    db = mysql_get_mydb()
    cursor = db.cursor()

    sql = "INSERT INTO skarr_quotes (quote) VALUES (%s)"

    with cursor:
        cursor.execute(sql, formatted_quote)
        db.commit()

def get_random_quote():
    db = mysql_get_mydb()
    cursor = db.cursor()

    sql = "SELECT * FROM skarr_quotes ORDER BY RAND() LIMIT 1"

    with cursor:
        cursor.execute(sql)

        quote = cursor.fetchone()
        return quote
