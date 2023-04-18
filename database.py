import mysql.connector

def connect():
    # Connect to the MySQL database
    db = mysql.connector.connect(
        host="localhost",
        user="username",
        password="password",
        database="smart_parking"
    )

    return db

def get_spaces():
    # Get the total number of parking spaces from the database
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM parking_spaces")
    result = cursor.fetchone()
    db.close()

    return result[0]

def get_booked_spaces():
    # Get the number of booked parking spaces from the database
    db = connect()
    cursor = db.cursor()
    cursor.execute("SELECT COUNT(*) FROM bookings")
    result = cursor.fetchone()
    db.close()

    return result[0]

def book_space(space_id, user_id):
    # Book a parking space for the user in the database
    db = connect()
    cursor = db.cursor()
    cursor.execute("INSERT INTO bookings (space_id, user_id) VALUES (%s, %s)", (space_id, user_id))
    db.commit()
    db.close()

def unbook_space(space_id):
    # Unbook a parking space in the database
    db = connect()
    cursor = db.cursor()
    cursor.execute("DELETE FROM bookings WHERE space_id = %s", (space_id,))
    db.commit()
    db.close()
