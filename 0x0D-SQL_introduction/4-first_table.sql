-- a script that create a table called first table 
-- the data base  name will be passed as the argument of mysql command
USE MySQL
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256)
);