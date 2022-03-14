from otree.api import *
import numpy
import itertools


doc = """
a.k.a. Keynesian beauty contest.
Players all guess a number; whoever guesses closest to
2/3 of the average wins.
See https://en.wikipedia.org/wiki/Guess_2/3_of_the_average
"""


class C(BaseConstants):
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    NAME_IN_URL = 'guess_two_thirds'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    treatmentvideo = models.BooleanField()

    guessx = models.IntegerField(
        min=0, max=100, label="Please pick your first number from 0 to 100:"
    )
    guessy = models.IntegerField(
        min=0, max=100, label="Please pick your second number from 0 to 100:"
    )

    internet = models.IntegerField(
        label = "Was your internet connection stable enough to watch the video or did you have other trouble?",
        choices=[
            [1, 'No problems watching the video'],
            [2, 'Some problems'],
            [3, 'Could not really watch'],
        ],
        widget = widgets.RadioSelectHorizontal
    )


    cognitiveload = models.IntegerField(
        label = "How mentally demanding was the Instruction? Just answer quickly and intuitively.",
        widget = widgets.RadioSelect,
        choices =[-4, -3, -2, -1, 0, 1, 2, 3, 4]
    )

    testslider = models.IntegerField(
        label="Does he look like a slider?",
        widget=widgets.RadioSelect,
        choices=[-3, -2, -1, 0, 1, 2, 3]
    )

    price = models.FloatField()
    number = models.IntegerField()

# FUNCTIONS
def creating_session(subsession):
    import random
    for player in subsession.get_players():
        player.treatmentvideo = random.choice([True, False])
        print('set treatment video to', player.treatmentvideo)


def set_payoff(player: Player):
    player.payoff = 1000-50*(abs(player.guessx-(2/3*player.guessx*player.guessy/2))+abs(player.guessy-(2/3*player.guessx*player.guessy/2)))


# PAGES
class Introduction(Page):
    pass


class Instruction1PGGVideo(Page):
    pass


class Instruction1PGGText(Page):
    @staticmethod
    def is_displayed(player: Player):
        return player.treatmentvideo


class QuestionInstruction(Page):
    form_model = 'player'

    @staticmethod
    def get_form_fields(player):
        if player.treatmentvideo:
            return ['internet', 'cognitiveload']
        else:
            return ['cognitiveload']




class Guess(Page):
    form_model = 'player'
    form_fields = ['guessx', 'guessy']

    @staticmethod
    def before_next_page(player, timeout_happened):
        player.set_payoff()


class Results(Page):
    pass


page_sequence = [Introduction, Instruction1PGGVideo, QuestionInstruction, Guess, Results]
