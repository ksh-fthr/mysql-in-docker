# このプロジェクトについて
Python､および SQLAlchemy / MySQL の学習を目的としたものです｡
上記の環境構築を容易にするため､ Docker/Docker Compose を用いています｡


# 環境について
以下の環境で実行・確認しています。

| 環境                                                         | バージョン              | 備考                         |
| ------------------------------------------------------------ | ----------------------- | ---------------------------- |
| macOS Catalina                                               | v10.15.7                |                              |
| [Docker Desktop for Mac](https://hub.docker.com/editions/community/docker-ce-desktop-mac/) | v3.3.3                  |                              |
| Docker                                                       | v20.10.6, build 370c289 | `$ docker --version`         |
| Docker Compose                                               | v1.29.1, build c34c88b2 | `$ docker-compose --version` |
| [Docker MySQL](https://hub.docker.com/_/mysql)               | v8.0.x                  | Dockerfile で指定            |
| [Docker Python](https://hub.docker.com/_/python)             | v3.9.x                  | 同上                         |
| [SQLAlchemy](https://www.sqlalchemy.org/)                    | v1.4.17                 | requirement.tx               |


# 構成

```bash
$ tree
.
├── LICENSE
├── README.md
├── docker-compose.yml
├── mysql
│   ├── Dockerfile
│   ├── init
│   │   └── initialize.sql
│   └── my.cnf
└── python
    ├── Dockerfile
    ├── requirement.txt
    └── script
        ├── insert.py
        ├── orm
        │   ├── model
        │   │   └── employee.py
        │   └── preparation.py
        ├── update.py
        └─ util
            └── time_util.py
```


# ブランチについて
現在はブランチを切らずに `main` ブランチのみで運用しておりますが､今後学習の目的にあわせてブランチを適宜作成するかもしれません｡ 


# コンテナに対する操作
## 起動
次のコマンドを実行することで Docker 上に Python と MySQL の環境が起動します｡

```bash
$ docker-compose up -d --build
```

`-d` はバックグラウンドで動かすオプションです。 フォアグラウンドで動かしたい場合は `-d` をつけずに実行してください。


## 停止
### サービスの停止
サービスは停止するが Docker コンテナは削除したくない場合は下記コマンドを実行してください。

```bash
$ docker-compose stop
```


### コンテナの停止
サービスの停止とサービスを提供するコンテナの削除、それからネットワークも削除したい場合は下記コマンドを実行してください。

```bash
$ docker-compose down
```


# DB と アプリについて
それぞれ以下の README.md をご参照ください｡

- [DB の README](./mysql/README.md)
- [アプリの README](./python/README.md)
