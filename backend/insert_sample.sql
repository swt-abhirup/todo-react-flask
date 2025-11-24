-- insert_sample.sql
-- Inserts some example todo rows for testing

BEGIN TRANSACTION;

INSERT INTO todos (task, completed) VALUES ('Buy milk', 0);
INSERT INTO todos (task, completed) VALUES ('Write README for todo-app', 0);
INSERT INTO todos (task, completed) VALUES ('Fix bug in auth flow', 1);
INSERT INTO todos (task, completed, created_at) VALUES ('Add docker-compose.yml', 0, '2025-11-01 09:15:00');
INSERT INTO todos (task, completed) VALUES ('Prepare demo GIF', 0);

COMMIT;
