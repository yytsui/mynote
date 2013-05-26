Backup wordpress site and move to a new host
############################################
:date: 2010-04-20 19:34
:author: yiyang
:category: Uncategorized
:slug: backup-wordpress-site-and-move-to-a-new-host

| 1.Backup the mysql database:
|  The db\_host\_name, db\_user\_name and db\_name can be found in
wp-config.php

::

    $mysqldump --add-drop-table -h db_host_name -u db_user_name -p db_name | bzip2 -c > ~/weblog.sql.bz2

2 Create a new mysql database:

::

    $ mysql -u root -p
    Enter password: 
    Welcome to the MySQL monitor.  Commands end with ; or \g.
    Your MySQL connection id is 149
    Server version: 5.1.41-3ubuntu12.8 (Ubuntu)
    Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.
    create database new_db_name;
    GRANT ALL ON new_db_name.* TO new_db_user_name@localhost IDENTIFIED BY "new_db_password"

| 3.Use scp or ftp to copy all wordpress files and database backup file
weblog.sql.bz2 to new host.
|  4.Change the wp-config.php to new db settings as the new one just
created.
|  5.Restore the data into the new database:

::

     $bunzip2 weblog.sql.bz2

| Note: If you want to deploy to a new domain, you may like open the
weblog.sql file use any text editor you like to
|  find the all 'olddomain.com' and replace them with 'newdomain.com'

::

     $mysql -h localhost -u weblog -p weblog < weblog.sql

