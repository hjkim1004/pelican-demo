AUTHOR = 'Heejeong Kim'
SITENAME = 'Pelican Demo'
SITEURL = ""

PATH = "content"
TIMEZONE = 'Asia/Seoul'
DEFAULT_LANG = 'en'

# THEME settings
THEME = "themes/svbtle"
THEME_STATIC_DIR = 'theme'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# GitHub
GITHUB_URL = "https://github.com/hjkim1004"

# Blogroll
LINKS = (
    ("Pelican", "https://getpelican.com/"),
    ("Python.org", "https://www.python.org/"),
    ("Jinja2", "https://palletsprojects.com/p/jinja/"),
    ("You can modify those links in your config file", "#"),
)

# Social widget
SOCIAL = (
    ("You can add links in your config file", "#"),
    ("Another social link", "#"),
)

DEFAULT_PAGINATION = 10

# path-specific metadata
EXTRA_PATH_METADATA = {
    "extra/robots.txt": {"path": "robots.txt"},
}

# static paths will be copied without parsing their contents
STATIC_PATHS = [
    "images",
    "extra/robots.txt",
]

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True