author: yiyang
comments: true
date: 2008-08-20 20:36:08
layout: post
slug: download-and-play-all-videos-in-your-youtube-playlist
title: Download (and play) all videos in your Youtube playlist
wordpress_id: 74
tags: Python,Web,youtube

[Last time](/download-all-videos-in-your-youtube-playlist.html) I wrote a program to download all videos in playlists,would it be nice if I can watch all these video one by one while downloading?  What we have to do is starting two threads, one for downloading and put the videos in queue and the other thread trying to get videos  from the queue and playing them.


    
    :::python
    def download_and_play(video_lists):
    	q = Queue(32)
    	threads = []
    	dt = PDThread(func=download_list_videos, args=(video_lists,q))
    	pt = PDThread(func=play_video, args=(q,))
    	threads.extend([dt, pt])
    	for t in threads:
    		t.start()
    	for t in threads:
    		t.join()
    
    class PDThread(threading.Thread):
    	def __init__(self, func, args):
    		threading.Thread.__init__(self)
    		self.func = func
    		self.args = args
    	
    	def run(self):
    		self.res = apply(self.func, self.args)
    
    



**update:** The source code now is on [ google code project youtube-playlists-videos-download.](http://code.google.com/p/youtube-playlists-videos-download/)
