from otree.api import *
import numpy
import itertools
import random

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
    Endowment = 1000
    Punishment = 50
    Correct_Instructions = 752
    payment_instructions = 200


class Subsession(BaseSubsession):
    pass


def creating_session(subsession):
    treatments = itertools.cycle(
        itertools.product([True, False], [True, False])
    )
    for player in subsession.get_players():
        treatment = next(treatments)
        player.treatmentvideo = treatment[0]
        player.survey = treatment[1]


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    survey = models.BooleanField()

    treatmentvideo = models.BooleanField()

    guessx = models.IntegerField(
        min=0, max=100, label="Please pick your first number from 0 to 100:"
    )
    guessy = models.IntegerField(
        min=0, max=100, label="Please pick your second number from 0 to 100:"
    )

    internet = models.IntegerField(
        label="Was your internet connection stable enough to watch the video or did you have other trouble?",
        choices=[
            [1, 'No problems watching the video'],
            [2, 'Some problems'],
            [3, 'Could not really watch'],
        ],
        widget=widgets.RadioSelectHorizontal
    )

    cognitiveload = models.IntegerField(
        label="How mentally demanding was understanding the Instruction for the Task? Just answer quickly and intuitively."
    )

    attention_check_instructions = models.IntegerField(
        min=0, max=10000, inital=1,
        label="What is my favorite number between 0 and 10000? (This is just to see if you read the Instructions). If you don't know, just put in 1."
    )

    pgg = models.FloatField()

    timeSpentInstructions = models.FloatField()
    timeSpentGuess = models.FloatField()
    timeSpentCognitive = models.FloatField()


# FUNCTIONS


def ppg_payment(player):
    player.participant.payoff += max(2000 - 50 * ((abs(player.guessx - 2 / 3 * (player.guessx + player.guessy) / 2)) + abs(
        player.guessy - (2 / 3 * (player.guessx + player.guessy) / 2))), 0)



#player.participant.payoff += 1000 - 50 * (abs(player.guessx - (2 / 3 * player.guessx * player.guessy / 2)) + abs(
  #      player.guessy - (2 / 3 * player.guessx * player.guessy / 2)))

# PAGES
class Introduction(Page):
    pass


class Instruction1PGGVideo(Page):
    form_model = 'player'
    form_fields = ['timeSpentInstructions']


class Instruction1PGGText(Page):
    pass


class QuestionInstruction(Page):
    form_model = 'player'
    timeout_seconds = 5 * 60
    @staticmethod
    def get_form_fields(player):
        if player.treatmentvideo:
            return ['internet', 'cognitiveload', 'attention_check_instructions']
        else:
            return ['cognitiveload', 'attention_check_instructions']

    @staticmethod
    def before_next_page(player, timeout_happened):
        if player.attention_check_instructions == C.Correct_Instructions:
            player.participant.payoff += C.payment_instructions
        else:
            player.participant.payoff += 0


class Guess(Page):
    form_model = 'player'
    form_fields = ['guessx', 'guessy', 'timeSpentGuess']
    timeout_seconds = 5 * 60
    timer_text = 'Time left to make a decision.'

    @staticmethod
    def before_next_page(player, timeout_happened):
        if timeout_happened:
            player.guessx = 100
            player.guessy = 100
        ppg_payment(player)




class Results(Page):
    pass


page_sequence = [Instruction1PGGVideo, QuestionInstruction, Guess, Results]
