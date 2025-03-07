# fake_db.py

import json
from pathlib import Path

# Class that loads the fake user database (to be deprecated soon)


class Database:
    def __init__(self, db_route: str):
        self.db_route = db_route
        self.db = self.load_db()

        for key in self.db.keys():
            self.db[key]["hashed_password"] = self.db[key]["hashed_password"].encode()

    def load_db(self):
        with open(self.db_route, "r") as file:
            data = file.read()
            return json.loads(data)


db_path = Path(__file__).parents[1] / "data/users_db_fake.json"
db_ob = Database(db_path)

users_db = db_ob.db
