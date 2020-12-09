from models.models import Base, Total, RequestsByType, LongestRequests, ServerErrorLongestRequests, \
    ClientErrorFrequentRequest
from sql_orm_client import MysqlOrmConnection


class LogOrmBuilder(object):
    def __init__(self, connection: MysqlOrmConnection):
        self.connection = connection
        self.engine = self.connection.connection.engine

    def create_table(self, name):
        if not self.engine.dialect.has_table(self.engine, name):
            Base.metadata.tables[name].create(self.engine)


    def add_record(self,record):
        self.connection.session.add(record)
        self.connection.session.commit()        

    def add_number_to_total(self, num):
        record = Total(
            number=num,
        )
        self.add_record(record)
        return record

    def add_to_requests_by_type(self, q_type, num):
        record = RequestsByType(
            number=num,
            type=q_type,
        )
        self.add_record(record)
        return record

    def add_to_longest_requests(self, url, response_code, content_length):
        record = LongestRequests(
            url=url,
            response_code=response_code,
            content_length=content_length,
        )
        self.add_record(record)
        return record

    def add_to_server_requests(self, ip, url, response_code):
        record = ServerErrorLongestRequests(
            url=url,
            response_code=response_code,
            ip=ip
        )
        self.add_record(record)
        return record

    def add_to_client_frequent_requests(self, ip, url, response_code):
        record = ClientErrorFrequentRequest(
            url=url,
            response_code=response_code,
            ip=ip
        )
        self.add_record(record)
        return record
