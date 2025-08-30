# picoGym Level 303: SQL Direct
Source: https://play.picoctf.org/practice/challenge/303

## Goal
Connect to this PostgreSQL server and find the flag!<br>
psql -h saturn.picoctf.net -p 49940 -U postgres pico<br>
Password is <b>postgres</b>

## What I learned
```
Postgres Basics

# Clear
\! clear                    \! cls
# List Databases
\list                       \l                  SHOW DATABASES;
# Connect to a database
\c mydatabase
# List tables in the current database/schema
\dt                                             SHOW TABLES;
# List all relations (tables, views, sequences)
\d
# Describe a table’s structure (column
s, types, constraints)
\d tablename
# List users/roles
\du

# SQL Standard
SELECT * FROM tablename LIMIT 10;

Optional Youtube: https://www.youtube.com/watch?v=MgKd0yKTMI8
```

## Solution
```
https://webshell.picoctf.org/

AsianHacker-picoctf@webshell:~$ psql -h saturn.picoctf.net -p 49940 -U postgres pico ⌨️
Password for user postgres: ⌨️
psql (14.17 (Ubuntu 14.17-0ubuntu0.22.04.1), server 15.2 (Debian 15.2-1.pgdg110+1))
WARNING: psql major version 14, server major version 15.
         Some psql features might not work.
Type "help" for help.

pico=# help ⌨️
You are using psql, the command-line interface to PostgreSQL.
Type:  \copyright for distribution terms
       \h for help with SQL commands ❤️
       \? for help with psql commands ❤️
       \g or terminate with semicolon to execute query
       \q to quit 👀
pico=# \h ⌨️
Available help:
  ABORT                            ALTER SEQUENCE                   CREATE AGGREGATE                 CREATE SUBSCRIPTION              DROP EXTENSION                   DROP TEXT SEARCH PARSER          REVOKE
  ALTER AGGREGATE                  ALTER SERVER                     CREATE CAST                      CREATE TABLE                     DROP FOREIGN DATA WRAPPER        DROP TEXT SEARCH TEMPLATE        ROLLBACK
  ALTER COLLATION                  ALTER STATISTICS                 CREATE COLLATION                 CREATE TABLE AS                  DROP FOREIGN TABLE               DROP TRANSFORM                   ROLLBACK PREPARED
  ALTER CONVERSION                 ALTER SUBSCRIPTION               CREATE CONVERSION                CREATE TABLESPACE                DROP FUNCTION                    DROP TRIGGER                     ROLLBACK TO SAVEPOINT
  ALTER DATABASE                   ALTER SYSTEM                     CREATE DATABASE                  CREATE TEXT SEARCH CONFIGURATION DROP GROUP                       DROP TYPE                        SAVEPOINT
  ALTER DEFAULT PRIVILEGES         ALTER TABLE                      CREATE DOMAIN                    CREATE TEXT SEARCH DICTIONARY    DROP INDEX                       DROP USER                        SECURITY LABEL
  ALTER DOMAIN                     ALTER TABLESPACE                 CREATE EVENT TRIGGER             CREATE TEXT SEARCH PARSER        DROP LANGUAGE                    DROP USER MAPPING                SELECT
  ALTER EVENT TRIGGER              ALTER TEXT SEARCH CONFIGURATION  CREATE EXTENSION                 CREATE TEXT SEARCH TEMPLATE      DROP MATERIALIZED VIEW           DROP VIEW                        SELECT INTO
  ALTER EXTENSION                  ALTER TEXT SEARCH DICTIONARY     CREATE FOREIGN DATA WRAPPER      CREATE TRANSFORM                 DROP OPERATOR                    END                              SET
  ALTER FOREIGN DATA WRAPPER       ALTER TEXT SEARCH PARSER         CREATE FOREIGN TABLE             CREATE TRIGGER                   DROP OPERATOR CLASS              EXECUTE                          SET CONSTRAINTS
  ALTER FOREIGN TABLE              ALTER TEXT SEARCH TEMPLATE       CREATE FUNCTION                  CREATE TYPE                      DROP OPERATOR FAMILY             EXPLAIN                          SET ROLE
  ALTER FUNCTION                   ALTER TRIGGER                    CREATE GROUP                     CREATE USER                      DROP OWNED                       FETCH                            SET SESSION AUTHORIZATION
  ALTER GROUP                      ALTER TYPE                       CREATE INDEX                     CREATE USER MAPPING              DROP POLICY                      GRANT                            SET TRANSACTION
  ALTER INDEX                      ALTER USER                       CREATE LANGUAGE                  CREATE VIEW                      DROP PROCEDURE                   IMPORT FOREIGN SCHEMA            SHOW
  ALTER LANGUAGE                   ALTER USER MAPPING               CREATE MATERIALIZED VIEW         DEALLOCATE                       DROP PUBLICATION                 INSERT                           START TRANSACTION
  ALTER LARGE OBJECT               ALTER VIEW                       CREATE OPERATOR                  DECLARE                          DROP ROLE                        LISTEN                           TABLE
  ALTER MATERIALIZED VIEW          ANALYZE                          CREATE OPERATOR CLASS            DELETE                           DROP ROUTINE                     LOAD                             TRUNCATE
  ALTER OPERATOR                   BEGIN                            CREATE OPERATOR FAMILY           DISCARD                          DROP RULE                        LOCK                             UNLISTEN
  ALTER OPERATOR CLASS             CALL                             CREATE POLICY                    DO                               DROP SCHEMA                      MOVE                             UPDATE
  ALTER OPERATOR FAMILY            CHECKPOINT                       CREATE PROCEDURE                 DROP ACCESS METHOD               DROP SEQUENCE                    NOTIFY                           VACUUM
  ALTER POLICY                     CLOSE                            CREATE PUBLICATION               DROP AGGREGATE                   DROP SERVER                      PREPARE                          VALUES
  ALTER PROCEDURE                  CLUSTER                          CREATE ROLE                      DROP CAST                        DROP STATISTICS                  PREPARE TRANSACTION              WITH
  ALTER PUBLICATION                COMMENT                          CREATE RULE                      DROP COLLATION                   DROP SUBSCRIPTION                REASSIGN OWNED                   
  ALTER ROLE                       COMMIT                           CREATE SCHEMA                    DROP CONVERSION                  DROP TABLE                       REFRESH MATERIALIZED VIEW        
  ALTER ROUTINE                    COMMIT PREPARED                  CREATE SEQUENCE                  DROP DATABASE                    DROP TABLESPACE                  REINDEX                          
  ALTER RULE                       COPY                             CREATE SERVER                    DROP DOMAIN                      DROP TEXT SEARCH CONFIGURATION   RELEASE SAVEPOINT                
  ALTER SCHEMA                     CREATE ACCESS METHOD             CREATE STATISTICS                DROP EVENT TRIGGER               DROP TEXT SEARCH DICTIONARY      RESET 
pico-# SHOW DATABASES; ⌨️
ERROR:  syntax error at or near "d"
LINE 1: d/
        ^
pico=# \list ⌨️
                                 List of databases
   Name    |  Owner   | Encoding |  Collate   |   Ctype    |   Access privileges   
-----------+----------+----------+------------+------------+-----------------------
 pico      | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 👀
 postgres  | postgres | UTF8     | en_US.utf8 | en_US.utf8 | 
 template0 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
 template1 | postgres | UTF8     | en_US.utf8 | en_US.utf8 | =c/postgres          +
           |          |          |            |            | postgres=CTc/postgres
(4 rows)
pico=# \dt ⌨️
         List of relations
 Schema | Name  | Type  |  Owner   
--------+-------+-------+----------
 public | flags👀 | table | postgres
(1 row)

pico=# \d flags ⌨️
                        Table "public.flags"
  Column   |          Type          | Collation | Nullable | Default 
-----------+------------------------+-----------+----------+---------
 id        | integer                |           | not null | 
 firstname | character varying(255) |           |          | 
 lastname  | character varying(255) |           |          | 
 address   | character varying(255) |           |          | 
Indexes:
    "flags_pkey" PRIMARY KEY, btree (id)
pico=# SELECT * FROM flags; ⌨️
 id | firstname | lastname  |                address                 
----+-----------+-----------+----------------------------------------
  1 | Luke      | Skywalker | picoCTF{L3arN_S0m3_5qL_t0d4Y_73b0678f} 🔐
  2 | Leia      | Organa    | Alderaan
  3 | Han       | Solo      | Corellia
(3 rows)
```

## Flag
picoCTF{L3arN_S0m3_5qL_t0d4Y_73b0678f}

## Continue
[Continue](./picoGym0358.md)