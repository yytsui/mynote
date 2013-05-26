Twitter and NLTK
################
:date: 2009-07-12 23:23
:author: yiyang
:category: Python, Web
:slug: twitter-and-nltk

By using `python-twitter API`_, to get the twitter public timeline , we
just have to write:

::


    import twitter
    api = twitter.Api()
    statuses = api.GetPublicTimeline()
    for s in statuses:
    print "%s:%s:%s" % (s.user.name, s.text, s.created_at)

If we can process the data further with NLTK, probabily  we can find
something interesting...

.. _python-twitter API: http://code.google.com/p/python-twitter/
