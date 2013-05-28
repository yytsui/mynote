author: yiyang
comments: true
date: 2006-02-01 21:17:54
layout: post
slug: how-to-scrape-websites-to-produce-rss-feeds-an-example
title: How to scrape websites to produce RSS feeds - An example
wordpress_id: 10
tags: Python

Although it's the era of Web 2.0, some websites still  do not have RSS feed. This Mandarin music digest web page I like to visit: [ URL music digest ]( http://digest.url.com.tw/music/ )  is an example. Because now days I read news in my [Bloglines ](http://bloglines.com/) account's feeds, I decide to scrape the URL music digest page to produce feeds. 
   The first part is scraping by using Python HTML/XML parser library[Beautiful Soup](http://www.crummy.com/software/BeautifulSoup/). The scraping results are saved to a list of dictionary. And fortunately, by Google for a while, I know I do not have the generate RSS XML from scratch, because[ PyRSS2Gen](http://www.dalkescientific.com/Python/PyRSS2Gen.html) has been there ready for use. Here is the final program codes list:



    
    
    :::python
    #!/usr/bin/env python
    import sys,urllib
    from BeautifulSoup import BeautifulSoup
    import PyRSS2Gen as RSS2
    import datetime
    
    reload(sys)
    sys.setdefaultencoding('utf-8')
    
    def urldigestscrape(url):
      file = urllib.urlopen(url)
      file = file.read().decode("utf-8")
      soup = BeautifulSoup(file)
      title = soup.html.body['id']
      items = []
      for item in soup.fetch('li',{'class':'post'}):
        link = item.a['href']
        subject = item.a.string
        summary = item.fetch('span',{'class':'item_list_contet'})[0].string
        referee = item.fetch('span',{'class':'item_list_creator'})[0].string
        items.append({'subject': subject ,
                      'link': link ,
                      'summary' : summary ,
                      'referee' : referee })
    
      return title,url,items
    
    def rss2gen(title,link,description,items,xmlfile):
      rss2items = []
      for item in items:
        rss2item = RSS2.RSSItem(title = item['subject'],
                                link = item['link'],
                                description = item['summary'],
                                guid = RSS2.Guid(item['link']),
                                pubDate = datetime.datetime.now())
        rss2items.append(rss2item)
    
    
      rss = RSS2.RSS2(title,link,description,lastBuildDate = datetime.datetime.now(),
                      items = rss2items)
      rss.write_xml(open(xmlfile, "w"))
    
    
    
    if __name__ == "__main__":
      title, url, items = urldigestscrape("http://digest.url.com.tw/music/")
      description = 'Myshare Digest:'+ title
      rss2gen(title,url,description,items,'urldigestmusic.xml')
    
    



