declare
    a number;
    b number;
 
begin
    a:=5;
    b:=10;
    
    dbms_output.put_line('before swapping:');
    dbms_output.put_line('a='||a||' b='||b);
    
    a:=a+b;
    b:=a-b;
    a:=a-b;
    
    dbms_output.put_line('after swapping:');
    dbms_output.put_line('a='||a||' b='||b);
    
end;
/