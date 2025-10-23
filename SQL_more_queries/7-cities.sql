-- Script create database hbtn_0d_usa and table cities
CREATE DATABASE IF NOT EXIST hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXIST cities (
    id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMERY KEY,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    CONSTRAINT fk_cities_state
        FOREIGN KEY (state_id) REFERENCE states(id)
);
