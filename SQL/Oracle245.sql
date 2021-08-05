create package average as
    procedure average_finder(n IN NUMBER);
    END average;

create or replace package body average as
procedure average_finder(n IN number)

is
avg NUMBER :=0 ;
sum1 NUMBER :=0 ;
count1 NUMBER :=0 ;
BEGIN
n1 := n;
WHILE n1>0
LOOP
count1 := count1 + 1;
sum1 := sum1 + n1;

END LOOP;
avg := sum1/count1;
DBMS_OUTPUT.PUT_LINE('the average is'||avg);

END average_finder;
end average;

--here
declare
n NUMBER;

BEGIN
n := &enter_a_number;
average.average_finder(n);

end;


drop package average;
show errors;