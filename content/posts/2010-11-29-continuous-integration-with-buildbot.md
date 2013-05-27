author: yiyang
comments: true
date: 2010-11-29 22:35:47
layout: post
slug: continuous-integration-with-buildbot
title: Continuous Integration with BuildBot
wordpress_id: 125
tags: git,Python,Testing

[Buildbot ](http://buildbot.net/) is a system to automate the compile/test cycle required by most software projects to validate code changes.

**Installation**

        :::bash
        sudo pip install buildbot


In addition to buildbot, ZopeInterface and Twisted which buildbot depends on will be also installed.

1.Creating a master

    
    :::bash
    mkdir buildbot
    cd buildbot
    buildbot create-master master
    mv master/master.cfg.sample master/master.cfg
    


Now start it:

    
    
    buildbot start $VIRTUAL_ENV/master
    


You will now see all of the log information from the master in this terminal.
You should see lines like this::

            2010-01-29 21:01:46+0200 [-] twisted.spread.pb.PBServerFactory starting on 9989
            2010-01-29 21:01:46+0200 [-] Starting factory
            2010-01-29 21:01:46+0200 [-] BuildMaster listening on port tcp:9989
            2010-01-29 21:01:46+0200 [-] configuration update started
            2010-01-29 21:01:46+0200 [-] configuration update complete

2.Creating a slave
Open a new terminal, and first enter the same sandbox you created before:

    
    :::bash
    buildbot create-slave slave localhost:9989 bot1name bot1passwd
    


The user:host pair, username, and password should be the same as the ones in
master.cfg; please verify this is the case.
Now, start the slave:

    
    
    buildbot start slave/
    


You should now be able to go to http://localhost:8010 and see the results. 

3. Configure the schedulers (for subversion)
 modify master.cfg

        :::python
        from buildbot.scheduler import Periodic,Scheduler
        c['schedulers'] = []
        periodic_every_30_seconds = Periodic(name="every_30_seconds", builderNames=["ubuntu810"], periodicBuildTimer=60)
        quick = Scheduler(name="quick", branch=None, treeStableTimer=0, builderNames=["ubuntu810" ])
        c['schedulers'].append(periodic_every_30_seconds)
        c['schedulers'].append(quick)
    



4. Configure the build step (for subversion)

        :::python
        from buildbot.steps import source, shell
        f1 = factory.BuildFactory()
        f1.addStep(source.SVN(mode='update',
        baseURL='svnrepourl',
        
        defaultBranch='trunk'))
        
        class NoseTest(shell.ShellCommand):
        name="nosetests"
        description = ["running unit tests"]
        descriptionDone = [name]
        
        f1.addStep(NoseTest, command=["nosetests","--with-doctest"])
        


5. Setup builders

        :::python
        b1 = {'name': "every_30_seconds",
        'slavename': "bot1name",
        'builddir': "slave_test_dir",
        'factory': f1,
        
        }
        c['builders'] = [b1]
    


6.Hook svn post-commit

Hook svn post-commit and add following line to svn-repositories/hooks/post-commit

        :::bash
        #!/bin/sh
        REPOS="$1"
        REV="$2"
        /path/to/svn_buildbot.py --repository "$REPOS" --revision "$REV" \
        --bbserver localhost --bbport 9989
    



For git, the instruction can be found [here.](http://buildmonkey.wordpress.com/2009/02/27/continious-integration-with-buildbot-and-git/)

