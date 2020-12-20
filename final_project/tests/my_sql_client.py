from sqla_wrapper import SQLAlchemy
from tests import settings


class MySqlConnection:
    def __init__(self, user='test_qa', password='qa_test'):
        self.user = user
        self.password = password
        self.host = settings.MYSQL_HOST
        self.port = settings.MYSQL_PORT
        self.db_name = 'test'
        self.db, self.connection = self.connect()

    def connect(self):
        db = SQLAlchemy(f'mysql+pymysql://{self.user}:{self.password}@{self.host}:{self.port}/{self.db_name}')
        return db, db.connection()


