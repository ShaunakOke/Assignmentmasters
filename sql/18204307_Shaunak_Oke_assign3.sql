create database Shaunak_Oke_18204307_ass3;
use database Shaunak_Oke_18204307_ass3;
--use "source path_of_bookdump.sql" to load data

--question1
select DISTINCT(a.title) from titles a,authors b where b.rank>1 and a.isbn=b.isbn;

--2
select title from titles where title not in (select DISTINCT(a.title) from titles a,authors b where b.rank>1 and a.isbn=b.isbn)

--3
select distinct(title),theme from titles,themes where (themes.theme like ("%magic%") and themes.theme like("%heroism%") and themes.theme not like("%evil%"))and titles.isbn=themes.isbn group by themes.isbn;

--empty set with and query!next command is or query to 
--demonstrate!!

select distinct(title),theme from titles,themes where (themes.theme like ("%magic%") or themes.theme like("%heroism%") and themes.theme not like("%evil%"))and titles.isbn=themes.isbn group by themes.isbn;

--4
select author from authors,themes where theme like "science" and authors.isbn=themes.isbn group by author having count(*)>1 ORDER BY count(*) DESC;

--5
select distinct(title) from titles,qualities,themes where (quality="intelligent" or quality="sophisticated") and theme like "%marriage%" and qualities.isbn=themes.isbn and qualities.isbn=titles.isbn;