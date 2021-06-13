# アプリの確認
Python の Docker コンテナに入って DB 操作するときは以下の手順で行えます。


## ホスト側での操作
### コンテナの確認
次のコマンドを実行して `CONTAINER ID` を確認します。

```bash
$ docker ps
CONTAINER ID   IMAGE                         COMMAND                  CREATED          STATUS         PORTS                                                  NAMES
d3577b0d7d52   python-work-in-docker_mysql   "docker-entrypoint.s…"   10 seconds ago   Up 5 seconds   0.0.0.0:3306->3306/tcp, :::3306->3306/tcp, 33060/tcp   docker-mysql-work
f11b0c0b0585   python-work-in-docker_app     "python3"                10 seconds ago   Up 6 seconds                                                          python-app
7655647a03a0   bc7a6b389ed2                  "docker-entrypoint.s…"   3 months ago     Up 4 days      0.0.0.0:5432->5432/tcp, :::5432->5432/tcp              docker-postgresql-work
```

( ここで取得した `CONTAINER ID` はあくまで上記コマンド実行時に確認できたものです。実際は実行する毎に異なる値になります )


### コンテナに入る
次のコマンドで `CONTAINER ID` を指定してコンテナに入ります。

```bash
$ ocker exec -it f11b0c0b0585 bash
root@hermes:/usr/local/python-app# 
```

これで python のコンテナに入りました｡以降は コンテナ上での作業になります。


## コンテナ上での操作
### アプリの確認

```bash
root@hermes:/usr/local/python-app# ls -l
合計 8
-rw-r--r-- 1 root root   54  6月 13 18:10 requirement.txt
drwxr-xr-x 4 root root 4096  6月 13 18:14 script

root@hermes:/usr/local/python-app# ls -l script/
合計 32
-rw-r--r-- 1 root root  1285  6月 13 18:10 insert.py
drwxr-xr-x 3 root root  4096  6月 13 18:14 orm
-rw-r--r-- 1 root root  1182  6月 13 18:10 update.py
drwxr-xr-x 2 root root  4096  6月 13 18:14 util
```

上記のとおりコンテナ上にアプリが配置されていることが確認できました｡


### insert の実行
`insert.py` を実行して `employee` テーブルにデータを登録します｡

```python
root@hermes:/usr/local/python-app# python script/insert.py 
2021-06-13 19:27:10.659317+09:00 process start
2021-06-13 19:27:11,847 INFO sqlalchemy.engine.Engine SHOW VARIABLES LIKE 'sql_mode'
2021-06-13 19:27:11,848 INFO sqlalchemy.engine.Engine [raw sql] {}
2021-06-13 19:27:11,861 INFO sqlalchemy.engine.Engine SHOW VARIABLES LIKE 'lower_case_table_names'
2021-06-13 19:27:11,862 INFO sqlalchemy.engine.Engine [generated in 0.00053s] {}
2021-06-13 19:27:11,868 INFO sqlalchemy.engine.Engine SELECT DATABASE()
2021-06-13 19:27:11,868 INFO sqlalchemy.engine.Engine [raw sql] {}
2021-06-13 19:27:11,872 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2021-06-13 19:27:12,132 INFO sqlalchemy.engine.Engine INSERT INTO employee (name, phone, created_at, updated_at) VALUES (%(name)s, %(phone)s, %(created_at)s, %(updated_at)s)
2021-06-13 19:27:12,133 INFO sqlalchemy.engine.Engine [generated in 0.00043s] {'name': 'employee000001', 'phone': '000001', 'created_at': datetime.datetime(2021, 6, 13, 19, 27, 10, 659459, tzinfo=datetime.timezone(datetime.timedelta(seconds=32400), 'JST')), 'updated_at': datetime.datetime(2021, 6, 13, 19, 27, 10, 659459, tzinfo=datetime.timezone(datetime.timedelta(seconds=32400), 'JST'))}
...
...
...
2021-06-13 19:27:36,409 INFO sqlalchemy.engine.Engine INSERT INTO employee (name, phone, created_at, updated_at) VALUES (%(name)s, %(phone)s, %(created_at)s, %(updated_at)s)
2021-06-13 19:27:36,409 INFO sqlalchemy.engine.Engine [cached since 24.31s ago] {'name': 'employee010000', 'phone': '010000', 'created_at': datetime.datetime(2021, 6, 13, 19, 27, 11, 788189, tzinfo=datetime.timezone(datetime.timedelta(seconds=32400), 'JST')), 'updated_at': datetime.datetime(2021, 6, 13, 19, 27, 11, 788189, tzinfo=datetime.timezone(datetime.timedelta(seconds=32400), 'JST'))}
2021-06-13 19:27:36,577 INFO sqlalchemy.engine.Engine COMMIT
process had got 25.942010402679443sec to done.
2021-06-13 19:27:36.601328+09:00 process had finished
```


### update の実行
`insert.py` を実行して `employee` テーブルのデータを更新します｡

```bash
root@hermes:/usr/local/python-app# python script/update.py
2021-06-13 19:30:16.467522+09:00 process start
2021-06-13 19:30:16,476 INFO sqlalchemy.engine.Engine SHOW VARIABLES LIKE 'sql_mode'
2021-06-13 19:30:16,476 INFO sqlalchemy.engine.Engine [raw sql] {}
2021-06-13 19:30:16,480 INFO sqlalchemy.engine.Engine SHOW VARIABLES LIKE 'lower_case_table_names'
2021-06-13 19:30:16,481 INFO sqlalchemy.engine.Engine [generated in 0.00031s] {}
2021-06-13 19:30:16,485 INFO sqlalchemy.engine.Engine SELECT DATABASE()
2021-06-13 19:30:16,485 INFO sqlalchemy.engine.Engine [raw sql] {}
2021-06-13 19:30:16,489 INFO sqlalchemy.engine.Engine BEGIN (implicit)
2021-06-13 19:30:16,492 INFO sqlalchemy.engine.Engine SELECT employee.id AS employee_id, employee.name AS employee_name, employee.phone AS employee_phone, employee.created_at AS employee_created_at, employee.updated_at AS employee_updated_at 
FROM employee 
 LIMIT %(param_1)s
2021-06-13 19:30:16,492 INFO sqlalchemy.engine.Engine [generated in 0.00045s] {'param_1': 10000}
2021-06-13 19:30:17,696 INFO sqlalchemy.engine.Engine UPDATE employee SET name=%(name)s, updated_at=%(updated_at)s WHERE employee.id = %(employee_id)s
2021-06-13 19:30:17,696 INFO sqlalchemy.engine.Engine [generated in 0.05504s] ({'name': 'up_employess000001', 'updated_at': datetime.datetime(2021, 6, 13, 19, 30, 16, 995368, tzinfo=datetime.timezone(datetime.timedelta(seconds=32400), 'JST')), 'employee_id': 1}, {'name': 'up_employess000002', 'updated_at': datetime.datetime(2021, 6, 13, 19, 30, 16, 995497, tzinfo=datetime.timezone(datetime.timedelta(seconds=32400), 'JST')), 'employee_id': 2}, {'name': 'up_employess000003', 'updated_at': datetime.datetime(2021, 6, 13, 19, 30, 16, 995540, tzinfo=datetime.timezone(datetime.timedelta(seconds=32400), 'JST')), 'employee_id': 3}, {'name': 'up_employess000004', 'updated_at': datetime.datetime(2021, 6, 13, 19, 30, 16, 995588, tzinfo=datetime.timezone(datetime.timedelta(seconds=32400), 'JST')), 'employee_id': 4}, {'name': 'up_employess000005', 'updated_at': datetime.datetime(2021, 6, 13, 19, 30, 16, 995630, tzinfo=datetime.timezone(datetime.timedelta(seconds=32400), 'JST')), 'employee_id': 5}, {'name': 'up_employess000006', 'updated_at': datetime.datetime(2021, 6, 13, 19, 30, 16, 995672, tzinfo=datetime.timezone(datetime.timedelta(seconds=32400), 'JST')), 'employee_id': 6}, {'name': 'up_employess000007', 'updated_at': datetime.datetime(2021, 6, 13, 19, 30, 16, 995719, tzinfo=datetime.timezone(datetime.timedelta(seconds=32400), 'JST')), 'employee_id': 7}, {'name': 'up_employess000008', 'updated_at': datetime.datetime(2021, 6, 13, 19, 30, 16, 995760, tzinfo=datetime.timezone(datetime.timedelta(seconds=32400), 'JST')), 'employee_id': 8}  ... displaying 10 of 10000 total bound parameter sets ...  {'name': 'up_employess009999', 'updated_at': datetime.datetime(2021, 6, 13, 19, 30, 17, 435364, tzinfo=datetime.timezone(datetime.timedelta(seconds=32400), 'JST')), 'employee_id': 9999}, {'name': 'up_employess010000', 'updated_at': datetime.datetime(2021, 6, 13, 19, 30, 17, 435415, tzinfo=datetime.timezone(datetime.timedelta(seconds=32400), 'JST')), 'employee_id': 10000})
2021-06-13 19:30:35,251 INFO sqlalchemy.engine.Engine COMMIT
process had got 18.806922674179077sec to done.
2021-06-13 19:30:35.274445+09:00 process had finished
```

