create database rejoyn;

use rejoyn;

show tables;

create table users (
	id int not null primary key auto_increment,
    full_name varchar(150) not null,
    email varchar(100) not null,
    password varchar(512) not null,
    dob date not null,
    gender char(1) not null -- M, F, O
);

select * from users;

delete from users where id = 1;

create table destinations_features (
	id int not null primary key auto_increment,
    feature varchar(100) not null unique
);

INSERT INTO destinations_features (feature)
VALUES 
    ('art_and_culture'),
    ('beach'),
    ('outdoor_adventures'),
    ('nightlife_and_entertainment'),
    ('great_food'),
    ('underrated_destinations'),
    ('safety'),
    ('weather');

select * from destinations_features;

create table users_preferences (
	id int not null primary key auto_increment,
    user_id int not null,
    feature_id int not null,
    score int not null,
    foreign key (user_id) references users(id),
    foreign key (feature_id) references destinations_features(id)
);