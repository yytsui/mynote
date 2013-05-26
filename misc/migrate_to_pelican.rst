http://kevin.deldycke.com/2013/02/wordpress-to-pelican/

pip install -e git+https://github.com/edmoody/pelican.git#egg=pelican
pelican-quickstart

Welcome to pelican-quickstart v3.2.0.

This script will help you create a new Pelican-based website.

Please answer the following questions so this script can generate the files
needed by Pelican.


> Where do you want to create your new web site? [.]
> What will be the title of this web site? Notes about mobile and web programming
> Who will be the author of this web site? Yiyang
> What will be the default language of this web site? [en]
> Do you want to specify a URL prefix? e.g., http://example.com   (Y/n) n
> Do you want to enable article pagination? (Y/n) Y
> How many articles per page do you want? [10]
> Do you want to generate a Makefile to easily manage your website? (Y/n) Y
> Do you want an auto-reload & simpleHTTP script to assist with theme and site development? (Y/n) Y
> Do you want to upload your website using FTP? (y/N) N
> Do you want to upload your website using SSH? (y/N) y
> What is the hostname of your SSH server? [localhost]
> What is the port of your SSH server? [22]
> What is your username on that server? [root]
> Where do you want to put your web site on that server? [/var/www] /home/yiyang/tmp/notewww
> Do you want to upload your website using Dropbox? (y/N) N
> Do you want to upload your website using S3? (y/N) N
Done. Your new project is available at /Users/emomo/note
(basic)[emomo@toufen note]$ ls
Makefile          content           develop_server.sh output            pelicanconf.py    publishconf.py
-bash: cd: note: No such file or directory
Makefile          content           develop_server.sh output            pelicanconf.py    publishconf.py

(basic)[emomo@toufen note]$ make serve

cd /Users/emomo/note/output && python -m pelican.server
/Users/emomo/pyenv/basic/lib/python2.7/site-packages/pytz/__init__.py:35: UserWarning: Module argparse was already imported from /System/Library/Frameworks/Python.framework/Versions/2.7/lib/python2.7/argparse.pyc, but /Users/emomo/pyenv/basic/lib/python2.7/site-packages is being added to sys.path
  from pkg_resources import resource_stream
serving at port 8000
1.0.0.127.in-addr.arpa - - [26/May/2013 12:30:54] "GET / HTTP/1.1" 200 -
1.0.0.127.in-addr.arpa - - [26/May/2013 12:30:54] "GET /theme/css/main.css HTTP/1.1" 200 -
1.0.0.127.in-addr.arpa - - [26/May/2013 12:30:54] "GET /theme/css/reset.css HTTP/1.1" 200 -
1.0.0.127.in-addr.arpa - - [26/May/2013 12:30:54] "GET /theme/css/pygment.css HTTP/1.1" 200 -
1.0.0.127.in-addr.arpa - - [26/May/2013 12:30:54] "GET /theme/css/typogrify.css HTTP/1.1" 200 -
1.0.0.127.in-addr.arpa - - [26/May/2013 12:30:54] "GET /theme/images/icons/rss.png HTTP/1.1" 200 -
1.0.0.127.in-addr.arpa - - [26/May/2013 12:30:54] code 404, message File not found
1.0.0.127.in-addr.arpa - - [26/May/2013 12:30:54] "GET /favicon.ico HTTP/1.1" 404 -


.export wordpress xml
wordpress admin/tools/export

$brew install haskell-platform
$cabal update
$cabal install cabal-install
$cabal install pandoc
$pelican-import --wpfile -o content/ misc/notesaboutprogrammingandotherstuff.wordpress.2013-05-26.xml


$make regenerate
[ ! -d /Users/emomo/note/output ] || find /Users/emomo/note/output -mindepth 1 -delete
pelican -r /Users/emomo/note/content -o /Users/emomo/note/output -s /Users/emomo/note/pelicanconf.py
  --- AutoReload Mode: Monitoring `content`, `theme` and `settings` for changes. ---

-> Modified: content, theme, settings. re-generating...
/Users/emomo/note/content/a-simple-example-of-backbone-js-with-node-js.rst:9: (WARNING/2) Line block ends without a blank line.
/Users/emomo/note/content/allpass-lowpass-reverberator-in-adsp-2181-ez-kit-lite.rst:29: (WARNING/2) Line block ends without a blank line.
/Users/emomo/note/content/allpass-lowpass-reverberator-in-adsp-2181-ez-kit-lite.rst:36: (WARNING/2) Line block ends without a blank line.
/Users/emomo/note/content/another-usage-of-web-testing-tool-auto-browsing-for-checking-your-library-account-status.rst:9: (WARNING/2) Line block ends without a blank line.
/Users/emomo/note/content/backup-wordpress-site-and-move-to-a-new-host.rst:9: (WARNING/2) Line block ends without a blank line.
/Users/emomo/note/content/backup-wordpress-site-and-move-to-a-new-host.rst:30: (WARNING/2) Line block ends without a blank line.
/Users/emomo/note/content/backup-wordpress-site-and-move-to-a-new-host.rst:40: (WARNING/2) Line block ends without a blank line.
/Users/emomo/note/content/continuous-integration-with-buildbot.rst:36: (WARNING/2) Line block ends without a blank line.
/Users/emomo/note/content/continuous-integration-with-buildbot.rst:40: (ERROR/3) Inconsistent literal block quoting.
/Users/emomo/note/content/continuous-integration-with-buildbot.rst:47: (WARNING/2) Line block ends without a blank line.
/Users/emomo/note/content/continuous-integration-with-buildbot.rst:55: (WARNING/2) Line block ends without a blank line.
/Users/emomo/note/content/cuil-a-new-search-engine-developed-by-ex-googlers.rst:11: (WARNING/2) Inline interpreted text or phrase reference start-string without end-string.
/Users/emomo/note/content/cuil-a-new-search-engine-developed-by-ex-googlers.rst:16: (WARNING/2) Explicit markup ends without a blank line; unexpected unindent.
/Users/emomo/note/content/deploying-django-project-with-nginx-and-uwsgi-in-ubuntu-10-04.rst:41: (WARNING/2) Line block ends without a blank line.
/Users/emomo/note/content/deploying-django-project-with-nginx-and-uwsgi-in-ubuntu-10-04.rst:72: (WARNING/2) Line block ends without a blank line.
/Users/emomo/note/content/deploying-django-project-with-nginx-and-uwsgi-in-ubuntu-10-04.rst:76: (WARNING/2) Line block ends without a blank line.
/Users/emomo/note/content/deploying-django-project-with-nginx-and-uwsgi-in-ubuntu-10-04.rst:162: (WARNING/2) Line block ends without a blank line.
/Users/emomo/note/content/develope-with-remote-upstrem-but-rename-local-master-as-master-and-remote-master-as-upstream.rst:2: (WARNING/2) Block quote ends without a blank line; unexpected unindent.
/Users/emomo/note/content/develope-with-remote-upstrem-but-rename-local-master-as-master-and-remote-master-as-upstream.rst:2: (SEVERE/4) Missing matching underline for section title overline.

################################################################################################
:date: 2010-05-02 21:04
:author: yiyang
WARNING: Could not process /Users/emomo/note/content/develope-with-remote-upstrem-but-rename-local-master-as-master-and-remote-master-as-upstream.rst
/Users/emomo/note/content/develope-with-remote-upstrem-but-rename-local-master-as-master-and-remote-master-as-upstream.rst:2: (SEVERE/4) Missing matching underline for section title overline.

################################################################################################
:date: 2010-05-02 21:04
:author: yiyang
/Users/emomo/note/content/django-and-memcached-part-2.rst:9: (WARNING/2) Line block ends without a blank line.
/Users/emomo/note/content/django-and-memcached-part-2.rst:30: (WARNING/2) Line block ends without a blank line.
/Users/emomo/note/content/download-all-videos-in-your-youtube-playlist.rst:91: (WARNING/2) Line block ends without a blank line.
/Users/emomo/note/content/fck-programming.rst:8: (WARNING/2) Inline interpreted text or phrase reference start-string without end-string.
/Users/emomo/note/content/fck-programming.rst:13: (WARNING/2) Explicit markup ends without a blank line; unexpected unindent.
/Users/emomo/note/content/how-to-install-editable-python-packages-virtualenv-pip.rst:25: (WARNING/2) Line block ends without a blank line.
/Users/emomo/note/content/how-to-scrape-websites-to-produce-rss-feeds-an-example.rst:9: (WARNING/2) Line block ends without a blank line.
/Users/emomo/note/content/how-to-setup-a-git-repo-in-dreamhost.rst:34: (WARNING/2) Line block ends without a blank line.
/Users/emomo/note/content/load-testing-with-jmeter.rst:9: (WARNING/2) Line block ends without a blank line.
/Users/emomo/note/content/memcached-multi-mecanize-and-django-see-how-memcached-is-working.rst:17: (WARNING/2) Line block ends without a blank line.
/Users/emomo/note/content/memcached-multi-mecanize-and-django-see-how-memcached-is-working.rst:42: (WARNING/2) Line block ends without a blank line.
/Users/emomo/note/content/memcached-multi-mecanize-and-django-see-how-memcached-is-working.rst:50: (WARNING/2) Line block ends without a blank line.
/Users/emomo/note/content/memcached-multi-mecanize-and-django-see-how-memcached-is-working.rst:120: (WARNING/2) Line block ends without a blank line.
/Users/emomo/note/content/memcached-multi-mecanize-and-django-see-how-memcached-is-working.rst:128: (WARNING/2) Line block ends without a blank line.
/Users/emomo/note/content/mp32youtube-make-a-youtube-videos-list-from-your-mp3-library.rst:9: (WARNING/2) Line block ends without a blank line.
/Users/emomo/note/content/pycon-2007-web-framework-panel.rst:11: (WARNING/2) Inline literal start-string without end-string.
/Users/emomo/note/content/pycon-2007-web-framework-panel.rst:15: (WARNING/2) malformed hyperlink target.
/Users/emomo/note/content/python-developments-with-multi-editable-packages.rst:9: (WARNING/2) Line block ends without a blank line.
/Users/emomo/note/content/rent-a-house-by-locations-a-google-maps-application.rst:9: (WARNING/2) Line block ends without a blank line.
/Users/emomo/note/content/rotary-speaker-simulation-in-sb-live-51-emu10k1.rst:89: (WARNING/2) Line block ends without a blank line.
/Users/emomo/note/content/rotary-speaker-simulation-in-sb-live-51-emu10k1.rst:95: (WARNING/2) Inline interpreted text or phrase reference start-string without end-string.
/Users/emomo/note/content/rotary-speaker-simulation-in-sb-live-51-emu10k1.rst:95: (WARNING/2) Line block ends without a blank line.
/Users/emomo/note/content/selenium-a-functional-testing-tool-for-web-applications.rst:9: (WARNING/2) Line block ends without a blank line.
/Users/emomo/note/content/selenium-a-functional-testing-tool-for-web-applications.rst:9: (ERROR/3) Undefined substitution referenced: "Selenium_SreenShot".
/Users/emomo/note/content/serving-static-files-in-django-in-development-mode.rst:16: (WARNING/2) Cannot analyze code. No Pygments lexer found for "literal-block".
/Users/emomo/note/content/serving-static-files-in-django-in-development-mode.rst:20: (ERROR/3) Content block expected for the "code" directive; none found.
/Users/emomo/note/content/setting-up-django-in-dreamhost.rst:15: (WARNING/2) Cannot analyze code. No Pygments lexer found for "syntax".
/Users/emomo/note/content/stereo-delay-effects-vst-plugin.rst:47: (WARNING/2) Line block ends without a blank line.
/Users/emomo/note/content/talking-about-scrum.rst:12: (ERROR/3) Undefined substitution referenced: "scrum_s".
/Users/emomo/note/content/the-beer-organ.rst:8: (WARNING/2) Inline literal start-string without end-string.
/Users/emomo/note/content/the-beer-organ.rst:11: (WARNING/2) malformed hyperlink target.
/Users/emomo/note/content/the_python_propertybuiltin.rst:8: (WARNING/2) Inline literal start-string without end-string.
/Users/emomo/note/content/the_python_propertybuiltin.rst:11: (WARNING/2) malformed hyperlink target.
Done: Processed 87 articles and 0 pages in 3.05 seconds.

