Install Redis in ubuntu 10.04
#############################
:date: 2011-02-25 21:37
:author: yiyang
:category: deployment, Python, Web
:slug: install-redis-in-ubuntu-10-04

1. Install redis server

::

     $wget http://redis.googlecode.com/files/redis-2.2.2.tar.gz
     $tar xvfz redis-2.2.2.tar.gz 
     $cd redis-2.2.2/
     $sudo mkdir -p /opt/redis
     $sudo make PREFIX=/opt/redis install 
     $ tree /opt/redis

| so what we have now is:
|  /opt/redis
|  └── bin
|  ├── redis-benchmark
|  ├── redis-check-aof
|  ├── redis-check-dump
|  ├── redis-cli
|  └── redis-server

2. Init script /etc/init.d/redis

::

    #!/bin/sh

    PATH=/opt/redis/bin:/sbin:/bin:/usr/sbin:/usr/bin
    NAME=redis

    test -x $DAEMON || exit 0

    set -e

    case "$1" in
      start)
            echo -n "Starting $DESC: "

            start-stop-daemon --start --user redis -c redis:redis \
                --startas /opt/redis/bin/redis-server -- /opt/redis/redis.conf

            echo "$NAME."
            ;;
      stop)
            echo -n "Stopping $DESC: "

            start-stop-daemon --stop --exec /opt/redis/bin/redis-server -c redis:redis \
                /opt/redis/bin/redis-server -- /opt/redis/redis.conf

            echo "$NAME."
            ;;
          *)    
                N=/etc/init.d/$NAME
                echo "Usage: $N {start|stop}" >&2
                exit 1
                ;;
        esac
        
        exit 0

3. Redis config file /opt/redis/redis.conf

::

    $sudo  cp /path/to/redis_src/redis.conf /opt/redis/redis.conf

4. change file mode and owner

::

    $ chmod +x /etc/init.d/redis
    $ sudo chown -R redis:redis /opt/redis
    $ sudo touch /var/log/redis.log
    $ sudo chown redis:redis /var/log/redis.log

5. Install redis python client

::

    $ pip install redis

6. Start redis and see if it works

::

    $ sudo /etc/init.d/redis start
    $ ipython
    Python 2.6.5 (r265:79063, Apr 16 2010, 13:57:41) 
    In [1]: import redis
    In [2]: rs = redis.Redis("localhost")
    In [3]: rs.set("city", "Vancouver")
    Out[3]: True

at the same time run in other terminal

::

    $ sudo ngrep -d any port 6379

you should able to see something like...

| interface: any
|  filter: (ip or ip6) and ( port 6379 )
|  ####
|  T 127.0.0.1:52788 -> 127.0.0.1:6379 [AP]
|  \*2..$6..SELECT..$1..0..
|  ##
|  T 127.0.0.1:6379 -> 127.0.0.1:52788 [AP]
|  +OK..
|  ##
|  T 127.0.0.1:52788 -> 127.0.0.1:6379 [AP]
|  \*3..$3..SET..$4..city..$9..Vancouver.
|  #
|  T 127.0.0.1:6379 -> 127.0.0.1:52788 [AP]
|  +OK..
|  #
