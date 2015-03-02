Python developments with multi editable packages
################################################
:date: 2010-09-01 22:37
:author: yiyang
:category: Python
:slug: python-developments-with-multi-editable-packages

| It's often that people have to integrate third party open source
applications into their projects. In some cases, we may like to modify
the packages to
|  fit our applications, or even theris is a bug that has to be fix to
make it work in our app. The most simple and easy way to handle this to
clone the
|  repository and copy the source code into the development code
repositories. However, the distadvange of just copying codes is that we
lost the advantage
|  of syncing with upstream. For example, if there are some bug fixes in
original upstream source, then we cannot just pull from it, we have to
do a copy
|  and paste again. And it we fix bugs for the upstream 3rd party
library, in this case, to let these patches being merges is send the
pacthes files by
|  email to the package maintainer, at the same, we also have to be
careful that the patches does not messy up with other part of source
code which in our
|  app but not in the upstream repositories. In short, isn't it handy
that we `can fork a project, pull in upstream change`_ and `push our
change`_ as usual? Well, using virtualenv and pip can help us acheieve
this goal quite easily.

1.The first step is setup a virtual enviroement

::

    yiyang@casablanca:~/try2/other$ virtualenv --no-site-packages bar
    New python executable in bar/bin/python2.6
    Also creating executable in bar/bin/python
    Installing setuptools............done.
    yiyang@casablanca:~/try2/other$ cd bar/
    yiyang@casablanca:~/try2/other/bar$ source bin/activate
    (bar)yiyang@casablanca:~/try2/other/bar$ 

2. install non-editable and editable pacakge with pip

::

    ----------------------------requirements.txt-----------------------------
        django
    -e git+https://github.com/jacobian/django-shorturls.git#egg=DjangoShorturls
    -e git+https://github.com/ojii/django-classy-tags.git#egg=ClassyTags
    -----------------------------------------------------------------------------------

    (bar)yiyang@casablanca:~/try2/other/bar$ pip install -r requirements.txt 
    Obtaining DjangoShorturls from git+https://github.com/jacobian/django-shorturls.git#egg=DjangoShorturls (from -r requirements.txt (line 2))
      Cloning https://github.com/jacobian/django-shorturls.git to ./src/djangoshorturls
    Unpacking objects: 100% (98/98), done.
      Running setup.py egg_info for package DjangoShorturls
    Obtaining ClassyTags from git+https://github.com/ojii/django-classy-tags.git#egg=ClassyTags (from -r requirements.txt (line 3))
      Cloning https://github.com/ojii/django-classy-tags.git to ./src/classytags
      Running setup.py egg_info for package ClassyTags
    Downloading/unpacking django (from -r requirements.txt (line 1))
      Downloading Django-1.2.5.tar.gz (6.4Mb): 6.4Mb downloaded
      Running setup.py egg_info for package django
    Requirement already satisfied (use --upgrade to upgrade): setuptools in ./lib/python2.6/site-packages/setuptools-0.6c11-py2.6.egg (from DjangoShorturls->-r requirements.txt (line 2))
    Installing collected packages: ClassyTags, django, DjangoShorturls
      Running setup.py develop for ClassyTags
        Creating /home/yiyang/try2/other/bar/lib/python2.6/site-packages/django-classy-tags.egg-link (link to .)
        Adding django-classy-tags 0.3.0 to easy-install.pth file
        
        Installed /home/yiyang/try2/other/bar/src/classytags
      Running setup.py install for django
        changing mode of build/scripts-2.6/django-admin.py from 644 to 755
        changing mode of /home/yiyang/try2/other/bar/bin/django-admin.py to 755
      Running setup.py develop for DjangoShorturls
        Creating /home/yiyang/try2/other/bar/lib/python2.6/site-packages/django-shorturls.egg-link (link to src)
        Adding django-shorturls 1.0.1 to easy-install.pth file
        
        Installed /home/yiyang/try2/other/bar/src/djangoshorturls/src
    Successfully installed ClassyTags django DjangoShorturls


    ---------------lib/python2.6/site-packages/easy-install.pth----------------
    /home/yiyang/try2/other/bar/src/classytags
    /home/yiyang/try2/other/bar/src/djangoshorturls/src
    ----------------------------------------------------------------------------------------------

What happens is that pip will use git to clone the specify repositories
to src/[under-case-name-whatever#egg=]

::

    (bar)yiyang@casablanca:~/try2/other/bar/src/classytags$ ls /home/yiyang/try2/other/bar/src/classytags/.git
    branches  config  description  HEAD  hooks  index  info  logs  objects  packed-refs  refs

and add links lib/python2.6/site-packages/easy-install.pth then python
know where it is.

::

    ipython 
    ......
    In [2]: import classytags
    In [3]: classytags.__file__
    Out[3]: '/home/yiyang/try2/other/bar/src/classytags/classytags/__init__.pyc'
    ......

.. _can fork a project, pull in upstream change: %20http://help.github.com/forking/
.. _push our change: http://help.github.com/pull-requests/
