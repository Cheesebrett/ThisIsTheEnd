from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'survey_treatment'
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
        widget=widgets.RadioSelect,
        min=0, max=5,
        choices=[1, 2, 3, 4, 5],
        label="How good is your English on a scale from 0 to 5? 5 is equivalent to a native speaker:"
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
                                  label='I have been familiar with a similar Task before this Experiment (the one were you had to pick two numbers)')
    offer_2 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4],
                                  label='I have been familiar with a similar "Matrix Task" before this Experiment')

    ABIC_1 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4], label='I dont "pay attention"')
    ABIC_2 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4], label='I am self-controlled')
    ABIC_3 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4], label='I concentrate easily')
    ABIC_4 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4], label='I am a careful thinker')
    Oddity_2 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4],
                                   label='I... select the leftmost answer please to show you read this')
    ABIC_5 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4], label='I am a steady thinker')
    ABIC_6 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4], label='I do things without thinking')
    ABIC_7 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4],
                                 label='I say things without thinking')
    ABIC_8 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4], label='I act "on Impulse"')
    ABIC_9 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4],
                                 label='I act on the spur of the moment')
    ABIC_10 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4], label='I plan tasks carefully')
    ABIC_11 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4],
                                  label='I plan trips well ahead of time')
    ABIC_12 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4], label='I plan for job security')
    ABIC_13 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4], label='I am future oriented')

    experience2 = models.IntegerField(
        widget=widgets.RadioSelect,
        choices=[
            [1, '0-99'],
            [2, '100-299'],
            [3, '300-499'],
            [4, '500-799'],
            [5, '800+'],
        ],
        label="What is the total amount of HIITs you have done? Please select the answer one above your actual prior choice to prove you read this.",
    )

    suggestions_box = models.StringField(
        label="Do you have any recommendations or comments on this experiment? No input is required.", blank=True)

    Oddity_1 = models.IntegerField(widget=widgets.RadioSelect, choices=[1, 2, 3, 4],
                                   label='Is the following statement true?: bee rhymes with tree')


# FUNCTIONS
# PAGES
class SurveyTreatment1(Page):
    form_model = 'player'
    form_fields = ['gender', 'age', 'education', 'origin']


class SurveyTreatment2(Page):
    form_model = 'player'
    form_fields = ['english']

class SurveyTreatment3(Page):
    form_model = 'player'
    form_fields = ['experience']


class SurveyTreatment4(Page):
    form_model = 'player'
    form_fields = ['offer_1', 'offer_2', 'Oddity_1']


class SurveyTreatment5(Page):
    form_model = 'player'
    form_fields = ['ABIC_6', 'ABIC_1', 'ABIC_12']


class SurveyTreatment6(Page):
    form_model = 'player'
    form_fields = ['ABIC_10', 'ABIC_11', 'Oddity_2']


class SurveyTreatment7(Page):
    form_model = 'player'
    form_fields = ['ABIC_2', 'ABIC_4', 'ABIC_5', 'ABIC_13']


class SurveyTreatment8(Page):
    form_model = 'player'
    form_fields = ['ABIC_7', 'ABIC_8', 'ABIC_9', 'ABIC_3']


class SurveyTreatment9(Page):
    form_model = 'player'
    form_fields = ['experience2']

class SurveyTreatment10(Page):
    form_model = 'player'
    form_fields = ['suggestions_box']

page_sequence = [SurveyTreatment1, SurveyTreatment2, SurveyTreatment3, SurveyTreatment4, SurveyTreatment5, SurveyTreatment6, SurveyTreatment7, SurveyTreatment8, SurveyTreatment9, SurveyTreatment10]

