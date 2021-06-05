DECLARE 
    si number(9,2);
    fact number(9,2);
p  NUMBER(9, 2);   
    r  NUMBER(9, 2);    
    t  NUMBER(9, 2);
PROCEDURE simpleintrest(p IN OUT number,r IN OUT number,t IN OUT number) IS
BEGIN
    si := ( p * r * t ) / 100;
    dbms_output.Put_line('Simple Interest = ' ||si);    
END;

BEGIN
    p := &p;
    r := &r;
    t := &t;
    simpleintrest(p,r,t);
END;