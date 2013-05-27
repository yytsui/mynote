author: yiyang
comments: true
date: 2011-02-10 22:49:43
layout: post
slug: deploying-django-project-with-nginx-and-uwsgi-in-ubuntu-10-04
title: Deploying django project with nginx and uwsgi in Ubuntu 10.04
wordpress_id: 234
tags: deployment,Django,Web

1. Install Nginx

          :::bash
          $ sudo apt-get install python-software-properties
          $ sudo apt-add-repository ppa:nginx/stable
          $ sudo apt-get update
          $ sudo apt-get install nginx

2.Install uwsgi

          :::bash
          $virtualenv --no-site-packages foo
          $cd foo
          $source bin/activate
          (foo)$ easy_install -U distribute
          (foo)$ pip install http://projects.unbit.it/downloads/uwsgi-latest.tar.gz 


then you shall see:

          *** uWSGI is ready, launch it with /path/to/foo/bin/uwsgi ***

3.create the user "uwsgi" 

          :::bash
          $sudo adduser --system --no-create-home --disabled-login --disabled-password --group uwsgi
          $sudo touch /var/log/uwsgi.log
          $sudo chown uwsgi /var/log/uwsgi.log


4. Install required python packages:
   The final django project source code directories tree looks like this: 

            project/
            ├── coolapp
            │   ├── forms.py
            │   ├── __init__.py
            │   ├── models.py
            │   ├── tests.py
            │   └── views.py
            ├── deployment
            │   ├── nginx.conf
            │   ├── redis.conf
            │   ├── redis-init-deb.sh
            │   └── uwsgi-init-deb.sh
            ├── __init__.py
            ├── manage.py
            ├── requirements.txt
            ├── settings.py
            ├── urls.py
            └── wsgi.py

The wsgi.py and files in deployment directory are cofig files and initial scripts for nginx, uwsgi and redis. We will talk about that later
The requirements.txt is [pip requirement file](https://www.pip-installer.org/en/latest/requirement-format.html).
Just run

          :::bash
          (foo)$pip install -r requirements.txt


all the required python packages and dependences will be installed. Depends on your project, it may take a while, so good time to have a
cup of tea or coffee :)

5 Config nginx:
   I would suggest the put nginx config inside the source code repository, ex,   project/deployment/nginx.conf , then it's under version control. 
  
    
    
      user www-data;
    
    pid /var/run/nginx.pid;
    
    worker_processes 4;
    events {
        worker_connections 100;
    }
    
    
    
    http {
        ##
        # Basic Settings
        ##
    
        sendfile on;
        tcp_nopush on;
        tcp_nodelay on;
        keepalive_timeout 65;
        types_hash_max_size 2048;
        # server_tokens off;
    
        # server_names_hash_bucket_size 64;
        # server_name_in_redirect off;
    
        include /etc/nginx/mime.types;
        default_type application/octet-stream;
    
        ##
        # Logging Settings
        ##
    
        access_log /var/log/nginx/access.log;
        error_log /var/log/nginx/error.log;
    
        ##
        # Gzip Settings
        ##
    
        gzip on;
        gzip_disable "msie6";
    
        upstream uwsgicluster {
            server 127.0.0.1:9001;
            # more servers here for load balancing
        }
    
        # The actual HTTP sever.
        server {
            listen 80;
            server_name ifryrice.com;
            charset     utf-8;
    
            # For our CSS/JS/FILES
            location /media {
                alias /path/to/project/media/;
            }
    
            location /admin_media {
            alias /path/too/foo/lib/python2.6/site-packages/django/contrib/admin/media/;
            }
    
            # Proxy everything else to the backend
            location / {
                uwsgi_pass uwsgicluster;
                include uwsgi_params;
    
    
            }
        }
    }
    


then link this file to /etc/nginx/nginx.conf

         :::bash
         $sudo ln -s /path/to/project/deployment/nginx.conf /etc/nginx/nginx.conf
    



6. Setup uwsgi init script.
   The content of /project/deployment/uwsgi-init-deb.sh is something like this:

        :::bash
        #!/bin/sh
        PATH=/sbin:/bin:/usr/sbin:/usr/bin
        DAEMON=/path/to/foo/bin/uwsgi
        OWNER=uwsgi
        NAME=uwsgi
        DESC=uwsgi
        #make isaute2 accessible
        PYTHONPATH=/path/to/foo
        #virtual python env home
        HOME=/path/to/foo
        MODULE=project.wsgi
        test -x $DAEMON || exit 0
        # Include uwsgi defaults if available
        if [ -f /etc/default/uwsgi ] ; then
                . /etc/default/uwsgi
        fi
        set -e
        DAEMON_OPTS="-s 127.0.0.1:9001 -M 4 -t 30 -A 4 -p 4 -d /var/log/uwsgi.log --pythonpath $PYTHONPATH --module $MODULE --home $HOME"
        case "$1" in
          start)
                echo -n "Starting $DESC: "
                start-stop-daemon --start --chuid $OWNER:$OWNER --user $OWNER \
                        --exec $DAEMON -- $DAEMON_OPTS
                echo "$NAME."
                ;;
          stop)
                echo -n "Stopping $DESC: "
                start-stop-daemon --signal 3 --user $OWNER --quiet --retry 2 --stop \
                        --exec $DAEMON
                echo "$NAME."
                ;;
          reload)
                killall -1 $DAEMON
                ;;
          force-reload)
                killall -15 $DAEMON
               ;;
          restart)
                echo -n "Restarting $DESC: "
                start-stop-daemon --signal 3 --user $OWNER --quiet --retry 2 --stop \
                        --exec $DAEMON
                sleep 1
                start-stop-daemon --user $OWNER --start --quiet --chuid $OWNER:$OWNER \
                       --exec $DAEMON -- $DAEMON_OPTS
                echo "$NAME."
                ;;
          status)  
                killall -10 $DAEMON
                ;;
              *)  
                    N=/etc/init.d/$NAME
                    echo "Usage: $N {start|stop|restart|reload|force-reload|status}" >&2
                    exit 1
                    ;;
            esac
            exit 0


and then

        :::bash
        $sudo ln -s /home/path/to/project/deployment/uwsgi-init-deb.sh /etc/init.d/uwsgi



7. project/wsgi.py

        :::python
        import os
        import sys
        import django.core.handlers.wsgi
        
        sys.path.append(os.path.abspath(os.path.dirname(__file__)))
        os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
        application = django.core.handlers.wsgi.WSGIHandler()
        



8. Start uwsgi and nginx service:

           :::bash
           $sudo /etc/init.d/uwsgi start
           $sudo /etc/init.d/nginx start


  That's it, the web application should be accessible on the server.

