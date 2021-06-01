# flaskmysql


pip install flask

pip install flask-mysql

pip install pymysql

mysql -u root -p 
default password 1234

create database flaskapp

use flaskapp
create table Myusers( firstname varchar(20), lastname varchar(20))
select * from Myusers


# WITH AWS RDS AND DOCKER IMAGE:
================================

Once the database is ready, copy the below details:

        database-1.cgoiztchij9u.us-east-1.rds.amazonaws.com
        3306
        user: admin
        password: pwd

![image](https://user-images.githubusercontent.com/54719289/106190341-8b697180-61cf-11eb-92a0-449fcfff269c.png)

# Run the docker image in EC2 instance after docker installation & start the service:
  
      docker pull mysql/mysql-server
      
   ![image](https://user-images.githubusercontent.com/54719289/106191063-63c6d900-61d0-11eb-9fdb-f8727ec22de5.png)
  
     docker run --name mysqlserver -d mysql/mysql-server:latest

  ![image](https://user-images.githubusercontent.com/54719289/106191438-dfc12100-61d0-11eb-85de-5408c6456530.png)

      Run with port number: 3306
      
      
     docker run --name mysqlserver -p 3306:3306 -d mysql/mysql-server:latest
     
  ![image](https://user-images.githubusercontent.com/54719289/106191850-65dd6780-61d1-11eb-9009-53da16cb4949.png)
   
     
# Inside container set the password:

    ALTER USER 'admin'@'localhost' IDENTIFIED BY 'pwd'
  
    since mysql  password needs to e passed with docker run:
  
  ![image](https://user-images.githubusercontent.com/54719289/106192638-780bd580-61d2-11eb-8d09-62c84f279570.png)


# docker run with mysql password:

    docker run --name mysqlserver -p 3306:3306 --env='MYSQL_ROOT_PASSWORD=password1' -d mysql/mysql-server:latest
    
    Enter password as password1
    
 ![image](https://user-images.githubusercontent.com/54719289/106193279-4e06e300-61d3-11eb-927e-7e59de010c08.png)
 
 
 Note: CHange this password in python application
   
# Docker run with rds host:

```
 docker run --name mysql  --env='MYSQL_ROOT_PASSWORD=admin123'  -h db1.cdcey7nbdoev.us-east-1.rds.amazonaws.com -p 3306:3306 -d mysql/mysql-server:latest
 docker exec -it mysql bash
 mysql -u root -p
 show databases;
 create database user;
 use user;
 create table userdetail(empno integer, empname varchar(20));
 insert into userdetail values(101,'Archu');
 insert into userdetail values(102,'Architha');
 select * from userdetail;
 
mysql> select * from userdetail;
+-------+----------+
| empno | empname  |
+-------+----------+
|   101 | Archu    |
|   102 | Architha |
+-------+----------+
2 rows in set (0.00 sec)



        
```
![image](https://user-images.githubusercontent.com/54719289/120368631-3323b700-c30a-11eb-944a-3de2c547737e.png)



# Docker run with rds host and volume:

```
 docker run --name mysql  -v /tmp/storedb:/var/lib/mysql --env='MYSQL_ROOT_PASSWORD=admin123'  -h db1.cdcey7nbdoev.us-east-1.rds.amazonaws.com -p 3306:3306 -d mysql/mysql-server:latest
 
 docker exec mysql sh -c 'exec mysqldump --all-databases -u root -p admin123' > /tmp/dump.sql
```
