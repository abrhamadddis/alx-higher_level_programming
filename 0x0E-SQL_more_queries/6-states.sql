-- A Script that create a Data base hbtn_0d_usa and the table states
-- (in the database hbtn_0d_usa) on your MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
use hbtn_0d_usa
CREATE TABLE states(
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  name varchar(256) NOT NULL
);