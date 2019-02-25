create database Shaunak_Oke_18204307_ass2;
use database Shaunak_Oke_18204307_ass2;

create table titles(isbn varchar(13),title varchar(150));

load data local infile "D:/cstuff2/sql/Books.csv" into table titles Fields terminated by ',' lines terminated by '\n'
ignore 1 lines(isbn,title);

create table authors(isbn varchar(13),author varchar(40),ranks int(3));

load data local infile "D:/cstuff2/sql/authors.csv" into table authors Fields terminated by ',' lines terminated by '\n'
ignore 1 lines;

create table themes(isbn varchar(13),themes varchar(40),ranks int(3));

load data local infile "D:/cstuff2/sql/themes.csv" into table themes Fields terminated by ',' lines terminated by '\n'
ignore 1 lines;

create table qualities(isbn varchar(13),qualities varchar(40),ranks int(3));

load data local infile "D:/cstuff2/sql/qualities.csv" into table qualities Fields terminated by ',' lines terminated by '\n'
ignore 1 lines;