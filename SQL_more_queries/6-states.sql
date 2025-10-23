-- Script create database and table states
CREATE DATABASE IF NOT EXIST hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXIST states (
    id INT NOT NULL AUTO_INCREMENT UNIQUE PRIMERY KEY,
    name VARCHAR(256) NOT NULL
);
