import sqlite3
import json
from pathlib import Path

# Insert data
# movies = json.loads(
#     Path("./python_standard_library/json/movies.json").read_text())

# with sqlite3.connect("db.sqlite3") as connection:
#     command = "INSERT INTO Movies VALUES (?, ?, ?)"
#     for movie in movies:
#         connection.execute(command, tuple(movie.values()))
#     connection.commit()


# Read Data

with sqlite3.connect("db.sqlite3") as connection:
    command = "select * FROM Movies"
    cursor = connection.execute(command)
    # for row in cursor:
    #     print(row)
    movies = cursor.fetchall()
    print(movies)
