CREATE DATABASE djangokurs;
CREATE USER djangokurs_adminuser WITH PASSWORD 'Sifra123!';
ALTER ROLE djangokurs_adminuser SET client_encoding TO 'utf8';
ALTER ROLE djangokurs_adminuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE djangokurs_adminuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE djangokurs TO djangokurs_adminuser;

ALTER USER djangokurs_adminuser WITH PASSWORD 'Sifra123!';
