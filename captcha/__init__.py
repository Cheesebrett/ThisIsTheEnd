from otree.api import *


author = 'Lukas Gaerttner and modifications by Daniel Klein'
doc = """
This is an introduction and a captcha task to check for bots.
"""


class Constants(BaseConstants):
    name_in_url = 'captcha'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    captcha = models.IntegerField(
        min=0,
        max=100,
        label="Answer:",
        doc="The participant is classified as a bot if the answer to the question is not 12.",
    )

    agree = models.IntegerField(
        label="Do you agree with the Terms described in the Introduction?",
        choices=[
            [1, 'agree'],
        ],
    )



# FUNCTIONS
# PAGES
class Introduction(Page):
    timeout_seconds = 5*60

    form_model = 'player'
    form_fields = ['agree']

class IntroductionWrong(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.agree != 1

    pass


class Captcha(Page):
    timeout_seconds = 60

    form_model = 'player'
    form_fields = ['captcha']


class CaptchaWrong(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.captcha != 12

    pass


page_sequence = [Introduction, Captcha, CaptchaWrong]
