from otree.api import *

author = 'Your name here'
doc = """
Simple implementation of 12-item Raven's progressive matrices.
"""


class C(BaseConstants):
    NAME_IN_URL = 'raven_matrices'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    EARNING_PER_ITEM = 0.26


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # formfields for the first page and demographic questions
    consent = models.BooleanField(
        label='''I understand that all the data collected from my responses will only be used for research and my
                    identity will be kept anonymous.''',
        choices=[[True, 'I consent'], [False, 'I do not consent']]
    )
    age = models.IntegerField(
        label='''What is your age (in years)?'''
    )
    sex = models.StringField(
        label='''What is your sex assigned at birth?''',
        choices=['Male', 'Female']
    )
    gender = models.StringField(
        label='''What is your Gender?''',
        choices=['Male', 'Female', 'Other']
    )
    religion = models.StringField(
        label='''What is your religion?''',
        choices=['Hindu', 'Muslim', 'Christian', 'Sikh', ' Jaïn', 'Other', 'No religion']
    )
    jati = models.StringField(
        label='''What is your Jati?''',
        blank=True
    )
    school = models.StringField(
        label='''What type of school did you attend?''',
        choices=['Private', 'Government School']
    )
    caste = models.StringField(
        label='''What is your caste group? ''',
        choices=['SC', 'ST', 'OBC', 'General Category']
    )
    num_people_household = models.IntegerField(
        label='''How many people live in your household (including yourself)?'''
    )
    num_years_education = models.IntegerField(
        label='''How many years of education have you completed?'''
    )
    father_occupation = models.IntegerField(
        label='''What is your father’s occupation? If retired please specify the last occupation''',
        choices=[[1, 'Cultivation own land'], [2, 'Cultivation leased land'], [3, 'Agricultural labour'],
                 [4, 'Animal husbandry'],
                 [5, 'Rental income'], [6, 'Self-employment'],
                 [7, 'Skilled labour (electrician, plumber, tailor, carpenter, mason)'],
                 [8, 'Unskilled labour (construction worker, helper, stone cutter, NREGA work etc)'],
                 [9,
                  'Non farm petty business (kirana store, tailoring shop, carpentry shop, handicrafts  business, fishing etc)'],
                 [10, 'Salaried in private firm'], [11, 'Salaried in govt enterprise'], [12, 'Household work'],
                 [13, 'Consultant/freelance'], [14, 'Gig worker (Ola, Uber, Zomato, Swiggy etc)'], [88, 'Others']]
    )
    mother_occupation = models.IntegerField(
        label='''What is your mother’s occupation?  If retired please specify the last occupation''',
        choices=[[1, 'Cultivation own land'], [2, 'Cultivation leased land'], [3, 'Agricultural labour'],
                 [4, 'Animal husbandry'],
                 [5, 'Rental income'], [6, 'Self-employment'],
                 [7, 'Skilled labour (electrician, plumber, tailor, carpenter, mason)'],
                 [8, 'Unskilled labour (construction worker, helper, stone cutter, NREGA work etc)'],
                 [9,
                  'Non farm petty business (kirana store, tailoring shop, carpentry shop, handicrafts  business, fishing etc)'],
                 [10, 'Salaried in private firm'], [11, 'Salaried in govt enterprise'], [12, 'Household work'],
                 [13, 'Consultant/freelance'], [14, 'Gig worker (Ola, Uber, Zomato, Swiggy etc)'], [88, 'Others']]
    )
    father_education = models.IntegerField(
        label='''What is your father’s education?''',
        choices=[[1, 'No Schooling'], [2, 'Pre-Primary'], [3, 'Primary'], [4, 'Secondary'], [5, 'Higher']]
    )
    mother_education = models.IntegerField(
        label='''What is your mother’s education?''',
        choices=[[1, 'No Schooling'], [2, 'Pre-Primary'], [3, 'Primary'], [4, 'Secondary'], [5, 'Higher']]
    )
    family_income = models.BooleanField(
        label='''Is your family income less than  INR 100,000 per year?''',
        choices=[[True, 'Yes'], [False, 'No']]
    )
    state = models.StringField(label="What is your State of residence?",  # TODO: Change to State / Union territory?
                               choices=[
                                   "I do not live in India",
                                   "Andaman and Nicobar Islands (UT)",
                                   "Andhra Pradesh",
                                   "Arunāchal Pradesh",
                                   "Assam",
                                   "Bihār",
                                   "Chandigarh (UT)",
                                   "Chhattīsgarh",
                                   "Dādra and Nagar Haveli (UT)",
                                   "Daman and Diu (UT)",
                                   "Delhi",
                                   "Goa",
                                   "Gujarāt",
                                   "Haryāna",
                                   "Himāchal Pradesh",
                                   "Jammu and Kashmīr (UT)",
                                   "Jhārkhand",
                                   "Karnātaka",
                                   "Kerala",
                                   "Ladākh (UT)",
                                   "Lakshadweep (UT)",
                                   "Madhya Pradesh",
                                   "Mahārāshtra",
                                   "Manipur",
                                   "Meghālaya",
                                   "Mizoram",
                                   "Nāgāland",
                                   "Orissa",
                                   "Puducherry (UT)",
                                   "Punjab",
                                   "Rājasthān",
                                   "Sikkim",
                                   "Tamil Nādu",
                                   "Telangāna",
                                   "Tripura",
                                   "Uttar Pradesh",
                                   "Uttarākhand",
                                   "West Bengal",
                               ])
    urban_rural = models.IntegerField(
        label='''Do you live in an urban or rural area?''',
        choices=[[1, 'Metro urban'], [2, 'Other urban'], [3, 'Rural']]
    )

    # Form fields for the Raven matrices (only track which answer a participant selected)
    raven_1 = models.IntegerField(
        choices=(1, 2, 3, 4, 5, 6, 7, 8),
        widget=widgets.RadioSelectHorizontal,
        label="Please, indicate which of the eight options completes the pattern in the picture.",
        blank=True,
        initial=0
    )
    raven_2 = models.IntegerField(
        choices=(1, 2, 3, 4, 5, 6, 7, 8),
        widget=widgets.RadioSelectHorizontal,
        label="Please, indicate which of the eight options completes the pattern in the picture.",
        blank=True,
        initial=0
    )
    raven_3 = models.IntegerField(
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
    raven_5 = models.IntegerField(
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
    raven_9 = models.IntegerField(
        choices=(1, 2, 3, 4, 5, 6, 7, 8),
        widget=widgets.RadioSelectHorizontal,
        label="Please, indicate which of the eight options completes the pattern in the picture.",
        blank=True,
        initial=0
    )
    raven_10 = models.IntegerField(
        choices=(1, 2, 3, 4, 5, 6, 7, 8),
        widget=widgets.RadioSelectHorizontal,
        label="Please, indicate which of the eight options completes the pattern in the picture.",
        blank=True,
        initial=0
    )
    raven_11 = models.IntegerField(
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
    raven_2_correct = models.BooleanField(initial=False)
    raven_3_correct = models.BooleanField(initial=False)
    raven_4_correct = models.BooleanField(initial=False)
    raven_5_correct = models.BooleanField(initial=False)
    raven_6_correct = models.BooleanField(initial=False)
    raven_7_correct = models.BooleanField(initial=False)
    raven_8_correct = models.BooleanField(initial=False)
    raven_9_correct = models.BooleanField(initial=False)
    raven_10_correct = models.BooleanField(initial=False)
    raven_11_correct = models.BooleanField(initial=False)
    raven_12_correct = models.BooleanField(initial=False)

    # Total number of correct matrices + payoff  --> see pages.py
    ravenNumberCorrect = models.IntegerField(initial=0)


# PAGES
class Introduction(Page):
    # Introductory page, sends players that do not consent to  'no_consent'
    form_model = 'player'
    form_fields = ['consent']

    def app_after_this_page(player: Player, upcoming_apps):
        participant = player.participant
        if player.consent == True:
            participant.consent = True
        else:
            participant.consent = False
            return 'no_consent'


class Instructions(Page):
    pass


class RavenMatrices(Page):
    # main page, that displays the raven matrices
    timeout_seconds = 480  # <- adjust timer duration here

    form_model = 'player'
    form_fields = [
        'raven_1',
        'raven_2',
        'raven_3',
        'raven_4',
        'raven_5',
        'raven_6',
        'raven_7',
        'raven_8',
        'raven_9',
        'raven_10',
        'raven_11',
        'raven_12',
    ]  # Add additional Raven matrices form fields here

    # Input correct solutions to raven matrices here
    # Make sure that they track the correct answer!
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        if player.raven_1 == 7:
            player.ravenNumberCorrect = player.ravenNumberCorrect + 1
            player.raven_1_correct = True
            player.payoff += C.EARNING_PER_ITEM
        if player.raven_2 == 4:
            player.ravenNumberCorrect = player.ravenNumberCorrect + 1
            player.raven_2_correct = True
            player.payoff += C.EARNING_PER_ITEM
        if player.raven_3 == 6:
            player.ravenNumberCorrect = player.ravenNumberCorrect + 1
            player.raven_3_correct = True
            player.payoff += C.EARNING_PER_ITEM
        if player.raven_4 == 2:
            player.ravenNumberCorrect = player.ravenNumberCorrect + 1
            player.raven_4_correct = True
            player.payoff += C.EARNING_PER_ITEM
        if player.raven_5 == 4:
            player.ravenNumberCorrect = player.ravenNumberCorrect + 1
            player.raven_5_correct = True
            player.payoff += C.EARNING_PER_ITEM
        if player.raven_6 == 7:
            player.ravenNumberCorrect = player.ravenNumberCorrect + 1
            player.raven_6_correct = True
            player.payoff += C.EARNING_PER_ITEM
        if player.raven_7 == 8:
            player.ravenNumberCorrect = player.ravenNumberCorrect + 1
            player.raven_7_correct = True
            player.payoff += C.EARNING_PER_ITEM
        if player.raven_8 == 7:
            player.ravenNumberCorrect = player.ravenNumberCorrect + 1
            player.raven_8_correct = True
            player.payoff += C.EARNING_PER_ITEM
        if player.raven_9 == 5:
            player.ravenNumberCorrect = player.ravenNumberCorrect + 1
            player.raven_9_correct = True
            player.payoff += C.EARNING_PER_ITEM
        if player.raven_10 == 5:
            player.ravenNumberCorrect = player.ravenNumberCorrect + 1
            player.raven_10_correct = True
            player.payoff += C.EARNING_PER_ITEM
        if player.raven_11 == 4:
            player.ravenNumberCorrect = player.ravenNumberCorrect + 1
            player.raven_11_correct = True
            player.payoff += C.EARNING_PER_ITEM
        if player.raven_12 == 1:
            player.ravenNumberCorrect = player.ravenNumberCorrect + 1
            player.raven_12_correct = True
            player.payoff += C.EARNING_PER_ITEM


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        part_fee = player.session.config['participation_fee']
        total = part_fee + player.payoff
        return dict(
            part_fee=part_fee, total=total
        )


class Demographics_1(Page):
    form_model = 'player'
    form_fields = ['age', 'sex', 'gender', 'religion', 'jati', 'school', 'caste', 'num_people_household',
                   'num_years_education']


class Demographics_2(Page):
    form_model = 'player'
    form_fields = ['father_occupation', 'mother_occupation', 'father_education', 'mother_education', 'family_income',
                   'state', 'urban_rural']


page_sequence = [Instructions, RavenMatrices, Results]
