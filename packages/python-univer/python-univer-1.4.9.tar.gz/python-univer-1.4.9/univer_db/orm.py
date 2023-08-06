import urllib
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()


def get_session(config):
    quoted = urllib.parse.quote_plus('DRIVER={driver};Server={host};Database={db};UID={user};PWD={password};TDS_Version=7.3;Port=1433;'.format(
        driver=config.driver, host=config.host, db=config.db, user=config.user, password=config.password))
    engine = create_engine('mssql+pyodbc:///?odbc_connect={}'.format(quoted),
                           pool_size=config.pool_size, max_overflow=config.max_overflow)

    engine.connect()

    session_factory = sessionmaker(bind=engine)

    return session_factory


def get_base():
    return Base
