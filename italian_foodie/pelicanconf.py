#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Caterina'
SITENAME = 'Italian Foodie'
SITETITLE = 'Best Italian Food Recipes'
SITESUBTITLE = 'Find Best & Delicious Italian Food Recipes'
SITEURL = 'https://xxxxxxxxxxxxx.com'

PATH = 'content'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'https://getpelican.com/'),
#          ('Python.org', 'https://www.python.org/'),
#          ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
#          ('You can modify those links in your config file', '#'),)

# # Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

# Syam Custom Settings

DIRECT_TEMPLATES = ['index', 'contact', 'copyright', 'dmca', 'privacy-policy', '404', 'single']
TEMPLATE_PAGES = {'recipes.html': 'recipes/index.html',
                  'recipes-old.html': 'recipes/index-old.html',
                  'single.html': 'recipes/single.html'}
SITEDESCRIPTION = 'Thousand best favourite Italian food recipes from food lovers'
SITEKEYWORDS = 'Italian foods, Italian recipes, Italian cuisine, Italian dishes, pasta recipes, pizza recipes'
THEME = 'theme'
THEME_STATIC_DIR = 'static'
