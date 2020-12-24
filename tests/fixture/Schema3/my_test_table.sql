/*
Purpose:
This a new table to show how auto documentation can add new objects quickly.
Dependent Objects:
    Type    |Name
    Schema   |my_test_schema
ChangeLog:
	Date    |    Author    |    Ticket    |    Modification
	2020-10-26    |  Developer_2  |   T-220    |    Initial Definition
*/
CREATE TABLE IF NOT EXISTS my_test_schema.my_test_table (
    name character varying,
    value smallint,
    object_owner character varying
) DISTRIBUTED BY (name, value)
PARTITION BY (object_owner)
;
