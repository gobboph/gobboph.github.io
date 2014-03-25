#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Roberto Gobbetti'
SITENAME = u'Roberto Gobbetti'
SITEURL = 'http://localhost:8000'

TIMEZONE = 'America/New York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

DISPLAY_PAGES_ON_MENU = True

GITHUB_URL = 'http://github.com/gobboph'


# Blogroll
LINKS =  ()

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/robertogobbetti'),
          ('github','https://github.com/gobboph'),
          ('linkedin','https://www.linkedin.com/in/robertogobbetti'),)

TWITTER_USERNAME = 'robertogobbetti'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True


STATIC_PATHS = (['images', 'files', 'extras'])
#PATH_METADATA = (['content'])

EXTRA_PATH_METADATA = {
    #'extras/robots.txt': {'path': 'robots.txt'},
    'extras/favicon.ico': {'path': 'favicon.ico'},
}


INDEX_SAVE_AS= 'blog/index.html'


THEME = "pureS"

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
#PROFILE_IMAGE_URL = '/images/avere.JPG'
AUTHOR_EMAIL = 'robertogobbetti@gmail.com'
TAGLINE = ''
DISQUS_SITENAME = 'gobbo_ph'



ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'
AUTHOR_URL = 'blog/author/{slug}/'
AUTHOR_SAVE_AS = 'blog/author/{slug}/index.html'
CATEGORY_URL = 'blog/category/{slug}/'
CATEGORY_SAVE_AS = 'blog/category/{slug}/index.html'
TAG_URL = 'blog/tag/{slug}/'
TAG_SAVE_AS = 'blog/tag/{slug}/index.html'

# do not make pages of the type {slug}/index.html as this clashed with
# other github repositories with the same name as {slug}
PAGE_URL = '{slug}.html'
PAGE_SAVE_AS = '{slug}.html'

ARCHIVES_SAVE_AS = 'blog/archives.html'
AUTHORS_SAVE_AS = 'blog/authors.html'
CATEGORIES_SAVE_AS = 'blog/categories.html'
TAGS_SAVE_AS = 'blog/tags.html'

MENUITEMS = [
	#('Projects', 'projects.html'),
	('Blog', 'blog/'),
]
DISPLAY_PAGES_ON_MENU = True


# plugin render_math
MATH = {'color':'blue', 'align':'left'}

TYPOGRIFY = True



