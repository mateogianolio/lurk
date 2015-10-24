lurk
====

Tiny python script which converts HTML from web pages that match a certain CSS pattern into JSON.
::

    $ pip install lurk

=====
usage
=====
::

    from lurk import lurk

    for link in lurk('http://en.wikipedia.org/wiki/en', 'a'):
        if 'href' in link:
            print link

=======
example
=======

Familiarize yourself with [CSS attribute selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors).
::

    $ ./lurk \
    http://www.gnu.org/software/libc/manual/html_node/Function-Index.html \
    'a[href*="#index-"]' \
    > links.json

This command yields a JSON object containing an array of links to all GNU C functions:
::

    [
      {
        "code": "*pthread_getspecific",
        "href": "Thread_002dspecific-Data.html#index-_002apthread_005fgetspecific"
      },

      {
        "code": "*sbrk",
        "href": "Resizing-the-Data-Segment.html#index-_002asbrk"
      },

      // ...
    ]
