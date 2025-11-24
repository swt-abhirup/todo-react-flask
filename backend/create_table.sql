-- create_table.sql
-- Creates the todos table for SQLite (fields: id, task, completed, created_at)

PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS todos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL,
    completed INTEGER NOT NULL DEFAULT 0,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
