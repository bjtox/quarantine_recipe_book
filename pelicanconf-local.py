#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
import os

AUTHOR = 'Antonio Bitonti'
SITENAME = 'Il Ricettario'
SITEURL = 'http://localhost:8000'

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

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

DIRECT_TEMPLATES = ('index', 'categories', 'tags', 'archives', 'search')

DISPLAY_CATEGORIES_ON_MENU = True
STATIC_PATHS = ['images', 'articles']

ARTICLE_PATHS = ['articles']
ARTICLE_URL = 'category/{category}/{slug}/'
ARTICLE_SAVE_AS = 'category/{category}/{slug}/index.html'

PAGE_URL = 'pages/{slug}/'
PAGE_SAVE_AS = 'pages/{slug}/index.html'

THEME = '..'

SOCIAL = {
    'style': {
        'size': 'medium', # small, medium, large
        'hover': True,    # True, False
        'button': False,  # True, False
    },
    # for SOCIAL, jojo supports uk-icon in uikit2
    # but jojo only recover following icons' color
    'icons': (
        # ('envelope-square', '#'),
        ('facebook-square', 'https://www.facebook.com/BiToX'),
        ('github-square', 'https://github.com/bjtox'),
        ('instagram-square', 'https://www.instagram.com/ab_bito'),
        # ('linkedin-square', '#'),
        # ('skype', '#'),
        # ('twitter-square', '#'),
        # ('weixin', '#'),
    )
}

NEWEST_ARTICLES = 10 # set 0 to hide this panel

# SIMPLE_PANELS = (
#     {
#         'badge': {
#             'string': 'Love',
#             # type can be specified as '' or 'success' or 'warning' or 'danger'
#             # by default, '' is blue, 'success' is green, 'warning' is orange and 'danger' is red
#             # please reference to uikit2
#             'type': 'danger',
#         },
#         'title': 'My Favorite Food',
#         'photo': 'food.jpg',
#         'content': 'I really love it!',
#         'link': ('Where to eat it?', '#'),
#     },
# )

# left side buttons
SHARE_BUTTONS = True
CONTROL_BUTTONS = True

AUTHOR_INFO = {
    'id': AUTHOR,
    'photo': 'io.jpg',
    # 'intro_keywords': (
    #     ('a cute dog', '#'),
    #     ('a charming blogger', '#'),
    # ),
    # 'intro': [
    #     'Hi, my name is jojo, I am a cute dog!'
    # ],
    'url': os.path.join(SITEURL, 'pages', 'about-me'),
    'social': SOCIAL,
}

# top
NAV = {
    'sitename': SITENAME,
    'navitems': (
        {
            'primary': ('Categorie', os.path.join(SITEURL, 'categories.html')),
            'secondary': (
                {'type':'header', 'name':'Ricette'},
                {'link':('Antipasti', os.path.join(SITEURL, 'category', 'antipasti.html')) },
                {'link':('Primi', os.path.join(SITEURL, 'category', 'primi.html')) },
                {'link':('Secondi', os.path.join(SITEURL, 'category', 'secondi.html')) },
                {'link':('Contorni', os.path.join(SITEURL, 'category', 'contorni.html')) },
                {'link':('Dolci', os.path.join(SITEURL, 'category', 'dolci.html')) },
                {'link':('Svuotafrigo', os.path.join(SITEURL, 'category', 'svuotafrigo.html')) },
                {'type':'divider'},
                {'link':('misc', os.path.join(SITEURL, 'category', 'misc.html'))},
            )
        },
    )
}

# footer
FOOTER = {
    'year': 2020,
    'author': AUTHOR,
    'license': {
        'name': 'The MIT License',
        'link': 'https://opensource.org/licenses/MIT',
    }
}
