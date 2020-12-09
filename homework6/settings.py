from urllib.parse import urljoin

APP_HOST, APP_PORT = '127.0.0.1', 1050
APP_URL = f'http://{APP_HOST}:{APP_PORT}'

MOCK_HOST, MOCK_PORT = '127.0.0.1', 1052
MOCK_URL = f'http://{MOCK_HOST}:{MOCK_PORT}'

MOCK_VALID_URL = urljoin(MOCK_URL, 'valid')
APP_SHUTDOWN_URL = urljoin(APP_URL, 'shutdown')
MOCK_SHUTDOWN_URL = urljoin(MOCK_URL, 'shutdown')
