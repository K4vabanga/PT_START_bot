CREATE DATABASE DB_DATABASE;

CREATE USER DB_USER WITH REPLICATION ENCRYPTED PASSWORD 'DB_PASSWORD';
GRANT ALL PRIVILEGES ON DATABASE DB_DATABASE TO DB_USER;

CREATE USER DB_REPL_USER WITH REPLICATION ENCRYPTED PASSWORD 'DB_REPL_PASSWORD';

\connect DB_DATABASE;

CREATE TABLE IF NOT EXISTS emails (
    ID SERIAL PRIMARY KEY,
    Email VARCHAR(100) NOT NULL
);

CREATE TABLE IF NOT EXISTS phones (
    ID SERIAL PRIMARY KEY,
    PhoneNumber VARCHAR(100) NOT NULL
);

INSERT INTO emails(Email) VALUES('mail@mail.mail');
INSERT INTO emails(Email) VALUES('a2@a.a');
INSERT INTO phones(PhoneNumber) VALUES('+7(952)8125252');
INSERT INTO phones(PhoneNumber) VALUES('80000000000');
