.. _database:

==============
Database Notes
==============


Install and Configure PostgreSQL
================================

 1. install postgrelsql: https://help.ubuntu.com/community/PostgreSQL

.. code-block:: bash

     $ sudo apt-get install postgresql pgadmin3

2. server setup: 
     To start off, we need to change the PostgreSQL postgres user password; we will not be able to access the server otherwise. 
     As the “postgres” Linux user, we will execute the psql command. This will be also used in pgadmin3 to connect to the pogresql server.

.. code-block:: bash

     $ sudo -u postgres psql postgres
     \password postgres

3. create a Postgres user who also can create a database.

.. code-block:: bash

    $ sudo su postgres 
    $ createuser rhinocloud -P 
      Enter password for new role: (enter password here) rhinocloud
      Enter it again: (enter password here) 
      Shall the new role be a superuser? (y/n) n 
      Shall the new role be allowed to create databases? (y/n) y 
      Shall the new role be allowed to create more new roles? (y/n) n 
    $ exit

4. create a postgres database with owner

.. code-block:: bash

   $ createdb --encoding=UNICODE --owner=rhinobooks rhinobooks

interactive postgresql
======================

.. code-block:: bash

    psql -d database_name -U user_name


  if the error message: psql: FATAL: Ident authentication failed for user "user_name"
  change the pg_hba.conf http://www.cyberciti.biz/faq/psql-fatal-ident-authentication-failed-for-user/ 
  ~/.pgpss
  md5? ident?

How can I see the raw SQL queries Django is running?
====================================================
http://docs.djangoproject.com/en/dev/faq/models/#how-can-i-see-the-raw-sql-queries-django-is-running
Make sure your Django DEBUG setting is set to True. Then, just do this:

.. code-block:: python

    >>> from django.db import connection
    >>> connection.queries
    [{'sql': 'SELECT polls_polls.id,polls_polls.question,polls_polls.pub_date FROM polls_polls',
    'time': '0.002'}]

connection.queries is only available if DEBUG is True. It's a list of dictionaries in order of query execution. Each dictionary has the following:

sql == The raw SQL statement,
time == How long the statement took to execute, in seconds.

connection.queries includes all SQL statements == INSERTs, UPDATES, SELECTs, etc. Each time your app hits the database, the query will be 
recorded. Note that the raw SQL logged in connection.queries may not include parameter quoting. Parameter quoting is performed by the 
database-specific backend, and not all backends provide a way to retrieve the SQL after quoting.


How to compare two postgresql schema:
=====================================
* dump schema from db:

.. code-block:: bash

   sudo su postgres
   pg_dump -s database_name > production_schema.sql
   pg_dump -s database_name > development_schema.sql

* apgdiff

download and install `apgdiff <http://apgdiff.sourceforge.net/>`_

.. code-block:: bash

  java -jar apgdiff.jar production_schema.sql development_schema_dump.sql > diff.sql


Backup and restore postgresql database:
=======================================

.. code-block:: bash

   sudo su postgres
   pg_dump database_name > /tmp/backup.sql
   (password: postgres's password)

to restore:

.. code-block:: bash

   psql dbname < backup.sql

http://www.postgresql.org/docs/8.1/interactive/backup.html


