-- Creates database 'hbtn_0d_usa' and the table 'states' in the same database im MySQL server.
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(id INT PRIMARY KEY AUTO_INCREMENT UNIQUE NOT NULL, name VARCHAR(256) NOT NULL);
