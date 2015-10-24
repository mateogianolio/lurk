# lurk

Tiny python script which converts HTML from web pages that match a certain CSS pattern into JSON.

[BeautifulSoup 4](http://www.crummy.com/software/BeautifulSoup/) is the only required external
dependency and can be installed with ```pip install beautifulsoup4```.

### Usage

```bash
$ git clone https://github.com/mateogianolio/lurk.git
$ ./lurk <url> <selector> [> <output file>]
```

### Example

Familiarize yourself with [CSS attribute selectors](https://developer.mozilla.org/en-US/docs/Web/CSS/Attribute_selectors).

```bash
$ ./lurk \
http://www.gnu.org/software/libc/manual/html_node/Function-Index.html \
'a[href*="#index-"]' \
> links.json
```

This command yields a JSON object containing an array of links to all GNU C functions:

```javascript
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
```
