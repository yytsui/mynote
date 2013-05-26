Setting up Django in Dreamhost
##############################
:date: 2006-05-14 20:56
:author: yiyang
:category: Django, Python
:slug: setting-up-django-in-dreamhost

Jeff Croft wrote up a very good `tutorial`_ showing how to setup Django
application in Dreamhost. For those who are already familiar with
settiong up a subdomain and creating a MySQL database in Dreamhost, the
subsections to notice are:

1. Set environrmnt variables in ~/.bash\_profile:

.. code:: syntax

    export PATH=$PATH:$HOME/path/to/django/bin
    export PYTHONPATH=$PYTHONPATH:$HOME/path/to/django_src:$HOME/path/to/django_projects
    export DJANGO_SETTINGS_MODULE=myproject1.settings:myproject2.setting

2.Install and configure FastCGI

3.Set up mod\_rewrite

4.Install Django’s built-in administrative interface

.. _tutorial: http://www2.jeffcroft.com/blog/2006/may/11/django-dreamhost/
