create database infydb;
use infydb;
drop table if exists admins;
drop table if exists user;
drop table if exists foodcourt;
drop table if exists menuitems;
drop table if exists order;
drop table if exists item;
create table admins(emp_id int primary key, password varchar(50));
<<<<<<< HEAD
insert into admins(emp_id,password) values(582629,'vasa@9999V');
=======
>>>>>>> 34cb5fecf03f3a0afbf6e49219d729ef8e1d6661

create table user(emp_id int primary key, name varchar(50), password varchar(50),email varchar(50),phone_no varchar(50));

create table foodcourt(fc_id int primary key, name varchar(50),contact_info varchar(50),is_active boolean);


create table menuitems(
    -> item_id int primary key,
    -> fc_id int,
    -> name varchar(50),
    -> description text,
    -> price decimal(10,2),
    -> category varchar(50),
    -> is_available boolean,
    -> foreign key(fc_id) references foodCourt(fc_id));

create table orders(
    -> order_id int primary key auto_increment,
    -> emp_id int,
    -> order_time timestamp,
    -> total_amount decimal(8,2),
    -> status varchar(50),
    -> foreign key(emp_id) references user(emp_id))
    -> auto_increment=1000;

create table item(order_item_id int primary key,order_id int references (order_id) Order,item_id int references (item_id) Menu,price decimal(8,2),quantity int);
