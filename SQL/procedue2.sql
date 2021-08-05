CREATE PACKAGE circle AS
    FUNCTION area(radius NUMBER) RETURN DECIMAL;
    function circumference(radius NUMBER) RETURN DECIMAL;
    END circle;


--package Body
create or replace PACKAGE body circle as
--Area
    function area(radius NUMBER)
    return DECIMAL
    
    is
    circle_area DECIMAL;
    BEGIN
    circle_area := 3.14 * radius * radius; 
    RETURN circle_area;
    END area;
--circumference
    function circumference(radius NUMBER)
    RETURN DECIMAL
    is
    circle_circumference DECIMAL;
    BEGIN
    circle_circumference := 2 * 3.14 * radius;
    RETURN circle_circumference;
    END circumference;
END circle;

 --Result 
BEGIN
  DBMS_OUTPUT.PUT_LINE ('area ' || circle.area(7) );
  DBMS_OUTPUT.PUT_LINE('circumference ' || circle.circumference(7));
END; 

