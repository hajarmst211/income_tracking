-- test_query.sql


INSERT INTO users (username, first_name, last_name, password_hash) VALUES
('jdoe', 'John', 'Doe', 'pbkdf2:sha256:600000$randomhash');
