--Here I am creating two table
CREATE TABLE Test
(
  test_id    INTEGER,
  value      NUMBER,
  test_date  DATE
);

CREATE TABLE Test_audit
(
  test_id    INTEGER,
  value      NUMBER,
  test_date  DATE
);

--Here I am creating trigger

CREATE TRIGGER trg_test
AFTER INSERT ON Test
FOR EACH ROW
WHEN (NEW.value > 1000)
BEGIN
    INSERT INTO Test_audit
    VALUES(:NEW.test_id, :NEW.value, :NEW.test_date);
END trg_test;

--Here I am Inserting two values into the table 
--just to verify whether my trigger is working or not

INSERT INTO Test values(
  1,1000,TO_DATE('14/09/2008','DD/MM/YYYY')
);
INSERT INTO Test values(
  2,1040,TO_DATE('15/09/2008','DD/MM/YYYY')
);

--Verifying the result
select * from Test_audit;







drop TRIGGER trg_test;
drop table Test;
drop table Test_audit;
show errors;