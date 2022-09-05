-- A script that create table id_not_null on my SQL server
CREATE TABLE IF NOT EXISTs id_not_null (
    id INT  DEFAULT 1,
    name varchar(256)
);
