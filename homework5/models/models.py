from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Request(Base):
    __tablename__ = 'requests'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(50))
    url = Column(String(50), nullable=False)
    request_type = Column(String(50), nullable=False)
    protocol = Column(String(30), nullable=False)
    response_code = Column(String(50), nullable=False)
    content_length = Column(String(50), nullable=False)

    def __repr__(self):
        return f"Request(" \
            f"ip='{self.ip}', " \
            f"url='{self.url}', " \
            f"request_type='{self.request_type}', " \
            f"protocol='{self.protocol}', " \
            f"response_code='{self.response_code}', " \
            f"content_length='{self.content_length}')"


class Total(Base):
    __tablename__ = 'total'
    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(Integer)


class RequestsByType(Base):
    __tablename__ = 'requests_by_type'
    id = Column(Integer, primary_key=True, autoincrement=True)
    number = Column(Integer)
    type = Column(String(10))


class LongestRequests(Base):
    __tablename__ = 'longest_requests'
    id = Column(Integer, primary_key=True, autoincrement=True)
    url = Column(String(200))
    response_code = Column(Integer)
    content_length = Column(Integer)


class ServerErrorLongestRequests(Base):
    __tablename__ = 'server_error_longest_requests'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(30))
    url = Column(String(500))
    response_code = Column(Integer)


class ClientErrorFrequentRequest(Base):
    __tablename__ = 'client_error_frequent_request'
    id = Column(Integer, primary_key=True, autoincrement=True)
    ip = Column(String(30))
    url = Column(String(500))
    response_code = Column(Integer)
