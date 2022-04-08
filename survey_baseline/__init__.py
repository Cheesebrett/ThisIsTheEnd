from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'survey_baseline'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    gender = models.IntegerField(
        label="What is your gender?",
        choices=[
            [1, 'Male'],
            [2, 'Female'],
            [3, 'Other'],
        ],
    )

    age = models.IntegerField(
        min=0, max=100, label="What is your age?"
    )

    math = models.IntegerField(widget=widgets.RadioSelect, label="I am very good in math?", choices=[1, 2, 3, 4, 5])
    english = models.IntegerField(widget=widgets.RadioSelect, label="I speak English fluently?",
                                  choices=[1, 2, 3, 4, 5])
    rhyme = models.IntegerField(widget=widgets.RadioSelect, label="Tree rhymes with bee?", choices=[1, 2, 3, 4, 5])
    familiarity = models.IntegerField(widget=widgets.RadioSelect,
                                      label="I have been familiar with this task or a similar task before this experiment?",
                                      choices=[1, 2, 3, 4, 5])
    offer_5 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4, 5])

    suggestions_box = models.StringField()


# FUNCTIONS
# PAGES
class QuestionsBaseline(Page):
    form_model = 'player'
    form_fields = ['gender', 'age', 'math', 'english', 'rhyme', 'familiarity', 'offer_5', 'suggestions_box']




page_sequence = [QuestionsBaseline]
