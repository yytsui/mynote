author: yiyang
comments: true
date: 2010-04-15 21:17:18
layout: post
slug: setup-python-2-5-and-appengine-development-enviroenment-in-ubuntu-10-04-lucid-lynx
title: Setup python 2.5 and appengine development enviroenment in Ubuntu 10.04 Lucid Lynx
wordpress_id: 153
tags: Python,Web

1.Install Python 2.5
add the following two lines at the end of your  /etc/apt/sources.list

      :::bash
      deb http://ppa.launchpad.net/fkrull/deadsnakes/ubuntu lucid main
      deb-src http://ppa.launchpad.net/fkrull/deadsnakes/ubuntu lucid main

then  run:

        :::bash
        $ sudo apt-get update
        $ sudo apt-get install python2.5 python2.5-devel


2. virtualenv for python 2.5

          :::bash
          $virtualenv --python=python2.5 py25
          $source py25/bin/activate

3. add alias to .bashrc

          :::bash
          alias py25= 'source  py25/bin/activate'


   now everytime when we open a new window, we can type in py25 to python2.5 environment

4. Download sdk and follow the HelloWorld Tutorial [then](http://code.google.com/appengine/docs/python/gettingstarted/devenvironment.html).
  
