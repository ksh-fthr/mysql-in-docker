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
);

grant all privileges on company.* to `mysql`@'%';
flush privileges;
