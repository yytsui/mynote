Setup python 2.5 and appengine development enviroenment in Ubuntu 10.04 Lucid Lynx
##################################################################################
:date: 2010-04-15 21:17
:author: yiyang
:category: Python, Web
:slug: setup-python-2-5-and-appengine-development-enviroenment-in-ubuntu-10-04-lucid-lynx

| 1.Install Python 2.5
|  add the following two lines at the end of your /etc/apt/sources.list

::

      deb http://ppa.launchpad.net/fkrull/deadsnakes/ubuntu lucid main
      deb-src http://ppa.launchpad.net/fkrull/deadsnakes/ubuntu lucid main
     

then run:

::

    $ sudo apt-get update
    $ sudo apt-get install python2.5 python2.5-devel

2. virtualenv for python 2.5

::

      
      $virtualenv --python=python2.5 py25
      $source py25/bin/activate

3. add alias to .bashrc

::

      
       alias py25= 'source  py25/bin/activate'

now everytime when we open a new window, we can type in py25 to
python2.5 environment

| 4 .\ `google app engine`_
|  download sdk and follow the HelloWorld Tutorial then.

.. _google app engine: http://code.google.com/appengine/docs/python/gettingstarted/devenvironment.html
