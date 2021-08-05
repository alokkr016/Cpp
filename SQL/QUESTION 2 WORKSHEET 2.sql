
CREATE TABLE College(EMPNO NUMBER(4),Name varchar(20),Dept VARCHAR2(25),DOB DATE,SALARY NUMBER(10));

INSERT INTO College(EMPNO, Name, Dept, DOB, SALARY) VALUES
(12,'Raj','Computer',TO_DATE('12/01/2016', 'DD/MM/YYYY'),23000);
INSERT INTO College(empno, name, dept, dob, salary)
VALUES (13,'Vivek','Chemistry',TO_DATE('16/06/2007','DD/MM/YYYY'),25000);
INSERT INTO College VALUES (14,'Ajay','Guard',TO_DATE('14/09/2008','DD/MM/YYYY'),52000);
INSERT INTO College VALUES (15,'Shivam','Cleaner',TO_DATE('14/09/2002','DD/MM/YYYY'),12400);
INSERT INTO College VALUES (16,'Mukesh','Driver',TO_DATE('14/09/2001','DD/MM/YYYY'),4000);

SELECT * FROM College Order by DOB ;
SELECT * FROM College Where Dept='Computer';
SELECT * FROM College Order by SALARY DESC;
SELECT COUNT(*), NAME
FROM College GROUP BY Dept, NAME;
SELECT * FROM College where SALARY>25000;






