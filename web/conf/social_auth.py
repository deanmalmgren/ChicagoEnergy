"""
Settings for the social_auth app

http://django-social-auth.readthedocs.org/en/latest/configuration.html
"""

# add this app to installed apps if it's not in there already
if not 'social_auth' in INSTALLED_APPS:
    INSTALLED_APPS += ('social_auth',)


AUTHENTICATION_BACKENDS = (
    'social_auth.backends.twitter.TwitterBackend',
    # 'social_auth.backends.facebook.FacebookBackend',
    # 'social_auth.backends.google.GoogleOAuthBackend',
    'social_auth.backends.google.GoogleOAuth2Backend',
    # 'social_auth.backends.google.GoogleBackend',
    # 'social_auth.backends.yahoo.YahooBackend',
    # 'social_auth.backends.browserid.BrowserIDBackend',
    # 'social_auth.backends.contrib.linkedin.LinkedinBackend',
    # 'social_auth.backends.contrib.disqus.DisqusBackend',
    # 'social_auth.backends.contrib.livejournal.LiveJournalBackend',
    # 'social_auth.backends.contrib.orkut.OrkutBackend',
    # 'social_auth.backends.contrib.foursquare.FoursquareBackend',
    # 'social_auth.backends.contrib.github.GithubBackend',
    # 'social_auth.backends.contrib.vkontakte.VKontakteBackend',
    # 'social_auth.backends.contrib.live.LiveBackend',
    # 'social_auth.backends.contrib.skyrock.SkyrockBackend',
    # 'social_auth.backends.contrib.yahoo.YahooOAuthBackend',
    # 'social_auth.backends.contrib.readability.ReadabilityBackend',
    # 'social_auth.backends.OpenIDBackend',
    'django.contrib.auth.backends.ModelBackend',
)

# The Cheating Commish app credentials
TWITTER_CONSUMER_KEY = 'wF7TR5bCF1KZShSYwl92XQ'
TWITTER_CONSUMER_SECRET = 'pXUUEG4OtCToc3tYrHBlblfucaHsjEPrnWarVX25VQU'

# @CheatingCommish read-write
TWITTER_ACCESS_TOKEN = '1281835585-3fu1FsUWQCGCLfkWf5u1v11cPKM5uSj2cidWM8h'
TWITTER_ACCESS_TOKEN_SECRET = 'IGz5itQ3fRXaPRX18TG6utZBctDIEiHM09XJqQs'

# FACEBOOK_APP_ID              = ''
# FACEBOOK_API_SECRET          = ''
# LINKEDIN_CONSUMER_KEY        = ''
# LINKEDIN_CONSUMER_SECRET     = ''
# ORKUT_CONSUMER_KEY           = ''
# ORKUT_CONSUMER_SECRET        = ''
# GOOGLE_CLIENT_ID             = ''
# GOOGLE_CLIENT_SECRET         = ''
GOOGLE_OAUTH2_CLIENT_ID      = '956251549077.apps.googleusercontent.com'
GOOGLE_OAUTH2_CLIENT_SECRET  = '_lMeWoW6ov5aHGiu4xTArLCk'
# FOURSQUARE_CONSUMER_KEY      = ''
# FOURSQUARE_CONSUMER_SECRET   = ''
# VK_APP_ID                    = ''
# VK_API_SECRET                = ''
# LIVE_CLIENT_ID               = ''
# LIVE_CLIENT_SECRET           = ''
# SKYROCK_CONSUMER_KEY         = ''
# SKYROCK_CONSUMER_SECRET      = ''
# YAHOO_CONSUMER_KEY           = ''
# YAHOO_CONSUMER_SECRET        = ''
# READABILITY_CONSUMER_SECRET  = ''
# READABILITY_CONSUMER_SECRET  = ''

if 'social_auth.context_processors.social_auth_by_type_backends' not in \
        TEMPLATE_CONTEXT_PROCESSORS:
    TEMPLATE_CONTEXT_PROCESSORS += (
        'social_auth.context_processors.social_auth_by_name_backends',
        # 'social_auth.context_processors.social_auth_backends',
        # 'social_auth.context_processors.social_auth_by_type_backends',
        # 'social_auth.context_processors.social_auth_login_redirect',
    )

# set up the django logins
LOGIN_URL          = '/login-form/'
LOGIN_REDIRECT_URL = '/'
LOGIN_ERROR_URL    = '/login-error/'

