Download all videos in your Youtube playlist
############################################
:date: 2008-08-09 20:36
:author: yiyang
:category: Python, Web, youtube
:slug: download-all-videos-in-your-youtube-playlist

Sometimes I want to watch the videos of my or even my friend's Youtube
playlists in my laptop while I am not online. Therefore I google around
and found some tools to download the videos. `Most of them`_\ either
web-base or firefox plugin just let me download one video each time
except `youtube-dl`_ . So now the problem become how to extract the
video url links (or youtube id) from my playlists and fetch them to
youtube-dl, and fortunately with `Youtube API`_ we can do that easily.
The first step is download
http://www.arrakis.es/~rggi3/youtube-dl/youtube-dl and then rename it to
youtubeDL.py for code reuse as a Python module. Then we can start to
extract the video links. Here is a quick implementation.

::

    import feedparser, urllib, re, sys
    #download http://www.arrakis.es/~rggi3/youtube-dl/youtube-dl and then rename it to youtube-dl
    from youtubeDL import FileDownloader, YoutubeIE, MetacafeIE, YoutubePlaylistIE, DownloadError

    def retrieve_playlist(username):
        playlists_url = 'http://gdata.youtube.com/feeds/api/users/%s/playlists' %username
        feed = feedparser.parse(playlists_url)
        playlists = []
        for en in feed.entries:
            title = en.title
            id_num = en.id.split('/')[-1]
            pages = gen_playlist_pages(id_num)
            playlists.append(dict(title=title, id_num=id_num, pages=pages))
        return playlists


    def gen_playlist_pages(id_num):
        playlist_pages = []
        page = 'http://gdata.youtube.com/feeds/api/playlists/%s' % id_num
        pages = []
        for i in range(4):
            params = urllib.urlencode({'start-index':1+50*i, 'max-results':50})
            _page = '%s?%s' % (page, params)
            pages.append(_page)
        return pages

    def get_video_links_from_playlists(playlists):
        video_lists = []
        for pl in playlists:
            video_links = []
            for p in pl['pages']:
                feed = feedparser.parse(p)
                for en in feed.entries:
                    if re.search(r'watch',en.link):
                        video_links.append(en.link)
            pl.update(dict(video_links=video_links))
            video_lists.append(pl)
        return video_lists

    def download_videos(video_lists):
        youtube_ie = YoutubeIE()
        metacafe_ie = MetacafeIE(youtube_ie)
        youtube_pl_ie = YoutubePlaylistIE(youtube_ie)

        for vl in video_lists:
            outtmpl = vl.get('title','no_playlist_title') + u'/%(stitle)s-%(id)s.%(ext)s'
            fd = FileDownloader({'outtmpl': outtmpl})
            fd.add_info_extractor(youtube_pl_ie)
            fd.add_info_extractor(metacafe_ie)
            fd.add_info_extractor(youtube_ie)
            try:
                retcode = fd.download(vl.get('video_links'))
            except DownloadError:
                # yes, we should handle this... maybe later
                pass
                    
        sys.exit(retcode)

    if __name__ == '__main__':
        pls = retrieve_playlist('your_youtube_username_here')
        video_list = get_video_links_from_playlists(pls)
        download_videos(video_list)

Just put youtubeDL.py and this script file as playlists-dl.py in the
same directory, and change 'your\_youtube\_username\_here' to your user
name then run python playlists-dl.py then all the video clips in all
your playlists will be downloaded :).

| Todo:
|  1. let user can specify username in command line.
|  2. if user specify the playlists id, then just download videos in
those playlist.
|  3. use multi-thread to save total download time.
|  4. play the downloaded videos while other download still going on ...
|  5. ...

.. _Most of them: http://www.downloadandsaveyoutubevideos.info/
.. _youtube-dl: tp://www.arrakis.es/~rggi3/youtube-dl/
.. _Youtube API: http://code.google.com/apis/youtube/2.0/developers_guide_protocol.html
