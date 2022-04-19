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

    education = models.StringField(
        choices=[
            'Elementary school',
            'High school',
            'College',
            'Bachelor',
            'Master',
            'Doctoral Degree',
            'Other',
        ],
        label="My highest education level is:",
    )

    origin = models.StringField(
        choices=[
            'USA',
            'India',
            'Other',
        ],
        label="My Country of origin is:",
    )

    english = models.IntegerField(
        min=0, max=5,
        label="How good are you in English on a scale from 0 to 5? 5 is equivalent to a native speaker:"
    )
    experience = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=[
            [1, '0-99'],
            [2, '100-299'],
            [3, '300-499'],
            [4, '500-799'],
            [5, '800+'],
        ],
        label="What is the total amount of HIITs you have done?",
    )
    offer_1 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4],
                                  label='I have been familiar with a similar Task before this Experiment')
    offer_2 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4],
                                  label='I have been familiar with a similar Cogntive Task before this Experiment')
    offer_3 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4],
                                  label='Please select the leftmost answer to show you read this question')
    offer_4 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4],
                                  label='The following statment is true?: Bee rhymes with Tree')
    offer_5 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4],
                                  label='I have been familiar with a similar Task before this Experiment')

    ABIC_1 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4], label='I dont "pay attention"')
    ABIC_2 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4], label='I am self-controlled')
    ABIC_3 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4], label='I concentrate easily')
    ABIC_4 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4], label='I am a careful thinker')
    Oddity_1 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4],
                                   label='I... select the leftmost answer please')
    ABIC_5 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4], label='I am a steady thinker')
    ABIC_6 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4], label='I do things without thinking')
    ABIC_7 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4],
                                 label='I say things without thinking')
    ABIC_8 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4], label='I act "on Impulse"')
    Oddity_2 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4],
                                   label='I...does tree ryhmes with bee?')
    ABIC_9 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4],
                                 label='I act on the spur of the moment')
    ABIC_10 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4], label='I plan tasks carefully')
    ABIC_11 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4],
                                  label='I plan trips well ahead of time')
    ABIC_12 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4], label='I plan for job security')
    ABIC_13 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4], label='I am future oriented')

    experience2 = models.IntegerField(
        widget= widgets.RadioSelect,
        choices=[
            [1, '0-99'],
            [2, '100-299'],
            [3, '300-499'],
            [4, '500-799'],
            [5, '800+'],
        ],
        label="What is the total amount of HIITs you have done? Please select the answer one above your actual choice to prove you read this.",
    )


    suggestions_box = models.StringField(label="Do you have any recommendations or comments on this experiment? No input is required.", blank=True)




# FUNCTIONS
# PAGES
class QuestionsBaseline(Page):
    form_model = 'player'
    form_fields = ['gender', 'age', 'education', 'origin', 'english', 'experience', 'experience2', 'suggestions_box', 'ABIC_1', 'ABIC_2', 'ABIC_3', 'ABIC_4', 'ABIC_5', 'ABIC_6', 'ABIC_7', 'ABIC_8', 'Oddity_1', 'ABIC_9', 'ABIC_10', 'Oddity_2', 'ABIC_11', 'ABIC_12', 'ABIC_13']




page_sequence = [QuestionsBaseline]
