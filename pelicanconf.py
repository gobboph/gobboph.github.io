#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Roberto Gobbetti'
SITENAME = u'Roberto Gobbetti'
SITEURL = ''

TIMEZONE = 'America/New York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS =  ()

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/robertogobbetti'),
          )

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


STATIC_PATHS = (['images', 'files', 'extras'])

THEME = "pure"

# plugins
PLUGIN_PATH = 'pelican-plugins'
PLUGINS = [
	'sitemap', 'gravatar', 'render_math',
	'liquid_tags.img', 'liquid_tags.video',
	'liquid_tags.youtube', 'liquid_tags.vimeo',
	'liquid_tags.include_code', 
	# 'liquid_tags.notebook',
]

# pure theme specific
COVER_IMG_URL = '/images/bamboo.JPG'
AUTHOR_EMAIL = 'robertogobbetti@gmail.com'
TAGLINE = ''
DISQUS_SITENAME = ''




