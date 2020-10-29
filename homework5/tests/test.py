
import pytest

from models.models import Request
from sql_orm_client import MysqlOrmConnection
from request_builder import RequestBuilder
from helpers import fake_req


class TestMysqlOrm(object):
    @pytest.fixture(scope='function', autouse=True)
    def setup(self, mysql_orm_client):
        self.mysql: MysqlOrmConnection = mysql_orm_client
        self.builder: RequestBuilder = RequestBuilder(connection=self.mysql)

    def add_fake_req(self):
        request = Request(
            ip=fake_req.ip(),
            url=fake_req.url(),
            protocol='HTTP/1.1',
            request_type=fake_req.request_type(),
            response_code=fake_req.response_code(),
            content_length=fake_req.content_length(),
        )
        return self.builder.add_request(request)


    def test(self):
        self.builder.create_requests()
        req = self.add_fake_req()
        assert req.ip == self.mysql.session.query(Request).first().ip
