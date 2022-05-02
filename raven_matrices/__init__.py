from otree.api import *
import itertools
author = 'Your name here'
doc = """
Simple implementation of 12-item Raven's progressive matrices. reduced to 6 items
"""


class C(BaseConstants):
    NAME_IN_URL = 'raven_matrices'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    EARNING_PER_ITEM = 200


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    survey = models.BooleanField()

    # Form fields for the Raven matrices (only track which answer a participant selected)
    raven_1 = models.IntegerField(
        choices=(1, 2, 3, 4, 5, 6, 7, 8),
        widget=widgets.RadioSelectHorizontal,
        label="Please, indicate which of the eight options completes the pattern in the picture.",
        blank=True,
        initial=0
    )

    raven_4 = models.IntegerField(
        choices=(1, 2, 3, 4, 5, 6, 7, 8),
        widget=widgets.RadioSelectHorizontal,
        label="Please, indicate which of the eight options completes the pattern in the picture.",
        blank=True,
        initial=0
    )

    raven_6 = models.IntegerField(
        choices=(1, 2, 3, 4, 5, 6, 7, 8),
        widget=widgets.RadioSelectHorizontal,
        label="Please, indicate which of the eight options completes the pattern in the picture.",
        blank=True,
        initial=0
    )
    raven_7 = models.IntegerField(
        choices=(1, 2, 3, 4, 5, 6, 7, 8),
        widget=widgets.RadioSelectHorizontal,
        label="Please, indicate which of the eight options completes the pattern in the picture.",
        blank=True,
        initial=0
    )
    raven_8 = models.IntegerField(
        choices=(1, 2, 3, 4, 5, 6, 7, 8),
        widget=widgets.RadioSelectHorizontal,
        label="Please, indicate which of the eight options completes the pattern in the picture.",
        blank=True,
        initial=0
    )

    raven_12 = models.IntegerField(
        choices=(1, 2, 3, 4, 5, 6, 7, 8),
        widget=widgets.RadioSelectHorizontal,
        label="Please, indicate which of the eight options completes the pattern in the picture.",
        blank=True,
        initial=0
    )

    # Mark if a specific matrix was answered correctly (for payoff and data analysis purposes)
    raven_1_correct = models.BooleanField(initial=False)

    raven_4_correct = models.BooleanField(initial=False)

    raven_6_correct = models.BooleanField(initial=False)
    raven_7_correct = models.BooleanField(initial=False)
    raven_8_correct = models.BooleanField(initial=False)

    raven_12_correct = models.BooleanField(initial=False)

    # Total number of correct matrices + payoff  --> see pages.py
    ravenNumberCorrect = models.IntegerField(initial=0)


# PAGES

class Instructions(Page):
    pass


class RavenMatrices(Page):
    # main page, that displays the raven matrices
    timeout_seconds = 4*60  # <- adjust timer duration here

    form_model = 'player'
    form_fields = [
        'raven_1',

        'raven_4',
        'raven_6',
        'raven_7',
        'raven_8',
        'raven_12',
    ]  # Add additional Raven matrices form fields here

    # Input correct solutions to raven matrices here
    # Make sure that they track the correct answer!
    @staticmethod
    def before_next_page(player: Player, timeout_happened):

        if player.raven_1 == 6:
            player.ravenNumberCorrect = player.ravenNumberCorrect + 1
            player.raven_1_correct = True
            player.participant.payoff += C.EARNING_PER_ITEM
        if player.raven_4 == 2:
            player.ravenNumberCorrect = player.ravenNumberCorrect + 1
            player.raven_4_correct = True
            player.participant.payoff += C.EARNING_PER_ITEM

        if player.raven_6 == 7:
            player.ravenNumberCorrect = player.ravenNumberCorrect + 1
            player.raven_6_correct = True
            player.participant.payoff += C.EARNING_PER_ITEM
        if player.raven_7 == 8:
            player.ravenNumberCorrect = player.ravenNumberCorrect + 1
            player.raven_7_correct = True
            player.participant.payoff += C.EARNING_PER_ITEM
        if player.raven_8 == 7:
            player.ravenNumberCorrect = player.ravenNumberCorrect + 1
            player.raven_8_correct = True
            player.participant.payoff += C.EARNING_PER_ITEM
        if player.raven_12 == 5:
            player.ravenNumberCorrect = player.ravenNumberCorrect + 1
            player.raven_12_correct = True
            player.participant.payoff += C.EARNING_PER_ITEM

    @staticmethod
    def app_after_this_page(player, upcoming_apps):
        print('upcoming_apps is', upcoming_apps)
        if player.participant.survey == True:
            return "survey_treatment"


page_sequence = [Instructions, RavenMatrices]
