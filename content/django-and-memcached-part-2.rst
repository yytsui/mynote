django and memcached (part 2)
#############################
:date: 2011-01-07 20:57
:author: yiyang
:category: Django
:slug: django-and-memcached-part-2

| As shown in my `previous post`_, it's very easy to "cache every page
that does not have GET or POST parameters", but what
|  about those "GET" or "POST" requests which involved read from or
write to database? Say if we want to get the "Stuff"
|  list, we have to make sure it's fast enough from cache 'fresh', i.e.
not the stall records which have been already change in database?
|  Django provides cache API to achieve this:

::

    from app.models import Stuff
    from django.core.cache import cache

    def find_some_stuff_for_user(request):
        cache_key = 'stuff_list_for_%s' % request.user.pk
        stuff_list = cache.get(cache_key)
        if stuff_list is None:
            stuff_list = Stuff.objects.filter(user=request.user)
            cache.set(cache_key, stuff_list)
        return stuff_list

| This make sure the access is fast from cache as long as the 'stuff' is
there, otherwise getting them from
|  database and cached them. But what about making sure it's fresh?
since it's possible to create, update and
|  delete the data somewhere else? It turns out Django signals are the
solution:

::

    from django.core.cache import cache
    from django.db.models import signals
    def make_sure_the_stuff_list_in_cache_is_fresh(request):
        cache_key = 'stuff_list_for_%s' request.user.pk
        cache_key.delete(cache_key)
    signals.post_save.connect(make_sure_the_stuff_list_in_cache_is_fresh, sender=Stuff)
    signals.post_delete.connect(make_sure_the_stuff_list_in_cache_is_fresh, sender=Stuff)

Actually, there are already handy django apps `johnny-cache`_ and
`cache-machine`_ which can do this automatically.

.. _previous post: http://heyheymymy.net/django/memcached-multi-mecanize-and-django-see-how-memcached-is-working
.. _johnny-cache: http://packages.python.org/johnny-cache/
.. _cache-machine: http://jbalogh.me/projects/cache-machine/
