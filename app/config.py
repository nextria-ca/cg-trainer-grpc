import os

HOST = os.getenv('HOST', 'localhost')
PORT = int(os.getenv('PORT', 50051))
DATABASE_HOST = os.getenv('DATABASE_HOST', 'localhost')
DATABASE_PORT = int(os.getenv('DATABASE_PORT', 1521))
DATABASE = os.getenv('DATABASE', 'FREEPDB1')
USER = os.getenv('USER', 'oracle')
PASSWORD = os.getenv('PASSWORD', 'oracle')
MIN_POOL_SIZE = int(os.getenv('MIN_POOL_SIZE', 1))
MAX_POOL_SIZE = int(os.getenv('MAX_POOL_SIZE', 5))
POOL_INCREMENT = int(os.getenv('POOL_INCREMENT', 1))
NUM_WORKERS = int(os.getenv('NUM_WORKERS', 1))
NATIVE_SQL_DEBUG = bool(os.getenv('NATIVE_SQL_DEBUG', 'False'))
