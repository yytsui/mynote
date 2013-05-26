How to download flcikr pictures with specific tags and use them as screensaver slides
#####################################################################################
:date: 2007-02-06 14:24
:author: yiyang
:category: Python, Web
:slug: how-to-download-flcikr-pictures-with-specific-tags-and-use-them-as-screensaver-slides

`Flickr Leech`_ is a slick site I often visit. One can browse mutiple
pictures by favorite tags, user name, interestingness ...etc at the same
time. Today when I was looking at all those beautiful pictures from all
over the world again, an idea came to me ... Maybe I can download those
pictures automatically as my screensaver slides? Then I started to dig
into `Flickr API`_ , it turns out the answer is yes indeed. Here is my
quick hack with Python: `flickrDownload.py`_ . After excuting

*python flickrDownload.py dog 200*

I was starting download the most popular 200 pictures which were tagged
with "dog" from Flicke. Then I open f-spot in Ubuntu and tag all these
pictures with dog,

|image0|

and go to Edit->Preference to set them as my screensaver slides.

.. _Flickr Leech: http://www.flickrleech.net/
.. _Flickr API: http://www.flickr.com/services/api/
.. _flickrDownload.py: http://weblog.tekverse.com/files/download/flickrDownload.py

.. |image0| image:: http://weblog.tekverse.com/files/pictures/flickr_dogs_f-spot.png
   :target: http://weblog.tekverse.com/files/pictures/flickr_dogs_f-spot.png
