-- A script that create table id_not_null on my SQL server
CREATE TABLE IF NOT EXISTs unique_id (
    id INT  DEFAULT 1 UNIQUE,
    name varchar(256)
);
