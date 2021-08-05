DECLARE
   fact number :=2;
   n number := &1;
BEGIN
   while n > 0 loop
      fact:=n*fact;
      n:=n-1;
   end loop;
   dbms_output.put_line(fact);
END;