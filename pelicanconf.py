#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'The iHop'
SITENAME = u'The iHop Manual'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/London'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (
    ('Waldo Collective', 'http://waldocollective.org'),
)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = 'themes/Flex'

# put articles (posts) in blog/
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'

# move the blog into a sub directory
INDEX_SAVE_AS = 'blog/index.html'
INDEX_URL = 'blog/'

#now move all the category and tag stuff to that blog/ dir as well
CATEGORY_URL = 'blog/category/{slug}.html'
CATEGORY_SAVE_AS = 'blog/category/{slug}.html'
CATEGORIES_URL = 'blog/category/'
CATEGORIES_SAVE_AS = 'blog/category/index.html'
TAG_URL = 'blog/tag/{slug}.html'
TAG_SAVE_AS = 'blog/tag/{slug}.html'
TAGS_URL = 'blog/tag/'
TAGS_SAVE_AS = 'blog/tag/index.html'
ARCHIVES_SAVE_AS = 'blog/archives/archives.html'
ARCHIVES_URL = 'blog/archives/archives.html'
AUTHOR_SAVE_AS = 'blog/{slug}.html'
AUTHORS_SAVE_AS = 'blog/authors.html'

# put pages in the root directory
PAGE_SAVE_AS = '{slug}.html'
PAGE_URL = '{slug}.html'
