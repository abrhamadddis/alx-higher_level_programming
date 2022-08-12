-- creates a table called Second_tabele in the current database in your MySQL server.
CREATE TABLE IF NOT EXISTS second_table (
	id INT,
	name VARCHAR(256),
    score INT
);
-- insert some data
INSERT INTO second_table vALUES (1, "John", 10);
INSERT INTO second_table vALUES (2, "Alex", 3);
INSERT INTO second_table vALUES (3, "Bob", 14);
INSERT INTO second_table vALUES (4, "George", 8);
