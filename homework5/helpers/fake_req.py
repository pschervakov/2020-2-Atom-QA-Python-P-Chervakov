from faker import Faker
from random import choice , randint
faker = Faker()

def ip():
	return faker.ipv4()


def url():
	return faker.url()


def response_code():
	responses=(100,101,200,201,202,203,204,205,206,300,301,302,303,304,305,
	307,400,401,402,403,404,405,406,407,408,409,410,411,412,413,414,415,
	416,417,500,501,502,503,504,505)
	return choice(responses)


def request_type():
	types=('GET','POST','PUT', 'DELETE','CONNECT', 'PATCH', 'HEAD')
	return choice(types)

def content_length():
	return randint(1,10000)
