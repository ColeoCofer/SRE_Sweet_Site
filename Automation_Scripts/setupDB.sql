CREATE DATABASE sreproject;
CREATE USER sreprojectuser WITH PASSWORD 'trump';
ALTER ROLE sreprojectuser SET client_encoding TO 'utf8';
ALTER ROLE sreprojectuser SET client_encoding TO 'utf8';
ALTER ROLE sreprojectuser SET timezone TO 'UTC';
GRANT ALL PRIVILEGES ON DATABASE sreproject TO sreprojectuser;