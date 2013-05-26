http://kevin.deldycke.com/2013/02/wordpress-to-pelican/

pip install -e git+https://github.com/edmoody/pelican.git#egg=pelican
pelican-quickstart

Welcome to pelican-quickstart v3.2.0.

This script will help you create a new Pelican-based website.

Please answer the following questions so this script can generate the files
needed by Pelican.


> Where do you want to create your new web site? [.]
> What will be the title of this web site? Notes about mobile and web programming
> Who will be the author of this web site? Yiyang
> What will be the default language of this web site? [en]
> Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) n
> Do you want to enable article pagination? (Y/n) Y
> How many articles per page do you want? [10]
> Do you want to generate a Makefile to easily manage your website? (Y/n) Y
> Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) Y
> Do you want to upload your website using FTP? (y/N) N
> Do you want to upload your website using SSH? (y/N) y
> What is the hostname of your SSH server? [localhost]
> What is the port of your SSH server? [22]
> What is your username on that server? [root]
> Where do you want to put your web site on that server? [/var/www] /home/yiyang/tmp/notewww
> Do you want to upload your website using Dropbox? (y/N) N
> Do you want to upload your website using S3? (y/N) N
Done. Your new project is available at /Users/emomo/note
(basic)[emomo@toufen note]$ ls
Makefile          content           develop_server.sh output            pelicanconf.py    publishconf.py
-bash: cd: note: No such file or directory
Makefile          content           develop_server.sh output            pelicanconf.py    publishconf.py

(basic)[emomo@toufen note]$ make serve

cd /Users/emomo/note/output && python -m pelican.server
/Users/emomo/pyenv/basic/lib/python2.7/site-packages/pytz/__init__.py:35: UserWarning: Module argparse was already imported from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/argparse.pyc, but /Users/emomo/pyenv/basic/lib/python2.7/site-packages is being added to sys.path
  from pkg_resources import resource_stream
serving at port 8000
1.0.0.127.in-addr.arpa - - [26/May/2013 12:30:54] "GET / HTTP/1.1" 200 -
1.0.0.127.in-addr.arpa - - [26/May/2013 12:30:54] "GET /theme/css/main.css HTTP/1.1" 200 -
1.0.0.127.in-addr.arpa - - [26/May/2013 12:30:54] "GET /theme/css/reset.css HTTP/1.1" 200 -
1.0.0.127.in-addr.arpa - - [26/May/2013 12:30:54] "GET /theme/css/pygment.css HTTP/1.1" 200 -
1.0.0.127.in-addr.arpa - - [26/May/2013 12:30:54] "GET /theme/css/typogrify.css HTTP/1.1" 200 -
1.0.0.127.in-addr.arpa - - [26/May/2013 12:30:54] "GET /theme/images/icons/rss.png HTTP/1.1" 200 -
1.0.0.127.in-addr.arpa - - [26/May/2013 12:30:54] code 404, message File not found
1.0.0.127.in-addr.arpa - - [26/May/2013 12:30:54] "GET /favicon.ico HTTP/1.1" 404 -


.export wordpress xml
wordpress admin/tools/export

