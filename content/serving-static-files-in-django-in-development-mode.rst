Serving static files in Django (in development mode)
####################################################
:date: 2006-05-28 23:12
:author: yiyang
:category: Django, Javascript
:slug: serving-static-files-in-django-in-development-mode

I got stuck today while I was trying to have the javascripts running
with Django.After reading Django document: `How to serve static files`_
, I finally figure out the step by step procedure:

step 1.

put this in urls.py

.. code:: literal-block

    r'^site_media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': '/path/to/media'}),

.. code:: literal-block

so now the file /path/to/media/js/myscript.js will be made available at
the URL /site\_media/js/myscript.js.

step 2.

In the template file, change the javascript directive line to <script
src="/site\_media/js/myscript.js" type="text/javascript"></script>

That's it.However,there is a "big, fat disclaimer" in the document which
said "

Using this method is **inefficient** and **insecure**. Do not use this
in a production setting. Use this only for development.

For information on serving static files in an Apache production
environment, see the `Django mod\_python documentation`_." ... I think I
need to spend some time on this topic in the future.

.. _How to serve static files: http://www.djangoproject.com/documentation/static_files/
.. _Django mod\_python documentation: http://www.djangoproject.com/documentation/modpython/#serving-media-files
