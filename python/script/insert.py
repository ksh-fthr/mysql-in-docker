import sys
import time

from orm.preparation import Session
from orm.model.employee import Employee
from util.time_util import elapsed_time, jst_time

sys.path.append("./script")


##
# 実処理
#
def insert():
    rdb_session = Session()
    for i in range(10000):
        work_num = i + 1
        work_time = jst_time(time.time())
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
print(f'{jst_time(start_time)} process start')


try:
    insert()
except Exception as e:
    print(f'error: {format(str(e))}')


end_time = time.time()
print(f'process had got {elapsed_time(start_time, end_time)}sec to done.')
print(f'{jst_time(end_time)} process had finished')

