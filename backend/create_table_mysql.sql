-- create_table_mysql.sql
-- Creates database and todos table for MySQL / MariaDB

-- Optional: create a database (change name as you like)
CREATE DATABASE IF NOT EXISTS todo_app CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;
USE todo_app;

CREATE TABLE IF NOT EXISTS todos (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    task TEXT NOT NULL,
    completed TINYINT(1) NOT NULL DEFAULT 0,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;
