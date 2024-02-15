-- creates the database hbtn_0d_2 and user user_0d_2
-- creating  database
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- creating a user
CREATE USER IF NOT EXISTS user_0d_2@localhost IDENTIFIED BY 'user_0d_2_pwd';
-- grants SELECT privileges to the user
GRANT SELECT ON hbtn_0d_2.* TO user_0d_2@localhost;
