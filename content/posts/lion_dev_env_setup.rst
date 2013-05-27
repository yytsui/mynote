Lion Development Environment Setup
###################################

:date: 2012-03-08 10:20
:tags: mac, setup
:slug: mac_osx_lion_development_environment_setup
:author: Yiyang
:layout: post



Iterm2
=======
install `iterm2 <http://www.iterm2.com/>`_

Homebrew
========
install `homebrew <https://github.com/mxcl/homebrew/wiki/installation>`_

.. code-block:: bash

    /usr/bin/ruby -e "$(/usr/bin/curl -fksSL https://raw.github.com/mxcl/homebrew/master/Library/Contributions/install_homebrew.rb)"

curl and wget
=============

.. code-block:: bash

    brew install curl wget

macvim
======
to enable python and ruby interpreter

.. code-block:: bash

    brew install https://raw.github.com/mxcl/homebrew/master/Library/Formula/macvim.rb

then link vimrc and vimfile


set PATH
========
edit /etc/paths, make sure /usr/local/bin is before /usr/bin, then the brew installed vim
will be used, otherwise vim will call /usr/bin/vim which is defult from Apple.

git configuration
=================

.. code-block:: bash

    git config --global user.name "Your Name Comes Here"
    git config --global user.email you@yourdomain.example.com
    git config --global color.ui true

qgit
====
 install qt:

.. code-block:: bash

    %brew install qt

install modified version of qgit

.. code-block:: bash

    % git clone https://github.com/scalm/QGit-mod.git
    % qmake qgit.pro
    % make
    % make install
    % cp bin/path/to/qgit /usr/local/bin/


PostgreSQL
==========

.. code-block:: bash

    % brew install postgresql
    % initdb /usr/local/var/postgres #make sure this dir is empty, otherwise delete it and recreate it.

If this is your first install, automatically load on login with:

.. code-block:: bash

    % mkdir -p ~/Library/LaunchAgents
    % cp /usr/local/Cellar/postgresql/9.1.3/homebrew.mxcl.postgresql.plist ~/Library/LaunchAgents/
    % launchctl load -w ~/Library/LaunchAgents/homebrew.mxcl.postgresql.plist

If this is an upgrade and you already have the homebrew.mxcl.postgresql.plist loaded:

.. code-block:: bash

    % launchctl unload -w ~/Library/LaunchAgents/homebrew.mxcl.postgresql.plist
    % cp /usr/local/Cellar/postgresql/9.1.3/homebrew.mxcl.postgresql.plist ~/Library/LaunchAgents/
    % launchctl load -w ~/Library/LaunchAgents/homebrew.mxcl.postgresql.plist

Or start manually with:

.. code-block:: bash

 pg_ctl -D /usr/local/var/postgres -l /usr/local/var/postgres/server.log start

And stop with:

.. code-block:: bash

 pg_ctl -D /usr/local/var/postgres stop -s -m fast

PostGIS
=======

.. code-block:: bash

    % brew install postgis
    
==> Installing postgis dependency: gdal
==> Downloading http://download.osgeo.org/gdal/gdal-1.9.0.tar.gz
######################################################################## 100.0%
==> ./configure --prefix=/usr/local/Cellar/gdal/1.9.0 --mandir=/usr/local/Cellar/gdal/1.9.0/share/man --disable-debug --with-local=/usr/local/Cellar/gdal/1.9.0 --with-threads --w
==> make
==> make install
==> python setup.py install_lib --install-dir=/usr/local/Cellar/gdal/1.9.0/lib/python2.7/site-packages
==> make man
==> make install-man
==> Caveats
This version of GDAL was built with Python support.  In addition to providing
modules that makes GDAL functions available to Python scripts, the Python
binding provides ~18 additional command line tools.

Unless you are using Homebrew's Python, both the bindings and the
additional tools will be unusable unless the following directory is added to
the PYTHONPATH:

    /usr/local/lib/python2.7/site-packages

how to do this:
http://stackoverflow.com/questions/4757178/how-do-you-set-your-pythonpath-in-an-already-created-virtualenv

==> Installing postgis
==> Downloading http://postgis.org/download/postgis-2.0.0.tar.gz
######################################################################## 100.0%
==> ./configure --with-projdir=/usr/local --with-jsondir=/usr/local/Cellar/json-c/0.9 --with-pgconfig=/usr/local/Cellar/postgresql/9.1.3/bin/pg_config --disable-nls
==> make
==> make install DESTDIR=/private/tmp/homebrew-postgis-2.0.0-6cqA/postgis-2.0.0/stage
==> Caveats
To create a spatially-enabled database, see the documentation:
http://postgis.refractions.net/documentation/manual-1.5/ch02.html#id2630392
and to upgrade your existing spatial databases, see here:
http://postgis.refractions.net/documentation/manual-1.5/ch02.html#upgrading

PostGIS SQL scripts installed to:
  /usr/local/share/postgis
PostGIS plugin libraries installed to:
  /usr/local/Cellar/postgresql/9.1.3/lib
PostGIS extension modules installed to:
  /usr/local/Cellar/postgresql/9.1.3/share/postgresql/extension

Pgadmin3
========
Downlad and install, add a new service localhost, username and password are the same with the mac user.


MySQL
=====
 Read the `instruction <http://gpiot.com/mac-os-x-lion-the-perfect-setup-for-python-django/>`_ here.

Install
-------

Download the MySQL installation package:
Mac OS X ver. 10.6 (x86, 64-bit), DMG Archive
Install the app as you normally would, double-click the DMG file and follow the instructions. I recommend to 
install the 3 items: the main package, the startup item and the preference panel widget (for added control in  your System Preferences).
Once it’s all installed, go to your System Preferences, go to MySQL, and start the server.

set PATH
--------
append /usr/local/mysql/bin to /etc/paths

Setup MySQL users:
------------------

First, we want to reset the root password.

.. code-block:: bash

    % mysqladmin -u root password NEWPASSWORD

Then, I like to create a personal user for connecting locally (rather than connecting with root).
Start MySQL:

.. code-block:: bash

    % /usr/local/mysql/bin/mysql -u root -p

(Then enter your root password)
Create a new user and assign it all privileges on all databases, or on a specific database (up to you!).

.. code-block:: bash

    mysql> CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
    mysql> GRANT ALL PRIVILEGES ON *.* TO 'username'@'localhost';

Sequel Pro
----------
I like to use Sequel Pro to manage my database and users, rather than using the command line.
If you are re-intalling Sequel Pro, you may want to copy and move you favourites from that path,
from one machine to another: ~/Library/Preferences/com.google.code.sequel-pro.plist

Install mysql-python
--------------------
In a specific virtualenv,

.. code-block:: bash

    pip install mysql-python

If you got error message, check if /usr/local/mysql/bin is in PATH.


.. code-block:: bash

    % ipython
    % import MySQLdb

It’s likely you will come with the following error:
Library not loaded: libmysqlclient.18.dylib
Here’s how I fixed it, add the following line to your  ~/.bash_profile:

.. code-block:: bash

    export DYLD_LIBRARY_PATH=/usr/local/mysql/lib:$DYLD_LIBRARY_PATH

Save the file and then re-open a new Terminal window for the changes to take effect!
That should be fixed!



pygame
======

Pretty important to get the latest `SDL_image.framework <http://www.libsdl.org/projects/SDL_image/>`_ if you want actual PNG/JPEG support:

Otherwise it will only load Windows BMP files as you will see this during the build:

/Library/Frameworks//SDL_image.framework/SDL_image, missing required architecture x86_64 in file

To Install:
Down load the dmg file, double click
Copy the SDL_image.framework to /Library/Frameworks


.. code-block:: bash

    brew install sdl sdl_image sdl_mixer sdl_ttf smpeg portmidi
    pip install hg+http://bitbucket.org/pygame/pygame  #in virtualenv


redis
=====


.. code-block:: bash

    brew install redis

==> Caveats
If this is your first install, automatically load on login with:

.. code-block:: bash

    mkdir -p ~/Library/LaunchAgents
    cp /usr/local/Cellar/redis/2.4.13/homebrew.mxcl.redis.plist ~/Library/LaunchAgents/
    launchctl load -w ~/Library/LaunchAgents/homebrew.mxcl.redis.plist

If this is an upgrade and you already have the homebrew.mxcl.redis.plist loaded:

.. code-block:: bash

    launchctl unload -w ~/Library/LaunchAgents/homebrew.mxcl.redis.plist
    cp /usr/local/Cellar/redis/2.4.13/homebrew.mxcl.redis.plist ~/Library/LaunchAgents/
    launchctl load -w ~/Library/LaunchAgents/homebrew.mxcl.redis.plist

To start redis manually:

.. code-block:: bash

    redis-server /usr/local/etc/redis.conf

To access the server:

.. code-block:: bash

    redis-cli


neo4j
=====

.. code-block:: bash

    brew install neo4j

==> Caveats
Quick-start guide:

    1. Start the server manually:
        neo4j start

    2. Open webadmin:
        open http://localhost:7474/webadmin/

    3. Start exploring the REST API:
        curl -v http://localhost:7474/db/data/

    4. Stop:
        neo4j stop

To launch on startup, install launchd-agent to ~/Library/LaunchAgents/ with:
    neo4j install

If this is an upgrade, see:
    /usr/local/Cellar/neo4j/community-1.7-unix/libexec/UPGRADE.txt

The manual can be found in:
    /usr/local/Cellar/neo4j/community-1.7-unix/libexec/doc/

