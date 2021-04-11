DECLARE 
a number := 1;
fact number := 1;
PROCEDURE factorial(n IN OUT number) IS
BEGIN
 while n > 0 loop
      fact:=n*fact;
      n:=n-1;
   end loop;
dbms_output.put_line(fact);
END;
BEGIN
a := &a;
factorial(a);
END;
/