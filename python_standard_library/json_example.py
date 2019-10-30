import json
from pathlib import Path

# write JSon
movies = [
    {"id": 1, "title": "Terminator", "year": 1989},
    {"id": 12, "title": "Kindergarten Cop", "year": 1993},
]

data = json.dumps(movies)

print(data)

Path("python_standard_library/json/movies.json").write_text(data)

# read Json
data_in = Path("python_standard_library/json/movies.json").read_text()
movies = json.loads(data_in)
print(movies)
print(movies[0]["title"])
