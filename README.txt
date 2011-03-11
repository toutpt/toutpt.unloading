Introduction
============

Add-on for Plone optimized to work with debianutils_. The goal is to unload Plone
and make it works great with Technologies like:

* Varnish_
* Memcache_
* Postgresql_

At zope level
=============

At zope level this add-on add a configuration override to force 
plone.memoize.ram cache component to use a memcached server.
Settings of memcached are taken from environement variable 'MEMCACHE_SERVER'. If
'MEMCACHE_SERVER' doens't exists defaults are used: 127.0.0.1:11211.
Products.Memcached is also a dependency to let you use RamCache object using
memcached. It is a must have when you work with a cluster of zope instance.

This add-on depend on relstorage and psycopg2 to make the zope database ready
to work on Postgresql_. It needs a specific zope configuration to activate it.
Check the Relstorage_ documentation & the debianutils setup.

At Plone level
==============

Once your zope is setup with this add-on you just have to install this add-on
as any other add-on to activate best pratice on your Plone site and make it
faster than ever.

