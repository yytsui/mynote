author: yiyang
comments: true
date: 2006-02-01 21:17:54
layout: post
slug: how-to-scrape-websites-to-produce-rss-feeds-an-example
title: How to scrape websites to produce RSS feeds - An example
wordpress_id: 10
tags: Python

Although it's the era of Web 2.0, some websites still  do not have RSS feed. This Mandarin music digest web page I like to visit: [ URL music digest ]( http://digest.url.com.tw/music/ )  is an example. Because now days I read news in my [Bloglines ](http://bloglines.com/) account's feeds, I decide to scrape the URL music digest page to produce feeds. <!-- more -->
   The first part is scraping by using Python HTML/XML parser library[Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/). The scraping results are saved to a list of dictionary. And fortunately, by Google for a while, I know I do not have the generate RSS XML from scratch, because[ PyRSS2Gen](http://www.dalkescientific.com/Python/PyRSS2Gen.html) has been there ready for use. Here is the final program codes list:



    
    
    <font color="#0000ff">#!/usr/bin/env python</font>
    <font color="#a020f0">import</font> sys,urllib
    <font color="#a020f0">from</font> BeautifulSoup <font color="#a020f0">import</font> BeautifulSoup
    <font color="#a020f0">import</font> PyRSS2Gen <font color="#a020f0">as</font> RSS2
    <font color="#a020f0">import</font> datetime
    
    reload(sys)
    sys.setdefaultencoding('<font color="#ff00ff">utf-8</font>')
    
    <font color="#804040"><b>def</b></font> <font color="#008080">urldigestscrape</font>(url):
      file = urllib.urlopen(url)
      file = file.read().decode("<font color="#ff00ff">utf-8</font>")
      soup = BeautifulSoup(file)
      title = soup.html.body['<font color="#ff00ff">id</font>']
      items = []
      <font color="#804040"><b>for</b></font> item <font color="#804040"><b>in</b></font> soup.fetch('<font color="#ff00ff">li</font>',{'<font color="#ff00ff">class</font>':'<font color="#ff00ff">post</font>'}):
        link = item.a['<font color="#ff00ff">href</font>']
        subject = item.a.string
        summary = item.fetch('<font color="#ff00ff">span</font>',{'<font color="#ff00ff">class</font>':'<font color="#ff00ff">item_list_contet</font>'})[0].string
        referee = item.fetch('<font color="#ff00ff">span</font>',{'<font color="#ff00ff">class</font>':'<font color="#ff00ff">item_list_creator</font>'})[0].string
        items.append({'<font color="#ff00ff">subject</font>': subject ,
                      '<font color="#ff00ff">link</font>': link ,
                      '<font color="#ff00ff">summary</font>' : summary ,
                      '<font color="#ff00ff">referee</font>' : referee })
    
      <font color="#804040"><b>return</b></font> title,url,items
    
    <font color="#804040"><b>def</b></font> <font color="#008080">rss2gen</font>(title,link,description,items,xmlfile):
      rss2items = []
      <font color="#804040"><b>for</b></font> item <font color="#804040"><b>in</b></font> items:
        rss2item = RSS2.RSSItem(title = item['<font color="#ff00ff">subject</font>'],
                                link = item['<font color="#ff00ff">link</font>'],
                                description = item['<font color="#ff00ff">summary</font>'],
                                guid = RSS2.Guid(item['<font color="#ff00ff">link</font>']),
                                pubDate = datetime.datetime.now())
        rss2items.append(rss2item)
    
    
      rss = RSS2.RSS2(title,link,description,lastBuildDate = datetime.datetime.now(),
                      items = rss2items)
      rss.write_xml(open(xmlfile, "<font color="#ff00ff">w</font>"))
    
    
    
    <font color="#804040"><b>if</b></font> __name__ == "<font color="#ff00ff">__main__</font>":
      title, url, items = urldigestscrape("<font color="#ff00ff"><a href="http://digest.url.com.tw/music/">http://digest.url.com.tw/music/</a></font>")
      description = '<font color="#ff00ff">Myshare Digest:</font>'+ title
      rss2gen(title,url,description,items,'<font color="#ff00ff">urldigestmusic.xml</font>')
    
    



