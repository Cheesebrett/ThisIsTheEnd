from os import environ


#SESSION_CONFIGS = [
 #   dict(
  #      name='guess_two_thirds',
   #     display_name="Guess 2/3 of the Average",
    #    app_sequence=['captcha', 'guess_two_thirds', 'survey_baseline', 'payment_info'],
     #   num_demo_participants=1,
    #)
#]


#app_sequence=['captcha', 'guess_two_thirds', 'survey_baseline'],
# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']


SESSION_CONFIGS = [
    dict(
        name='guess_two_thirds',
        display_name="Guess 2/3 of the Average",
        app_sequence=['guess_two_thirds', 'raven_matrices', 'survey_baseline', 'survey_treatment', 'payment_info'],
        num_demo_participants=4,
    )
]


SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=0.0005, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = ['survey', 'treatmentvideo']
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'Dollar'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""


SECRET_KEY = '5156009382389'

INSTALLED_APPS = ['otree']
