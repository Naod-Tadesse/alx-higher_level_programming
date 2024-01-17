-- script creates msql sever for user

CREATE USER IF NOT EXISTS 
user_0d_1@localhost IDENTIFIED BY 'user_0d_1';
GRANT ALL PRIVILEGES
ON *.* TO 'user_0d_1'@'
IDENTIFIED BY 'user_0d_1_pwd';
FLUSH PRIVILEGES;
