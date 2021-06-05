create package average as
    procedure average_finder;
    END average;

create or replace package body average as
procedure average_finder
is
avg1 NUMBER :=0 ;
sum1 NUMBER :=0 ;
count1 NUMBER :=0 ;
n NUMBER := 0;
BEGIN

WHILE (n1<>0)
LOOP
n := &enter_a_number;
count1 := count1 + 1;
sum1 := sum1 + n1;

END LOOP;
avg1 := sum1/count1;
DBMS_OUTPUT.PUT_LINE('the average is '||avg1);

END average_finder;
end average;

--start here
BEGIN
average.average_finder;
end;
show errors;