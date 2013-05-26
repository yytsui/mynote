author: yiyang
comments: true
date: 2009-07-12 23:23:49
layout: post
slug: twitter-and-nltk
title: Twitter and NLTK
wordpress_id: 100
tags: Python,Web

By using [python-twitter API](http://code.google.com/p/python-twitter/), to get the twitter public timeline , we just have to write:


    
    
    
    import twitter
    api = twitter.Api()
    statuses = api.GetPublicTimeline()
    for s in statuses:
    print "%s:%s:%s" % (s.user.name, s.text, s.created_at)
    



If we can process the data further with NLTK, probabily  we can find something interesting...
