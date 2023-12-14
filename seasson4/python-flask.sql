create database users;

use users;

# Tables
create table Users(id int, username varchar(100), name varchar(100), lastname varchar(255), phone int(20), email varchar(250));
show tables;
drop table Users;

alter table Users add age int; # Add field
alter table Users drop column age; # Delete field
alter table Users modify column email varchar(50);
alter table Users modify column phone varchar(50);
alter table Users add primary key (id);
alter table Users modify column id int AUTO_INCREMENT;
select * from Users where username='prueba.2';

# Insert Data
insert into Users (email, username)	values ('johan.luna@finkargo.comidid','johan.luna');
insert into Users (email, username)	values ('johan.luna@finkargo.com','johan.luna');
insert into Users (email, username)	values ('prueba.2@finkargo.com','prueba.2');
insert into Users (id, email, username, lastname, phone)values (1, 'johanluna777@gmail.com', 'jl777', 'Luna Bermeo', 3105405342);

# DELETE FROM Users WHERE email = 'johan.luna@finkargo.com' LIMIT 1;
DELETE FROM Users WHERE id = 1;
# DELETE FROM Users WHERE email = 'johan.luna@finkargo.com' ORDER BY id LIMIT 1; # Fx with ChatGPT

# Update data
select * from Users;
update Users set username = 'angie1995',
name = 'Angie Fernanda',
 lastname = 'Loaiza Paez',
 phone = 3127930518,
 email = 'fernandaloaiza1226@gmail.com'
 where id = 2;