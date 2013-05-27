author: yiyang
comments: true
date: 2010-12-19 20:38:19
layout: post
slug: memcached-multi-mecanize-and-django-see-how-memcached-is-working
title: memcached ,  multi-mecanize and django (part 1) — see how memcached is working
wordpress_id: 175
tags: Django

1. Install and run  [memcached](http://memcached.org/) in daemon mode in ububtu 

        :::bash
        % sudo apt-get install memcached
        % sudo pip install python-memcached
        % sudo memcached -d -u www-data -p 11211 -m 10
    


2. settings.py
for the per-site cache , setup the cache middleware to cache every page that doesn't have GET or POST parameters: 

        :::python
        CACHE_BACKEND = 'memcached://127.0.0.1:11211/'
        MIDDLEWARE_CLASSES = (
            'django.middleware.cache.UpdateCacheMiddleware',
             #OtherMiddlware
            'django.middleware.common.CommonMiddleware',
             #.....
            'django.middleware.cache.FetchFromCacheMiddleware',
        )


Note: the "update" middleware must be first in the list, and the "fetch" middleware must be last. 

3.Use [ngrep](http://ngrep.sourceforge.net/) to make sure memcahed is working:
  Just run

        :::bash
        % ngrep -d any port 11211
    


then point the browser or wget to the url of web application homepage, you should see some log text flying by if memached service is working.
To see the key, value CRUD action only, just run

        :::bash
        % ngrep -W none -T -d any "^(get|set|delete|END|STORED|VALUE|DELETED)" port 11211 | awk '{print $1 " " $2}'


4, See the performance difference by stress testing:
    Download the [Multi-mechanize](http://code.google.com/p/multi-mechanize/) package. copy the default_project to my_project,
    then  create a file my_project/test_scripts/my_test.py:

    :::python
    import mechanize
    import time
    
    class Transaction(object):
        def __init__(self):
            self.custom_timers = {}
        
        def run(self):
            # create a Browser instance
            #n = random.randint(1, 500)
            br = mechanize.Browser()
            # don't bother with robots.txt
            br.set_handle_robots(False)
            # add a custom header so wikipedia allows our requests
            br.addheaders = [('User-agent', 'StressTesting')]
            
            url = 'http://mywebapp.com/'
            # start the timer
            start_timer = time.time()
            # submit the request
            resp = br.open(url)
            resp.read()
            # stop the timer
            latency = time.time() - start_timer
            
            # store the custom timer
            self.custom_timers['Load_Test_Page'] = latency   
            
            # verify responses are valid
            assert (resp.code == 200), 'Bad HTTP Response'
            #assert ('Some_text_in_home_page'% in resp.get_data()), 'Text Assertion Failed'
            
    
    if __name__ == '__main__':
        trans = Transaction()
        trans.run()
        print trans.custom_timers
    



and the config file my_project/config.cfg

        :::bash
        [global]
        run_time: 30
        rampup: 30
        console_logging: on
        results_ts_interval: 5
        
        [user_group-1]
        threads:200
        script: local1.py
        
        [user_group-2]
        threads: 200
        script: local2.py
        



run the stress test without memcahed, and then with memcached service again:

    
    
    :::bash
    % python multi-mechanize.py my_project
    



5. See the test result under my_project/results:
    In my test case , without memached: there are 169 errors(almost all of them are 504 Gateway Timeout) in 945 transaction during 30 seconds.
   The error rate is 18%, and the transaction response time look like this :
   the average is 3.43 sec.
   ![response time without memcached](|filename|/images/no_cached.png)

   Response Time: raw data (all points)
    ![no cached raw](|filename|/images/no_cached_raw.png)
   With memcahed service is working, the same machine source can handle 2092 transactions in 30 seconds without any error!
   and the average response time is reduced to 0.60 sec.
  ![response time with memcached](|filename|/images/cached.png)

  ![memched raw data](|filename|/images/cached_raw.png)
