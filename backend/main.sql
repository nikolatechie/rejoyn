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

create table user_groups (
	id int not null primary key auto_increment,
    group_id int not null,
    user_id int not null,
    foreign key (user_id) references users(id)
);

-- Select data from all tables
show tables;
select * from users;
select * from users_preferences;
select * from destinations_features;
select * from user_groups;

insert into user_groups (group_id, user_id)
values
	(0, 2),
    (0, 3),
    (0, 4),
    (0, 5),
    (0, 6);

insert into users_preferences (user_id, feature_id, score)
values
(2, 2, 4), (2, 4, 4), (2, 8, 5),
(3, 1, 4), (3, 7, 4),
(4, 3, 5), (4, 4, 5), (4, 6, 3), (4, 7, 4),
(5, 1, 4), (5, 3, 4), (5, 4, 4),
(6, 7, 3), (6, 8, 5), (6, 5, 4)