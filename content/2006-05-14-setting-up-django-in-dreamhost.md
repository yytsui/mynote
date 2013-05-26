author: yiyang
comments: true
date: 2006-05-14 20:56:49
layout: post
slug: setting-up-django-in-dreamhost
title: Setting up Django in Dreamhost
wordpress_id: 12
tags: Django,Python

Jeff Croft wrote up a very good [tutorial](http://www2.jeffcroft.com/blog/2006/may/11/django-dreamhost/) showing how to setup Django application in Dreamhost. For those who are already familiar with settiong up a subdomain and creating a MySQL database in Dreamhost, the subsections to notice are:

1. Set environrmnt variables  in ~/.bash_profile:

    
    <span class="nb">export </span><span class="nv">PATH</span><span class="o">=</span><span class="nv">$PATH</span>:$HOME/path/to/django/bin
    <span class="nb">export </span><span class="nv">PYTHONPATH</span><span class="o">=</span><span class="nv">$PYTHONPATH</span>:$HOME/path/to/django_src:$HOME/path/to/django_projects
    <span class="nb">export </span><span class="nv">DJANGO_SETTINGS_MODULE</span><span class="o">=</span>myproject1.settings:myproject2.setting


2.Install and configure FastCGI

3.Set up mod_rewrite

4.Install Django’s built-in administrative interface
