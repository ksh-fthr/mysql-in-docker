from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session as SessionClass
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

Base = declarative_base()


##
# DB 接続の準備
#
class MasterSlaveSession(SessionClass):
    is_updating = False

    def get_bind(self, mapper=None, clause=None):
        return engine


myDB = URL.create(
    drivername='mysql+pymysql',
    host='172.30.10.100',
    port='3306',
    username='mysql',
    password='mysqladmin',
    database='company'
)


# `echo` の値が `True` だと実行のたびにSQLが出力される
engine = create_engine(
    url=myDB,
    connect_args={
        'charset': 'utf8mb4'
    },
    pool_recycle=25200,
    echo=True
)

Session = sessionmaker(
    # autocommit=True, # これがあると遅い？
    class_=MasterSlaveSession
)

