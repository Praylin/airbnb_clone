create user 'airbnb_user_dev'@'%' identified by 'airbnb_dev password';
create user 'airbnb_user_prod'@'localhost' identified by 'airbnb_prod password';
create database airbnb_dev;
create database airbnb_prod;
grant all privileges on airbnb_dev.* to airbnb_user_dev;
grant all privileges on airbnb_prod.* to airbnb_user_prod;
