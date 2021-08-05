
DECLARE
    vCOUNT   NUMBER;
    prime   NUMBER;
    vSUM     NUMBER;
    i       NUMBER;
    j       NUMBER;
BEGIN
    vSUM := 2;
    vCOUNT := 0;
    prime := 1;
    i := 3;

    WHILE vCOUNT < 100
    LOOP
        j := i / 2;

        FOR k IN 2 .. j
        LOOP
            IF i MOD j = 0
            THEN
                prime := 0;
            END IF;

            IF prime = 1
            THEN
                vSUM := vSUM + i;
                vCOUNT := vCOUNT + 1;
            END IF;
        END LOOP;

        i := i + 1;
    END LOOP;

    DBMS_OUTPUT.put_line (vSUM);
END;
/