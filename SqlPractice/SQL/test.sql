DECLARE
n NUMBER;
avg1 NUMBER :=0;
sum1 NUMBER :=0;
count1 NUMBER := 0;
BEGIN
n := &enter_a_number;
WHILE(n<>0)
LOOP

count1 := count1+1;
sum1 := sum1+n;
n := &enter_a_number;
END LOOP;
avg1 := sum1/count1;
DBMS_OUTPUT.PUT_LINE('the average is'||avg1);
END;