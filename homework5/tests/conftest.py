import pytest
from sql_orm_client import MysqlOrmConnection

@pytest.fixture(scope='session')
def mysql_orm_client():
    return MysqlOrmConnection(user='root', password='1234', db_name='REQUESTS')
