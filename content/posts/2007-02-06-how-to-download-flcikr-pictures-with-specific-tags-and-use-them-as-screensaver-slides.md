author: yiyang
comments: true
date: 2007-02-06 14:24:47
layout: post
slug: how-to-download-flcikr-pictures-with-specific-tags-and-use-them-as-screensaver-slides
title: How to download flcikr pictures with specific tags and use them as screensaver
  slides
wordpress_id: 16
tags: Python,Web

[Flickr Leech](http://www.flickrleech.net/) is a slick site I often visit. One can browse mutiple pictures by favorite tags, user name,  interestingness ...etc at the same time. Today when I was looking at all those beautiful pictures from all over the world again, an idea came to me ... Maybe I can download those pictures automatically as my screensaver slides? Then I started to dig into [Flickr API](http://www.flickr.com/services/api/) , it turns out the answer is yes indeed. Here is my quick hack with Python: [flickrDownload.py](http://weblog.tekverse.com/files/download/flickrDownload.py) . After excuting

_python flickrDownload.py dog 200_

I was starting download the most popular 200 pictures which were tagged with "dog" from Flicke. Then I open f-spot in Ubuntu and tag all these pictures with dog,

[![](http://weblog.tekverse.com/files/pictures/flickr_dogs_f-spot.png)](http://weblog.tekverse.com/files/pictures/flickr_dogs_f-spot.png)

and go to Edit->Preference to set them as my screensaver slides.
