import sqlalchemy
from sqlalchemy.orm import sessionmaker


class MysqlOrmConnection(object):
    def __init__(self, user, password, db_name):
        self.user = user
        self.password = password
        self.db_name = db_name
        self.port = 3306
        self.host = '127.0.0.1'
        self.connection = self.connect()
        session = sessionmaker(bind=self.connection)
        self.session = session()

    def get_connection(self, db_created=False):
        user = self.user
        password = self.password
        host = self.host
        port = self.port
        db = self.db_name if db_created else ''
        engine = sqlalchemy.create_engine(f'mysql+pymysql://{user}:{password}@{host}:{port}/{db}')
        return engine.connect()

    def connect(self):
        connection = self.get_connection(db_created=False)

        connection.execute(f'DROP DATABASE IF EXISTS {self.db_name}')
        connection.execute(f'CREATE DATABASE {self.db_name}')
        connection.close()

        return self.get_connection(db_created=True)
