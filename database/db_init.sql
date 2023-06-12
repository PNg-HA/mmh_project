CREATE USER 'auth_user'@'localhost' IDENTIFIED BY 'Auth123';

CREATE DATABASE auth;

GRANT ALL PRIVILEGES ON auth.* TO 'auth_user'@'localhost';

USE auth;

CREATE TABLE user (
  id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
  username VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL
);

INSERT INTO user (username, password) VALUES ('quannguyen', 'quan123');

CREATE DATABASE gateway;

GRANT ALL PRIVILEGES ON gateway.* TO 'auth_user'@'localhost';
FLUSH PRIVILEGES;

USE gateway;

CREATE TABLE opaque (
    id INT AUTO_INCREMENT PRIMARY KEY,
    auth_key VARCHAR(255) NOT NULL,
    opaque_key VARCHAR(255) NOT NULL
);

CREATE DATABASE svc;

GRANT ALL PRIVILEGES ON svc.* TO 'auth_user'@'localhost';
FLUSH PRIVILEGES;


USE svc;

CREATE TABLE tasks (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    description VARCHAR(255),
    due_date DATE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);
