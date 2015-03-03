.._buildbot

========
Buildbot
========

`Buildbot <http://buildbot.net/>` is a system to automate the compile/test cycle required by most software projects to validate code changes.

Installation
------------

.. code-block:: bash

    sudo pip install buildbot 

In addition to buildbot, ZopeInterface? and Twisted which buildbot depends on will be also installed.

Creating a master
-----------------


.. code-block:: bash

    mkdir buildbot
    cd buildbot
    buildbot create-master master
    mv master/master.cfg.sample master/master.cfg


Now start it:

.. code-block:: bash

  buildbot start $VIRTUAL_ENV/master

You will now see all of the log information from the master in this terminal.
You should see lines like this::

  2009-07-29 21:01:46+0200 [-] twisted.spread.pb.PBServerFactory starting on 9989
  2009-07-29 21:01:46+0200 [-] Starting factory <twisted.spread.pb.PBServerFactory instance at 0x1fc8ab8>
  2009-07-29 21:01:46+0200 [-] BuildMaster listening on port tcp:9989
  2009-07-29 21:01:46+0200 [-] configuration update started
  2009-07-29 21:01:46+0200 [-] configuration update complete

Creating a slave
----------------

Open a new terminal, and first enter the same sandbox you created before:

.. code-block:: bash

  buildbot create-slave slave localhost:9989 bot1name bot1passwd

The user:host pair, username, and password should be the same as the ones in
master.cfg; please verify this is the case.

Now, start the slave:

.. code-block:: bash

  buildbot start slave/

You should now be able to go to http://localhost:8010, where you will see
a web page similar to:



Configuring the buildmaster
---------------------------

 modify master.cfg

1. Configure the schedulers (subversion)

.. code-block:: python

    from buildbot.scheduler import Periodic,Scheduler
    c['schedulers'] = []
    periodic_every_30_seconds = Periodic(name="every_30_seconds", builderNames=["ubuntu810"], periodicBuildTimer=60)

    quick = Scheduler(name="quick", branch=None, treeStableTimer=0, builderNames=["ubuntu810" ])
    c['schedulers'].append(periodic_every_30_seconds)
    c['schedulers'].append(quick)

2. Configure the build step (subversion)

.. code-block:: python

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

3. Setup builders

.. code-block:: python

    b1 = {'name': "every_30_seconds",
          'slavename': "bot1name",
          'builddir': "slave_test_dir",
           'factory': f1,

           }
    c['builders'] = [b1]

Hook svn post-commit
--------------------
Hook svn post-commit and add following line to svn-repositories/hooks/post-commit

.. code-block:: bash

    #!/bin/sh
    REPOS="$1"
    REV="$2"
    /path/to/svn_buildbot.py --repository "$REPOS" --revision "$REV" \
      --bbserver localhost --bbport 9989

Git
---
1. In the buildbot/contrib directory, you will find git_buildbot.py. Copy this to the remote server your public git repo is being hosted on. You need to make sure that python and twisted are installed on this host, since the script uses the twisted frame for network interactions. Make sure to edit master variable in the script to point to the server hostname and listening port of your buildbot instance. Example:

      master="some.remotehost.com:9989"
2. On the remote server, create a post-receive hook script file in your public repo and make sure it’s executable. You would do this under gitrepo/hooks and point the script to run the git_buildbot.py script with arguments. Some like this:

.. code-block:: bash

    #!/bin/sh
    /home/yiyang/buildbot/git_buildbot.py -l /tmp/bot.log -v

3. Once that’s done, you’ll need to edit your buildbot instance’s master.cfg file to add a PBChangesource statement. This will have buildbot listen for the changes being sent by the git_buildbot.py script. Do this:

.. code-block:: python

      from buildbot.changes.pb import PBChangeSource
      c['change_source'] = PBChangeSource()

4. Next we’ll add a scheduler to catch the changes. Make sure that you specify the branch as master, otherwise your changes will get ignored by the scheduler:

.. code-block:: python

      c['schedulers'] = []
      test_schedule = Scheduler(name="test", branch="master", treeStableTimer=0, builderNames=["test-builder"])
      c['schedulers'].append(test_schedule) 

5. Now we’ll add a build factory that will get executed when the changes occur. For simplicity sake, we’ll just pull (or fetch in the case of buildbot) the latest revision of the code. Note that the repourl we’re using is prefaced by ssh. This is why you’ve previously setup your ssh keys between your slave and the git repo:

.. code-block:: python

      test_factory = factory.BuildFactory()
      test_factory.addStep(Git(repourl="ssh://gitrepo.somehost.com/home/jedi/gitrepo"))
      test_factory.addStep(ShellCommand, command=["python", "manage.py", "test"]) #for django

glitch here: for django, make sure python manage.py  can import the right module by tweaking manage.py, since the code
willbe checked into slavedir+builddir+'build' which always causes import django_project_name.settings raise an exception.
One solution is to have manage_test.py which specify the path, then the test command will be python manage_test.py test.

6. Restart your buildbot server and make sure your slave is attached.

7. Checkout, edit, commit and push a file in the code base your using to test this setup. You should see the following:

    * Buildbot gets the change notice from the post-receive hook.
    * Buildbot hands the change off to the builder.
    * The buildslave runs the job and successfully gets the code update.

make sure the permission setting is right and the svn_buildbot.py is from buidbot source code contrib/svn_buildbot.py.

Now we can Check building and testing report.

Open the browser and point to localhost:8010 you should the testing report in every commit and every 30 seconds.

Ref:
http://buildmonkey.wordpress.com/2009/02/27/continious-integration-with-buildbot-and-git/

for the setup config file, check
slave config:   example_codes/buildbot_config/buildbot.tac
git_buildbot.py:   example_codes/buildbot_config/git_buildbot.py
master config:   example_codes/buildbot_config/master.cfg

