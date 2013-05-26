 Develope with remote upstrem but  rename local master as master and remote master as 'upstream'
################################################################################################
:date: 2010-05-02 21:04
:author: yiyang
:category: git
:slug: develope-with-remote-upstrem-but-rename-local-master-as-master-and-remote-master-as-upstream

::

    git clone  repo_url
    git branch --track upstream origin/master

then we will have a new branch setion in .git/config

::

    [branch "upstream"]
        remote = origin
        merge = refs/heads/master

| And then delete the master branch section in .git/config
|  delete this:

::

    [branch "upstream"]
        remote = origin
        merge = refs/heads/master

Make sure we check to the upstream branch before we pull:

::

    git checkout upstream
    git pull

then go back master to merge:

::

    git checkout master
    git merge upstream

