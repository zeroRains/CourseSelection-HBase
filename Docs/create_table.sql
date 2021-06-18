create table student(
  id serial,
  sno varchar(10) primary key,
  name varchar(6),
  passwd varchar(16),
  sex char(1),
  birthday smalldatetime,
  age int,
  classnum varchar(10)
);

create table teacher(
    id serial,
    tno varchar(10) primary key ,
    name varchar(6),
    passwd varchar(16),
    sex char(1),
    birthday smalldatetime,
    age int,
    position varchar(20),
    collegenum int
);

create table college(
  id serial,
  num int primary key ,
  name varchar(20)
);

create table class(
    id serial,
    num varchar(10) primary key ,
    collegenum int
);

create table schedule(
    id serial,
    cno varchar(10) primary key ,
    semester varchar(10)
)

create table course(
    id serial,
    coursecode varchar(10) primary key ,
    name varchar(20),
    credit float,
    cno varchar(10)
);

create table teach(
    id  serial,
    tno varchar(10),
    cno varchar(10),
    num int,
    primary key (tno,cno)
);

create table selection(
    id serial,
    cno varchar(10),
    sno varchar(10),
    usual float,
    exam float,
    score float,
    primary key (cno,sno)

);