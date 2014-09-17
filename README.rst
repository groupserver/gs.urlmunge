.. sectnum::

Introduction
============

This product ``wsgi`` `middleware`_ component for `GroupServer`_. It was
written because Zope 2.13.13 broke simple URL-rewriting using the
`VirtualHostMonster`_.

All this product does is set the ``SERVER_URL``, so skinning *works,*
getting the correct values from ``repoze.vhm`` [#repoze].

..  _middleware: http://www.python.org/dev/peps/pep-0333/#middleware-components-that-play-both-sides
..  _GroupServer: http://groupserver.org
..  _VirtualHostMonster: http://old.zope.org/Members/4am/SiteAccess2/info
..  [#repoze]: The ``repoze.vhm`` `documentation
    <http://pypi.python.org/pypi/repoze.vhm/0.14>`_

