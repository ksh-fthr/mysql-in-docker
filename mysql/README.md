# DB の確認
mysql の Docker コンテナに入って DB 操作するときは以下の手順で行えます。


# 作成される DB
`docker-compose up -d --build` を実行することで `./mysql/init/initialize.sql` が実行され、mysql のコンテナには `company` DB が作成されます。
DB の情報は以下のとおりです。

| DB名    | テーブル | ユーザ名 | パスワード |
| ------- | -------- | -------- | ---------- |
| company | employee | mysql    | mysqladmin |


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
$ docker exec -it d3577b0d7d52 bash
root@jolyn:/#
```

これで mysql のコンテナに入りました｡以降は コンテナ上での作業になります。


## コンテナ上での操作
### mysql に入る
次のコマンドで `psql` に入ります。

```bash
root@jolyn:/# mysql -umysql -p
Enter password:             # 前掲のパスワードを入力してください
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9
Server version: 8.0.25 MySQL Community Server - GPL

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> 
```

以降は mysql クライアント 上での作業になります。


### mysql クライアント 上での操作
#### 作成済みのデータベース一覧

```mysql
mysql> show databases;
+--------------------+
| Database           |
+--------------------+
| company            |
| information_schema |
+--------------------+
2 rows in set (0.01 sec)
```


#### company DB へ接続

```mysql
mysql> use company;
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed 
```


#### テーブル一覧

```mysql
mysql> show tables;
+-------------------+
| Tables_in_company |
+-------------------+
| employee          |
+-------------------+
1 row in set (0.01 sec)
```
