#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Antonio Bitonti'
SITENAME = 'Il Ricettario'
SITEURL = 'http://localhost:8000/'
RELATIVE_URLS = False

PATH = 'content'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'it'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

DEFAULT_PAGINATION = 10

DIRECT_TEMPLATES = ('index', 'categories', 'tags', 'archives', 'search')

DISPLAY_CATEGORIES_ON_MENU = True
STATIC_PATHS = ['images', 'articles']

ARTICLE_PATHS = ['articles']
ARTICLE_URL = 'article/{category}/{slug}/index.html'
ARTICLE_SAVE_AS = 'article/{category}/{slug}/index.html'

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

THEME = 'themes/pelican-elegant-custom'

SOCIAL = (
    ('Email', 'antonio.bitonti@gmail.com', 'My Email Address'),
    ("Github", "https://github.com/bjtox", "My GitHubSpace"),
    ("Facebook", "https://www.facebook.com/BiToX"),
)

NEWEST_ARTICLES = 10 # set 0 to hide this panel

SHARE_BUTTONS = True
CONTROL_BUTTONS = True

AUTHOR_INFO = {
    'id': AUTHOR,
    'photo': 'io.jpg',
    'url': os.path.join(SITEURL, 'pages', 'about-me'),
    'social': SOCIAL,
}

TAGS_URL = "tags.html"
CATEGORIES_URL = "categories.html"
ARCHIVES_URL = "archives.html"
SEARCH_URL = "search.html"


PLUGIN_PATH = 'plugins/'
PLUGINS = ['tipue_search','extract_toc']

SOCIAL_PROFILE_LABEL = 'Contatti'

MARKDOWN = {
  'extension_configs': {
    'markdown.extensions.toc': {},
    'markdown.extensions.admonition': {}
  }
}
