create table alok2(id number(10) primary key,name varchar2(100));  
create or replace procedure "INSERTUSER"    
(id IN NUMBER,    
name IN VARCHAR2)    
is    
begin    
insert into alok2 values(id,name);    
end;    
/   
BEGIN    
   insertuser(101,'Rahul');  
   dbms_output.put_line('record inserted successfully');    
END;    


select * from alok2;