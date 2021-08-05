DECLARE
    grade CHAR(1);
BEGIN
    grade := '2';
    CASE
        WHEN grade = 'A' THEN DBMS_OUTPUT.PUT_LINE('Excellent');
        WHEN grade = 'B' THEN DBMS_OUTPUT.PUT_LINE('Very Good');
        WHEN grade = 'C' THEN DBMS_OUTPUT.PUT_LINE('Good');
        WHEN grade = 'D' THEN DBMS_OUTPUT.PUT_LINE('fair');
        WHEN grade = 'F' THEN DBMS_OUTPUT.PUT_LINE('Poor');  
    END CASE;
EXCEPTION
    WHEN CASE_NOT_FOUND THEN
        DBMS_OUTPUT.PUT_LINE('No such grade');
END;

        