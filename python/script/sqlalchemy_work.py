import sys
import time

from datetime import datetime, timedelta, timezone
from sqlalchemy import create_engine, Column, String, Integer, Boolean, Date, DateTime
from sqlalchemy.orm import sessionmaker, Session as SessionClass
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.engine.url import URL

Base = declarative_base()
JST = timezone(timedelta(hours=+9), 'JST')

##
# モデル
#
class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer(), primary_key=True, autoincrement=True)
    name = Column(String(100))
    phone = Column(String(100))
    created_at = Column(DateTime())
    updated_at = Column(DateTime())

    def __repr__(self):
        return "<Employee (id={}, name='{}', phone='{}'".format(self.id, self.name, self.phone)

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

engine = create_engine(
    url=myDB,
    connect_args={
        'charset': 'utf8mb4'
    },
    pool_recycle=25200,
    echo=True # Trueだと実行のたびにSQLが出力される
)

Session = sessionmaker(
    # autocommit=True, # これがあると遅い？
    class_=MasterSlaveSession
)

##
# 実処理
#
def insert():
    rdb_session = Session()
    for i in range(10000):
        work_num = i + 1
        work_time = datetime.fromtimestamp(time.time(), JST)
        employee = Employee()
        employee.name = 'employee' + str(work_num).zfill(6)
        employee.phone = str(work_num).zfill(6)
        employee.created_at = work_time
        employee.updated_at = work_time
        rdb_session.add(employee)

        # autocommit ありでここで flush() すると毎行トランザクションが発生するので遅い
        # rdb_session.flush()

    # autocommit ありの場合は flush(), なしの場合は commit() するとトランザクションは処理対象行全体にかかるので早い
    # rdb_session.flush()
    rdb_session.commit()


##
# ここから実行時の処理
#
start_time = time.time()
print(f'{datetime.fromtimestamp(start_time, JST)} process start')


try:
    insert()
except Exception as e:
    print(f'error: {format(str(e))}')


end_time = time.time()
elapsed_time = end_time - start_time
print(f'process had got {elapsed_time}sec to done.')
print(f'{datetime.fromtimestamp(end_time, JST)} process had finished')

