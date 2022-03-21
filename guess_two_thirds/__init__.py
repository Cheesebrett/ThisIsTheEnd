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
    Correct_Instructions = 886
    payment_instructions = 1

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
        label = "How mentally demanding was understanding the Instruction for the Task? Just answer quickly and intuitively."
    )


    attention_check_instructions = models.IntegerField(
        min=0, max=10000, label = "What is my favorite number between 0 and 10000? (This is just to see if you read the Instructions)"
    )

    gender = models.IntegerField(
        label = "What is your gender?",
        choices=[
            [1, 'Male'],
            [2, 'Female'],
            [3, 'Other'],
        ],
    )

    age = models.IntegerField(
        min = 0, max = 100, label = "What is your age?"
    )


    math = models.IntegerField(widget=widgets.RadioSelect, label = "I am very good in math?", choices=[1, 2, 3, 4, 5])
    english = models.IntegerField(widget=widgets.RadioSelect, label = "I speak English fluently?", choices=[1, 2, 3, 4, 5])
    rhyme = models.IntegerField(widget=widgets.RadioSelect, label = "Tree rhymes with bee?", choices=[1, 2, 3, 4, 5])
    familiarity = models.IntegerField(widget=widgets.RadioSelect, label = "I have been familiar with this task or a similar task before this experiment?", choices=[1, 2, 3, 4, 5])
    offer_5 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5])

    suggestions_box = models.StringField()

# FUNCTIONS
def creating_session(subsession):
    for player in subsession.get_players():
        player.treatmentvideo = random.choice([True, False])
        print('set treatment video to', player.treatmentvideo)

def ppg_payment(player):
    player.ppg = 1000-50*(abs(player.guessx-(2/3*player.guessx*player.guessy/2))+abs(player.guessy-(2/3*player.guessx*player.guessy/2)))


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
            return ['internet', 'cognitiveload', 'attention_check_instructions']
        else:
            return ['cognitiveload', 'attention_check_instructions']

    @staticmethod
    def before_next_page(player, timeout_happened):
        if player.attention_check_instructions == C.Correct_Instructions:
            player.payoff = C.payment_instructions
        else:
            player.payoff = 0


class Guess(Page):
    form_model = 'player'
    form_fields = ['guessx', 'guessy']
    timeout_seconds = 60
    timer_text = 'Time left to make a decision!'

    @staticmethod
    def before_next_page(player, timeout_happened):
        if timeout_happened:
            player.guessx = 100
            player.guessy = 100

class Survey(Page):
    form_model = 'player'
    form_fields = ['gender', 'age', 'math', 'english', 'rhyme', 'familiarity', 'offer_5', 'suggestions_box']

class Results(Page):
    pass


page_sequence = [Introduction, Instruction1PGGVideo, QuestionInstruction, Guess, Survey, Results]
