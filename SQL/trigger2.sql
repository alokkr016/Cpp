
create table employee(
    id INTEGER,
    age NUMBER
);

CREATE TRIGGER  Check_age  BEFORE INSERT ON employee 
FOR EACH ROW
BEGIN
IF NEW.age < 25 THEN
SET MESSAGE_TEXT = 'ERROR: 
         AGE MUST BE ATLEAST 25 YEARS!';
END IF;
END;

