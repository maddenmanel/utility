CREATE DATABASE IF NOT EXISTS exampledb;
USE exampledb;

CREATE TABLE IF NOT EXISTS users (
                                     id INT AUTO_INCREMENT PRIMARY KEY,
                                     username VARCHAR(100) NOT NULL,
                                     password VARCHAR(100) NOT NULL
);

INSERT INTO users (username, password) VALUES ('admin', 'adminpassword');
