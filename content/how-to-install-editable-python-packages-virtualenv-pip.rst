How to install editable python packages: virtualenv + pip
#########################################################
:date: 2010-01-11 21:05
:author: yiyang
:category: Django, Python
:slug: how-to-install-editable-python-packages-virtualenv-pip

::

    %virtualenv --no-site-packages testenv
    %cd testenv/
    %source bin/activate
    (testenv)%easy_install pip
    (testenv)%pip install -e svn+http://svn.scipy.org/svn/numpy/trunk

=> egg created, but linked to .src/numpy

::

    (testenv)%pip install -e git+git://github.com/pinax/atom-format.git#egg=atom-format
    (testenv)%pip install -e git+git://github.com/django/django.git#egg=django
    (testenv)%pip install -e git+git://github.com/pinax/diff-match-patch.git#egg=diff-match-patch

| Obtaining diff-match-patch from
git+git://github.com/pinax/diff-match-patch.git#egg=diff-match-patch
|  Cloning git://github.com/pinax/diff-match-patch.git to
./src/diff-match-patch
|  remote: Counting objects: 7, done.
|  remote: Compressing objects: 100% (7/7), done.
|  remote: Total 7 (delta 0), reused 0 (delta 0)
|  Running setup.py egg\_info for package diff-match-patch
|  Installing collected packages: diff-match-patch
|  Running setup.py develop for diff-match-patch
|  Creating
/tmp/testenv/lib/python2.6/site-packages/diff-match-patch.egg-link (link
to .)
|  Adding diff-match-patch 20100110 to easy-install.pth file

| Installed i/tmp/testenv/src/diff-match-patch
|  Successfully installed diff-match-patch
