import mysql.connector
from mysql.connector import errorcode

config = {
    'user': 'root',
    'password': 'K4n4t0&r1k4!',
    'host': 'localhost',
    'database': 'movies',
    'raise_on_warnings': True
}

try:
    db = mysql.connector.connect(**config)
    cursor = db.cursor()

    # Query 1: Select all fields from the studio table
    query1 = "SELECT * FROM studio"
    cursor.execute(query1)

    # Print the results in a tabular format
    print("Studio:")
    print("{:<20} {:<20}".format("Studio ID", "Studio Name"))
    for row in cursor:
        print("{:<20} {:<20}".format(*row))

    # Query 2: Select all fields from the genre table
    query2 = "SELECT * FROM genre"
    cursor.execute(query2)

    # Print the results in a tabular format
    print("\nGenre:")
    print("{:<20} {:<20}".format("Genre ID", "Genre Name"))
    for row in cursor:
        print("{:<20} {:<20}".format(*row))

    #Query 3: short films
    query3 = "SELECT name FROM movie WHERE runtime < 120 "
    cursor.execute(query3)

    print("\nMovies with runtime less than 2 hours:")
    for row in cursor:
        print(row[0])

    # Query 4: List of film names and directors, ordered by director
    query4 = "SELECT name, director FROM movie ORDER BY director"
    cursor.execute(query4)

    # Print the results in a tabular format
    print("\nDirector:")
    print("{:<20} {:<20}".format("Film Name", "Director"))
    for row in cursor:
        print("{:<20} {:<20}".format(*row))


except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("The supplied username or password is invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
