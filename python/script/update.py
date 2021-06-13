import sys
import time

sys.path.append("./script")

from orm.preparation import Session
from orm.model.employee import Employee
from util.time_util import elapsed_time, jst_time


##
# 実処理
#
def update():
    rdb_session = Session()
    query = rdb_session.query(Employee).limit(10000)
    
    for employee in query:
        work_time = jst_time(time.time())
        employee.name = employee.name.replace('employee', ('up_employess'))
        employee.updated_at = work_time

        # autocommit ありでここで flush() すると毎行トランザクションが発生するので遅い
        # rdb_session.flush()

    # autocommit ありの場合は flush(), なしの場合は commit() するとトランザクションは処理対象行全体にかかるので早い
    # rdb_session.flush()
    rdb_session.commit()


##
# ここから実行時の処理
#
start_time = time.time()
print(f'{jst_time(start_time)} process start')


try:
    update()
except Exception as e:
    print(f'error: {format(str(e))}')


end_time = time.time()
print(f'process had got {elapsed_time(start_time, end_time)}sec to done.')
print(f'{jst_time(end_time)} process had finished')

