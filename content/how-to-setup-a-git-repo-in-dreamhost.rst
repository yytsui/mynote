How to setup a git repo in dreamhost
####################################
:date: 2010-03-19 05:53
:author: yiyang
:category: git
:slug: how-to-setup-a-git-repo-in-dreamhost

1. add a git repo in dreamhost:

::

    ssh foo@bar.dreamhost.com
    cd ~/git
    mkdir hochala.git
    cd hochala.git/
    git --bare init

| 2. add remote in git configure
|  add this part to .git/config (in the local repo)

::

    [remote "origin"]
        fetch = +refs/heads/*:refs/remotes/origin/*
        url = ssh://foo@bar.dreamhost.com/home/foo/git/hochala.git

or just do this under local existed git repo:

::

    git remote add origin ssh://foo@bar.dreamhost.com/home/foo/git/cookbook.git

| now we can start to use git clone ssh://...., git push origin master,
git pull ... etc.
|  3. Avoid typing password everytime
|  Assume that we already have ssh public key, in local machine, (make
sure dir .ssh exist remote machine already)

::

     cat .ssh/id_rsa.pub | ssh foo@bar.dreamhost.com 'cat >> .ssh/authorized_keys'
     ssh foo@bar.dreamhost.com
     chmod 700 .ssh
     chmod 600 .ssh/authorized_keys 

,then everytime we can login without typing password again.
