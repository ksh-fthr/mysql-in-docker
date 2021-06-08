drop database if exists company;
create database company;

use company;

drop table if exists employee;
create table if not exists employee (
	id serial,
    name varchar(100) not null unique,
    phone varchar(100),
    created_at datetime DEFAULT NULL,
    updated_at datetime DEFAULT NULL,
    primary key(id)
    -- index(name(100))
);

-- insert into employee(name, tel) values('hogehoge', '000-0000-0000');
-- insert into employee(name, tel) values('piyopiyo', '111-1111-1111');
-- insert into employee(name, tel) values('fugafuga', '222-2222-2222');

grant all privileges on company.* to `mysql`@'%';
flush privileges;
