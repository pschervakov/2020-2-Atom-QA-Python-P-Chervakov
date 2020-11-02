from models.models import Base, Request

from sql_orm_client import MysqlOrmConnection



class RequestBuilder(object):
    def __init__(self, connection: MysqlOrmConnection):
        self.connection = connection
        self.engine = self.connection.connection.engine

    def create_requests(self):
        if not self.engine.dialect.has_table(self.engine, 'requests'):
            Base.metadata.tables['requests'].create(self.engine)

    def add_request(self, request):
        self.connection.session.add(request)
        self.connection.session.commit()
        return request
