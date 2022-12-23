-- This is a SQL script that creates a sample MySQL database.

CREATE DATABASE IF NOT EXISTS demo_db;
USE demo_db;

DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id int(11) NOT NULL AUTO_INCREMENT,
  username varchar(255) DEFAULT NULL,
  PRIMARY KEY (id)
);
INSERT INTO users VALUES (1,'A first user'), (2, 'A second user');

DROP TABLE IF EXISTS measurements;
CREATE TABLE measurements (
  id int(11) NOT NULL AUTO_INCREMENT,
  user_id int(11) DEFAULT NULL,
  type varchar(255) DEFAULT NULL,
  value decimal(19,2) DEFAULT NULL,
  PRIMARY KEY (id),
  KEY `FK175jrgmth3sqngovh75yyql3q` (user_id),
  CONSTRAINT `FK175jrgmth3sqngovh75yyql3q` FOREIGN KEY (user_id) REFERENCES users (id)
);
INSERT INTO measurements VALUES (1,1,'TEMPERATURE', 32.4), (2,2,'TEMPERATURE', 28.5),(3,1,'WEIGHT', 45),(4,1,'WEIGHT', 23),(5,1,'WEIGHT', 65),(6,1,'WEIGHT', 51),(7,2,'WEIGHT', 64),(8,2,'WEIGHT', 67),(9,2,'WEIGHT', 49);

