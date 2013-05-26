author: yiyang
comments: true
date: 2008-04-03 10:24:24
layout: post
slug: music-recommendations-by-audioscrobbler
title: Music Recommendations by audioscrobbler
wordpress_id: 19
tags: Python,Web

I have been reading [Programming Collective Intelligence](http://www.oreilly.com/catalog/9780596529321) by Toby Segaran recently. It's quite interesting and inspiring. In chapter 2 , the author talks about how to make recommendation by using preference datas of  a  group  people.  Usually, to  do this, iwe get the rating data, then we implent an reasonable algorithm to calucalte the 'metric' (or score) by taking advantage of the data. Then we make recommendation by the order of metric/score.

For  example, if I know want to extend my music collections, asking other people who also have the same favorite band with me  might be the best bet. Thanks to [Audioscrobbler](http://www.audioscrobbler.net/data/webservices/), the [Last.FM](http://last.fm) web service, we can collect this data quite easy. With pyscrobbler,  a set of python bindings to  AudioScrobbler APIs based on ElementTree, we can write a function to get the rating data and calculate the score.:

    
    
    from audioscrobbler import AudioScrobblerQuery
    import operator,sys
    
    #n total numbers of bands to be recommended.
    def getRecommendations(favoriteBand,n=10):
    	#since audioscrobbler return 50 fans by default, so we use 50 as full score.
    	FULLSCORE = 50
    	fans = [f.element().get('username') for f in AudioScrobblerQuery(artist=favoriteBand).fans()]
    	bands= {}
    	for f in fans:
    		for a in AudioScrobblerQuery(user=f).topartists()[:FULLSCORE]:
    			name = a.name.__str__()
    			rank = int(a.rank.__str__())
    			#so rank #1 will get score=FULLSCORE, rank #2 will get score=FULLSCORE-1, ...etc.
    			score = FULLSCORE - rank + 1
    			if name in bands:
    				bands[name] += score
    			else:
    				bands[name] = score
    	#we do not return the artist the user just pass in.
    	del bands[favoriteBand]
    	recom = sorted(bands.items(), key=operator.itemgetter(1),reverse=True)
    	return recom[:n]
    
    



Here are the two examples to run this function in IPython shell:

In [3]: getRecommendations('U2')
Out[3]:
[('Red Hot Chili Peppers', 757),
('Coldplay', 669),
('The Beatles', 532),
('Nirvana', 423),
('Aerosmith', 409),
('R.E.M.', 401),
('Moby', 381),
('Queen', 379),
('Pink Floyd', 378),
('Green Day', 376)]

In [4]: getRecommendations('Belle and Sebastian')
Out[4]:
[('The Beatles', 960),
('Radiohead', 829),
('The Smiths', 580),
('Cat Power', 529),
('The Arcade Fire', 478),
('The White Stripes', 469),
('Elliott Smith', 431),
('of Montreal', 424),
('The Shins', 411),
('Bob Dylan', 390)]

Depending on my years of rock music listening experience, I think the results are quite impressive :)
