-- Prepares a MySQL server for the project

CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- Create a new user if the user does not exist
CREATE USER IF NOT EXISTS 'hbnb_test'@'localhost' IDENTIFIED BY 'hbnb_test_pwd';
-- Grant permissions
GRANT ALL PRIVILEGES ON hbnb_test_db.* TO 'hbnb_test'@'localhost';
-- Grant select priviledges on performance_schema
GRANT SELECT ON performance_schema.* TO 'hbnb_test'@'localhost';
-- Flush privileges
FLUSH PRIVILEGES;
