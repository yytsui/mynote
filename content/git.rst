.. _git:

=========
Git Notes
=========

How to setup a git repo in dreamhost
====================================
1. add a git repo in dreamhost:

.. code-block:: bash

    ssh belowz@eskimos.dreamhost.com
    cd ~/git
    mkdir hochala.git
    cd hochala.git/
    git --bare init

2. add remote in git configure
add this part to .git/config (in the local repo)

.. code-block:: bash

    [remote "origin"]
        fetch = +refs/heads/*:refs/remotes/origin/*
        url = ssh://belowz@eskimos.dreamhost.com/home/belowz/git/hochala.git

or just do this under local existed git repo:

.. code-block:: bash

    git remote add origin ssh://belowz@eskimos.dreamhost.com/home/belowz/git/cookbook.git

now we can start to use git clone ssh://...., git push origin master, git pull ... etc.

3. Avoid typing password everytime
Assume that we already have ssh public key, in local machine, (make sure dir .ssh exist remote machine already)

.. code-block:: bash

     cat .ssh/id_rsa.pub | ssh belowz@eskimos.dreamhost.com 'cat >> .ssh/authorized_keys'
     ssh belowz@eskimos.dreamhost.com
     chmod 700 .ssh
     chmod 600 .ssh/authorized_keys 

,then everytime we can login without typing password again




List all svn:externals recursively
==================================
http://stackoverflow.com/questions/681833/list-all-svnexternals-recursively

.. code-block:: bash

    svn propget svn:externals -R


git cherry-pick --since?
========================

http://old.nabble.com/cherry-pick---since---td10105685.html

.. code-block:: bash

    git format-patch --stdin --binary --full-index -k from..to | git am -k -3

apply patchs from one repo to another repo
==========================================
make sure checkout to the branch in the dst repo you want to apply at first!!!

.. code-block:: bash

    $yiyang@casablanca:~/devel/django_apps/crm$ git format-patch -k --stdout --src-prefix=apps/external_apps/crm/ --dst-prefix=apps/external_apps/crm/  
                       --all | (cd /home/yiyang/devel/rhinobooks/apps/external_apps/crm && git am -3 -k)



Develope with remote upstrem but  rename local master as master and remote master as 'upstream':
================================================================================================

.. code-block:: bash

     git clone  repo_url
     git branch --track upstream origin/master

then we will have a new branch setion in .git/config

.. code-block:: bash

     [branch "upstream"]
        remote = origin
        merge = refs/heads/master

And then delete the master branch section in .git/config
delete this:

.. code-block:: bash

     [branch "upstream"]
        remote = origin
        merge = refs/heads/master

But!!! make sure we check to the upstream branch before we pull:
 
.. code-block:: bash

     git checkout upstream
     git pull

then go back master to merge:

.. code-block:: bash

     git checkout master
     git merge upstream

Syncing a Forked git Repository With a Master Repository’s Changes
==================================================================
http://chriscase.cc/2011/02/syncing-a-forked-git-repository-with-a-master-repositorys-changes/
1. Forked a repo using github web interface, say now we have
   git@github.com:edmoody/beets.git
   forked from
   https://github.com/sampsyo/beets.git

2. clone from forked repo

.. code-block:: bash

   git clone git@github.com:edmoody/beets.git

3. add  original repo as upstream

.. code-block:: bash

    % cd beets
    % git remote add upstream  https://github.com/sampsyo/beets.git

4. fetch and merge
.. code-block:: bash

    % git fetch upstream
    % git merge upstream/master
5. push to forked repo

.. code-block:: bash
    % git push origin master

sync done!


Ref:

| http://progit.org/book/ch9-5.html
| http://github.com/guides/git-cheat-sheet
| http://stackoverflow.com/questions/658885/how-do-you-get-git-to-always-pull-from-a-specific-branch


