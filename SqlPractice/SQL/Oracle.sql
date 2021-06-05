create table customer(customer_id number(4), cust_name varchar2(20), city varchar2(10), grade number(6), salesman_id number(5));
insert into customer values(3002,'Nick Rimando','New York',100,5001);
insert into customer values(3007,'Brad Davis','New York',200,5001);
insert into customer values(3005,'Graham Zusi','California',200,5002);
insert into customer values(3008,'Julian Green','London',300,5002);
insert into customer values(3004,'Fabian Johnson','Paris',300,5006);
insert into customer values(3009,'Geoff Cameron','Berlin',100,5003);
insert into customer values(3003,'Jozy Altidor','Moscow',200,5007);
insert into customer values(3001,'Brad Gulzan','London',null,5005);


create table elitesalesman(salesman_id number(5),name varchar2(20),city varchar2(10),commission float(5));
insert into elitesalesman values(5001,'James Hong','New York',0.15);
insert into elitesalesman values(5002,'Nail Knite','Paris',0.13);
insert into elitesalesman values(5005,'Pit ALex','London',0.11);
insert into elitesalesman values(5006,'Mc Lyon','Paris',0.14);
insert into elitesalesman values(5007,'Paul Adam','Rome',0.13);
insert into elitesalesman values(5003,'Lauson Hen','San jose',0.12);

CREATE VIEW incentive
AS SELECT DISTINCT salesman_id, name
FROM elitesalesman a
WHERE 3 <=
   (SELECT COUNT (*)
    FROM elitesalesman b
    WHERE a.salesman_id = b.salesman_id);

select * from incentive;



create view newyorkcity
as select distinct name 
from elitesalesman a 
where a.city = 'New York';

select * from newyorkcity;

create view idnamecity
as select salesman_id, name, city
from elitesalesman;

select * from idnamecity;