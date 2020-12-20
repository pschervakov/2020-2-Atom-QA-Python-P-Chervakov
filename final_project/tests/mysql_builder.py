from tests.my_sql_client import MySqlConnection
from sqlalchemy.ext.automap import automap_base

Base = automap_base()


class MySqlBuilder:
    def __init__(self, connection: MySqlConnection):
        self.db = connection.db
        self.connection = connection.connection
        Base = automap_base()
        Base.prepare(self.db.engine, reflect=True)
        self.User = Base.classes.test_users

    def get_usernames(self):
        users = []
        for el in self.get_records():
            users.append(el.username)
        return users

    def get_records(self):
        return self.db.query(self.User).all()

    def get_record_by_name(self, name):
        records = self.get_records()
        for el in records:
            if el.username == name:
                return el
        return -1

    def delete_user(self, name):
        self.db.query(self.User).filter(self.User.username == name).delete()
        self.db.commit()

    def add_user(self, name, email, password, access=1, active=0):
        self.db.add(self.User(username=name, email=email, password=password, access=access, active=active))
        self.db.commit()

    def block_user(self, name):
        record = self.get_record_by_name(name)
        record.access = 0
        self.db.commit()

    def unblock_user(self, name):
        record = self.get_record_by_name(name)
        record.access = 13
        self.db.commit()
