create database rejoyn;

use rejoyn;

create table users (
	id int not null primary key auto_increment,
    full_name varchar(150) not null,
    email varchar(100) not null,
    password varchar(512) not null,
    dob date not null,
    gender char(1) not null -- M, F, O
);

-- select * from users